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
from openapi_client.models.pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367625488 import (
    PydanticMainOcrreceiptParserReceiptParserDataClass94559367625488,
)
from openapi_client.models.pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367638928 import (
    PydanticMainOcrreceiptParserReceiptParserDataClass94559367638928,
)
from openapi_client.models.pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367643952 import (
    PydanticMainOcrreceiptParserReceiptParserDataClass94559367643952,
)
from openapi_client.models.pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367647808 import (
    PydanticMainOcrreceiptParserReceiptParserDataClass94559367647808,
)
from openapi_client.models.pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367655488 import (
    PydanticMainOcrreceiptParserReceiptParserDataClass94559367655488,
)
from openapi_client.models.pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367664464 import (
    PydanticMainOcrreceiptParserReceiptParserDataClass94559367664464,
)
from openapi_client.models.pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367671728 import (
    PydanticMainOcrreceiptParserReceiptParserDataClass94559367671728,
)
from openapi_client.models.pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367675488 import (
    PydanticMainOcrreceiptParserReceiptParserDataClass94559367675488,
)
from openapi_client.models.pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367681824 import (
    PydanticMainOcrreceiptParserReceiptParserDataClass94559367681824,
)
from openapi_client.models.pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367689088 import (
    PydanticMainOcrreceiptParserReceiptParserDataClass94559367689088,
)
from openapi_client.models.pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367696352 import (
    PydanticMainOcrreceiptParserReceiptParserDataClass94559367696352,
)
from typing import Set
from typing_extensions import Self


class OcrreceiptParserResponseModel(BaseModel):
    """
    OcrreceiptParserResponseModel
    """  # noqa: E501

    klippa: Optional[
        PydanticMainOcrreceiptParserReceiptParserDataClass94559367643952
    ] = None
    mindee: Optional[
        PydanticMainOcrreceiptParserReceiptParserDataClass94559367625488
    ] = None
    affinda: Optional[
        PydanticMainOcrreceiptParserReceiptParserDataClass94559367655488
    ] = None
    microsoft: Optional[
        PydanticMainOcrreceiptParserReceiptParserDataClass94559367647808
    ] = None
    tabscanner: Optional[
        PydanticMainOcrreceiptParserReceiptParserDataClass94559367638928
    ] = None
    google: Optional[
        PydanticMainOcrreceiptParserReceiptParserDataClass94559367664464
    ] = None
    amazon: Optional[
        PydanticMainOcrreceiptParserReceiptParserDataClass94559367671728
    ] = None
    dataleon: Optional[
        PydanticMainOcrreceiptParserReceiptParserDataClass94559367675488
    ] = None
    veryfi: Optional[
        PydanticMainOcrreceiptParserReceiptParserDataClass94559367681824
    ] = None
    var_base64: Optional[
        PydanticMainOcrreceiptParserReceiptParserDataClass94559367689088
    ] = Field(default=None, alias="base64")
    eden_ai: Optional[
        PydanticMainOcrreceiptParserReceiptParserDataClass94559367696352
    ] = Field(default=None, alias="eden-ai")
    __properties: ClassVar[List[str]] = [
        "klippa",
        "mindee",
        "affinda",
        "microsoft",
        "tabscanner",
        "google",
        "amazon",
        "dataleon",
        "veryfi",
        "base64",
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
        """Create an instance of OcrreceiptParserResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of mindee
        if self.mindee:
            _dict["mindee"] = self.mindee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of affinda
        if self.affinda:
            _dict["affinda"] = self.affinda.to_dict()
        # override the default output from pydantic by calling `to_dict()` of microsoft
        if self.microsoft:
            _dict["microsoft"] = self.microsoft.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tabscanner
        if self.tabscanner:
            _dict["tabscanner"] = self.tabscanner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of google
        if self.google:
            _dict["google"] = self.google.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amazon
        if self.amazon:
            _dict["amazon"] = self.amazon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dataleon
        if self.dataleon:
            _dict["dataleon"] = self.dataleon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of veryfi
        if self.veryfi:
            _dict["veryfi"] = self.veryfi.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_base64
        if self.var_base64:
            _dict["base64"] = self.var_base64.to_dict()
        # override the default output from pydantic by calling `to_dict()` of eden_ai
        if self.eden_ai:
            _dict["eden-ai"] = self.eden_ai.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OcrreceiptParserResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "klippa": PydanticMainOcrreceiptParserReceiptParserDataClass94559367643952.from_dict(
                    obj["klippa"]
                )
                if obj.get("klippa") is not None
                else None,
                "mindee": PydanticMainOcrreceiptParserReceiptParserDataClass94559367625488.from_dict(
                    obj["mindee"]
                )
                if obj.get("mindee") is not None
                else None,
                "affinda": PydanticMainOcrreceiptParserReceiptParserDataClass94559367655488.from_dict(
                    obj["affinda"]
                )
                if obj.get("affinda") is not None
                else None,
                "microsoft": PydanticMainOcrreceiptParserReceiptParserDataClass94559367647808.from_dict(
                    obj["microsoft"]
                )
                if obj.get("microsoft") is not None
                else None,
                "tabscanner": PydanticMainOcrreceiptParserReceiptParserDataClass94559367638928.from_dict(
                    obj["tabscanner"]
                )
                if obj.get("tabscanner") is not None
                else None,
                "google": PydanticMainOcrreceiptParserReceiptParserDataClass94559367664464.from_dict(
                    obj["google"]
                )
                if obj.get("google") is not None
                else None,
                "amazon": PydanticMainOcrreceiptParserReceiptParserDataClass94559367671728.from_dict(
                    obj["amazon"]
                )
                if obj.get("amazon") is not None
                else None,
                "dataleon": PydanticMainOcrreceiptParserReceiptParserDataClass94559367675488.from_dict(
                    obj["dataleon"]
                )
                if obj.get("dataleon") is not None
                else None,
                "veryfi": PydanticMainOcrreceiptParserReceiptParserDataClass94559367681824.from_dict(
                    obj["veryfi"]
                )
                if obj.get("veryfi") is not None
                else None,
                "base64": PydanticMainOcrreceiptParserReceiptParserDataClass94559367689088.from_dict(
                    obj["base64"]
                )
                if obj.get("base64") is not None
                else None,
                "eden-ai": PydanticMainOcrreceiptParserReceiptParserDataClass94559367696352.from_dict(
                    obj["eden-ai"]
                )
                if obj.get("eden-ai") is not None
                else None,
            }
        )
        return _obj