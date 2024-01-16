from typing import Literal, List
import uuid
from pydantic import BaseModel
from sqlmodel import Field, SQLModel


Speaker = Literal["narrator", "jake", "emily"]


class TranscriptLine(BaseModel):
    """A line of the transcript"""

    # speaker is one of narrator, Jake, or emily
    speaker: Speaker
    text: str


class Transcript(BaseModel):
    """The transcript of the podcast episode"""

    transcript_lines: List[TranscriptLine]


class Episode(SQLModel, table=True):
    id: str = Field(default_factory=uuid.uuid4, primary_key=True)
    status: str
    url: str
