from functools import lru_cache
import uuid
from typing import Annotated, Optional
from fastapi import BackgroundTasks, Depends, FastAPI
from fastapi.responses import StreamingResponse
import uvicorn
from llama_index.program import OpenAIPydanticProgram
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from api.custom_types import Transcript

from api.tts_provider import get_tts_provider, TTSProvider

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    openai_api_key: Optional[str] = None
    aws_access_key_id: Optional[str] = None
    aws_secret_access_key: Optional[str] = None
    aws_region: Optional[str] = None
    aws_default_region: Optional[str] = None
    replicate_api_token: Optional[str] = None


@lru_cache()
def get_settings():
    return Settings()


app = FastAPI()


async def generate_episode(article_text: str):
    transcript_body = await generate_transcript_body(article_text)
    provider = get_tts_provider("openai")
    audio = await generate_audio(transcript_body, provider)
    return audio


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


async def generate_audio(transcript: Transcript, provider: TTSProvider):
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
    return result


@app.get("/api/python")
def hello_world(settings: Annotated[Settings, Depends(get_settings)]):
    # print the environment

    return {"message": "hello world"}


class CreateEpisodeRequest(BaseModel):
    article_text: str


database = {}


async def generate_episode_with_id(id: str, article_text: str):
    database[id] = {"state": "processing"}
    result = await generate_episode(article_text)
    database[id]["state"] = "done"
    database[id]["result"] = result
    return result


@app.post("/api/episode_create_task")
async def episode_create_task(
    create_episode_request: CreateEpisodeRequest, background_tasks: BackgroundTasks
):
    id = uuid.uuid4()
    print(str(id))
    background_tasks.add_task(
        generate_episode_with_id, str(id), create_episode_request.article_text
    )

    return {"status": "success"}


@app.get("/api/episode/{id}")
async def episode_get(id: str):
    if id not in database:
        return {"status": "not found"}
    if database[id]["state"] == "processing":
        return {"status": "processing"}
    if database[id]["state"] == "done":
        return StreamingResponse(database[id]["result"], media_type="audio/mpeg")


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # hello_world()


if __name__ == "__main__":
    main()
