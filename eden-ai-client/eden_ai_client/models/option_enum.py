from enum import Enum


class OptionEnum(str, Enum):
    FEMALE = "FEMALE"
    MALE = "MALE"

    def __str__(self) -> str:
        return str(self.value)
