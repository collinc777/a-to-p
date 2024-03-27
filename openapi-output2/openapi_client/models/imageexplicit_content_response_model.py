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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.pydantic_main_imageexplicit_content_explicit_content_data_class94559364221568 import (
    PydanticMainImageexplicitContentExplicitContentDataClass94559364221568,
)
from openapi_client.models.pydantic_main_imageexplicit_content_explicit_content_data_class94559364230016 import (
    PydanticMainImageexplicitContentExplicitContentDataClass94559364230016,
)
from openapi_client.models.pydantic_main_imageexplicit_content_explicit_content_data_class94559364240752 import (
    PydanticMainImageexplicitContentExplicitContentDataClass94559364240752,
)
from openapi_client.models.pydantic_main_imageexplicit_content_explicit_content_data_class94559364359824 import (
    PydanticMainImageexplicitContentExplicitContentDataClass94559364359824,
)
from openapi_client.models.pydantic_main_imageexplicit_content_explicit_content_data_class94559364404912 import (
    PydanticMainImageexplicitContentExplicitContentDataClass94559364404912,
)
from openapi_client.models.pydantic_main_imageexplicit_content_explicit_content_data_class94559364412192 import (
    PydanticMainImageexplicitContentExplicitContentDataClass94559364412192,
)
from openapi_client.models.pydantic_main_imageexplicit_content_explicit_content_data_class94559364642800 import (
    PydanticMainImageexplicitContentExplicitContentDataClass94559364642800,
)
from openapi_client.models.pydantic_main_imageexplicit_content_explicit_content_data_class94559364648912 import (
    PydanticMainImageexplicitContentExplicitContentDataClass94559364648912,
)
from typing import Set
from typing_extensions import Self


class ImageexplicitContentResponseModel(BaseModel):
    """
    ImageexplicitContentResponseModel
    """  # noqa: E501

    microsoft: Optional[
        PydanticMainImageexplicitContentExplicitContentDataClass94559364648912
    ] = None
    google: Optional[
        PydanticMainImageexplicitContentExplicitContentDataClass94559364642800
    ] = None
    picpurify: Optional[
        PydanticMainImageexplicitContentExplicitContentDataClass94559364412192
    ] = None
    amazon: Optional[
        PydanticMainImageexplicitContentExplicitContentDataClass94559364404912
    ] = None
    clarifai: Optional[
        PydanticMainImageexplicitContentExplicitContentDataClass94559364359824
    ] = None
    api4ai: Optional[
        PydanticMainImageexplicitContentExplicitContentDataClass94559364221568
    ] = None
    sentisight: Optional[
        PydanticMainImageexplicitContentExplicitContentDataClass94559364230016
    ] = None
    eden_ai: Optional[
        PydanticMainImageexplicitContentExplicitContentDataClass94559364240752
    ] = Field(default=None, alias="eden-ai")
    __properties: ClassVar[List[str]] = [
        "microsoft",
        "google",
        "picpurify",
        "amazon",
        "clarifai",
        "api4ai",
        "sentisight",
        "eden-ai",
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
        """Create an instance of ImageexplicitContentResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of microsoft
        if self.microsoft:
            _dict["microsoft"] = self.microsoft.to_dict()
        # override the default output from pydantic by calling `to_dict()` of google
        if self.google:
            _dict["google"] = self.google.to_dict()
        # override the default output from pydantic by calling `to_dict()` of picpurify
        if self.picpurify:
            _dict["picpurify"] = self.picpurify.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amazon
        if self.amazon:
            _dict["amazon"] = self.amazon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of clarifai
        if self.clarifai:
            _dict["clarifai"] = self.clarifai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of api4ai
        if self.api4ai:
            _dict["api4ai"] = self.api4ai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sentisight
        if self.sentisight:
            _dict["sentisight"] = self.sentisight.to_dict()
        # override the default output from pydantic by calling `to_dict()` of eden_ai
        if self.eden_ai:
            _dict["eden-ai"] = self.eden_ai.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ImageexplicitContentResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "microsoft": PydanticMainImageexplicitContentExplicitContentDataClass94559364648912.from_dict(
                    obj["microsoft"]
                )
                if obj.get("microsoft") is not None
                else None,
                "google": PydanticMainImageexplicitContentExplicitContentDataClass94559364642800.from_dict(
                    obj["google"]
                )
                if obj.get("google") is not None
                else None,
                "picpurify": PydanticMainImageexplicitContentExplicitContentDataClass94559364412192.from_dict(
                    obj["picpurify"]
                )
                if obj.get("picpurify") is not None
                else None,
                "amazon": PydanticMainImageexplicitContentExplicitContentDataClass94559364404912.from_dict(
                    obj["amazon"]
                )
                if obj.get("amazon") is not None
                else None,
                "clarifai": PydanticMainImageexplicitContentExplicitContentDataClass94559364359824.from_dict(
                    obj["clarifai"]
                )
                if obj.get("clarifai") is not None
                else None,
                "api4ai": PydanticMainImageexplicitContentExplicitContentDataClass94559364221568.from_dict(
                    obj["api4ai"]
                )
                if obj.get("api4ai") is not None
                else None,
                "sentisight": PydanticMainImageexplicitContentExplicitContentDataClass94559364230016.from_dict(
                    obj["sentisight"]
                )
                if obj.get("sentisight") is not None
                else None,
                "eden-ai": PydanticMainImageexplicitContentExplicitContentDataClass94559364240752.from_dict(
                    obj["eden-ai"]
                )
                if obj.get("eden-ai") is not None
                else None,
            }
        )
        return _obj