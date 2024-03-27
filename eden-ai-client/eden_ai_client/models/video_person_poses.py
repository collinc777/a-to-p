from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VideoPersonPoses")


@_attrs_define
class VideoPersonPoses:
    """
    Attributes:
        pitch (int):
        roll (int):
        yaw (int):
    """

    pitch: int
    roll: int
    yaw: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pitch = self.pitch

        roll = self.roll

        yaw = self.yaw

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pitch": pitch,
                "roll": roll,
                "yaw": yaw,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pitch = d.pop("pitch")

        roll = d.pop("roll")

        yaw = d.pop("yaw")

        video_person_poses = cls(
            pitch=pitch,
            roll=roll,
            yaw=yaw,
        )

        video_person_poses.additional_properties = d
        return video_person_poses

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
