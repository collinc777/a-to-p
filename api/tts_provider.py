from typing import Literal
import aiolimiter
import openai
from tenacity import retry, stop_after_attempt, wait_exponential


limiter = aiolimiter.AsyncLimiter(49, 60)

OpenAIVoice = Literal["alloy", "echo", "fable", "onyx", "nova", "shimmer"]


class OpenAITTSProvider:
    client = openai.AsyncOpenAI()

    @classmethod
    @retry(
        wait=wait_exponential(multiplier=1, max=60),
        stop=stop_after_attempt(5),
    )
    async def speak(cls, text: str, voice: OpenAIVoice):
        async with limiter:
            response = await cls.client.audio.speech.create(
                model="tts-1",
                input=text,
                voice=voice,
            )
            result = await response.aread()
            return result
