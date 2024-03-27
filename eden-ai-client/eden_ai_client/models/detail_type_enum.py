from enum import Enum


class DetailTypeEnum(str, Enum):
    DOCUMENT_TYPE = "document_type"
    RESOLUTION = "resolution"

    def __str__(self) -> str:
        return str(self.value)
