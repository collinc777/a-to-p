from enum import Enum


class PersonalInformationSubCategoryType(str, Enum):
    AGE = "Age"
    EMAIL = "Email"
    NAME = "Name"
    PERSONTYPE = "PersonType"
    PHONE = "Phone"

    def __str__(self) -> str:
        return str(self.value)
