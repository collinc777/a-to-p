from enum import Enum


class ContentSubCategoryType(str, Enum):
    EXPLICIT = "Explicit"
    HEALTH = "Health"
    LEGAL = "Legal"
    MEDICAL = "Medical"
    MIDDLEFINGER = "MiddleFinger"
    POLITICS = "Politics"
    PUBLICSAFETY = "PublicSafety"
    QRCODE = "QRCode"

    def __str__(self) -> str:
        return str(self.value)
