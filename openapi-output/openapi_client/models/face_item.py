# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from openapi_client.models.face_accessories import FaceAccessories
from openapi_client.models.face_bounding_box import FaceBoundingBox
from openapi_client.models.face_emotions import FaceEmotions
from openapi_client.models.face_facial_hair import FaceFacialHair
from openapi_client.models.face_features import FaceFeatures
from openapi_client.models.face_hair import FaceHair
from openapi_client.models.face_landmarks import FaceLandmarks
from openapi_client.models.face_makeup import FaceMakeup
from openapi_client.models.face_occlusions import FaceOcclusions
from openapi_client.models.face_poses import FacePoses
from openapi_client.models.face_quality import FaceQuality
from typing import Optional, Set
from typing_extensions import Self

class FaceItem(BaseModel):
    """
    FaceItem
    """ # noqa: E501
    confidence: StrictInt
    landmarks: FaceLandmarks
    emotions: FaceEmotions
    poses: FacePoses
    age: StrictInt
    gender: StrictStr
    bounding_box: FaceBoundingBox
    hair: FaceHair
    facial_hair: FaceFacialHair
    quality: FaceQuality
    makeup: FaceMakeup
    accessories: FaceAccessories
    occlusions: FaceOcclusions
    features: FaceFeatures
    __properties: ClassVar[List[str]] = ["confidence", "landmarks", "emotions", "poses", "age", "gender", "bounding_box", "hair", "facial_hair", "quality", "makeup", "accessories", "occlusions", "features"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of FaceItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of landmarks
        if self.landmarks:
            _dict['landmarks'] = self.landmarks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of emotions
        if self.emotions:
            _dict['emotions'] = self.emotions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of poses
        if self.poses:
            _dict['poses'] = self.poses.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bounding_box
        if self.bounding_box:
            _dict['bounding_box'] = self.bounding_box.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hair
        if self.hair:
            _dict['hair'] = self.hair.to_dict()
        # override the default output from pydantic by calling `to_dict()` of facial_hair
        if self.facial_hair:
            _dict['facial_hair'] = self.facial_hair.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of makeup
        if self.makeup:
            _dict['makeup'] = self.makeup.to_dict()
        # override the default output from pydantic by calling `to_dict()` of accessories
        if self.accessories:
            _dict['accessories'] = self.accessories.to_dict()
        # override the default output from pydantic by calling `to_dict()` of occlusions
        if self.occlusions:
            _dict['occlusions'] = self.occlusions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of features
        if self.features:
            _dict['features'] = self.features.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FaceItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "confidence": obj.get("confidence"),
            "landmarks": FaceLandmarks.from_dict(obj["landmarks"]) if obj.get("landmarks") is not None else None,
            "emotions": FaceEmotions.from_dict(obj["emotions"]) if obj.get("emotions") is not None else None,
            "poses": FacePoses.from_dict(obj["poses"]) if obj.get("poses") is not None else None,
            "age": obj.get("age"),
            "gender": obj.get("gender"),
            "bounding_box": FaceBoundingBox.from_dict(obj["bounding_box"]) if obj.get("bounding_box") is not None else None,
            "hair": FaceHair.from_dict(obj["hair"]) if obj.get("hair") is not None else None,
            "facial_hair": FaceFacialHair.from_dict(obj["facial_hair"]) if obj.get("facial_hair") is not None else None,
            "quality": FaceQuality.from_dict(obj["quality"]) if obj.get("quality") is not None else None,
            "makeup": FaceMakeup.from_dict(obj["makeup"]) if obj.get("makeup") is not None else None,
            "accessories": FaceAccessories.from_dict(obj["accessories"]) if obj.get("accessories") is not None else None,
            "occlusions": FaceOcclusions.from_dict(obj["occlusions"]) if obj.get("occlusions") is not None else None,
            "features": FaceFeatures.from_dict(obj["features"]) if obj.get("features") is not None else None
        })
        return _obj


