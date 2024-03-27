from enum import Enum


class FinanceSubCategoryType(str, Enum):
    FINANCE = "Finance"
    GAMBLING = "Gambling"
    MONEYCONTENT = "MoneyContent"

    def __str__(self) -> str:
        return str(self.value)
