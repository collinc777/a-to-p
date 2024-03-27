from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.speech_diarization_entry import SpeechDiarizationEntry


T = TypeVar("T", bound="SpeechDiarization")


@_attrs_define
class SpeechDiarization:
    """
    Attributes:
        total_speakers (int):
        entries (Union[Unset, List['SpeechDiarizationEntry']]):
        error_message (Union[Unset, str]):
    """

    total_speakers: int
    entries: Union[Unset, List["SpeechDiarizationEntry"]] = UNSET
    error_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_speakers = self.total_speakers

        entries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        error_message = self.error_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_speakers": total_speakers,
            }
        )
        if entries is not UNSET:
            field_dict["entries"] = entries
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.speech_diarization_entry import SpeechDiarizationEntry

        d = src_dict.copy()
        total_speakers = d.pop("total_speakers")

        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = SpeechDiarizationEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        error_message = d.pop("error_message", UNSET)

        speech_diarization = cls(
            total_speakers=total_speakers,
            entries=entries,
            error_message=error_message,
        )

        speech_diarization.additional_properties = d
        return speech_diarization

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
