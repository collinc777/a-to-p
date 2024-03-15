from types import NoneType
from typing import AsyncGenerator, Callable, Iterable, List, Tuple
import instructor
import openai
from pydantic import BaseModel
from api.audio_generator import generate_episode_audio
from api.db import get_session_context

from api.models import (
    EpisodeFormat,
    EpisodeStatus,
    ExtractedArticle,
    Transcript,
    TranscriptLine,
    UpdateEpisodeDBInput,
)
from api.crud import crud_episode

client = instructor.patch(openai.AsyncClient())


class Section(BaseModel):
    title: str
    content: str
    subsections: List["Section"]


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


class SectionUserPromptArgs(BaseModel):
    article_text: str
    sections: List[Section]
    script_so_far: List[TranscriptLine]


SectionSystemPrompt = Callable[[], str]

SectionUserPrompt = Callable[[SectionUserPromptArgs], str]


def get_section_prompt_factories(
    episode_format: EpisodeFormat,
) -> Tuple[SectionUserPrompt, SectionSystemPrompt]:
    return get_section_user_prompt, get_section_system_prompt


async def gen_main_sections(
    *,
    article_text: str,
    outline: ArticleOutline,
    episode_format: EpisodeFormat,
    script_so_far: List[TranscriptLine],
):
    user_prompt_factory, section_prompt_factory = get_section_prompt_factories(
        episode_format
    )
    section_system_prompt = section_prompt_factory()
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


def get_section_user_prompt(
    input: SectionUserPromptArgs,
):
    return f"Generate a transcript for the CURRENT sections of the podcast based on the below article_text, section outline, and script so far. and article text.\n\nArticle Text: {input.article_text}\n\nSection Outlines to base the script on: {input.sections}\n\nScript So Far: {input.script_so_far}. Make it flow with the script so far. Keep in mind there will be content coming after unless it's the conclusion. No sign off until the conclusion! You are NOT writing the conclusion or ending the episode! Keep it Consice!"


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


def get_intro_system_prompt():
    return """You are a highly skilled podcast writer specializing in transforming articles into engaging NPR-style conversational podcast transcripts for a podcast titled ListenArt. Your task is to create a dynamic dialogue between two speakers, Jake and Emily. They will be discussing the content of the provided blog posts in a lively, informative, and concise manner. The conversation should mimic the natural flow of a professional podcast, with each speaker offering insights, asking questions, and elaborating on the topics presented. Your output must adhere strictly to a JSON format, ensuring each line of dialogue is correctly attributed to either Jake or Emily. Please use the following JSON structure to organize the conversation, making it easy to parse and understand. Remember, the focus is on creating a natural, NPR-style conversation that both informs and engages the listener, while maintaining impeccable JSON formatting."""


def get_section_system_prompt():
    return """You are a highly skilled podcast writer specializing in transforming articles into engaging NPR-style conversational podcast transcripts for a podcast titled ListenArt. Your task is to create dynamic dialogues between two speakers, Jake and Emily, discussing various topics presented in provided articles. Aim to craft a lively, informative, and concise conversation that mirrors the natural flow of professional podcasts. Implement the following enhancements to ensure the content is both engaging and accessible:

1. **Listener Engagement:** Integrate direct questions or prompts for the audience within the dialogue, encouraging them to reflect on the discussion or to participate by sharing their thoughts through social media or podcast platforms.

2. **Incorporate Examples:** Use specific examples or anecdotes to illustrate points, especially when discussing complex or abstract topics. These should help listeners visualize concepts and understand their real-world implications.

3. **Explain Technical Terms:** When using technical jargon or industry-specific terminology, include brief, accessible explanations or analogies. This ensures all listeners, regardless of their background, can follow the conversation easily.

4. **Strong Call-to-Action (CTA):** Conclude the transcript with a compelling CTA, motivating listeners to engage further with the topic. This could be an invitation to explore additional resources, participate in a related online community, or engage with a related interactive content piece.

Additionally, ensure the dialogue:

- Showcases a natural, NPR-style conversational tone between Jake and Emily, with a balance of insights, inquiries, and elaborations on the topics.
- Maintains impeccable JSON formatting for ease of parsing and understanding, with each line of dialogue correctly attributed to either Jake or Emily using the specified JSON structure.

Remember, the focus is on creating an NPR-style conversation that informs, engages, and invites the listener into the dialogue, while keeping the format structured and clear for digital consumption.
"""


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
