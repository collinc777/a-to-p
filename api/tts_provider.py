import json
import base64
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
                audio_format="mp3",
                settings=json.dumps({"openai": f"en_{voice}"}),
            )
            api_response = api_instance.audio_audio_text_to_speech_create(body)
            api_response.openai
            if not api_response.openai:
                raise Exception("No response from EdenAI")
            return base64.b64decode(str(api_response.openai.audio))
