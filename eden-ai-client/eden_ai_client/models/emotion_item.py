from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EmotionItem")


@_attrs_define
class EmotionItem:
    """This class is used in EmotionAnalysisDataClass to list emotion analysed.
    Args:
        - emotion (EmotionEnum): emotion of the text
        - emotion_score (float): score of the emotion


    Attributes:
        emotion (str):
        emotion_score (int):
    """

    emotion: str
    emotion_score: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        emotion = self.emotion

        emotion_score = self.emotion_score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emotion": emotion,
                "emotion_score": emotion_score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        emotion = d.pop("emotion")

        emotion_score = d.pop("emotion_score")

        emotion_item = cls(
            emotion=emotion,
            emotion_score=emotion_score,
        )

        emotion_item.additional_properties = d
        return emotion_item

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
