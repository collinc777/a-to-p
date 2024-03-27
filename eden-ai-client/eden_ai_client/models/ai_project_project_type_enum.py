from enum import Enum


class AIProjectProjectTypeEnum(str, Enum):
    ASKYODA = "AskYoDa"
    TRANSLATHOR = "Translathor"
    X_MERGE = "X-Merge"

    def __str__(self) -> str:
        return str(self.value)
