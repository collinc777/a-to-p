from enum import Enum


class PriceUnitTypeEnum(str, Enum):
    CHAR = "char"
    EXEC_TIME = "exec_time"
    FILE = "file"
    FREE = "free"
    HOUR = "hour"
    IMAGE = "image"
    MINUTE = "minute"
    PAGE = "page"
    REQUEST = "request"
    SECONDE = "seconde"
    SIZE = "size"
    TOKEN = "token"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
