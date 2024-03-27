from enum import Enum


class TypeEnum(str, Enum):
    AI = "ai"
    BUCKET = "bucket"
    DB = "db"
    DB_VECTOR = "db_vector"

    def __str__(self) -> str:
        return str(self.value)
