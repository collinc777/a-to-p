from functools import lru_cache
from typing import Annotated, List, Literal, Optional
from fastapi import Depends, FastAPI
import uvicorn
import os
from llama_index.program import OpenAIPydanticProgram
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    openai_api_key: Optional[str] = None


@lru_cache()
def get_settings():
    return Settings()


app = FastAPI()


class TranscriptLine(BaseModel):
    """A line of the transcript"""

    # speaker is one of narrator, collin, or allison
    speaker: Literal["narrator", "collin", "allison"]
    text: str


class Transcript(BaseModel):
    """The transcript of the podcast episode"""

    transcript_lines: List[TranscriptLine]


@app.get("/api/python")
def hello_world(settings: Annotated[Settings, Depends(get_settings)]) -> Transcript:
    # print the environment
    print(os.environ)

    program = OpenAIPydanticProgram.from_defaults(
        output_cls=Transcript,  # type: ignore
        prompt_template_str="Generate a fake podcast transcript",
        verbose=True,
    )
    output: Transcript = program()  # type: ignore
    return output


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # hello_world()


if __name__ == "__main__":
    main()
