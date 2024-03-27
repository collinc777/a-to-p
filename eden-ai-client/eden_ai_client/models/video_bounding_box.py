from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VideoBoundingBox")


@_attrs_define
class VideoBoundingBox:
    """
    Attributes:
        top (int):
        left (int):
        height (int):
        width (int):
    """

    top: int
    left: int
    height: int
    width: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        top = self.top

        left = self.left

        height = self.height

        width = self.width

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "top": top,
                "left": left,
                "height": height,
                "width": width,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        top = d.pop("top")

        left = d.pop("left")

        height = d.pop("height")

        width = d.pop("width")

        video_bounding_box = cls(
            top=top,
            left=left,
            height=height,
            width=width,
        )

        video_bounding_box.additional_properties = d
        return video_bounding_box

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