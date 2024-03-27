from enum import Enum


class OtherSubCategoryType(str, Enum):
    OFFENSIVE = "Offensive"
    OTHER = "Other"
    RELIGION = "Religion"
    SPOOF = "Spoof"

    def __str__(self) -> str:
        return str(self.value)
