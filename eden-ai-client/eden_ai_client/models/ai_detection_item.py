from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AiDetectionItem")


@_attrs_define
class AiDetectionItem:
    """
    Attributes:
        text (str):
        prediction (str):
        ai_score (int):
        ai_score_detail (int):
    """

    text: str
    prediction: str
    ai_score: int
    ai_score_detail: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        prediction = self.prediction

        ai_score = self.ai_score

        ai_score_detail = self.ai_score_detail

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "prediction": prediction,
                "ai_score": ai_score,
                "ai_score_detail": ai_score_detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        prediction = d.pop("prediction")

        ai_score = d.pop("ai_score")

        ai_score_detail = d.pop("ai_score_detail")

        ai_detection_item = cls(
            text=text,
            prediction=prediction,
            ai_score=ai_score,
            ai_score_detail=ai_score_detail,
        )

        ai_detection_item.additional_properties = d
        return ai_detection_item

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
