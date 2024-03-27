from enum import Enum


class TypeOfDataEnum(str, Enum):
    TEST = "TEST"
    TRAINING = "TRAINING"

    def __str__(self) -> str:
        return str(self.value)
