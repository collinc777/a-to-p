from enum import Enum


class FallbackTypeEnum(str, Enum):
    CONTINUE = "continue"
    RERUN = "rerun"

    def __str__(self) -> str:
        return str(self.value)
