from enum import Enum


class FinalStatusEnum(str, Enum):
    FAIL = "fail"
    SUCESS = "sucess"

    def __str__(self) -> str:
        return str(self.value)
