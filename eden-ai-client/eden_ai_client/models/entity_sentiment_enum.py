from enum import Enum


class EntitySentimentEnum(str, Enum):
    MIXED = "Mixed"
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"
    POSITIVE = "Positive"

    def __str__(self) -> str:
        return str(self.value)
