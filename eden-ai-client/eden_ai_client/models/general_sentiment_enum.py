from enum import Enum


class GeneralSentimentEnum(str, Enum):
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"
    POSITIVE = "Positive"

    def __str__(self) -> str:
        return str(self.value)
