from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.face_attributes import FaceAttributes
    from ..models.landmarks_video import LandmarksVideo
    from ..models.video_bounding_box import VideoBoundingBox


T = TypeVar("T", bound="VideoFace")


@_attrs_define
class VideoFace:
    """
    Attributes:
        offset (int):
        bounding_box (VideoBoundingBox):
        attributes (FaceAttributes):
        landmarks (LandmarksVideo):
    """

    offset: int
    bounding_box: "VideoBoundingBox"
    attributes: "FaceAttributes"
    landmarks: "LandmarksVideo"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        offset = self.offset

        bounding_box = self.bounding_box.to_dict()

        attributes = self.attributes.to_dict()

        landmarks = self.landmarks.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offset": offset,
                "bounding_box": bounding_box,
                "attributes": attributes,
                "landmarks": landmarks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.face_attributes import FaceAttributes
        from ..models.landmarks_video import LandmarksVideo
        from ..models.video_bounding_box import VideoBoundingBox

        d = src_dict.copy()
        offset = d.pop("offset")

        bounding_box = VideoBoundingBox.from_dict(d.pop("bounding_box"))

        attributes = FaceAttributes.from_dict(d.pop("attributes"))

        landmarks = LandmarksVideo.from_dict(d.pop("landmarks"))

        video_face = cls(
            offset=offset,
            bounding_box=bounding_box,
            attributes=attributes,
            landmarks=landmarks,
        )

        video_face.additional_properties = d
        return video_face

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
