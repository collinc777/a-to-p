from typing import Literal, List, Optional
from datetime import datetime
import uuid
from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Column

from api.sql_model_utils import pydantic_column_type


Speaker = Literal["narrator", "jake", "emily"]


class TranscriptLine(BaseModel):
    """A line of the transcript"""

    # speaker is one of narrator, Jake, or emily
    speaker: str
    text: str


class Transcript(BaseModel):
    """The transcript of the podcast episode"""

    transcript_lines: List[TranscriptLine]


class SQLModelBaseModel(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=True)
    last_edited: datetime = Field(default_factory=datetime.utcnow, nullable=True)


class Episode(SQLModelBaseModel, table=True):
    status: str
    url: str = Field(default=None, nullable=True)
    article_text: str
    transcript: Optional[Transcript] = Field(
        sa_column=Column(pydantic_column_type(Transcript)), default=None
    )
