from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.person_attributes import PersonAttributes
    from ..models.person_landmarks import PersonLandmarks
    from ..models.video_person_poses import VideoPersonPoses
    from ..models.video_person_quality import VideoPersonQuality
    from ..models.video_tracking_bounding_box import VideoTrackingBoundingBox


T = TypeVar("T", bound="PersonTracking")


@_attrs_define
class PersonTracking:
    """
    Attributes:
        offset (int):
        bounding_box (VideoTrackingBoundingBox):
        attributes (Union[Unset, PersonAttributes]):
        landmarks (Union[Unset, PersonLandmarks]):
        poses (Union[Unset, VideoPersonPoses]):
        quality (Union[Unset, VideoPersonQuality]):
    """

    offset: int
    bounding_box: "VideoTrackingBoundingBox"
    attributes: Union[Unset, "PersonAttributes"] = UNSET
    landmarks: Union[Unset, "PersonLandmarks"] = UNSET
    poses: Union[Unset, "VideoPersonPoses"] = UNSET
    quality: Union[Unset, "VideoPersonQuality"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        offset = self.offset

        bounding_box = self.bounding_box.to_dict()

        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        landmarks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.landmarks, Unset):
            landmarks = self.landmarks.to_dict()

        poses: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.poses, Unset):
            poses = self.poses.to_dict()

        quality: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offset": offset,
                "bounding_box": bounding_box,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if landmarks is not UNSET:
            field_dict["landmarks"] = landmarks
        if poses is not UNSET:
            field_dict["poses"] = poses
        if quality is not UNSET:
            field_dict["quality"] = quality

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.person_attributes import PersonAttributes
        from ..models.person_landmarks import PersonLandmarks
        from ..models.video_person_poses import VideoPersonPoses
        from ..models.video_person_quality import VideoPersonQuality
        from ..models.video_tracking_bounding_box import VideoTrackingBoundingBox

        d = src_dict.copy()
        offset = d.pop("offset")

        bounding_box = VideoTrackingBoundingBox.from_dict(d.pop("bounding_box"))

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, PersonAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = PersonAttributes.from_dict(_attributes)

        _landmarks = d.pop("landmarks", UNSET)
        landmarks: Union[Unset, PersonLandmarks]
        if isinstance(_landmarks, Unset):
            landmarks = UNSET
        else:
            landmarks = PersonLandmarks.from_dict(_landmarks)

        _poses = d.pop("poses", UNSET)
        poses: Union[Unset, VideoPersonPoses]
        if isinstance(_poses, Unset):
            poses = UNSET
        else:
            poses = VideoPersonPoses.from_dict(_poses)

        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, VideoPersonQuality]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = VideoPersonQuality.from_dict(_quality)

        person_tracking = cls(
            offset=offset,
            bounding_box=bounding_box,
            attributes=attributes,
            landmarks=landmarks,
            poses=poses,
            quality=quality,
        )

        person_tracking.additional_properties = d
        return person_tracking

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
