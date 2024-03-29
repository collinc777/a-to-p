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
from openapi_client.models.pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559363906848 import (
    PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363906848,
)
from openapi_client.models.pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559363957840 import (
    PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363957840,
)
from openapi_client.models.pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559363968704 import (
    PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363968704,
)
from openapi_client.models.pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559363976352 import (
    PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363976352,
)
from openapi_client.models.pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559363996048 import (
    PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363996048,
)
from openapi_client.models.pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559364008832 import (
    PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364008832,
)
from openapi_client.models.pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559364014112 import (
    PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364014112,
)
from openapi_client.models.pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559364015888 import (
    PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364015888,
)
from openapi_client.models.pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559364029664 import (
    PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364029664,
)
from openapi_client.models.pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559364048176 import (
    PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364048176,
)
from openapi_client.models.pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559364062544 import (
    PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364062544,
)
from typing import Set
from typing_extensions import Self


class OcrinvoiceParserResponseModel(BaseModel):
    """
    OcrinvoiceParserResponseModel
    """  # noqa: E501

    klippa: Optional[
        PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363906848
    ] = None
    mindee: Optional[
        PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363957840
    ] = None
    affinda: Optional[
        PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363976352
    ] = None
    microsoft: Optional[
        PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363968704
    ] = None
    google: Optional[
        PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363996048
    ] = None
    amazon: Optional[
        PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364015888
    ] = None
    dataleon: Optional[
        PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364008832
    ] = None
    rossum: Optional[
        PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364029664
    ] = None
    veryfi: Optional[
        PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364048176
    ] = None
    var_base64: Optional[
        PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364014112
    ] = Field(default=None, alias="base64")
    eden_ai: Optional[
        PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364062544
    ] = Field(default=None, alias="eden-ai")
    __properties: ClassVar[List[str]] = [
        "klippa",
        "mindee",
        "affinda",
        "microsoft",
        "google",
        "amazon",
        "dataleon",
        "rossum",
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
        """Create an instance of OcrinvoiceParserResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of google
        if self.google:
            _dict["google"] = self.google.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amazon
        if self.amazon:
            _dict["amazon"] = self.amazon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dataleon
        if self.dataleon:
            _dict["dataleon"] = self.dataleon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rossum
        if self.rossum:
            _dict["rossum"] = self.rossum.to_dict()
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
        """Create an instance of OcrinvoiceParserResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "klippa": PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363906848.from_dict(
                    obj["klippa"]
                )
                if obj.get("klippa") is not None
                else None,
                "mindee": PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363957840.from_dict(
                    obj["mindee"]
                )
                if obj.get("mindee") is not None
                else None,
                "affinda": PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363976352.from_dict(
                    obj["affinda"]
                )
                if obj.get("affinda") is not None
                else None,
                "microsoft": PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363968704.from_dict(
                    obj["microsoft"]
                )
                if obj.get("microsoft") is not None
                else None,
                "google": PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363996048.from_dict(
                    obj["google"]
                )
                if obj.get("google") is not None
                else None,
                "amazon": PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364015888.from_dict(
                    obj["amazon"]
                )
                if obj.get("amazon") is not None
                else None,
                "dataleon": PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364008832.from_dict(
                    obj["dataleon"]
                )
                if obj.get("dataleon") is not None
                else None,
                "rossum": PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364029664.from_dict(
                    obj["rossum"]
                )
                if obj.get("rossum") is not None
                else None,
                "veryfi": PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364048176.from_dict(
                    obj["veryfi"]
                )
                if obj.get("veryfi") is not None
                else None,
                "base64": PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364014112.from_dict(
                    obj["base64"]
                )
                if obj.get("base64") is not None
                else None,
                "eden-ai": PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364062544.from_dict(
                    obj["eden-ai"]
                )
                if obj.get("eden-ai") is not None
                else None,
            }
        )
        return _obj
