from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VideoPersonQuality")


@_attrs_define
class VideoPersonQuality:
    """
    Attributes:
        brightness (int):
        sharpness (int):
    """

    brightness: int
    sharpness: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        brightness = self.brightness

        sharpness = self.sharpness

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "brightness": brightness,
                "sharpness": sharpness,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        brightness = d.pop("brightness")

        sharpness = d.pop("sharpness")

        video_person_quality = cls(
            brightness=brightness,
            sharpness=sharpness,
        )

        video_person_quality.additional_properties = d
        return video_person_quality

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
