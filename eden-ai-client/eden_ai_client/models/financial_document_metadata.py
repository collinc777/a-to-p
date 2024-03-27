from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialDocumentMetadata")


@_attrs_define
class FinancialDocumentMetadata:
    """
    Attributes:
        document_index (Union[Unset, int]): Index of the detected document.
        document_page_number (Union[Unset, int]): Page number within the document.
        document_type (Union[Unset, str]): Type or category of the document.
    """

    document_index: Union[Unset, int] = UNSET
    document_page_number: Union[Unset, int] = UNSET
    document_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document_index = self.document_index

        document_page_number = self.document_page_number

        document_type = self.document_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_index is not UNSET:
            field_dict["document_index"] = document_index
        if document_page_number is not UNSET:
            field_dict["document_page_number"] = document_page_number
        if document_type is not UNSET:
            field_dict["document_type"] = document_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        document_index = d.pop("document_index", UNSET)

        document_page_number = d.pop("document_page_number", UNSET)

        document_type = d.pop("document_type", UNSET)

        financial_document_metadata = cls(
            document_index=document_index,
            document_page_number=document_page_number,
            document_type=document_type,
        )

        financial_document_metadata.additional_properties = d
        return financial_document_metadata

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
