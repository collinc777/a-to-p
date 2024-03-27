from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sentiment_b6e_enum import SentimentB6EEnum

T = TypeVar("T", bound="SegmentSentimentAnalysisDataClass")


@_attrs_define
class SegmentSentimentAnalysisDataClass:
    """This class is used in SentimentAnalysisDataClass to describe each segment analyzed.

    Args:
        - segment (str): The segment analyzed
        - sentiment (Literal['Positve', 'Negative', 'Neutral']) (Case is ignore): Sentiment of segment
        - sentiment_rate (float between 0 and 1): Rate of sentiment


    Attributes:
        segment (str):
        sentiment (SentimentB6EEnum):
        sentiment_rate (int):
    """

    segment: str
    sentiment: SentimentB6EEnum
    sentiment_rate: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        segment = self.segment

        sentiment = self.sentiment.value

        sentiment_rate = self.sentiment_rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "segment": segment,
                "sentiment": sentiment,
                "sentiment_rate": sentiment_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        segment = d.pop("segment")

        sentiment = SentimentB6EEnum(d.pop("sentiment"))

        sentiment_rate = d.pop("sentiment_rate")

        segment_sentiment_analysis_data_class = cls(
            segment=segment,
            sentiment=sentiment,
            sentiment_rate=sentiment_rate,
        )

        segment_sentiment_analysis_data_class.additional_properties = d
        return segment_sentiment_analysis_data_class

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
