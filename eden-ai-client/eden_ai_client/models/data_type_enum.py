from enum import Enum


class DataTypeEnum(str, Enum):
    AUDIO = "audio"
    CSV = "csv"
    PDF = "pdf"

    def __str__(self) -> str:
        return str(self.value)
