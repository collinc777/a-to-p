import abc
from typing import Literal

import aiolimiter
import openai
from tenacity import retry, stop_after_attempt, wait_exponential
from pyht import TTSOptions, Format, AsyncClient as phtClient


from api.models import Speaker
from api.settings import get_settings


class TTSProvider(abc.ABC):
    @classmethod
    @abc.abstractmethod
    async def speak(cls, text: str, speaker: Speaker) -> bytes:
        raise NotImplementedError("This method should be overridden by subclasses")

    @classmethod
    @abc.abstractmethod
    def _get_voice_for_speaker(cls, speaker: Speaker) -> str:
        """Get the voice for the speaker specific to the provider"""
        ...


limiter = aiolimiter.AsyncLimiter(49, 60)


class OpenAITTSProvider(TTSProvider):
    client = openai.AsyncOpenAI()

    @classmethod
    @retry(
        wait=wait_exponential(multiplier=1, max=60),
        stop=stop_after_attempt(5),
    )
    async def speak(cls, text: str, speaker: Speaker):
        async with limiter:
            voice = cls._get_voice_for_speaker(speaker)
            response = await cls.client.audio.speech.create(
                model="tts-1",
                input=text,
                voice=voice,  # type: ignore
            )
            result = await response.aread()
            return result

    @classmethod
    def _get_voice_for_speaker(cls, speaker: Speaker):
        speaker_to_voice = {
            "narrator": "onyx",
            "jake": "echo",
            "emily": "nova",
            "dillon": "onyx",
        }
        return speaker_to_voice.get(speaker, "alloy")


class PlayHtTTSProvider(TTSProvider):
    @classmethod
    def _get_voice_for_speaker(cls, speaker: Speaker) -> str:
        return ""

    @classmethod
    @retry(
        wait=wait_exponential(multiplier=1, max=50),
        stop=stop_after_attempt(5),
    )
    async def speak(cls, text: str, speaker: Speaker):
        client = phtClient(
            user_id=get_settings().playht_user_id,  # type: ignore
            api_key=get_settings().playht_secret_key,  # type: ignore
        )
        result = client.tts(
            text=text,
            options=TTSOptions(
                voice="s3://voice-cloning-zero-shot/028a32d4-6a79-4ca3-a303-d6559843114b/chris/manifest.json",
                format=Format.FORMAT_MP3,
            ),
            voice_engine="PlayHT2.0-turbo",
        )
        chunks = []
        async for chunk in result:
            chunks.append(chunk)

        return b"".join(chunks)


def get_tts_provider(provider: Literal["openai", "aws", "playht"]):
    match provider:
        case "openai":
            return OpenAITTSProvider()
        case "playht":
            return PlayHtTTSProvider()
        case "aws":
            raise NotImplementedError("AWS TTS not implemented yet")
        case _:
            raise ValueError(f"Unknown TTS provider {provider}")
