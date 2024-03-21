from io import BytesIO
from typing import Literal

from pydantic import AnyUrl, HttpUrl
from api.audio_generator import upload_fileobj
from api.models import Voice, VoiceCategory, VoiceProvider
import openai
import uuid
from api.db import get_session_context

sample_string = "The quick brown fox jumps over the lazy dog"


async def run():
    async with get_session_context() as session:
        voice_id = uuid.uuid4()
        voice = Voice(
            id=voice_id,
            provider=VoiceProvider.openai,
            speaker_name="echo",
            voice_category=VoiceCategory.male,
            voice_provider_voice_id="echo",
            sample_output=await open_ai_speak_and_upload("echo"),
        )
        #   voice = Voice(
        #     id=voice_id,
        #     provider=VoiceProvider.openai,
        #     speaker_name="alloy",
        #     voice_category=VoiceCategory.male,
        #     voice_provider_voice_id="alloy",
        #     sample_output=await open_ai_speak_and_upload("alloy"),
        # )
        session.add(voice)
        await session.commit()


async def open_ai_speak_and_upload(
    voice: Literal["alloy", "echo", "fable", "onyx", "nova", "shimmer"],
) -> str:
    open_ai_client = openai.AsyncOpenAI()
    response = await open_ai_client.audio.speech.create(
        model="tts-1",
        input=sample_string,
        voice=voice,
    )
    result = await response.aread()
    audio_url = await upload_fileobj(
        BytesIO(result), "a-to-p", f"voice_samples/{uuid.uuid4()}.mp3"
    )
    return str(audio_url)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
