from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.video_face_poses import VideoFacePoses


T = TypeVar("T", bound="FaceAttributes")


@_attrs_define
class FaceAttributes:
    """
    Attributes:
        headwear (int):
        frontal_gaze (int):
        eyes_visible (int):
        glasses (int):
        mouth_open (int):
        smiling (int):
        brightness (int):
        sharpness (int):
        pose (VideoFacePoses):
    """

    headwear: int
    frontal_gaze: int
    eyes_visible: int
    glasses: int
    mouth_open: int
    smiling: int
    brightness: int
    sharpness: int
    pose: "VideoFacePoses"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        headwear = self.headwear

        frontal_gaze = self.frontal_gaze

        eyes_visible = self.eyes_visible

        glasses = self.glasses

        mouth_open = self.mouth_open

        smiling = self.smiling

        brightness = self.brightness

        sharpness = self.sharpness

        pose = self.pose.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "headwear": headwear,
                "frontal_gaze": frontal_gaze,
                "eyes_visible": eyes_visible,
                "glasses": glasses,
                "mouth_open": mouth_open,
                "smiling": smiling,
                "brightness": brightness,
                "sharpness": sharpness,
                "pose": pose,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.video_face_poses import VideoFacePoses

        d = src_dict.copy()
        headwear = d.pop("headwear")

        frontal_gaze = d.pop("frontal_gaze")

        eyes_visible = d.pop("eyes_visible")

        glasses = d.pop("glasses")

        mouth_open = d.pop("mouth_open")

        smiling = d.pop("smiling")

        brightness = d.pop("brightness")

        sharpness = d.pop("sharpness")

        pose = VideoFacePoses.from_dict(d.pop("pose"))

        face_attributes = cls(
            headwear=headwear,
            frontal_gaze=frontal_gaze,
            eyes_visible=eyes_visible,
            glasses=glasses,
            mouth_open=mouth_open,
            smiling=smiling,
            brightness=brightness,
            sharpness=sharpness,
            pose=pose,
        )

        face_attributes.additional_properties = d
        return face_attributes

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
