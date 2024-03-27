from enum import Enum


class SimilarityMetricEnum(str, Enum):
    COSINE = "cosine"
    EUCLIDEAN = "euclidean"
    MANHATTAN = "manhattan"

    def __str__(self) -> str:
        return str(self.value)
