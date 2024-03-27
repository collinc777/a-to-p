from enum import Enum


class StatusE80Enum(str, Enum):
    FAILED = "failed"
    FINISHED = "finished"
    PROCESSING = "processing"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
