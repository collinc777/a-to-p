from typing import Iterable, List
import instructor
import openai
from pydantic import BaseModel

from api.models import TranscriptLine

client = instructor.patch(openai.AsyncClient())

class Section(BaseModel):
    title: str
    content: str
    subsections: List["Section"]

class ArticleOutline(BaseModel):
    title: str
    sections: list[Section]

async def generate_episode_longform(text: str):
    outline = await gen_outline(text)
    intro = await gen_intro(text, outline)
    script_so_far = intro
    return await gen_main_sections(article_text=text, outline=outline, script_so_far=script_so_far)

async def gen_main_sections(*, article_text: str, outline: ArticleOutline, script_so_far: List[TranscriptLine]):
    for section_outline in outline.sections[1:]:
        section_script = await gen_script_for_section(article_text, section_outline, script_so_far)
        script_so_far.extend(section_script)
    return script_so_far


async def gen_script_for_section(article_text: str, section: Section, script_so_far: List[TranscriptLine]):
    result = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        response_model=Iterable[TranscriptLine],
        max_tokens=4096,
        messages=[{
            "role": "system",
            "content": get_section_system_prompt()
        }, {
            "role": "user",
            "content": f"Generate a transcript for the section of the podcast based on the below article_text, section outline, and script so far. and article text.\n\nArticle Text: {article_text}\n\nSedction Outline: {section}\n\nScript So Far: {script_so_far}. Make it flow with the script so far. Keep in mind there will be content coming after. No sign off until the conclusion! You are NOT writing the conclusion or ending the episode!"
        }]
    )
    return result

async def gen_intro(article_text: str, outline: ArticleOutline) -> List[TranscriptLine]:
    result = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        response_model=Iterable[TranscriptLine],
        max_tokens=4096,
        messages=[{
            "role": "system",
            "content": get_intro_system_prompt()
        }, {
            "role": "user",
            "content": f"Generate a transcript for the intro of the podcast based on the below outline and article text.\n\nOutline: {outline}\n\nArticle Text: {article_text}"
        }]
    )
    return result

async def gen_outline(text: str) -> ArticleOutline:
    result = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        response_model=ArticleOutline,
        max_tokens=4096,
        messages=[{
            "role": "system",
            "content":  get_outline_system_prompt()
        }, {
            "role": "user",
            "content": "Create a detailed outline for the following article: " + text
        }]
    )
    return result


def get_outline_system_prompt():
    return "You are a highly skilled podcast writer specializing in transforming articles into outlines for a podcast transcript writer to use. Your task is to create an outline for an article for a podcast writer to utilize in their script generation. Given the complete text of an article, generate a detailed outline that includes the main title, sections with titles and brief descriptions, and any relevant subsections. Ensure the outline captures the core ideas and arguments presented in the article, organizing them logically. Your output must adhere strictly to a JSON format." 

def get_intro_system_prompt():
    return """You are a highly skilled podcast writer specializing in transforming blog posts into engaging NPR-style conversational podcast transcripts for a podcast titled ListenArt. Your task is to create a dynamic dialogue between two speakers, Jake and Emily. They will be discussing the content of the provided blog posts in a lively, informative, and in depth manner. The conversation should mimic the natural flow of a professional podcast, with each speaker offering insights, asking questions, and elaborating on the topics presented. Your output must adhere strictly to a JSON format, ensuring each line of dialogue is correctly attributed to either Jake or Emily. Please use the following JSON structure to organize the conversation, making it easy to parse and understand. Remember, the focus is on creating a natural, NPR-style conversation that both informs and engages the listener, while maintaining impeccable JSON formatting."""

def get_section_system_prompt():
    return """You are a highly skilled podcast writer specializing in transforming blog posts into engaging NPR-style conversational podcast transcripts for a podcast titled ListenArt. Your task is to create a dynamic dialogue between two speakers, Jake and Emily. They will be discussing the content of the provided blog posts in a lively, informative, and in depth manner. The conversation should mimic the natural flow of a professional podcast, with each speaker offering insights, asking questions, and elaborating on the topics presented. Your output must adhere strictly to a JSON format, ensuring each line of dialogue is correctly attributed to either Jake or Emily. Please use the following JSON structure to organize the conversation, making it easy to parse and understand. Remember, the focus is on creating a natural, NPR-style conversation that both informs and engages the listener, while maintaining impeccable JSON formatting."""

def pretty_print(script: List[TranscriptLine]):
    for line in script:
        print(f"{line.speaker}: {line.text}\n\n")