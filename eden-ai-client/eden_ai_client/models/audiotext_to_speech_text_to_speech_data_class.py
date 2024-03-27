from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_f43_enum import StatusF43Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="AudiotextToSpeechTextToSpeechDataClass")


@_attrs_define
class AudiotextToSpeechTextToSpeechDataClass:
    """
    Attributes:
        audio (str):
        voice_type (int):
        audio_resource_url (str):
        status (StatusF43Enum):
        original_response (Union[Unset, Any]): original response sent by the provider, hidden by default, show it by
            passing the `show_original_response` field to `true` in your request
    """

    audio: str
    voice_type: int
    audio_resource_url: str
    status: StatusF43Enum
    original_response: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        audio = self.audio

        voice_type = self.voice_type

        audio_resource_url = self.audio_resource_url

        status = self.status.value

        original_response = self.original_response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audio": audio,
                "voice_type": voice_type,
                "audio_resource_url": audio_resource_url,
                "status": status,
            }
        )
        if original_response is not UNSET:
            field_dict["original_response"] = original_response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        audio = d.pop("audio")

        voice_type = d.pop("voice_type")

        audio_resource_url = d.pop("audio_resource_url")

        status = StatusF43Enum(d.pop("status"))

        original_response = d.pop("original_response", UNSET)

        audiotext_to_speech_text_to_speech_data_class = cls(
            audio=audio,
            voice_type=voice_type,
            audio_resource_url=audio_resource_url,
            status=status,
            original_response=original_response,
        )

        audiotext_to_speech_text_to_speech_data_class.additional_properties = d
        return audiotext_to_speech_text_to_speech_data_class

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
