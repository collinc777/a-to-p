from enum import Enum


class DateAndTimeSubCategoryType(str, Enum):
    DATE = "Date"
    DATETIME = "DateTime"
    DURATION = "Duration"
    TIME = "Time"

    def __str__(self) -> str:
        return str(self.value)
