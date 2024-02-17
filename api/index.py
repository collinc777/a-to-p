import uuid

from fastapi.responses import StreamingResponse

from api.longform_episode_generator import (
    generate_episode_longform,
    generate_episode_shortform,
)
from api.crud_episode import crud_episode
from functools import lru_cache
from io import BytesIO
from typing import Annotated, Optional, AsyncGenerator
from fastapi import BackgroundTasks, Depends, FastAPI
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
import uvicorn
from pydantic import BaseModel, ConfigDict, Extra, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from api.models import Episode, ExtractedArticle, Transcript
import sentry_sdk

from api.tts_provider import get_tts_provider, TTSProvider

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="allow")
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
    sentry_dsn: Optional[str] = None


@lru_cache()
def get_settings():
    return Settings()


sentry_sdk.init(
    dsn=get_settings().sentry_dsn,
    traces_sample_rate=0.0,
    profiles_sample_rate=0.0,
)

engine = AsyncEngine(create_engine(get_settings().database_url))  # type: ignore


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)  # type: ignore
    async with async_session() as session:  # type: ignore
        yield session  # type: ignore


app = FastAPI()


async def generate_audio(
    *,
    transcript: Transcript,
    provider: TTSProvider,
    episode_id: str,
) -> str:
    # use tts to generate audio
    lines = transcript.transcript_lines
    tasks = [
        provider.speak(
            text=line.text,
            speaker=line.speaker.lower(),  # type: ignore
        )
        for line in lines
    ]
    import asyncio
    import io

    audios = await asyncio.gather(*tasks)  # type: ignore
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
    article_text: Optional[str] = None
    article_url: Optional[str] = None
    # either article_text or article_url must be provided

    @model_validator(mode="after")
    def check_article_text_or_url(self):
        article_text, article_url = (self.article_text, self.article_url)
        if not article_text and not article_url:
            raise ValueError("Either article_text or article_url must be provided")
        return self


async def generate_episode_audio(id: str):
    import uuid

    # update episode to processing
    async for session in get_session():
        episode = await crud_episode.get(session, uuid.UUID(id))
        if episode is None:
            raise ValueError("Episode not found")
        if episode.transcript is None:
            raise ValueError("Transcript not found")
        provider = get_tts_provider("openai")
        url = await generate_audio(
            transcript=episode.transcript, provider=provider, episode_id=id
        )
        await crud_episode.update(
            session, db_obj=episode, obj_in={"status": "done", "url": url}
        )
        return url


@app.post("/api/stream_episode_create_task")
async def stream_episode_create_task(
    create_episode_request: CreateEpisodeRequest,
    background_tasks: BackgroundTasks,
    session: AsyncSession = Depends(get_session),
):
    id = uuid.uuid4()
    article = None
    article_text = ""
    if create_episode_request.article_url:
        article = get_extracted_article(create_episode_request.article_url)
        article_text = article.text

    if create_episode_request.article_text:
        article_text = create_episode_request.article_text

    print(str(id))
    episode = Episode(
        id=id,
        status="started",
        url="",
        article_text=article_text,
        title=article.title if article and article.title else "Untitled",
        extracted_article=article,
    )
    session.add(episode)
    await session.commit()
    await session.refresh(episode)

    async def generate(episode: Episode):
        import json

        episode = await crud_episode.update(
            session, db_obj=episode, obj_in={"status": "generating_transcript"}
        )

        resulting_longform = generate_episode_longform(article_text)
        model_ref = None
        messages = []
        async for message in resulting_longform:
            messages.append(message)
            transcript = Transcript(transcript_lines=messages)
            payload = {"id": str(id), "transcript": transcript.model_dump()}
            yield f"data: {json.dumps(payload)}[SENTINEL]\n\n"
            model_ref = transcript
        episode = await crud_episode.update(
            session,
            db_obj=episode,
            obj_in={
                "transcript": Transcript(**model_ref.model_dump()),  # type: ignore
                "status": "generating_audio",
            },
        )
        background_tasks.add_task(generate_episode_audio, str(id))
        yield "data: [DONE]\n\n"

    return StreamingResponse(generate(episode=episode), media_type="text/event-stream")


@app.get("/api/episode/{id}")
async def episode_get(
    id: str,
    settings: Annotated[Settings, Depends(get_settings)],
    session: AsyncSession = Depends(get_session),
) -> Episode:
    episode = await crud_episode.get(session, uuid.UUID(id))
    if episode is None:
        return Episode(
            title="Not found",
            id=uuid.UUID(id),
            status="not found",
            url="",
            article_text="",
        )
    return episode


def get_extracted_article(url: str) -> ExtractedArticle:
    import trafilatura

    response = trafilatura.fetch_url(url)
    if not isinstance(response, str):
        raise Exception("response is not a string")

    t = trafilatura.bare_extraction(response)
    article = ExtractedArticle.model_validate(t)
    return article


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # hello_world()


if __name__ == "__main__":
    main()
