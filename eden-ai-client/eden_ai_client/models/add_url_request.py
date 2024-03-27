from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_url_request_metadata_item import AddUrlRequestMetadataItem


T = TypeVar("T", bound="AddUrlRequest")


@_attrs_define
class AddUrlRequest:
    """
    Attributes:
        urls (List[str]): Add multiple urls into the database, it loads all the text from HTML webpages into a document
            format.
        metadata (Union[Unset, List['AddUrlRequestMetadataItem']]):
    """

    urls: List[str]
    metadata: Union[Unset, List["AddUrlRequestMetadataItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        urls = self.urls

        metadata: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = []
            for metadata_item_data in self.metadata:
                metadata_item = metadata_item_data.to_dict()
                metadata.append(metadata_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "urls": urls,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.add_url_request_metadata_item import AddUrlRequestMetadataItem

        d = src_dict.copy()
        urls = cast(List[str], d.pop("urls"))

        metadata = []
        _metadata = d.pop("metadata", UNSET)
        for metadata_item_data in _metadata or []:
            metadata_item = AddUrlRequestMetadataItem.from_dict(metadata_item_data)

            metadata.append(metadata_item)

        add_url_request = cls(
            urls=urls,
            metadata=metadata,
        )

        add_url_request.additional_properties = d
        return add_url_request

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
