from enum import Enum


class LocationInformationSubCategoryType(str, Enum):
    ADDRESS = "Address"
    LOCATION = "Location"

    def __str__(self) -> str:
        return str(self.value)
