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
from openapi_client.models.pydantic_main_audiotext_to_speech_text_to_speech_data_class94559359101056 import PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359101056
from openapi_client.models.pydantic_main_audiotext_to_speech_text_to_speech_data_class94559359102096 import PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359102096
from openapi_client.models.pydantic_main_audiotext_to_speech_text_to_speech_data_class94559359103136 import PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359103136
from openapi_client.models.pydantic_main_audiotext_to_speech_text_to_speech_data_class94559359104176 import PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359104176
from openapi_client.models.pydantic_main_audiotext_to_speech_text_to_speech_data_class94559359105216 import PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359105216
from openapi_client.models.pydantic_main_audiotext_to_speech_text_to_speech_data_class94559359106256 import PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359106256
from openapi_client.models.pydantic_main_audiotext_to_speech_text_to_speech_data_class94559359237264 import PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359237264
from typing import Optional, Set
from typing_extensions import Self

class AudiotextToSpeechResponseModel(BaseModel):
    """
    AudiotextToSpeechResponseModel
    """ # noqa: E501
    microsoft: Optional[PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359106256] = None
    ibm: Optional[PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359105216] = None
    google: Optional[PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359104176] = None
    amazon: Optional[PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359103136] = None
    elevenlabs: Optional[PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359102096] = None
    lovoai: Optional[PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359101056] = None
    openai: Optional[PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359237264] = None
    __properties: ClassVar[List[str]] = ["microsoft", "ibm", "google", "amazon", "elevenlabs", "lovoai", "openai"]

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
        """Create an instance of AudiotextToSpeechResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ibm
        if self.ibm:
            _dict['ibm'] = self.ibm.to_dict()
        # override the default output from pydantic by calling `to_dict()` of google
        if self.google:
            _dict['google'] = self.google.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amazon
        if self.amazon:
            _dict['amazon'] = self.amazon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of elevenlabs
        if self.elevenlabs:
            _dict['elevenlabs'] = self.elevenlabs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lovoai
        if self.lovoai:
            _dict['lovoai'] = self.lovoai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of openai
        if self.openai:
            _dict['openai'] = self.openai.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AudiotextToSpeechResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "microsoft": PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359106256.from_dict(obj["microsoft"]) if obj.get("microsoft") is not None else None,
            "ibm": PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359105216.from_dict(obj["ibm"]) if obj.get("ibm") is not None else None,
            "google": PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359104176.from_dict(obj["google"]) if obj.get("google") is not None else None,
            "amazon": PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359103136.from_dict(obj["amazon"]) if obj.get("amazon") is not None else None,
            "elevenlabs": PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359102096.from_dict(obj["elevenlabs"]) if obj.get("elevenlabs") is not None else None,
            "lovoai": PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359101056.from_dict(obj["lovoai"]) if obj.get("lovoai") is not None else None,
            "openai": PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359237264.from_dict(obj["openai"]) if obj.get("openai") is not None else None
        })
        return _obj


