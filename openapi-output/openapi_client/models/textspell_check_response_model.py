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
from openapi_client.models.pydantic_main_textspell_check_spell_check_data_class94559369107088 import PydanticMainTextspellCheckSpellCheckDataClass94559369107088
from openapi_client.models.pydantic_main_textspell_check_spell_check_data_class94559369163728 import PydanticMainTextspellCheckSpellCheckDataClass94559369163728
from openapi_client.models.pydantic_main_textspell_check_spell_check_data_class94559369164672 import PydanticMainTextspellCheckSpellCheckDataClass94559369164672
from openapi_client.models.pydantic_main_textspell_check_spell_check_data_class94559369172032 import PydanticMainTextspellCheckSpellCheckDataClass94559369172032
from openapi_client.models.pydantic_main_textspell_check_spell_check_data_class94559369187248 import PydanticMainTextspellCheckSpellCheckDataClass94559369187248
from openapi_client.models.pydantic_main_textspell_check_spell_check_data_class94559369190960 import PydanticMainTextspellCheckSpellCheckDataClass94559369190960
from openapi_client.models.pydantic_main_textspell_check_spell_check_data_class94559369195264 import PydanticMainTextspellCheckSpellCheckDataClass94559369195264
from typing import Optional, Set
from typing_extensions import Self

class TextspellCheckResponseModel(BaseModel):
    """
    TextspellCheckResponseModel
    """ # noqa: E501
    sapling: Optional[PydanticMainTextspellCheckSpellCheckDataClass94559369107088] = None
    microsoft: Optional[PydanticMainTextspellCheckSpellCheckDataClass94559369172032] = None
    cohere: Optional[PydanticMainTextspellCheckSpellCheckDataClass94559369163728] = None
    ai21labs: Optional[PydanticMainTextspellCheckSpellCheckDataClass94559369164672] = None
    prowritingaid: Optional[PydanticMainTextspellCheckSpellCheckDataClass94559369187248] = None
    nlpcloud: Optional[PydanticMainTextspellCheckSpellCheckDataClass94559369190960] = None
    openai: Optional[PydanticMainTextspellCheckSpellCheckDataClass94559369195264] = None
    __properties: ClassVar[List[str]] = ["sapling", "microsoft", "cohere", "ai21labs", "prowritingaid", "nlpcloud", "openai"]

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
        """Create an instance of TextspellCheckResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of sapling
        if self.sapling:
            _dict['sapling'] = self.sapling.to_dict()
        # override the default output from pydantic by calling `to_dict()` of microsoft
        if self.microsoft:
            _dict['microsoft'] = self.microsoft.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cohere
        if self.cohere:
            _dict['cohere'] = self.cohere.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ai21labs
        if self.ai21labs:
            _dict['ai21labs'] = self.ai21labs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of prowritingaid
        if self.prowritingaid:
            _dict['prowritingaid'] = self.prowritingaid.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nlpcloud
        if self.nlpcloud:
            _dict['nlpcloud'] = self.nlpcloud.to_dict()
        # override the default output from pydantic by calling `to_dict()` of openai
        if self.openai:
            _dict['openai'] = self.openai.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TextspellCheckResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sapling": PydanticMainTextspellCheckSpellCheckDataClass94559369107088.from_dict(obj["sapling"]) if obj.get("sapling") is not None else None,
            "microsoft": PydanticMainTextspellCheckSpellCheckDataClass94559369172032.from_dict(obj["microsoft"]) if obj.get("microsoft") is not None else None,
            "cohere": PydanticMainTextspellCheckSpellCheckDataClass94559369163728.from_dict(obj["cohere"]) if obj.get("cohere") is not None else None,
            "ai21labs": PydanticMainTextspellCheckSpellCheckDataClass94559369164672.from_dict(obj["ai21labs"]) if obj.get("ai21labs") is not None else None,
            "prowritingaid": PydanticMainTextspellCheckSpellCheckDataClass94559369187248.from_dict(obj["prowritingaid"]) if obj.get("prowritingaid") is not None else None,
            "nlpcloud": PydanticMainTextspellCheckSpellCheckDataClass94559369190960.from_dict(obj["nlpcloud"]) if obj.get("nlpcloud") is not None else None,
            "openai": PydanticMainTextspellCheckSpellCheckDataClass94559369195264.from_dict(obj["openai"]) if obj.get("openai") is not None else None
        })
        return _obj

