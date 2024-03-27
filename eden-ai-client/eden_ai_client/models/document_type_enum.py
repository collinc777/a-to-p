from enum import Enum


class DocumentTypeEnum(str, Enum):
    AUTO_DETECT = "auto-detect"
    INVOICE = "invoice"
    RECEIPT = "receipt"

    def __str__(self) -> str:
        return str(self.value)
