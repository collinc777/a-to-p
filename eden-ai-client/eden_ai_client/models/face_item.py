from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.face_accessories import FaceAccessories
    from ..models.face_bounding_box import FaceBoundingBox
    from ..models.face_emotions import FaceEmotions
    from ..models.face_facial_hair import FaceFacialHair
    from ..models.face_features import FaceFeatures
    from ..models.face_hair import FaceHair
    from ..models.face_landmarks import FaceLandmarks
    from ..models.face_makeup import FaceMakeup
    from ..models.face_occlusions import FaceOcclusions
    from ..models.face_poses import FacePoses
    from ..models.face_quality import FaceQuality


T = TypeVar("T", bound="FaceItem")


@_attrs_define
class FaceItem:
    """
    Attributes:
        confidence (int):
        landmarks (FaceLandmarks):
        emotions (FaceEmotions):
        poses (FacePoses):
        age (int):
        gender (str):
        bounding_box (FaceBoundingBox):
        hair (FaceHair):
        facial_hair (FaceFacialHair):
        quality (FaceQuality):
        makeup (FaceMakeup):
        accessories (FaceAccessories):
        occlusions (FaceOcclusions):
        features (FaceFeatures):
    """

    confidence: int
    landmarks: "FaceLandmarks"
    emotions: "FaceEmotions"
    poses: "FacePoses"
    age: int
    gender: str
    bounding_box: "FaceBoundingBox"
    hair: "FaceHair"
    facial_hair: "FaceFacialHair"
    quality: "FaceQuality"
    makeup: "FaceMakeup"
    accessories: "FaceAccessories"
    occlusions: "FaceOcclusions"
    features: "FaceFeatures"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        confidence = self.confidence

        landmarks = self.landmarks.to_dict()

        emotions = self.emotions.to_dict()

        poses = self.poses.to_dict()

        age = self.age

        gender = self.gender

        bounding_box = self.bounding_box.to_dict()

        hair = self.hair.to_dict()

        facial_hair = self.facial_hair.to_dict()

        quality = self.quality.to_dict()

        makeup = self.makeup.to_dict()

        accessories = self.accessories.to_dict()

        occlusions = self.occlusions.to_dict()

        features = self.features.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confidence": confidence,
                "landmarks": landmarks,
                "emotions": emotions,
                "poses": poses,
                "age": age,
                "gender": gender,
                "bounding_box": bounding_box,
                "hair": hair,
                "facial_hair": facial_hair,
                "quality": quality,
                "makeup": makeup,
                "accessories": accessories,
                "occlusions": occlusions,
                "features": features,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.face_accessories import FaceAccessories
        from ..models.face_bounding_box import FaceBoundingBox
        from ..models.face_emotions import FaceEmotions
        from ..models.face_facial_hair import FaceFacialHair
        from ..models.face_features import FaceFeatures
        from ..models.face_hair import FaceHair
        from ..models.face_landmarks import FaceLandmarks
        from ..models.face_makeup import FaceMakeup
        from ..models.face_occlusions import FaceOcclusions
        from ..models.face_poses import FacePoses
        from ..models.face_quality import FaceQuality

        d = src_dict.copy()
        confidence = d.pop("confidence")

        landmarks = FaceLandmarks.from_dict(d.pop("landmarks"))

        emotions = FaceEmotions.from_dict(d.pop("emotions"))

        poses = FacePoses.from_dict(d.pop("poses"))

        age = d.pop("age")

        gender = d.pop("gender")

        bounding_box = FaceBoundingBox.from_dict(d.pop("bounding_box"))

        hair = FaceHair.from_dict(d.pop("hair"))

        facial_hair = FaceFacialHair.from_dict(d.pop("facial_hair"))

        quality = FaceQuality.from_dict(d.pop("quality"))

        makeup = FaceMakeup.from_dict(d.pop("makeup"))

        accessories = FaceAccessories.from_dict(d.pop("accessories"))

        occlusions = FaceOcclusions.from_dict(d.pop("occlusions"))

        features = FaceFeatures.from_dict(d.pop("features"))

        face_item = cls(
            confidence=confidence,
            landmarks=landmarks,
            emotions=emotions,
            poses=poses,
            age=age,
            gender=gender,
            bounding_box=bounding_box,
            hair=hair,
            facial_hair=facial_hair,
            quality=quality,
            makeup=makeup,
            accessories=accessories,
            occlusions=occlusions,
            features=features,
        )

        face_item.additional_properties = d
        return face_item

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
