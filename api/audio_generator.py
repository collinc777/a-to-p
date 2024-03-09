from io import BytesIO
import aioboto3
from typing import Tuple
from api.models import Episode, TranscriptLine
from api.settings import get_settings
from api.tts_provider import TTSProvider, get_tts_provider


async def generate_audio_for_line(
    *,
    line: TranscriptLine,
    provider: TTSProvider,
) -> Tuple[TranscriptLine, bytes]:
    if line.audio_url_id == line.computed_line_hash:
        audio_bytes = await get_file_obj(line.audio_url)
        return line, audio_bytes
    # use tts to generate audio
    audio = await provider.speak(
        text=line.text,
        speaker=line.speaker.lower(),
    )
    # save to a file
    audio_url = await upload_fileobj(
        BytesIO(audio), "a-to-p", f"line/{ line.computed_line_hash }.wav"
    )  # type: ignore
    line.audio_url = audio_url
    line.line_hash = line.computed_line_hash
    return line, audio


async def generate_audio(
    *,
    episode: Episode,
    provider: TTSProvider,
) -> str:
    # use tts to generate audio
    lines = episode.transcript.transcript_lines
    tasks = [generate_audio_for_line(line=line, provider=provider) for line in lines]
    import asyncio
    import io

    task_results = await asyncio.gather(*tasks)
    # convert byte strings to audio segments and add silence between them
    from pydub import AudioSegment

    silence = AudioSegment.silent(duration=500)  # 500 milliseconds of silence
    audio_segments = [
        AudioSegment.from_mp3(io.BytesIO(audio)) + silence for _, audio in task_results
    ]
    # combine the audio segments
    combined = sum(audio_segments, AudioSegment.empty())
    # save to a file
    result = combined.export(format="mp3")
    episode.episode_hash = episode.computed_episode_hash
    return await upload_fileobj(
        result, "a-to-p", f"episode/{ episode.episode_hash }.mp3"
    )  # type: ignore


async def generate_episode_audio(episode: Episode):
    # update episode to processing
    if episode.transcript is None:
        raise ValueError("Transcript not found")
    provider = get_tts_provider("openai")
    url = await generate_audio(episode=episode, provider=provider)
    return url


async def upload_fileobj(fileobj: BytesIO, bucket: str, key: str) -> str:
    settings = get_settings()
    session = aioboto3.Session()
    async with session.client(
        "s3",
        endpoint_url=settings.bucket_url,
        aws_access_key_id=settings.bucket_access_key_id,
        aws_secret_access_key=settings.bucket_secret_access_key,
    ) as client:
        response = await client.upload_fileobj(
            fileobj,
            bucket,
            key,
            ExtraArgs={"ACL": "public-read"},
        )  # type: ignore
        # check the path exists
        # url should be https://646290bc1d3bb40acc9629e92c0b0bf5.r2.cloudflarestorage.com/a-to-p/episode.mp3
        if not settings.bucket_public_url:
            raise Exception("bucket_public_url not set")
        return settings.bucket_public_url + "/" + key


async def get_file_obj(url: str) -> bytes:
    settings = get_settings()
    session = aioboto3.Session()
    async with session.client(
        "s3",
        endpoint_url=settings.bucket_url,
        aws_access_key_id=settings.bucket_access_key_id,
        aws_secret_access_key=settings.bucket_secret_access_key,
    ) as client:
        response = await client.get_object(Bucket="a-to-p", Key=url)
        return response["Body"].read()
