from enum import Enum


class XMergeListProjectTypeEnum(str, Enum):
    DOC_PARSER = "DOC_PARSER"
    TEXT = "TEXT"

    def __str__(self) -> str:
        return str(self.value)
