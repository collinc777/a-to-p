from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FaceBoundingBox")


@_attrs_define
class FaceBoundingBox:
    """
    Attributes:
        x_min (int):
        x_max (int):
        y_min (int):
        y_max (int):
    """

    x_min: int
    x_max: int
    y_min: int
    y_max: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        x_min = self.x_min

        x_max = self.x_max

        y_min = self.y_min

        y_max = self.y_max

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "x_min": x_min,
                "x_max": x_max,
                "y_min": y_min,
                "y_max": y_max,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        x_min = d.pop("x_min")

        x_max = d.pop("x_max")

        y_min = d.pop("y_min")

        y_max = d.pop("y_max")

        face_bounding_box = cls(
            x_min=x_min,
            x_max=x_max,
            y_min=y_min,
            y_max=y_max,
        )

        face_bounding_box.additional_properties = d
        return face_bounding_box

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
