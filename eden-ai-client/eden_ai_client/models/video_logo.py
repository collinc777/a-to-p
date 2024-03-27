from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.video_logo_bounding_box import VideoLogoBoundingBox


T = TypeVar("T", bound="VideoLogo")


@_attrs_define
class VideoLogo:
    """
    Attributes:
        timestamp (int):
        bounding_box (VideoLogoBoundingBox):
        confidence (int):
    """

    timestamp: int
    bounding_box: "VideoLogoBoundingBox"
    confidence: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp

        bounding_box = self.bounding_box.to_dict()

        confidence = self.confidence

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "bounding_box": bounding_box,
                "confidence": confidence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.video_logo_bounding_box import VideoLogoBoundingBox

        d = src_dict.copy()
        timestamp = d.pop("timestamp")

        bounding_box = VideoLogoBoundingBox.from_dict(d.pop("bounding_box"))

        confidence = d.pop("confidence")

        video_logo = cls(
            timestamp=timestamp,
            bounding_box=bounding_box,
            confidence=confidence,
        )

        video_logo.additional_properties = d
        return video_logo

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
