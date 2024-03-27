from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.final_status_enum import FinalStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audiotext_to_speech_async_text_to_speech_async_data_class_error import (
        AudiotextToSpeechAsyncTextToSpeechAsyncDataClassError,
    )


T = TypeVar("T", bound="AudiotextToSpeechAsyncTextToSpeechAsyncDataClass")


@_attrs_define
class AudiotextToSpeechAsyncTextToSpeechAsyncDataClass:
    """
    Attributes:
        audio (str):
        voice_type (int):
        audio_resource_url (str):
        id (str):
        final_status (FinalStatusEnum):
        original_response (Union[Unset, Any]): original response sent by the provider, hidden by default, show it by
            passing the `show_original_response` field to `true` in your request
        error (Union[Unset, AudiotextToSpeechAsyncTextToSpeechAsyncDataClassError]):
    """

    audio: str
    voice_type: int
    audio_resource_url: str
    id: str
    final_status: FinalStatusEnum
    original_response: Union[Unset, Any] = UNSET
    error: Union[Unset, "AudiotextToSpeechAsyncTextToSpeechAsyncDataClassError"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        audio = self.audio

        voice_type = self.voice_type

        audio_resource_url = self.audio_resource_url

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
                "audio": audio,
                "voice_type": voice_type,
                "audio_resource_url": audio_resource_url,
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
        from ..models.audiotext_to_speech_async_text_to_speech_async_data_class_error import (
            AudiotextToSpeechAsyncTextToSpeechAsyncDataClassError,
        )

        d = src_dict.copy()
        audio = d.pop("audio")

        voice_type = d.pop("voice_type")

        audio_resource_url = d.pop("audio_resource_url")

        id = d.pop("id")

        final_status = FinalStatusEnum(d.pop("final_status"))

        original_response = d.pop("original_response", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, AudiotextToSpeechAsyncTextToSpeechAsyncDataClassError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = AudiotextToSpeechAsyncTextToSpeechAsyncDataClassError.from_dict(_error)

        audiotext_to_speech_async_text_to_speech_async_data_class = cls(
            audio=audio,
            voice_type=voice_type,
            audio_resource_url=audio_resource_url,
            id=id,
            final_status=final_status,
            original_response=original_response,
            error=error,
        )

        audiotext_to_speech_async_text_to_speech_async_data_class.additional_properties = d
        return audiotext_to_speech_async_text_to_speech_async_data_class

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
