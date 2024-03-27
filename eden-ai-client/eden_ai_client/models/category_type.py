from enum import Enum


class CategoryType(str, Enum):
    CONTENT = "Content"
    DRUGANDALCOHOL = "DrugAndAlcohol"
    FINANCE = "Finance"
    HATEANDEXTREMISM = "HateAndExtremism"
    OTHER = "Other"
    SAFE = "Safe"
    SEXUAL = "Sexual"
    TOXIC = "Toxic"
    VIOLENCE = "Violence"

    def __str__(self) -> str:
        return str(self.value)
