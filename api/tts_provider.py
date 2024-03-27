import json
from typing import Literal
import aiolimiter
import openai
from openapi_client.api.text_to_speech_api import TextToSpeechApi
from openapi_client.models.audiotext_to_speech_text_to_speech_request import (
    AudiotextToSpeechTextToSpeechRequest,
)
from tenacity import retry, stop_after_attempt, wait_exponential

from api.settings import get_settings


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

    @classmethod
    async def eden_speak(cls, text: str, voice: OpenAIVoice):
        from eden_ai_client.api.text_to_speech.audio_audio_text_to_speech_create import (
            asyncio_detailed,
        )
        from eden_ai_client.models import AudiotextToSpeechTextToSpeechRequest
        from eden_ai_client import AuthenticatedClient

        client = AuthenticatedClient(
            "https://api.edenai.run/v2/",
            token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiOGQzNTk1MWItZmYzMS00YzMwLThiMjctZDAwMDkyZTE1ODMyIiwidHlwZSI6ImFwaV90b2tlbiJ9.B0yC9SUySSXKMt7pHbezxn9ArRogG56hl0k8VkTp9KU",
        )
        async with client as client:
            response = await asyncio_detailed(
                client=client,
                body=AudiotextToSpeechTextToSpeechRequest(
                    providers="openai",
                    text=text,
                    settings=json.dumps({"openai": f"en_{voice}"}),
                ),
            )
            print(response)

    @classmethod
    async def eden_speak_2(cls, text: str, voice: OpenAIVoice):
        from openapi_client.configuration import Configuration
        from openapi_client.api_client import ApiClient

        configuration = Configuration(
            access_token=get_settings().edenai_api_key,
        )
        with ApiClient(configuration) as api_client:
            api_instance = TextToSpeechApi(api_client)
            body = AudiotextToSpeechTextToSpeechRequest(
                providers="openai",
                text=text,
                settings=json.dumps({"openai": f"en_{voice}"}),
            )
            api_response = api_instance.audio_audio_text_to_speech_create(body)
            api_response.openai
            print(api_response)


if __name__ == "__main__":
    import asyncio

    async def main():
        await OpenAITTSProvider.eden_speak_2("Hello", "alloy")

    asyncio.run(main())
