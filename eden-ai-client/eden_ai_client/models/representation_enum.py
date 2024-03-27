from enum import Enum


class RepresentationEnum(str, Enum):
    DOCUMENT = "document"
    QUERY = "query"
    SYMETRIC = "symetric"

    def __str__(self) -> str:
        return str(self.value)
