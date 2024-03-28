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
from openapi_client.models.pydantic_main_textcustom_named_entity_recognition_custom_named_entity_recognition_data_class94559368332544 import PydanticMainTextcustomNamedEntityRecognitionCustomNamedEntityRecognitionDataClass94559368332544
from openapi_client.models.pydantic_main_textcustom_named_entity_recognition_custom_named_entity_recognition_data_class94559368333488 import PydanticMainTextcustomNamedEntityRecognitionCustomNamedEntityRecognitionDataClass94559368333488
from openapi_client.models.pydantic_main_textcustom_named_entity_recognition_custom_named_entity_recognition_data_class94559369096592 import PydanticMainTextcustomNamedEntityRecognitionCustomNamedEntityRecognitionDataClass94559369096592
from typing import Optional, Set
from typing_extensions import Self

class TextcustomNamedEntityRecognitionResponseModel(BaseModel):
    """
    TextcustomNamedEntityRecognitionResponseModel
    """ # noqa: E501
    cohere: Optional[PydanticMainTextcustomNamedEntityRecognitionCustomNamedEntityRecognitionDataClass94559368332544] = None
    openai: Optional[PydanticMainTextcustomNamedEntityRecognitionCustomNamedEntityRecognitionDataClass94559368333488] = None
    eden_ai: Optional[PydanticMainTextcustomNamedEntityRecognitionCustomNamedEntityRecognitionDataClass94559369096592] = Field(default=None, alias="eden-ai")
    __properties: ClassVar[List[str]] = ["cohere", "openai", "eden-ai"]

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
        """Create an instance of TextcustomNamedEntityRecognitionResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of eden_ai
        if self.eden_ai:
            _dict['eden-ai'] = self.eden_ai.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TextcustomNamedEntityRecognitionResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cohere": PydanticMainTextcustomNamedEntityRecognitionCustomNamedEntityRecognitionDataClass94559368332544.from_dict(obj["cohere"]) if obj.get("cohere") is not None else None,
            "openai": PydanticMainTextcustomNamedEntityRecognitionCustomNamedEntityRecognitionDataClass94559368333488.from_dict(obj["openai"]) if obj.get("openai") is not None else None,
            "eden-ai": PydanticMainTextcustomNamedEntityRecognitionCustomNamedEntityRecognitionDataClass94559369096592.from_dict(obj["eden-ai"]) if obj.get("eden-ai") is not None else None
        })
        return _obj


