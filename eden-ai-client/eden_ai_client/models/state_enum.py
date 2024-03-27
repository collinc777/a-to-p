from enum import Enum


class StateEnum(str, Enum):
    FAILED = "failed"
    FINISHED = "finished"
    PROCESSING = "processing"
    TIMEOUT_ERROR = "Timeout error"

    def __str__(self) -> str:
        return str(self.value)
