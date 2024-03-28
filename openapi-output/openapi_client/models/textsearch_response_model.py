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
from openapi_client.models.pydantic_main_textsearch_search_data_class94559368037760 import PydanticMainTextsearchSearchDataClass94559368037760
from openapi_client.models.pydantic_main_textsearch_search_data_class94559368053600 import PydanticMainTextsearchSearchDataClass94559368053600
from openapi_client.models.pydantic_main_textsearch_search_data_class94559368271696 import PydanticMainTextsearchSearchDataClass94559368271696
from typing import Optional, Set
from typing_extensions import Self

class TextsearchResponseModel(BaseModel):
    """
    TextsearchResponseModel
    """ # noqa: E501
    cohere: Optional[PydanticMainTextsearchSearchDataClass94559368053600] = None
    openai: Optional[PydanticMainTextsearchSearchDataClass94559368271696] = None
    google: Optional[PydanticMainTextsearchSearchDataClass94559368037760] = None
    __properties: ClassVar[List[str]] = ["cohere", "openai", "google"]

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
        """Create an instance of TextsearchResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cohere
        if self.cohere:
            _dict['cohere'] = self.cohere.to_dict()
        # override the default output from pydantic by calling `to_dict()` of openai
        if self.openai:
            _dict['openai'] = self.openai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of google
        if self.google:
            _dict['google'] = self.google.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TextsearchResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cohere": PydanticMainTextsearchSearchDataClass94559368053600.from_dict(obj["cohere"]) if obj.get("cohere") is not None else None,
            "openai": PydanticMainTextsearchSearchDataClass94559368271696.from_dict(obj["openai"]) if obj.get("openai") is not None else None,
            "google": PydanticMainTextsearchSearchDataClass94559368037760.from_dict(obj["google"]) if obj.get("google") is not None else None
        })
        return _obj


