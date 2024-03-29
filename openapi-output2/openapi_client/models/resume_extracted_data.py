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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.resume_education import ResumeEducation
from openapi_client.models.resume_lang import ResumeLang
from openapi_client.models.resume_personal_info import ResumePersonalInfo
from openapi_client.models.resume_skill import ResumeSkill
from openapi_client.models.resume_work_exp import ResumeWorkExp
from typing import Set
from typing_extensions import Self


class ResumeExtractedData(BaseModel):
    """
    ResumeExtractedData
    """  # noqa: E501

    personal_infos: ResumePersonalInfo
    education: ResumeEducation
    work_experience: ResumeWorkExp
    languages: Optional[List[ResumeLang]] = None
    skills: Optional[List[ResumeSkill]] = None
    certifications: Optional[List[ResumeSkill]] = None
    courses: Optional[List[ResumeSkill]] = None
    publications: Optional[List[ResumeSkill]] = None
    interests: Optional[List[ResumeSkill]] = None
    __properties: ClassVar[List[str]] = [
        "personal_infos",
        "education",
        "work_experience",
        "languages",
        "skills",
        "certifications",
        "courses",
        "publications",
        "interests",
    ]

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
        """Create an instance of ResumeExtractedData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of personal_infos
        if self.personal_infos:
            _dict["personal_infos"] = self.personal_infos.to_dict()
        # override the default output from pydantic by calling `to_dict()` of education
        if self.education:
            _dict["education"] = self.education.to_dict()
        # override the default output from pydantic by calling `to_dict()` of work_experience
        if self.work_experience:
            _dict["work_experience"] = self.work_experience.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item in self.languages:
                if _item:
                    _items.append(_item.to_dict())
            _dict["languages"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in skills (list)
        _items = []
        if self.skills:
            for _item in self.skills:
                if _item:
                    _items.append(_item.to_dict())
            _dict["skills"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in certifications (list)
        _items = []
        if self.certifications:
            for _item in self.certifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict["certifications"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in courses (list)
        _items = []
        if self.courses:
            for _item in self.courses:
                if _item:
                    _items.append(_item.to_dict())
            _dict["courses"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in publications (list)
        _items = []
        if self.publications:
            for _item in self.publications:
                if _item:
                    _items.append(_item.to_dict())
            _dict["publications"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in interests (list)
        _items = []
        if self.interests:
            for _item in self.interests:
                if _item:
                    _items.append(_item.to_dict())
            _dict["interests"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResumeExtractedData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "personal_infos": ResumePersonalInfo.from_dict(obj["personal_infos"])
                if obj.get("personal_infos") is not None
                else None,
                "education": ResumeEducation.from_dict(obj["education"])
                if obj.get("education") is not None
                else None,
                "work_experience": ResumeWorkExp.from_dict(obj["work_experience"])
                if obj.get("work_experience") is not None
                else None,
                "languages": [ResumeLang.from_dict(_item) for _item in obj["languages"]]
                if obj.get("languages") is not None
                else None,
                "skills": [ResumeSkill.from_dict(_item) for _item in obj["skills"]]
                if obj.get("skills") is not None
                else None,
                "certifications": [
                    ResumeSkill.from_dict(_item) for _item in obj["certifications"]
                ]
                if obj.get("certifications") is not None
                else None,
                "courses": [ResumeSkill.from_dict(_item) for _item in obj["courses"]]
                if obj.get("courses") is not None
                else None,
                "publications": [
                    ResumeSkill.from_dict(_item) for _item in obj["publications"]
                ]
                if obj.get("publications") is not None
                else None,
                "interests": [
                    ResumeSkill.from_dict(_item) for _item in obj["interests"]
                ]
                if obj.get("interests") is not None
                else None,
            }
        )
        return _obj
