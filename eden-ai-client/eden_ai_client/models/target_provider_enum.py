from enum import Enum


class TargetProviderEnum(str, Enum):
    COHERE = "cohere"
    GOOGLE = "google"
    OPENAI = "openai"

    def __str__(self) -> str:
        return str(self.value)
