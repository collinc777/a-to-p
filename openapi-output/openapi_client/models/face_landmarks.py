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

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class FaceLandmarks(BaseModel):
    """
    FaceLandmarks
    """ # noqa: E501
    left_eye: Optional[List[StrictInt]] = None
    left_eye_top: Optional[List[StrictInt]] = None
    left_eye_right: Optional[List[StrictInt]] = None
    left_eye_bottom: Optional[List[StrictInt]] = None
    left_eye_left: Optional[List[StrictInt]] = None
    right_eye: Optional[List[StrictInt]] = None
    right_eye_top: Optional[List[StrictInt]] = None
    right_eye_right: Optional[List[StrictInt]] = None
    right_eye_bottom: Optional[List[StrictInt]] = None
    right_eye_left: Optional[List[StrictInt]] = None
    left_eyebrow_left: Optional[List[StrictInt]] = None
    left_eyebrow_right: Optional[List[StrictInt]] = None
    left_eyebrow_top: Optional[List[StrictInt]] = None
    right_eyebrow_left: Optional[List[StrictInt]] = None
    right_eyebrow_right: Optional[List[StrictInt]] = None
    left_pupil: Optional[List[StrictInt]] = None
    right_pupil: Optional[List[StrictInt]] = None
    nose_tip: Optional[List[StrictInt]] = None
    nose_bottom_right: Optional[List[StrictInt]] = None
    nose_bottom_left: Optional[List[StrictInt]] = None
    mouth_left: Optional[List[StrictInt]] = None
    mouth_right: Optional[List[StrictInt]] = None
    right_eyebrow_top: Optional[List[StrictInt]] = None
    midpoint_between_eyes: Optional[List[StrictInt]] = None
    nose_bottom_center: Optional[List[StrictInt]] = None
    nose_left_alar_out_tip: Optional[List[StrictInt]] = None
    nose_left_alar_top: Optional[List[StrictInt]] = None
    nose_right_alar_out_tip: Optional[List[StrictInt]] = None
    nose_right_alar_top: Optional[List[StrictInt]] = None
    nose_root_left: Optional[List[StrictInt]] = None
    nose_root_right: Optional[List[StrictInt]] = None
    upper_lip: Optional[List[StrictInt]] = None
    under_lip: Optional[List[StrictInt]] = None
    under_lip_bottom: Optional[List[StrictInt]] = None
    under_lip_top: Optional[List[StrictInt]] = None
    upper_lip_bottom: Optional[List[StrictInt]] = None
    upper_lip_top: Optional[List[StrictInt]] = None
    mouth_center: Optional[List[StrictInt]] = None
    mouth_top: Optional[List[StrictInt]] = None
    mouth_bottom: Optional[List[StrictInt]] = None
    left_ear_tragion: Optional[List[StrictInt]] = None
    right_ear_tragion: Optional[List[StrictInt]] = None
    forehead_glabella: Optional[List[StrictInt]] = None
    chin_gnathion: Optional[List[StrictInt]] = None
    chin_left_gonion: Optional[List[StrictInt]] = None
    chin_right_gonion: Optional[List[StrictInt]] = None
    upper_jawline_left: Optional[List[StrictInt]] = None
    mid_jawline_left: Optional[List[StrictInt]] = None
    mid_jawline_right: Optional[List[StrictInt]] = None
    upper_jawline_right: Optional[List[StrictInt]] = None
    left_cheek_center: Optional[List[StrictInt]] = None
    right_cheek_center: Optional[List[StrictInt]] = None
    __properties: ClassVar[List[str]] = ["left_eye", "left_eye_top", "left_eye_right", "left_eye_bottom", "left_eye_left", "right_eye", "right_eye_top", "right_eye_right", "right_eye_bottom", "right_eye_left", "left_eyebrow_left", "left_eyebrow_right", "left_eyebrow_top", "right_eyebrow_left", "right_eyebrow_right", "left_pupil", "right_pupil", "nose_tip", "nose_bottom_right", "nose_bottom_left", "mouth_left", "mouth_right", "right_eyebrow_top", "midpoint_between_eyes", "nose_bottom_center", "nose_left_alar_out_tip", "nose_left_alar_top", "nose_right_alar_out_tip", "nose_right_alar_top", "nose_root_left", "nose_root_right", "upper_lip", "under_lip", "under_lip_bottom", "under_lip_top", "upper_lip_bottom", "upper_lip_top", "mouth_center", "mouth_top", "mouth_bottom", "left_ear_tragion", "right_ear_tragion", "forehead_glabella", "chin_gnathion", "chin_left_gonion", "chin_right_gonion", "upper_jawline_left", "mid_jawline_left", "mid_jawline_right", "upper_jawline_right", "left_cheek_center", "right_cheek_center"]

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
        """Create an instance of FaceLandmarks from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FaceLandmarks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "left_eye": obj.get("left_eye"),
            "left_eye_top": obj.get("left_eye_top"),
            "left_eye_right": obj.get("left_eye_right"),
            "left_eye_bottom": obj.get("left_eye_bottom"),
            "left_eye_left": obj.get("left_eye_left"),
            "right_eye": obj.get("right_eye"),
            "right_eye_top": obj.get("right_eye_top"),
            "right_eye_right": obj.get("right_eye_right"),
            "right_eye_bottom": obj.get("right_eye_bottom"),
            "right_eye_left": obj.get("right_eye_left"),
            "left_eyebrow_left": obj.get("left_eyebrow_left"),
            "left_eyebrow_right": obj.get("left_eyebrow_right"),
            "left_eyebrow_top": obj.get("left_eyebrow_top"),
            "right_eyebrow_left": obj.get("right_eyebrow_left"),
            "right_eyebrow_right": obj.get("right_eyebrow_right"),
            "left_pupil": obj.get("left_pupil"),
            "right_pupil": obj.get("right_pupil"),
            "nose_tip": obj.get("nose_tip"),
            "nose_bottom_right": obj.get("nose_bottom_right"),
            "nose_bottom_left": obj.get("nose_bottom_left"),
            "mouth_left": obj.get("mouth_left"),
            "mouth_right": obj.get("mouth_right"),
            "right_eyebrow_top": obj.get("right_eyebrow_top"),
            "midpoint_between_eyes": obj.get("midpoint_between_eyes"),
            "nose_bottom_center": obj.get("nose_bottom_center"),
            "nose_left_alar_out_tip": obj.get("nose_left_alar_out_tip"),
            "nose_left_alar_top": obj.get("nose_left_alar_top"),
            "nose_right_alar_out_tip": obj.get("nose_right_alar_out_tip"),
            "nose_right_alar_top": obj.get("nose_right_alar_top"),
            "nose_root_left": obj.get("nose_root_left"),
            "nose_root_right": obj.get("nose_root_right"),
            "upper_lip": obj.get("upper_lip"),
            "under_lip": obj.get("under_lip"),
            "under_lip_bottom": obj.get("under_lip_bottom"),
            "under_lip_top": obj.get("under_lip_top"),
            "upper_lip_bottom": obj.get("upper_lip_bottom"),
            "upper_lip_top": obj.get("upper_lip_top"),
            "mouth_center": obj.get("mouth_center"),
            "mouth_top": obj.get("mouth_top"),
            "mouth_bottom": obj.get("mouth_bottom"),
            "left_ear_tragion": obj.get("left_ear_tragion"),
            "right_ear_tragion": obj.get("right_ear_tragion"),
            "forehead_glabella": obj.get("forehead_glabella"),
            "chin_gnathion": obj.get("chin_gnathion"),
            "chin_left_gonion": obj.get("chin_left_gonion"),
            "chin_right_gonion": obj.get("chin_right_gonion"),
            "upper_jawline_left": obj.get("upper_jawline_left"),
            "mid_jawline_left": obj.get("mid_jawline_left"),
            "mid_jawline_right": obj.get("mid_jawline_right"),
            "upper_jawline_right": obj.get("upper_jawline_right"),
            "left_cheek_center": obj.get("left_cheek_center"),
            "right_cheek_center": obj.get("right_cheek_center")
        })
        return _obj


