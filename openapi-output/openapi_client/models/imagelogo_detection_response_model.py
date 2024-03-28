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
from openapi_client.models.pydantic_main_imagelogo_detection_logo_detection_data_class94559363427872 import PydanticMainImagelogoDetectionLogoDetectionDataClass94559363427872
from openapi_client.models.pydantic_main_imagelogo_detection_logo_detection_data_class94559363441296 import PydanticMainImagelogoDetectionLogoDetectionDataClass94559363441296
from openapi_client.models.pydantic_main_imagelogo_detection_logo_detection_data_class94559363452160 import PydanticMainImagelogoDetectionLogoDetectionDataClass94559363452160
from openapi_client.models.pydantic_main_imagelogo_detection_logo_detection_data_class94559364220800 import PydanticMainImagelogoDetectionLogoDetectionDataClass94559364220800
from openapi_client.models.pydantic_main_imagelogo_detection_logo_detection_data_class94559364386944 import PydanticMainImagelogoDetectionLogoDetectionDataClass94559364386944
from typing import Optional, Set
from typing_extensions import Self

class ImagelogoDetectionResponseModel(BaseModel):
    """
    ImagelogoDetectionResponseModel
    """ # noqa: E501
    microsoft: Optional[PydanticMainImagelogoDetectionLogoDetectionDataClass94559364220800] = None
    google: Optional[PydanticMainImagelogoDetectionLogoDetectionDataClass94559364386944] = None
    clarifai: Optional[PydanticMainImagelogoDetectionLogoDetectionDataClass94559363427872] = None
    api4ai: Optional[PydanticMainImagelogoDetectionLogoDetectionDataClass94559363441296] = None
    smartclick: Optional[PydanticMainImagelogoDetectionLogoDetectionDataClass94559363452160] = None
    __properties: ClassVar[List[str]] = ["microsoft", "google", "clarifai", "api4ai", "smartclick"]

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
        """Create an instance of ImagelogoDetectionResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of microsoft
        if self.microsoft:
            _dict['microsoft'] = self.microsoft.to_dict()
        # override the default output from pydantic by calling `to_dict()` of google
        if self.google:
            _dict['google'] = self.google.to_dict()
        # override the default output from pydantic by calling `to_dict()` of clarifai
        if self.clarifai:
            _dict['clarifai'] = self.clarifai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of api4ai
        if self.api4ai:
            _dict['api4ai'] = self.api4ai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of smartclick
        if self.smartclick:
            _dict['smartclick'] = self.smartclick.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ImagelogoDetectionResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "microsoft": PydanticMainImagelogoDetectionLogoDetectionDataClass94559364220800.from_dict(obj["microsoft"]) if obj.get("microsoft") is not None else None,
            "google": PydanticMainImagelogoDetectionLogoDetectionDataClass94559364386944.from_dict(obj["google"]) if obj.get("google") is not None else None,
            "clarifai": PydanticMainImagelogoDetectionLogoDetectionDataClass94559363427872.from_dict(obj["clarifai"]) if obj.get("clarifai") is not None else None,
            "api4ai": PydanticMainImagelogoDetectionLogoDetectionDataClass94559363441296.from_dict(obj["api4ai"]) if obj.get("api4ai") is not None else None,
            "smartclick": PydanticMainImagelogoDetectionLogoDetectionDataClass94559363452160.from_dict(obj["smartclick"]) if obj.get("smartclick") is not None else None
        })
        return _obj

