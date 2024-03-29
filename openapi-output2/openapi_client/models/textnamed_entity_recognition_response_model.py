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
from openapi_client.models.pydantic_main_textnamed_entity_recognition_named_entity_recognition_data_class94559368893296 import (
    PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368893296,
)
from openapi_client.models.pydantic_main_textnamed_entity_recognition_named_entity_recognition_data_class94559368894240 import (
    PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368894240,
)
from openapi_client.models.pydantic_main_textnamed_entity_recognition_named_entity_recognition_data_class94559368898224 import (
    PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368898224,
)
from openapi_client.models.pydantic_main_textnamed_entity_recognition_named_entity_recognition_data_class94559368902528 import (
    PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368902528,
)
from openapi_client.models.pydantic_main_textnamed_entity_recognition_named_entity_recognition_data_class94559368908400 import (
    PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368908400,
)
from openapi_client.models.pydantic_main_textnamed_entity_recognition_named_entity_recognition_data_class94559368911920 import (
    PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368911920,
)
from openapi_client.models.pydantic_main_textnamed_entity_recognition_named_entity_recognition_data_class94559368915088 import (
    PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368915088,
)
from openapi_client.models.pydantic_main_textnamed_entity_recognition_named_entity_recognition_data_class94559368921984 import (
    PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368921984,
)
from openapi_client.models.pydantic_main_textnamed_entity_recognition_named_entity_recognition_data_class94559368925152 import (
    PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368925152,
)
from openapi_client.models.pydantic_main_textnamed_entity_recognition_named_entity_recognition_data_class94559368937232 import (
    PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368937232,
)
from openapi_client.models.pydantic_main_textnamed_entity_recognition_named_entity_recognition_data_class94559368943056 import (
    PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368943056,
)
from typing import Set
from typing_extensions import Self


class TextnamedEntityRecognitionResponseModel(BaseModel):
    """
    TextnamedEntityRecognitionResponseModel
    """  # noqa: E501

    tenstorrent: Optional[
        PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368908400
    ] = None
    microsoft: Optional[
        PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368911920
    ] = None
    ibm: Optional[
        PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368915088
    ] = None
    google: Optional[
        PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368893296
    ] = None
    oneai: Optional[
        PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368894240
    ] = None
    amazon: Optional[
        PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368937232
    ] = None
    neuralspace: Optional[
        PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368921984
    ] = None
    lettria: Optional[
        PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368925152
    ] = None
    nlpcloud: Optional[
        PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368898224
    ] = None
    openai: Optional[
        PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368902528
    ] = None
    eden_ai: Optional[
        PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368943056
    ] = Field(default=None, alias="eden-ai")
    __properties: ClassVar[List[str]] = [
        "tenstorrent",
        "microsoft",
        "ibm",
        "google",
        "oneai",
        "amazon",
        "neuralspace",
        "lettria",
        "nlpcloud",
        "openai",
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
        """Create an instance of TextnamedEntityRecognitionResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of tenstorrent
        if self.tenstorrent:
            _dict["tenstorrent"] = self.tenstorrent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of microsoft
        if self.microsoft:
            _dict["microsoft"] = self.microsoft.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ibm
        if self.ibm:
            _dict["ibm"] = self.ibm.to_dict()
        # override the default output from pydantic by calling `to_dict()` of google
        if self.google:
            _dict["google"] = self.google.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oneai
        if self.oneai:
            _dict["oneai"] = self.oneai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amazon
        if self.amazon:
            _dict["amazon"] = self.amazon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of neuralspace
        if self.neuralspace:
            _dict["neuralspace"] = self.neuralspace.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lettria
        if self.lettria:
            _dict["lettria"] = self.lettria.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nlpcloud
        if self.nlpcloud:
            _dict["nlpcloud"] = self.nlpcloud.to_dict()
        # override the default output from pydantic by calling `to_dict()` of openai
        if self.openai:
            _dict["openai"] = self.openai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of eden_ai
        if self.eden_ai:
            _dict["eden-ai"] = self.eden_ai.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TextnamedEntityRecognitionResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "tenstorrent": PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368908400.from_dict(
                    obj["tenstorrent"]
                )
                if obj.get("tenstorrent") is not None
                else None,
                "microsoft": PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368911920.from_dict(
                    obj["microsoft"]
                )
                if obj.get("microsoft") is not None
                else None,
                "ibm": PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368915088.from_dict(
                    obj["ibm"]
                )
                if obj.get("ibm") is not None
                else None,
                "google": PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368893296.from_dict(
                    obj["google"]
                )
                if obj.get("google") is not None
                else None,
                "oneai": PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368894240.from_dict(
                    obj["oneai"]
                )
                if obj.get("oneai") is not None
                else None,
                "amazon": PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368937232.from_dict(
                    obj["amazon"]
                )
                if obj.get("amazon") is not None
                else None,
                "neuralspace": PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368921984.from_dict(
                    obj["neuralspace"]
                )
                if obj.get("neuralspace") is not None
                else None,
                "lettria": PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368925152.from_dict(
                    obj["lettria"]
                )
                if obj.get("lettria") is not None
                else None,
                "nlpcloud": PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368898224.from_dict(
                    obj["nlpcloud"]
                )
                if obj.get("nlpcloud") is not None
                else None,
                "openai": PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368902528.from_dict(
                    obj["openai"]
                )
                if obj.get("openai") is not None
                else None,
                "eden-ai": PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368943056.from_dict(
                    obj["eden-ai"]
                )
                if obj.get("eden-ai") is not None
                else None,
            }
        )
        return _obj
