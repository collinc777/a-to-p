from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SpeechDiarizationEntry")


@_attrs_define
class SpeechDiarizationEntry:
    """
    Attributes:
        segment (str):
        start_time (str):
        end_time (str):
        speaker (int):
        confidence (int):
    """

    segment: str
    start_time: str
    end_time: str
    speaker: int
    confidence: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        segment = self.segment

        start_time = self.start_time

        end_time = self.end_time

        speaker = self.speaker

        confidence = self.confidence

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "segment": segment,
                "start_time": start_time,
                "end_time": end_time,
                "speaker": speaker,
                "confidence": confidence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        segment = d.pop("segment")

        start_time = d.pop("start_time")

        end_time = d.pop("end_time")

        speaker = d.pop("speaker")

        confidence = d.pop("confidence")

        speech_diarization_entry = cls(
            segment=segment,
            start_time=start_time,
            end_time=end_time,
            speaker=speaker,
            confidence=confidence,
        )

        speech_diarization_entry.additional_properties = d
        return speech_diarization_entry

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
