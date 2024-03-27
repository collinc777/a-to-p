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
from openapi_client.models.pydantic_main_translationlanguage_detection_language_detection_data_class94559369354560 import (
    PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559369354560,
)
from openapi_client.models.pydantic_main_translationlanguage_detection_language_detection_data_class94559369355504 import (
    PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559369355504,
)
from openapi_client.models.pydantic_main_translationlanguage_detection_language_detection_data_class94559370049504 import (
    PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370049504,
)
from openapi_client.models.pydantic_main_translationlanguage_detection_language_detection_data_class94559370151328 import (
    PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370151328,
)
from openapi_client.models.pydantic_main_translationlanguage_detection_language_detection_data_class94559370156976 import (
    PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370156976,
)
from openapi_client.models.pydantic_main_translationlanguage_detection_language_detection_data_class94559370157936 import (
    PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370157936,
)
from openapi_client.models.pydantic_main_translationlanguage_detection_language_detection_data_class94559370164464 import (
    PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370164464,
)
from openapi_client.models.pydantic_main_translationlanguage_detection_language_detection_data_class94559370168224 import (
    PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370168224,
)
from openapi_client.models.pydantic_main_translationlanguage_detection_language_detection_data_class94559370185664 import (
    PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370185664,
)
from typing import Set
from typing_extensions import Self


class TranslationlanguageDetectionResponseModel(BaseModel):
    """
    TranslationlanguageDetectionResponseModel
    """  # noqa: E501

    microsoft: Optional[
        PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370157936
    ] = None
    ibm: Optional[
        PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370185664
    ] = None
    google: Optional[
        PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370049504
    ] = None
    oneai: Optional[
        PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559369354560
    ] = None
    amazon: Optional[
        PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370156976
    ] = None
    neuralspace: Optional[
        PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559369355504
    ] = None
    modernmt: Optional[
        PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370151328
    ] = None
    openai: Optional[
        PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370164464
    ] = None
    eden_ai: Optional[
        PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370168224
    ] = Field(default=None, alias="eden-ai")
    __properties: ClassVar[List[str]] = [
        "microsoft",
        "ibm",
        "google",
        "oneai",
        "amazon",
        "neuralspace",
        "modernmt",
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
        """Create an instance of TranslationlanguageDetectionResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of modernmt
        if self.modernmt:
            _dict["modernmt"] = self.modernmt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of openai
        if self.openai:
            _dict["openai"] = self.openai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of eden_ai
        if self.eden_ai:
            _dict["eden-ai"] = self.eden_ai.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TranslationlanguageDetectionResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "microsoft": PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370157936.from_dict(
                    obj["microsoft"]
                )
                if obj.get("microsoft") is not None
                else None,
                "ibm": PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370185664.from_dict(
                    obj["ibm"]
                )
                if obj.get("ibm") is not None
                else None,
                "google": PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370049504.from_dict(
                    obj["google"]
                )
                if obj.get("google") is not None
                else None,
                "oneai": PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559369354560.from_dict(
                    obj["oneai"]
                )
                if obj.get("oneai") is not None
                else None,
                "amazon": PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370156976.from_dict(
                    obj["amazon"]
                )
                if obj.get("amazon") is not None
                else None,
                "neuralspace": PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559369355504.from_dict(
                    obj["neuralspace"]
                )
                if obj.get("neuralspace") is not None
                else None,
                "modernmt": PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370151328.from_dict(
                    obj["modernmt"]
                )
                if obj.get("modernmt") is not None
                else None,
                "openai": PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370164464.from_dict(
                    obj["openai"]
                )
                if obj.get("openai") is not None
                else None,
                "eden-ai": PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370168224.from_dict(
                    obj["eden-ai"]
                )
                if obj.get("eden-ai") is not None
                else None,
            }
        )
        return _obj
