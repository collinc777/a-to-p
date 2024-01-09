from functools import lru_cache
from typing import Annotated, List, Literal, Optional
from fastapi import Depends, FastAPI
from mypy_boto3_polly import PollyClient
from mypy_boto3_polly.literals import VoiceIdType
import uvicorn
import os
from llama_index.program import OpenAIPydanticProgram
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    openai_api_key: Optional[str] = None
    aws_access_key_id: Optional[str] = None
    aws_secret_access_key: Optional[str] = None
    aws_region: Optional[str] = None
    aws_default_region: Optional[str] = None


@lru_cache()
def get_settings():
    return Settings()


app = FastAPI()

Speaker = Literal["narrator", "collin", "allison"]


class TranscriptLine(BaseModel):
    """A line of the transcript"""

    # speaker is one of narrator, collin, or allison
    speaker: Speaker
    text: str


class Transcript(BaseModel):
    """The transcript of the podcast episode"""

    transcript_lines: List[TranscriptLine]


async def generate_episode(article_text: str):
    transcript_body = await generate_transcript_body(article_text)
    audio = await generate_audio(transcript_body)
    return audio


async def generate_transcript_body(article_text: str):
    program = OpenAIPydanticProgram.from_defaults(
        output_cls=Transcript,  # type: ignore
        prompt_template_str="""You are a podcast writer. Convert blog posts into NPR-style podcast transcripts with 2 speakers: Rachel and Jack. YOU ONLY OUTPUT VALID JSON. Use the given format to extract information from the following input: {text}""",
        verbose=True,
    )
    output: Transcript = await program.acall(text=article_text)  # type: ignore
    return output


async def do_tts(line: str, voice: VoiceIdType) -> bytes:
    import boto3

    settings = get_settings()

    session = boto3.Session(
        aws_access_key_id=settings.aws_access_key_id,
        aws_secret_access_key=settings.aws_secret_access_key,
        region_name=settings.aws_region,
    )
    client: PollyClient = session.client("polly")
    result = client.synthesize_speech(
        Text=line, OutputFormat="mp3", VoiceId=voice, Engine="neural"
    )
    byte_string = result["AudioStream"].read()
    return byte_string


def get_voice_for_speaker(speaker: Speaker) -> VoiceIdType:
    return "Amy"


from pydub import AudioSegment


async def generate_audio(transcript: Transcript):
    # use tts to generate audio
    lines = transcript.transcript_lines
    tasks = []
    for line in lines:
        # add to tasks
        tasks.append(do_tts(line=line.text, voice=get_voice_for_speaker(line.speaker)))
    import asyncio
    import io

    audios = await asyncio.gather(*tasks)
    # convert byte strings to audio segments and add silence between them
    silence = AudioSegment.silent(duration=500)  # 500 milliseconds of silence
    audio_segments = [
        AudioSegment.from_mp3(io.BytesIO(audio)) + silence for audio in audios
    ]
    # combine the audio segments
    combined = sum(audio_segments, AudioSegment.empty())
    # save to a file
    combined.export("audio.mp3", format="mp3")
    return combined.raw_data


@app.get("/api/python")
def hello_world(settings: Annotated[Settings, Depends(get_settings)]):
    # print the environment

    return {"message": "hello world"}


@app.post("/api/episode")
async def episode_create(article_text: str):
    # generate the episode
    return await generate_episode(article_text)


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # hello_world()


if __name__ == "__main__":
    main()
