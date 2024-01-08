from functools import lru_cache
from typing import Annotated, Optional
from fastapi import Depends, FastAPI
import uvicorn
import os
from llama_index.program import OpenAIPydanticProgram
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env.local")
    openai_api_key: Optional[str] = None


@lru_cache()
def get_settings():
    return Settings()


# print environment variables
print(os.environ)
# print the settings
print(get_settings())

app = FastAPI()


class Transcript(BaseModel):
    """The transcript of the podcast episode"""

    content: str


@app.get("/api/python")
def hello_world(settings: Annotated[Settings, Depends(get_settings)]):
    # print the environment
    print(os.environ)

    program = OpenAIPydanticProgram.from_defaults(
        output_cls=Transcript,  # type: ignore
        prompt_template_str="Generate a fake podcast transcript",
        verbose=True,
    )
    output = program()
    return {"message": "Hello World"}


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # hello_world()


if __name__ == "__main__":
    main()
