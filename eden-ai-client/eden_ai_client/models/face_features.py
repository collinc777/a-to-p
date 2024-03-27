from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FaceFeatures")


@_attrs_define
class FaceFeatures:
    """
    Attributes:
        eyes_open (int):
        smile (int):
        mouth_open (int):
    """

    eyes_open: int
    smile: int
    mouth_open: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        eyes_open = self.eyes_open

        smile = self.smile

        mouth_open = self.mouth_open

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eyes_open": eyes_open,
                "smile": smile,
                "mouth_open": mouth_open,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        eyes_open = d.pop("eyes_open")

        smile = d.pop("smile")

        mouth_open = d.pop("mouth_open")

        face_features = cls(
            eyes_open=eyes_open,
            smile=smile,
            mouth_open=mouth_open,
        )

        face_features.additional_properties = d
        return face_features

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
