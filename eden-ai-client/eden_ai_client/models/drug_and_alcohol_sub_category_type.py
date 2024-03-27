from enum import Enum


class DrugAndAlcoholSubCategoryType(str, Enum):
    ALCOHOL = "Alcohol"
    DRINKING = "Drinking"
    DRUGPRODUCTS = "DrugProducts"
    DRUGUSE = "DrugUse"
    SMOKING = "Smoking"
    TOBACCO = "Tobacco"

    def __str__(self) -> str:
        return str(self.value)
