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
from openapi_client.models.pydantic_main_ocrresume_parser_resume_parser_data_class94559364145744 import (
    PydanticMainOcrresumeParserResumeParserDataClass94559364145744,
)
from openapi_client.models.pydantic_main_ocrresume_parser_resume_parser_data_class94559364149296 import (
    PydanticMainOcrresumeParserResumeParserDataClass94559364149296,
)
from openapi_client.models.pydantic_main_ocrresume_parser_resume_parser_data_class94559364152112 import (
    PydanticMainOcrresumeParserResumeParserDataClass94559364152112,
)
from openapi_client.models.pydantic_main_ocrresume_parser_resume_parser_data_class94559364163568 import (
    PydanticMainOcrresumeParserResumeParserDataClass94559364163568,
)
from openapi_client.models.pydantic_main_ocrresume_parser_resume_parser_data_class94559367589536 import (
    PydanticMainOcrresumeParserResumeParserDataClass94559367589536,
)
from openapi_client.models.pydantic_main_ocrresume_parser_resume_parser_data_class94559367595968 import (
    PydanticMainOcrresumeParserResumeParserDataClass94559367595968,
)
from typing import Set
from typing_extensions import Self


class OcrresumeParserResponseModel(BaseModel):
    """
    OcrresumeParserResponseModel
    """  # noqa: E501

    klippa: Optional[PydanticMainOcrresumeParserResumeParserDataClass94559367589536] = (
        None
    )
    extracta: Optional[
        PydanticMainOcrresumeParserResumeParserDataClass94559364163568
    ] = None
    affinda: Optional[
        PydanticMainOcrresumeParserResumeParserDataClass94559364145744
    ] = None
    senseloaf: Optional[
        PydanticMainOcrresumeParserResumeParserDataClass94559364149296
    ] = None
    hireability: Optional[
        PydanticMainOcrresumeParserResumeParserDataClass94559367595968
    ] = None
    eden_ai: Optional[
        PydanticMainOcrresumeParserResumeParserDataClass94559364152112
    ] = Field(default=None, alias="eden-ai")
    __properties: ClassVar[List[str]] = [
        "klippa",
        "extracta",
        "affinda",
        "senseloaf",
        "hireability",
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
        """Create an instance of OcrresumeParserResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of klippa
        if self.klippa:
            _dict["klippa"] = self.klippa.to_dict()
        # override the default output from pydantic by calling `to_dict()` of extracta
        if self.extracta:
            _dict["extracta"] = self.extracta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of affinda
        if self.affinda:
            _dict["affinda"] = self.affinda.to_dict()
        # override the default output from pydantic by calling `to_dict()` of senseloaf
        if self.senseloaf:
            _dict["senseloaf"] = self.senseloaf.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hireability
        if self.hireability:
            _dict["hireability"] = self.hireability.to_dict()
        # override the default output from pydantic by calling `to_dict()` of eden_ai
        if self.eden_ai:
            _dict["eden-ai"] = self.eden_ai.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OcrresumeParserResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "klippa": PydanticMainOcrresumeParserResumeParserDataClass94559367589536.from_dict(
                    obj["klippa"]
                )
                if obj.get("klippa") is not None
                else None,
                "extracta": PydanticMainOcrresumeParserResumeParserDataClass94559364163568.from_dict(
                    obj["extracta"]
                )
                if obj.get("extracta") is not None
                else None,
                "affinda": PydanticMainOcrresumeParserResumeParserDataClass94559364145744.from_dict(
                    obj["affinda"]
                )
                if obj.get("affinda") is not None
                else None,
                "senseloaf": PydanticMainOcrresumeParserResumeParserDataClass94559364149296.from_dict(
                    obj["senseloaf"]
                )
                if obj.get("senseloaf") is not None
                else None,
                "hireability": PydanticMainOcrresumeParserResumeParserDataClass94559367595968.from_dict(
                    obj["hireability"]
                )
                if obj.get("hireability") is not None
                else None,
                "eden-ai": PydanticMainOcrresumeParserResumeParserDataClass94559364152112.from_dict(
                    obj["eden-ai"]
                )
                if obj.get("eden-ai") is not None
                else None,
            }
        )
        return _obj
