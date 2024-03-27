from enum import Enum


class StatusF43Enum(str, Enum):
    FAIL = "fail"
    SUCESS = "sucess"

    def __str__(self) -> str:
        return str(self.value)
