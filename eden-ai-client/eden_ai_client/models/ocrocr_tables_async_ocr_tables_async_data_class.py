from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.final_status_enum import FinalStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ocrocr_tables_async_ocr_tables_async_data_class_error import (
        OcrocrTablesAsyncOcrTablesAsyncDataClassError,
    )
    from ..models.page import Page


T = TypeVar("T", bound="OcrocrTablesAsyncOcrTablesAsyncDataClass")


@_attrs_define
class OcrocrTablesAsyncOcrTablesAsyncDataClass:
    """
    Attributes:
        num_pages (int):
        id (str):
        final_status (FinalStatusEnum):
        pages (Union[Unset, List['Page']]):
        original_response (Union[Unset, Any]): original response sent by the provider, hidden by default, show it by
            passing the `show_original_response` field to `true` in your request
        error (Union[Unset, OcrocrTablesAsyncOcrTablesAsyncDataClassError]):
    """

    num_pages: int
    id: str
    final_status: FinalStatusEnum
    pages: Union[Unset, List["Page"]] = UNSET
    original_response: Union[Unset, Any] = UNSET
    error: Union[Unset, "OcrocrTablesAsyncOcrTablesAsyncDataClassError"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        num_pages = self.num_pages

        id = self.id

        final_status = self.final_status.value

        pages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pages, Unset):
            pages = []
            for pages_item_data in self.pages:
                pages_item = pages_item_data.to_dict()
                pages.append(pages_item)

        original_response = self.original_response

        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "num_pages": num_pages,
                "id": id,
                "final_status": final_status,
            }
        )
        if pages is not UNSET:
            field_dict["pages"] = pages
        if original_response is not UNSET:
            field_dict["original_response"] = original_response
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ocrocr_tables_async_ocr_tables_async_data_class_error import (
            OcrocrTablesAsyncOcrTablesAsyncDataClassError,
        )
        from ..models.page import Page

        d = src_dict.copy()
        num_pages = d.pop("num_pages")

        id = d.pop("id")

        final_status = FinalStatusEnum(d.pop("final_status"))

        pages = []
        _pages = d.pop("pages", UNSET)
        for pages_item_data in _pages or []:
            pages_item = Page.from_dict(pages_item_data)

            pages.append(pages_item)

        original_response = d.pop("original_response", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, OcrocrTablesAsyncOcrTablesAsyncDataClassError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = OcrocrTablesAsyncOcrTablesAsyncDataClassError.from_dict(_error)

        ocrocr_tables_async_ocr_tables_async_data_class = cls(
            num_pages=num_pages,
            id=id,
            final_status=final_status,
            pages=pages,
            original_response=original_response,
            error=error,
        )

        ocrocr_tables_async_ocr_tables_async_data_class.additional_properties = d
        return ocrocr_tables_async_ocr_tables_async_data_class

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
