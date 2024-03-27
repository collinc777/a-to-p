from enum import Enum


class DbProviderEnum(str, Enum):
    QDRANT = "qdrant"
    SUPABASE = "supabase"

    def __str__(self) -> str:
        return str(self.value)
