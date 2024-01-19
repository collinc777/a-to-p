from contextlib import asynccontextmanager
import uuid
from .crud_episode import crud_episode
from functools import lru_cache
from io import BytesIO
from typing import Annotated, Optional, AsyncGenerator
from fastapi import BackgroundTasks, Depends, FastAPI
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, Field, create_engine, Session
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
import uvicorn
from llama_index.program import OpenAIPydanticProgram
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from api.models import Episode, Transcript

from api.tts_provider import get_tts_provider, TTSProvider

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    openai_api_key: Optional[str] = None
    aws_access_key_id: Optional[str] = None
    aws_secret_access_key: Optional[str] = None
    bucket_access_key_id: Optional[str] = None
    bucket_secret_access_key: Optional[str] = None
    bucket_url: Optional[str] = None
    bucket_public_url: Optional[str] = None
    aws_region: Optional[str] = None
    aws_default_region: Optional[str] = None
    replicate_api_token: Optional[str] = None
    database_url: Optional[str] = None


@lru_cache()
def get_settings():
    return Settings()


engine = AsyncEngine(create_engine(get_settings().database_url))  # type: ignore


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)  # type: ignore
    async with async_session() as session:  # type: ignore
        yield session  # type: ignore


app = FastAPI()


async def generate_episode(article_text: str, episode_id: str) -> str:
    transcript_body = await generate_transcript_body(article_text)
    provider = get_tts_provider("openai")
    url = await generate_audio(
        transcript=transcript_body, provider=provider, episode_id=episode_id
    )
    return url


async def generate_transcript_body(article_text: str):
    from llama_index.llms import OpenAI

    program = OpenAIPydanticProgram.from_defaults(
        output_cls=Transcript,  # type: ignore
        llm=OpenAI(model="gpt-4-1106-preview"),
        prompt_template_str="""You are a highly skilled podcast writer specializing in transforming blog posts into engaging NPR-style conversational podcast transcripts. Your task is to create a dynamic dialogue between two speakers, Jake and Emily. They will be discussing the content of the provided blog posts in a lively, informative manner. The conversation should mimic the natural flow of a professional podcast, with each speaker offering insights, asking questions, and elaborating on the topics presented. Your output must adhere strictly to a JSON format, ensuring each line of dialogue is correctly attributed to either Jake or Emily. Please use the following JSON structure to organize the conversation, making it easy to parse and understand. Here's the input you need to work with: {text}. Remember, the focus is on creating a natural, NPR-style conversation that both informs and engages the listener, while maintaining impeccable JSON formatting.""",
        verbose=True,
    )
    output: Transcript = await program.acall(text=article_text)  # type: ignore
    return output


async def generate_audio(
    *,
    transcript: Transcript,
    provider: TTSProvider,
    episode_id: str,
) -> str:
    settings = get_settings()
    # use tts to generate audio
    lines = transcript.transcript_lines
    tasks = []
    for line in lines:
        # add to tasks
        tasks.append(provider.speak(text=line.text, speaker=line.speaker))
    import asyncio
    import io

    audios = await asyncio.gather(*tasks)
    # convert byte strings to audio segments and add silence between them
    from pydub import AudioSegment

    silence = AudioSegment.silent(duration=500)  # 500 milliseconds of silence
    audio_segments = [
        AudioSegment.from_mp3(io.BytesIO(audio)) + silence for audio in audios
    ]
    # combine the audio segments
    combined = sum(audio_segments, AudioSegment.empty())
    # save to a file
    result = combined.export(format="mp3")
    return upload_fileobj(result, "a-to-p", f"{ episode_id }.mp3")  # type: ignore


def upload_fileobj(fileobj: BytesIO, bucket: str, key: str) -> str:
    import boto3

    settings = get_settings()
    client = boto3.client(
        "s3",
        endpoint_url=settings.bucket_url,
        aws_access_key_id=settings.bucket_access_key_id,
        aws_secret_access_key=settings.bucket_secret_access_key,
    )
    response = client.upload_fileobj(
        fileobj,  # type: ignore
        bucket,
        key,
        ExtraArgs={"ACL": "public-read"},
    )  # type: ignore
    print(response)
    # check the path exists
    # url should be https://646290bc1d3bb40acc9629e92c0b0bf5.r2.cloudflarestorage.com/a-to-p/episode.mp3
    if not settings.bucket_public_url:
        raise Exception("bucket_public_url not set")
    return settings.bucket_public_url + "/" + key


@app.get("/api/python")
def hello_world(settings: Annotated[Settings, Depends(get_settings)]):
    # print the environment

    return {"message": "hello world"}


class CreateEpisodeRequest(BaseModel):
    article_text: str


async def generate_episode_with_id(id: str):
    settings = get_settings()
    import uuid

    # update episode to processing
    async for session in get_session():
        episode = await crud_episode.get(session, uuid.UUID(id))
        if episode is None:
            return
        episode = await crud_episode.update(
            session, db_obj=episode, obj_in={"status": "processing"}
        )
        result = await generate_episode(episode.article_text, id)
        await crud_episode.update(
            session, db_obj=episode, obj_in={"status": "done", "url": result}
        )
        return result


@app.post("/api/episode_create_task")
async def episode_create_task(
    create_episode_request: CreateEpisodeRequest,
    background_tasks: BackgroundTasks,
    session: AsyncSession = Depends(get_session),
) -> Episode:
    id = uuid.uuid4()
    print(str(id))
    episode = Episode(
        id=id,
        status="started",
        url="",
        article_text=create_episode_request.article_text,
    )
    session.add(episode)
    await session.commit()
    await session.refresh(episode)
    print(episode)
    background_tasks.add_task(generate_episode_with_id, str(id))
    return episode


@app.get("/api/episode/{id}")
async def episode_get(
    id: str,
    settings: Annotated[Settings, Depends(get_settings)],
    session: AsyncSession = Depends(get_session),
) -> Episode:
    episode = await crud_episode.get(session, uuid.UUID(id))
    if episode is None:
        return Episode(id=uuid.UUID(id), status="not found", url="", article_text="")
    return episode


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # hello_world()


if __name__ == "__main__":
    main()
