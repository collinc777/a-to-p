from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CustomDocumentParsingAsyncRequestUsersWebhookParameters")


@_attrs_define
class CustomDocumentParsingAsyncRequestUsersWebhookParameters:
    """Json data that contains of additional parameters that will be sent back to the webhook receiver             (ex: api
    key for security or client's data ID to link the result internally).             Will only be used when
    webhook_receiver is set.

    """

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        custom_document_parsing_async_request_users_webhook_parameters = cls()

        custom_document_parsing_async_request_users_webhook_parameters.additional_properties = d
        return custom_document_parsing_async_request_users_webhook_parameters

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
