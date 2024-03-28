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
from openapi_client.models.pydantic_main_textanonymization_anonymization_data_class94559364102208 import PydanticMainTextanonymizationAnonymizationDataClass94559364102208
from openapi_client.models.pydantic_main_textanonymization_anonymization_data_class94559364103152 import PydanticMainTextanonymizationAnonymizationDataClass94559364103152
from openapi_client.models.pydantic_main_textanonymization_anonymization_data_class94559368088560 import PydanticMainTextanonymizationAnonymizationDataClass94559368088560
from openapi_client.models.pydantic_main_textanonymization_anonymization_data_class94559369000928 import PydanticMainTextanonymizationAnonymizationDataClass94559369000928
from openapi_client.models.pydantic_main_textanonymization_anonymization_data_class94559369024192 import PydanticMainTextanonymizationAnonymizationDataClass94559369024192
from typing import Optional, Set
from typing_extensions import Self

class TextanonymizationResponseModel(BaseModel):
    """
    TextanonymizationResponseModel
    """ # noqa: E501
    microsoft: Optional[PydanticMainTextanonymizationAnonymizationDataClass94559364102208] = None
    emvista: Optional[PydanticMainTextanonymizationAnonymizationDataClass94559364103152] = None
    oneai: Optional[PydanticMainTextanonymizationAnonymizationDataClass94559368088560] = None
    amazon: Optional[PydanticMainTextanonymizationAnonymizationDataClass94559369000928] = None
    openai: Optional[PydanticMainTextanonymizationAnonymizationDataClass94559369024192] = None
    __properties: ClassVar[List[str]] = ["microsoft", "emvista", "oneai", "amazon", "openai"]

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
        """Create an instance of TextanonymizationResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of microsoft
        if self.microsoft:
            _dict['microsoft'] = self.microsoft.to_dict()
        # override the default output from pydantic by calling `to_dict()` of emvista
        if self.emvista:
            _dict['emvista'] = self.emvista.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oneai
        if self.oneai:
            _dict['oneai'] = self.oneai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amazon
        if self.amazon:
            _dict['amazon'] = self.amazon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of openai
        if self.openai:
            _dict['openai'] = self.openai.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TextanonymizationResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "microsoft": PydanticMainTextanonymizationAnonymizationDataClass94559364102208.from_dict(obj["microsoft"]) if obj.get("microsoft") is not None else None,
            "emvista": PydanticMainTextanonymizationAnonymizationDataClass94559364103152.from_dict(obj["emvista"]) if obj.get("emvista") is not None else None,
            "oneai": PydanticMainTextanonymizationAnonymizationDataClass94559368088560.from_dict(obj["oneai"]) if obj.get("oneai") is not None else None,
            "amazon": PydanticMainTextanonymizationAnonymizationDataClass94559369000928.from_dict(obj["amazon"]) if obj.get("amazon") is not None else None,
            "openai": PydanticMainTextanonymizationAnonymizationDataClass94559369024192.from_dict(obj["openai"]) if obj.get("openai") is not None else None
        })
        return _obj

