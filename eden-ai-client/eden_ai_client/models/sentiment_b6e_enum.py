from enum import Enum


class SentimentB6EEnum(str, Enum):
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"
    POSITIVE = "Positive"

    def __str__(self) -> str:
        return str(self.value)
