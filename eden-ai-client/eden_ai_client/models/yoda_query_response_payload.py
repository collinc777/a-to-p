from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.yoda_query_response_payload_metadata import YodaQueryResponsePayloadMetadata


T = TypeVar("T", bound="YodaQueryResponsePayload")


@_attrs_define
class YodaQueryResponsePayload:
    """
    Attributes:
        metadata (YodaQueryResponsePayloadMetadata):
        page_content (str):
    """

    metadata: "YodaQueryResponsePayloadMetadata"
    page_content: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadata = self.metadata.to_dict()

        page_content = self.page_content

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata": metadata,
                "page_content": page_content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.yoda_query_response_payload_metadata import YodaQueryResponsePayloadMetadata

        d = src_dict.copy()
        metadata = YodaQueryResponsePayloadMetadata.from_dict(d.pop("metadata"))

        page_content = d.pop("page_content")

        yoda_query_response_payload = cls(
            metadata=metadata,
            page_content=page_content,
        )

        yoda_query_response_payload.additional_properties = d
        return yoda_query_response_payload

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
