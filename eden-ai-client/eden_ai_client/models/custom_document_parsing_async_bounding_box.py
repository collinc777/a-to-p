from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CustomDocumentParsingAsyncBoundingBox")


@_attrs_define
class CustomDocumentParsingAsyncBoundingBox:
    """
    Attributes:
        left (int):
        top (int):
        width (int):
        height (int):
    """

    left: int
    top: int
    width: int
    height: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        left = self.left

        top = self.top

        width = self.width

        height = self.height

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "left": left,
                "top": top,
                "width": width,
                "height": height,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        left = d.pop("left")

        top = d.pop("top")

        width = d.pop("width")

        height = d.pop("height")

        custom_document_parsing_async_bounding_box = cls(
            left=left,
            top=top,
            width=width,
            height=height,
        )

        custom_document_parsing_async_bounding_box.additional_properties = d
        return custom_document_parsing_async_bounding_box

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
