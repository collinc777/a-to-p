from enum import Enum


class SexualSubCategoryType(str, Enum):
    ADULTTOYS = "AdultToys"
    NUDITY = "Nudity"
    PARTIALNUDITY = "PartialNudity"
    REVEALINGCLOTHES = "RevealingClothes"
    SEXUAL = "Sexual"
    SEXUALACTIVITY = "SexualActivity"
    SEXUALSITUATIONS = "SexualSituations"
    SUGGESTIVE = "Suggestive"

    def __str__(self) -> str:
        return str(self.value)
