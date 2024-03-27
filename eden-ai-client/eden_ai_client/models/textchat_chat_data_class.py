from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_f43_enum import StatusF43Enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_message_data_class import ChatMessageDataClass


T = TypeVar("T", bound="TextchatChatDataClass")


@_attrs_define
class TextchatChatDataClass:
    """
    Attributes:
        generated_text (str):
        status (StatusF43Enum):
        message (Union[Unset, List['ChatMessageDataClass']]):
        original_response (Union[Unset, Any]): original response sent by the provider, hidden by default, show it by
            passing the `show_original_response` field to `true` in your request
    """

    generated_text: str
    status: StatusF43Enum
    message: Union[Unset, List["ChatMessageDataClass"]] = UNSET
    original_response: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        generated_text = self.generated_text

        status = self.status.value

        message: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.message, Unset):
            message = []
            for message_item_data in self.message:
                message_item = message_item_data.to_dict()
                message.append(message_item)

        original_response = self.original_response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "generated_text": generated_text,
                "status": status,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if original_response is not UNSET:
            field_dict["original_response"] = original_response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chat_message_data_class import ChatMessageDataClass

        d = src_dict.copy()
        generated_text = d.pop("generated_text")

        status = StatusF43Enum(d.pop("status"))

        message = []
        _message = d.pop("message", UNSET)
        for message_item_data in _message or []:
            message_item = ChatMessageDataClass.from_dict(message_item_data)

            message.append(message_item)

        original_response = d.pop("original_response", UNSET)

        textchat_chat_data_class = cls(
            generated_text=generated_text,
            status=status,
            message=message,
            original_response=original_response,
        )

        textchat_chat_data_class.additional_properties = d
        return textchat_chat_data_class

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
