from enum import Enum


class ResolutionEnum(str, Enum):
    VALUE_0 = "256x256"
    VALUE_1 = "512x512"
    VALUE_2 = "1024x1024"

    def __str__(self) -> str:
        return str(self.value)
