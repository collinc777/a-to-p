from fastapi import FastAPI
from llama_index.program import OpenAIPydanticProgram
from pydantic import BaseModel

app = FastAPI()


class Transcript(BaseModel):
    """The transcript of the podcast episode"""

    content: str


@app.get("/api/python")
def hello_world():
    program = OpenAIPydanticProgram.from_defaults(
        output_cls=Transcript,
        prompt_template_str="Generate a fake podcast transcript",
        verbose=True,
    )
    output = program()
    return {"message": "Hello World"}
