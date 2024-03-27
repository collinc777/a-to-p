from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.final_status_enum import FinalStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ocranonymization_async_anonymization_async_data_class_error import (
        OcranonymizationAsyncAnonymizationAsyncDataClassError,
    )


T = TypeVar("T", bound="OcranonymizationAsyncAnonymizationAsyncDataClass")


@_attrs_define
class OcranonymizationAsyncAnonymizationAsyncDataClass:
    """
    Attributes:
        document (str):
        document_url (str):
        id (str):
        final_status (FinalStatusEnum):
        original_response (Union[Unset, Any]): original response sent by the provider, hidden by default, show it by
            passing the `show_original_response` field to `true` in your request
        error (Union[Unset, OcranonymizationAsyncAnonymizationAsyncDataClassError]):
    """

    document: str
    document_url: str
    id: str
    final_status: FinalStatusEnum
    original_response: Union[Unset, Any] = UNSET
    error: Union[Unset, "OcranonymizationAsyncAnonymizationAsyncDataClassError"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document = self.document

        document_url = self.document_url

        id = self.id

        final_status = self.final_status.value

        original_response = self.original_response

        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document": document,
                "document_url": document_url,
                "id": id,
                "final_status": final_status,
            }
        )
        if original_response is not UNSET:
            field_dict["original_response"] = original_response
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ocranonymization_async_anonymization_async_data_class_error import (
            OcranonymizationAsyncAnonymizationAsyncDataClassError,
        )

        d = src_dict.copy()
        document = d.pop("document")

        document_url = d.pop("document_url")

        id = d.pop("id")

        final_status = FinalStatusEnum(d.pop("final_status"))

        original_response = d.pop("original_response", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, OcranonymizationAsyncAnonymizationAsyncDataClassError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = OcranonymizationAsyncAnonymizationAsyncDataClassError.from_dict(_error)

        ocranonymization_async_anonymization_async_data_class = cls(
            document=document,
            document_url=document_url,
            id=id,
            final_status=final_status,
            original_response=original_response,
            error=error,
        )

        ocranonymization_async_anonymization_async_data_class.additional_properties = d
        return ocranonymization_async_anonymization_async_data_class

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
