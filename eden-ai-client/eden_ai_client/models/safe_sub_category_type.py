from enum import Enum


class SafeSubCategoryType(str, Enum):
    NOTSAFE = "NotSafe"
    SAFE = "Safe"

    def __str__(self) -> str:
        return str(self.value)
