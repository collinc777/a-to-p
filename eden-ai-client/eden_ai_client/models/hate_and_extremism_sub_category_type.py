from enum import Enum


class HateAndExtremismSubCategoryType(str, Enum):
    EXTREMIST = "Extremist"
    HARASSMENT = "Harassment"
    HATE = "Hate"
    RACY = "Racy"
    THREATENING = "Threatening"

    def __str__(self) -> str:
        return str(self.value)
