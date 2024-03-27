from enum import Enum


class ViolenceSubCategoryType(str, Enum):
    GRAPHICVIOLENCEORGORE = "GraphicViolenceOrGore"
    PHYSICALVIOLENCE = "PhysicalViolence"
    VIOLENCE = "Violence"
    WEAPONVIOLENCE = "WeaponViolence"

    def __str__(self) -> str:
        return str(self.value)
