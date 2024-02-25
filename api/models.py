from enum import Enum
from typing import Literal, List, Optional
from datetime import datetime
import uuid
from pydantic import BaseModel, ConfigDict, model_validator
from sqlmodel import Field, SQLModel, Column
import strawberry

from api.sql_model_utils import pydantic_column_type


Speaker = Literal["narrator", "jake", "emily"]


class CreateEpisodeRequest(BaseModel):
    article_text: Optional[str] = None
    article_url: Optional[str] = None
    # either article_text or article_url must be provided

    @model_validator(mode="after")
    def check_article_text_or_url(self):
        article_text, article_url = (self.article_text, self.article_url)
        if not article_text and not article_url:
            raise ValueError("Either article_text or article_url must be provided")
        return self


@strawberry.enum
class EpisodeStatus(str, Enum):
    done = "done"
    failed = "failed"
    generating_audio = "generating_audio"
    generating_transcript = "generating_transcript"
    processing = "processing"
    started = "started"


class ExtractedArticle(SQLModel):
    title: str
    text: str
    author: Optional[str]
    url: Optional[str]
    hostname: Optional[str]
    description: Optional[str]
    sitename: Optional[str]
    date: Optional[str]
    # allow extra
    model_config = ConfigDict(extra="allow")


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


class UpdateEpisodeInput(SQLModel):
    title: Optional[str] = None
    url: Optional[str] = None
    article_text: Optional[str] = None
    transcript: Optional[Transcript] = None
    extracted_article: Optional[ExtractedArticle] = None


class UpdateEpisodeDBInput(UpdateEpisodeInput):
    status: Optional[EpisodeStatus] = None


class Episode(SQLModelBaseModel, table=True):
    title: Optional[str]
    status: EpisodeStatus
    url: str = Field(default=None, nullable=True)
    article_text: str
    transcript: Optional[Transcript] = Field(
        sa_column=Column(pydantic_column_type(Transcript)), default=None
    )
    extracted_article: Optional[ExtractedArticle] = Field(
        sa_column=Column(pydantic_column_type(ExtractedArticle)), default=None
    )
