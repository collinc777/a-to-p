import abc
from typing import AsyncIterator, Literal

from api.models import Speaker


class TTSProvider(abc.ABC):
    @abc.abstractmethod
    def speak(self, text: str, speaker: Speaker) -> AsyncIterator[bytes]:
        raise NotImplementedError("This method should be overridden by subclasses")

    @abc.abstractmethod
    def _get_voice_for_speaker(self, speaker: Speaker) -> str:
        """Get the voice for the speaker specific to the provider"""
        raise NotImplementedError("This method should be overridden by subclasses")


class OpenAITTSProvider(TTSProvider):
    def __init__(self):
        import openai

        self.client = openai.AsyncOpenAI()

    async def speak(self, text: str, speaker: Speaker) -> AsyncIterator[bytes]:
        import openai

        client = openai.AsyncOpenAI()
        voice = self._get_voice_for_speaker(speaker)
        response = await client.audio.speech.create(
            model="tts-1",
            input=text,
            voice=voice,  # type: ignore
        )
        result = await response.aiter_bytes()
        return result

    def _get_voice_for_speaker(self, speaker: Speaker):
        speaker_to_voice = {
            "narrator": "onyx",
            "jake": "echo",
            "emily": "nova",
        }
        return speaker_to_voice.get(speaker, "alloy")  # type: ignore


def get_tts_provider(provider: Literal["openai", "aws"]):
    match provider:
        case "openai":
            return OpenAITTSProvider()
        case "aws":
            raise NotImplementedError("AWS TTS not implemented yet")
        case _:
            raise ValueError(f"Unknown TTS provider {provider}")
