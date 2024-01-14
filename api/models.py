from typing import Literal, List
from pydantic import BaseModel


Speaker = Literal["narrator", "jake", "emily"]


class TranscriptLine(BaseModel):
    """A line of the transcript"""

    # speaker is one of narrator, Jake, or emily
    speaker: Speaker
    text: str


class Transcript(BaseModel):
    """The transcript of the podcast episode"""

    transcript_lines: List[TranscriptLine]
