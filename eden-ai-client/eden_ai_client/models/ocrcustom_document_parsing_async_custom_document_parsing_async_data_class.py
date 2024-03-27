from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.final_status_enum import FinalStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_document_parsing_async_item import CustomDocumentParsingAsyncItem
    from ..models.ocrcustom_document_parsing_async_custom_document_parsing_async_data_class_error import (
        OcrcustomDocumentParsingAsyncCustomDocumentParsingAsyncDataClassError,
    )


T = TypeVar("T", bound="OcrcustomDocumentParsingAsyncCustomDocumentParsingAsyncDataClass")


@_attrs_define
class OcrcustomDocumentParsingAsyncCustomDocumentParsingAsyncDataClass:
    """
    Attributes:
        id (str):
        final_status (FinalStatusEnum):
        items (Union[Unset, List['CustomDocumentParsingAsyncItem']]):
        original_response (Union[Unset, Any]): original response sent by the provider, hidden by default, show it by
            passing the `show_original_response` field to `true` in your request
        error (Union[Unset, OcrcustomDocumentParsingAsyncCustomDocumentParsingAsyncDataClassError]):
    """

    id: str
    final_status: FinalStatusEnum
    items: Union[Unset, List["CustomDocumentParsingAsyncItem"]] = UNSET
    original_response: Union[Unset, Any] = UNSET
    error: Union[Unset, "OcrcustomDocumentParsingAsyncCustomDocumentParsingAsyncDataClassError"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        final_status = self.final_status.value

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        original_response = self.original_response

        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "final_status": final_status,
            }
        )
        if items is not UNSET:
            field_dict["items"] = items
        if original_response is not UNSET:
            field_dict["original_response"] = original_response
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_document_parsing_async_item import CustomDocumentParsingAsyncItem
        from ..models.ocrcustom_document_parsing_async_custom_document_parsing_async_data_class_error import (
            OcrcustomDocumentParsingAsyncCustomDocumentParsingAsyncDataClassError,
        )

        d = src_dict.copy()
        id = d.pop("id")

        final_status = FinalStatusEnum(d.pop("final_status"))

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = CustomDocumentParsingAsyncItem.from_dict(items_item_data)

            items.append(items_item)

        original_response = d.pop("original_response", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, OcrcustomDocumentParsingAsyncCustomDocumentParsingAsyncDataClassError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = OcrcustomDocumentParsingAsyncCustomDocumentParsingAsyncDataClassError.from_dict(_error)

        ocrcustom_document_parsing_async_custom_document_parsing_async_data_class = cls(
            id=id,
            final_status=final_status,
            items=items,
            original_response=original_response,
            error=error,
        )

        ocrcustom_document_parsing_async_custom_document_parsing_async_data_class.additional_properties = d
        return ocrcustom_document_parsing_async_custom_document_parsing_async_data_class

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
