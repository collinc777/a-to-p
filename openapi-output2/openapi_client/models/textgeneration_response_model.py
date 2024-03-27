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
from openapi_client.models.pydantic_main_textgeneration_generation_data_class94559369053024 import (
    PydanticMainTextgenerationGenerationDataClass94559369053024,
)
from openapi_client.models.pydantic_main_textgeneration_generation_data_class94559369053968 import (
    PydanticMainTextgenerationGenerationDataClass94559369053968,
)
from openapi_client.models.pydantic_main_textgeneration_generation_data_class94559369055456 import (
    PydanticMainTextgenerationGenerationDataClass94559369055456,
)
from openapi_client.models.pydantic_main_textgeneration_generation_data_class94559369058896 import (
    PydanticMainTextgenerationGenerationDataClass94559369058896,
)
from openapi_client.models.pydantic_main_textgeneration_generation_data_class94559369066432 import (
    PydanticMainTextgenerationGenerationDataClass94559369066432,
)
from openapi_client.models.pydantic_main_textgeneration_generation_data_class94559369067376 import (
    PydanticMainTextgenerationGenerationDataClass94559369067376,
)
from openapi_client.models.pydantic_main_textgeneration_generation_data_class94559369073472 import (
    PydanticMainTextgenerationGenerationDataClass94559369073472,
)
from openapi_client.models.pydantic_main_textgeneration_generation_data_class94559369074416 import (
    PydanticMainTextgenerationGenerationDataClass94559369074416,
)
from openapi_client.models.pydantic_main_textgeneration_generation_data_class94559369078400 import (
    PydanticMainTextgenerationGenerationDataClass94559369078400,
)
from typing import Set
from typing_extensions import Self


class TextgenerationResponseModel(BaseModel):
    """
    TextgenerationResponseModel
    """  # noqa: E501

    meta: Optional[PydanticMainTextgenerationGenerationDataClass94559369073472] = None
    google: Optional[PydanticMainTextgenerationGenerationDataClass94559369074416] = None
    cohere: Optional[PydanticMainTextgenerationGenerationDataClass94559369053024] = None
    mistral: Optional[PydanticMainTextgenerationGenerationDataClass94559369053968] = (
        None
    )
    amazon: Optional[PydanticMainTextgenerationGenerationDataClass94559369055456] = None
    ai21labs: Optional[PydanticMainTextgenerationGenerationDataClass94559369058896] = (
        None
    )
    clarifai: Optional[PydanticMainTextgenerationGenerationDataClass94559369066432] = (
        None
    )
    openai: Optional[PydanticMainTextgenerationGenerationDataClass94559369067376] = None
    anthropic: Optional[PydanticMainTextgenerationGenerationDataClass94559369078400] = (
        None
    )
    __properties: ClassVar[List[str]] = [
        "meta",
        "google",
        "cohere",
        "mistral",
        "amazon",
        "ai21labs",
        "clarifai",
        "openai",
        "anthropic",
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
        """Create an instance of TextgenerationResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict["meta"] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of google
        if self.google:
            _dict["google"] = self.google.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cohere
        if self.cohere:
            _dict["cohere"] = self.cohere.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mistral
        if self.mistral:
            _dict["mistral"] = self.mistral.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amazon
        if self.amazon:
            _dict["amazon"] = self.amazon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ai21labs
        if self.ai21labs:
            _dict["ai21labs"] = self.ai21labs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of clarifai
        if self.clarifai:
            _dict["clarifai"] = self.clarifai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of openai
        if self.openai:
            _dict["openai"] = self.openai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anthropic
        if self.anthropic:
            _dict["anthropic"] = self.anthropic.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TextgenerationResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "meta": PydanticMainTextgenerationGenerationDataClass94559369073472.from_dict(
                    obj["meta"]
                )
                if obj.get("meta") is not None
                else None,
                "google": PydanticMainTextgenerationGenerationDataClass94559369074416.from_dict(
                    obj["google"]
                )
                if obj.get("google") is not None
                else None,
                "cohere": PydanticMainTextgenerationGenerationDataClass94559369053024.from_dict(
                    obj["cohere"]
                )
                if obj.get("cohere") is not None
                else None,
                "mistral": PydanticMainTextgenerationGenerationDataClass94559369053968.from_dict(
                    obj["mistral"]
                )
                if obj.get("mistral") is not None
                else None,
                "amazon": PydanticMainTextgenerationGenerationDataClass94559369055456.from_dict(
                    obj["amazon"]
                )
                if obj.get("amazon") is not None
                else None,
                "ai21labs": PydanticMainTextgenerationGenerationDataClass94559369058896.from_dict(
                    obj["ai21labs"]
                )
                if obj.get("ai21labs") is not None
                else None,
                "clarifai": PydanticMainTextgenerationGenerationDataClass94559369066432.from_dict(
                    obj["clarifai"]
                )
                if obj.get("clarifai") is not None
                else None,
                "openai": PydanticMainTextgenerationGenerationDataClass94559369067376.from_dict(
                    obj["openai"]
                )
                if obj.get("openai") is not None
                else None,
                "anthropic": PydanticMainTextgenerationGenerationDataClass94559369078400.from_dict(
                    obj["anthropic"]
                )
                if obj.get("anthropic") is not None
                else None,
            }
        )
        return _obj
