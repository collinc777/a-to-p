from enum import Enum


class ToxicSubCategoryType(str, Enum):
    DEROGATORY = "Derogatory"
    INSULT = "Insult"
    OBSCENE = "Obscene"
    PROFANITY = "Profanity"
    THREAT = "Threat"
    TOXIC = "Toxic"

    def __str__(self) -> str:
        return str(self.value)
