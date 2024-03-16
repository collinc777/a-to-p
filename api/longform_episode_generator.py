from typing import AsyncGenerator, Callable, Iterable, List, Tuple
import instructor
import openai
from pydantic import BaseModel
from api.audio_generator import generate_episode_audio
from api.db import get_session_context

from api.models import (
    EpisodeFormat,
    EpisodeFormatType,
    EpisodeStatus,
    ExtractedArticle,
    Section,
    Transcript,
    TranscriptLine,
    UpdateEpisodeDBInput,
)
from api.crud import crud_episode
from api.prompts import (
    DialogueSectionSystemPrompt,
    EducationalSectionSystemPrompt,
    InterviewSectionSystemPrompt,
    MonologueSectionSystemPrompt,
    NewsCurrentEventsSectionSystemPrompt,
    PanelDiscussionSystemPrompt,
    SectionSystemPrompt,
    SectionUserPromptArgs,
    StorytellingSectionSystemPrompt,
    section_user_prompt,
)

client = instructor.patch(openai.AsyncClient())


class ArticleOutline(BaseModel):
    title: str
    sections: list[Section]


async def generate_episode_audio_task(episode_id):
    async with get_session_context() as session:
        episode = await crud_episode.get(session, episode_id)
        if episode is None:
            raise ValueError("Episode not found")
        url = await generate_episode_audio(episode=episode)
        episode = await crud_episode.update(
            session,
            db_obj=episode,
            obj_in=UpdateEpisodeDBInput(
                url=url,
                status=EpisodeStatus.done,
                transcript=episode.transcript,
                episode_hash=episode.computed_episode_hash,
            ),
        )
        return episode


async def generate_episode_task(episode_id):
    async with get_session_context() as session:
        episode = await crud_episode.get(session, episode_id)
        if episode is None:
            raise ValueError("Episode not found")
        episode = await crud_episode.update(
            session, db_obj=episode, obj_in={"status": "generating_transcript"}
        )

        try:
            resulting_longform = generate_episode_longform(
                episode.article_text, episode.episode_format
            )
            messages = []
            async for message in resulting_longform:
                messages.append(message)
                transcript = Transcript(transcript_lines=messages)
                episode = await crud_episode.update(
                    session,
                    db_obj=episode,
                    obj_in=UpdateEpisodeDBInput(transcript=transcript),
                )
            episode = await crud_episode.update(
                session,
                db_obj=episode,
                obj_in=UpdateEpisodeDBInput(status=EpisodeStatus.generating_audio),
            )
            url = await generate_episode_audio(episode=episode)
            episode = await crud_episode.update(
                session,
                db_obj=episode,
                obj_in=UpdateEpisodeDBInput(
                    status=EpisodeStatus.done,
                    url=url,
                    episode_hash=episode.computed_episode_hash,
                ),
            )
        except RuntimeError:
            episode = await crud_episode.update(
                session,
                db_obj=episode,
                obj_in=UpdateEpisodeDBInput(status=EpisodeStatus.failed),
            )
            raise


async def generate_episode_longform(text: str, episode_format: EpisodeFormat):
    outline = await gen_outline(text)
    script_so_far = []
    async for line in gen_main_sections(
        article_text=text,
        outline=outline,
        script_so_far=script_so_far,
        episode_format=episode_format,
    ):
        yield line
    # script_so_far = intro
    # return await gen_main_sections(article_text=text, outline=outline, script_so_far=script_so_far)


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


SectionUserPrompt = Callable[[SectionUserPromptArgs], str]


def get_section_prompt_factories(
    episode_format: EpisodeFormat,
) -> Tuple[SectionUserPrompt, SectionSystemPrompt]:
    match episode_format.episode_format_type:
        case EpisodeFormatType.dialogue:
            return section_user_prompt, DialogueSectionSystemPrompt(
                speakers=("jake", "emily")
            )
        case EpisodeFormatType.monologue:
            return section_user_prompt, MonologueSectionSystemPrompt(speaker="jake")

        case EpisodeFormatType.interview:
            return section_user_prompt, InterviewSectionSystemPrompt(
                interviewee="emily", interviewer="jake"
            )
        case EpisodeFormatType.panel:
            return section_user_prompt, PanelDiscussionSystemPrompt(
                speakers=("jake", "emily", "dillon")
            )
        case EpisodeFormatType.educational:
            return section_user_prompt, EducationalSectionSystemPrompt(
                speakers=("jake", "emily")
            )

        case EpisodeFormatType.storytelling:
            return section_user_prompt, StorytellingSectionSystemPrompt(speaker="jake")

        case EpisodeFormatType.news_current_events:
            return section_user_prompt, NewsCurrentEventsSectionSystemPrompt(
                speakers=("jake", "emily")
            )

        case EpisodeFormatType.tts:
            return section_user_prompt, MonologueSectionSystemPrompt(speaker="jake")

        case _:
            return section_user_prompt, DialogueSectionSystemPrompt(
                speakers=("jake", "emily")
            )


async def gen_main_sections(
    *,
    article_text: str,
    outline: ArticleOutline,
    episode_format: EpisodeFormat,
    script_so_far: List[TranscriptLine],
):
    user_prompt_factory, section_system_prompt = get_section_prompt_factories(
        episode_format
    )
    section_system_prompt = section_system_prompt.get_prompt("Listen Art")
    for section_outline in chunks(outline.sections, 2):
        section_user_prompt = user_prompt_factory(
            SectionUserPromptArgs(
                article_text=article_text,
                sections=section_outline,
                script_so_far=script_so_far,
            )
        )
        section_script = await gen_script_for_sections(
            section_system_prompt=section_system_prompt,
            section_user_prompt=section_user_prompt,
        )
        async for line in section_script:
            yield line
            script_so_far.append(line)


async def gen_script_for_sections(
    *,
    section_system_prompt: str,
    section_user_prompt: str,
) -> AsyncGenerator[TranscriptLine, None]:
    result = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        stream=True,
        temperature=0.2,
        presence_penalty=0.5,
        response_model=Iterable[TranscriptLine],
        messages=[
            {"role": "system", "content": section_system_prompt},
            {"role": "user", "content": section_user_prompt},
        ],
    )  # type: ignore
    return result


async def gen_outline(text: str) -> ArticleOutline:
    result = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        response_model=ArticleOutline,
        messages=[
            {"role": "system", "content": get_outline_system_prompt()},
            {
                "role": "user",
                "content": f"Create a detailed outline for the following article. We will be using this outline for creating a podcast transcript from the article so make sure you put in all the relevant content: \n\n{text}",
            },
        ],
    )  # type: ignore
    return result


def get_outline_system_prompt():
    return "You are a highly skilled podcast writer specializing in transforming articles into outlines for a podcast transcript writer to use. Your task is to create a detailed outline from an article for a podcast writer to utilize in their script generation. Given the complete text of an article, generate a detailed outline that includes the main title, intro, conclusion, and sections with titles brief descriptions, and any detailed subsections. Ensure the outline captures the core ideas and arguments presented in the article, organizing them logically. The longer the article, the more sections there should be in the outline. Your output must adhere strictly to a JSON format."


def pretty_print(script: List[TranscriptLine]):
    for line in script:
        print(f"{line.speaker}: {line.text}\n\n")


def extract_article(url: str) -> ExtractedArticle:
    import trafilatura

    response = trafilatura.fetch_url(url)
    if not isinstance(response, str):
        raise Exception("response is not a string")

    t = trafilatura.bare_extraction(response)
    article = ExtractedArticle.model_validate(t)
    return article
