from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PlagiaDetectionCandidate")


@_attrs_define
class PlagiaDetectionCandidate:
    """
    Attributes:
        url (str):
        plagia_score (int):
        prediction (str):
        plagiarized_text (str):
    """

    url: str
    plagia_score: int
    prediction: str
    plagiarized_text: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        plagia_score = self.plagia_score

        prediction = self.prediction

        plagiarized_text = self.plagiarized_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "plagia_score": plagia_score,
                "prediction": prediction,
                "plagiarized_text": plagiarized_text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        plagia_score = d.pop("plagia_score")

        prediction = d.pop("prediction")

        plagiarized_text = d.pop("plagiarized_text")

        plagia_detection_candidate = cls(
            url=url,
            plagia_score=plagia_score,
            prediction=prediction,
            plagiarized_text=plagiarized_text,
        )

        plagia_detection_candidate.additional_properties = d
        return plagia_detection_candidate

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
