from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FaceOcclusions")


@_attrs_define
class FaceOcclusions:
    """
    Attributes:
        eye_occluded (bool):
        forehead_occluded (bool):
        mouth_occluded (bool):
    """

    eye_occluded: bool
    forehead_occluded: bool
    mouth_occluded: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        eye_occluded = self.eye_occluded

        forehead_occluded = self.forehead_occluded

        mouth_occluded = self.mouth_occluded

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eye_occluded": eye_occluded,
                "forehead_occluded": forehead_occluded,
                "mouth_occluded": mouth_occluded,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        eye_occluded = d.pop("eye_occluded")

        forehead_occluded = d.pop("forehead_occluded")

        mouth_occluded = d.pop("mouth_occluded")

        face_occlusions = cls(
            eye_occluded=eye_occluded,
            forehead_occluded=forehead_occluded,
            mouth_occluded=mouth_occluded,
        )

        face_occlusions.additional_properties = d
        return face_occlusions

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
