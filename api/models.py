from enum import Enum
import hashlib
from typing import Literal, List, Optional
from datetime import datetime
import uuid
from pydantic import BaseModel, ConfigDict, computed_field, model_validator
from sqlmodel import Field, SQLModel, Column
import strawberry

from api.sql_model_utils import pydantic_column_type


Speaker = Literal["narrator", "jake", "emily", "dillon"]


class SQLModelBaseModel(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=True)
    last_edited: datetime = Field(default_factory=datetime.utcnow, nullable=True)


def Relationship(*, back_populates: str):
    from sqlmodel import Relationship as SQLModelRelationship

    return SQLModelRelationship(
        back_populates=back_populates, sa_relationship_kwargs={"lazy": "selectin"}
    )


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
class EpisodeFormatType(str, Enum):
    monologue = "monologue"
    dialogue = "dialogue"
    interview = "interview"
    panel = "panel"
    educational = "educational"
    storytelling = "storytelling"
    news_current_events = "news_current_events"
    tts = "tts"


@strawberry.enum
class EpisodeStatus(str, Enum):
    done = "done"
    failed = "failed"
    generating_audio = "generating_audio"
    generating_transcript = "generating_transcript"
    processing = "processing"
    started = "started"
    not_found = "not_found"


class ExtractedArticleModel(SQLModelBaseModel, table=True):
    title: str
    text: str
    author: Optional[str]
    url: Optional[str]
    hostname: Optional[str]
    description: Optional[str]
    sitename: Optional[str]
    date: Optional[str]
    episode: Optional["Episode"] = Relationship(back_populates="extracted_article")
    # allow extra
    model_config = ConfigDict(extra="allow")


class TranscriptLine(BaseModel):
    """A line of the transcript"""

    # speaker is one of narrator, Jake, or emily
    speaker: str
    text: str
    line_hash: Optional[str] = None
    audio_url: Optional[str] = None

    @computed_field
    @property
    def computed_line_hash(self) -> str:
        input_str = f"{self.speaker}-{self.text}"
        hash_object = hashlib.sha256(input_str.encode())
        hex_dig = hash_object.hexdigest()
        return hex_dig

    @computed_field
    @property
    def audio_url_id(self) -> Optional[str]:
        if not self.audio_url:
            return None
        return self.audio_url.split("/")[-1]


class Transcript(BaseModel):
    """The transcript of the podcast episode"""

    transcript_lines: List[TranscriptLine]


class UpdateEpisodeInput(SQLModel):
    title: Optional[str] = None
    url: Optional[str] = None
    article_text: Optional[str] = None
    transcript: Optional[Transcript] = None
    episode_hash: Optional[str] = None


class UpdateEpisodeDBInput(UpdateEpisodeInput):
    status: Optional[EpisodeStatus] = None


@strawberry.enum
class VoiceProvider(str, Enum):
    openai = "openai"
    aws = "aws"
    playht = "playht"


@strawberry.enum
class VoiceCategory(str, Enum):
    male = "male"
    female = "female"
    kid = "kid"


class Voice(SQLModelBaseModel, table=True):
    speaker_name: str
    voice_category: VoiceCategory
    provider: VoiceProvider
    voice_provider_voice_id: str
    sample_output: str


class EpisodeFormat(SQLModelBaseModel, table=True):
    display_value: str = Field(unique=True)
    episode_format_type: EpisodeFormatType = Field(unique=True)
    episodes: List["Episode"] = Relationship(back_populates="episode_format")
    index: int


class Episode(SQLModelBaseModel, table=True):
    title: Optional[str]
    status: EpisodeStatus
    episode_format_id: uuid.UUID = Field(foreign_key="episodeformat.id")
    episode_format: EpisodeFormat = Relationship(back_populates="episodes")
    url: str = Field(default=None, nullable=True)
    article_text: str
    transcript: Optional[Transcript] = Field(
        sa_column=Column(pydantic_column_type(Transcript)), default=None
    )
    extracted_article: Optional[ExtractedArticleModel] = Relationship(
        back_populates="episode"
    )
    extracted_article_id: Optional[uuid.UUID] = Field(
        foreign_key="extractedarticlemodel.id", nullable=True
    )
    episode_hash: Optional[str] = None

    @computed_field
    @property
    def computed_episode_hash(self) -> Optional[str]:
        if self.transcript is None:
            return None
        transcript_lines = self.transcript.transcript_lines
        input_str = f"{transcript_lines}"
        hash_object = hashlib.sha256(input_str.encode())
        hex_dig = hash_object.hexdigest()
        return hex_dig

    @computed_field
    @property
    def audio_url_id(self) -> Optional[str]:
        if not self.url:
            return None
        return self.url.split("/")[-1]


class Section(BaseModel):
    title: str
    content: str
    subsections: List["Section"]
