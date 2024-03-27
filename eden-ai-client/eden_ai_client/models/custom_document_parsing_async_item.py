from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.custom_document_parsing_async_bounding_box import CustomDocumentParsingAsyncBoundingBox


T = TypeVar("T", bound="CustomDocumentParsingAsyncItem")


@_attrs_define
class CustomDocumentParsingAsyncItem:
    """
    Attributes:
        confidence (int):
        value (str):
        query (str):
        bounding_box (CustomDocumentParsingAsyncBoundingBox):
        page (int):
    """

    confidence: int
    value: str
    query: str
    bounding_box: "CustomDocumentParsingAsyncBoundingBox"
    page: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        confidence = self.confidence

        value = self.value

        query = self.query

        bounding_box = self.bounding_box.to_dict()

        page = self.page

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confidence": confidence,
                "value": value,
                "query": query,
                "bounding_box": bounding_box,
                "page": page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_document_parsing_async_bounding_box import CustomDocumentParsingAsyncBoundingBox

        d = src_dict.copy()
        confidence = d.pop("confidence")

        value = d.pop("value")

        query = d.pop("query")

        bounding_box = CustomDocumentParsingAsyncBoundingBox.from_dict(d.pop("bounding_box"))

        page = d.pop("page")

        custom_document_parsing_async_item = cls(
            confidence=confidence,
            value=value,
            query=query,
            bounding_box=bounding_box,
            page=page,
        )

        custom_document_parsing_async_item.additional_properties = d
        return custom_document_parsing_async_item

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
