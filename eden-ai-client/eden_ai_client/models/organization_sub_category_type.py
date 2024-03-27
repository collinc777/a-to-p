from enum import Enum


class OrganizationSubCategoryType(str, Enum):
    BUISNESSNUMBER = "BuisnessNumber"
    COMPANYNAME = "CompanyName"
    COMPANYNUMBER = "CompanyNumber"

    def __str__(self) -> str:
        return str(self.value)
