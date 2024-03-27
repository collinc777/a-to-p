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
from openapi_client.models.pydantic_main_textsyntax_analysis_syntax_analysis_data_class94559367951472 import (
    PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559367951472,
)
from openapi_client.models.pydantic_main_textsyntax_analysis_syntax_analysis_data_class94559368792608 import (
    PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368792608,
)
from openapi_client.models.pydantic_main_textsyntax_analysis_syntax_analysis_data_class94559368794976 import (
    PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368794976,
)
from openapi_client.models.pydantic_main_textsyntax_analysis_syntax_analysis_data_class94559368807376 import (
    PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368807376,
)
from openapi_client.models.pydantic_main_textsyntax_analysis_syntax_analysis_data_class94559368813120 import (
    PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368813120,
)
from openapi_client.models.pydantic_main_textsyntax_analysis_syntax_analysis_data_class94559368820224 import (
    PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368820224,
)
from typing import Set
from typing_extensions import Self


class TextsyntaxAnalysisResponseModel(BaseModel):
    """
    TextsyntaxAnalysisResponseModel
    """  # noqa: E501

    ibm: Optional[
        PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368820224
    ] = None
    emvista: Optional[
        PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559367951472
    ] = None
    google: Optional[
        PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368792608
    ] = None
    amazon: Optional[
        PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368807376
    ] = None
    lettria: Optional[
        PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368813120
    ] = None
    eden_ai: Optional[
        PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368794976
    ] = Field(default=None, alias="eden-ai")
    __properties: ClassVar[List[str]] = [
        "ibm",
        "emvista",
        "google",
        "amazon",
        "lettria",
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
        """Create an instance of TextsyntaxAnalysisResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ibm
        if self.ibm:
            _dict["ibm"] = self.ibm.to_dict()
        # override the default output from pydantic by calling `to_dict()` of emvista
        if self.emvista:
            _dict["emvista"] = self.emvista.to_dict()
        # override the default output from pydantic by calling `to_dict()` of google
        if self.google:
            _dict["google"] = self.google.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amazon
        if self.amazon:
            _dict["amazon"] = self.amazon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lettria
        if self.lettria:
            _dict["lettria"] = self.lettria.to_dict()
        # override the default output from pydantic by calling `to_dict()` of eden_ai
        if self.eden_ai:
            _dict["eden-ai"] = self.eden_ai.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TextsyntaxAnalysisResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "ibm": PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368820224.from_dict(
                    obj["ibm"]
                )
                if obj.get("ibm") is not None
                else None,
                "emvista": PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559367951472.from_dict(
                    obj["emvista"]
                )
                if obj.get("emvista") is not None
                else None,
                "google": PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368792608.from_dict(
                    obj["google"]
                )
                if obj.get("google") is not None
                else None,
                "amazon": PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368807376.from_dict(
                    obj["amazon"]
                )
                if obj.get("amazon") is not None
                else None,
                "lettria": PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368813120.from_dict(
                    obj["lettria"]
                )
                if obj.get("lettria") is not None
                else None,
                "eden-ai": PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368794976.from_dict(
                    obj["eden-ai"]
                )
                if obj.get("eden-ai") is not None
                else None,
            }
        )
        return _obj
