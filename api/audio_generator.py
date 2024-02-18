from io import BytesIO
from api import crud_episode
from api.crud_episode import CRUDEpisode
from api.db import get_session_context
from api.models import Transcript
from api.settings import get_settings
from api.tts_provider import TTSProvider, get_tts_provider


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


async def generate_episode_audio(id: str):
    import uuid

    # update episode to processing
    async with get_session_context() as session:
        episode = await CRUDEpisode.get(session, uuid.UUID(id))
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
