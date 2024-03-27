from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FaceEmotions")


@_attrs_define
class FaceEmotions:
    """
    Attributes:
        joy (int):
        sorrow (int):
        anger (int):
        surprise (int):
        disgust (int):
        fear (int):
        confusion (int):
        calm (int):
        unknown (int):
        neutral (int):
        contempt (int):
    """

    joy: int
    sorrow: int
    anger: int
    surprise: int
    disgust: int
    fear: int
    confusion: int
    calm: int
    unknown: int
    neutral: int
    contempt: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        joy = self.joy

        sorrow = self.sorrow

        anger = self.anger

        surprise = self.surprise

        disgust = self.disgust

        fear = self.fear

        confusion = self.confusion

        calm = self.calm

        unknown = self.unknown

        neutral = self.neutral

        contempt = self.contempt

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "joy": joy,
                "sorrow": sorrow,
                "anger": anger,
                "surprise": surprise,
                "disgust": disgust,
                "fear": fear,
                "confusion": confusion,
                "calm": calm,
                "unknown": unknown,
                "neutral": neutral,
                "contempt": contempt,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        joy = d.pop("joy")

        sorrow = d.pop("sorrow")

        anger = d.pop("anger")

        surprise = d.pop("surprise")

        disgust = d.pop("disgust")

        fear = d.pop("fear")

        confusion = d.pop("confusion")

        calm = d.pop("calm")

        unknown = d.pop("unknown")

        neutral = d.pop("neutral")

        contempt = d.pop("contempt")

        face_emotions = cls(
            joy=joy,
            sorrow=sorrow,
            anger=anger,
            surprise=surprise,
            disgust=disgust,
            fear=fear,
            confusion=confusion,
            calm=calm,
            unknown=unknown,
            neutral=neutral,
            contempt=contempt,
        )

        face_emotions.additional_properties = d
        return face_emotions

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
