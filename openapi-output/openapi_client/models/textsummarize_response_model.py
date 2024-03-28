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
from openapi_client.models.pydantic_main_textsummarize_summarize_data_class94559363614384 import PydanticMainTextsummarizeSummarizeDataClass94559363614384
from openapi_client.models.pydantic_main_textsummarize_summarize_data_class94559363895952 import PydanticMainTextsummarizeSummarizeDataClass94559363895952
from openapi_client.models.pydantic_main_textsummarize_summarize_data_class94559363917488 import PydanticMainTextsummarizeSummarizeDataClass94559363917488
from openapi_client.models.pydantic_main_textsummarize_summarize_data_class94559363928880 import PydanticMainTextsummarizeSummarizeDataClass94559363928880
from openapi_client.models.pydantic_main_textsummarize_summarize_data_class94559364428208 import PydanticMainTextsummarizeSummarizeDataClass94559364428208
from openapi_client.models.pydantic_main_textsummarize_summarize_data_class94559364620768 import PydanticMainTextsummarizeSummarizeDataClass94559364620768
from openapi_client.models.pydantic_main_textsummarize_summarize_data_class94559364661856 import PydanticMainTextsummarizeSummarizeDataClass94559364661856
from openapi_client.models.pydantic_main_textsummarize_summarize_data_class94559364732896 import PydanticMainTextsummarizeSummarizeDataClass94559364732896
from openapi_client.models.pydantic_main_textsummarize_summarize_data_class94559367615696 import PydanticMainTextsummarizeSummarizeDataClass94559367615696
from openapi_client.models.pydantic_main_textsummarize_summarize_data_class94559368039472 import PydanticMainTextsummarizeSummarizeDataClass94559368039472
from openapi_client.models.pydantic_main_textsummarize_summarize_data_class94559368273408 import PydanticMainTextsummarizeSummarizeDataClass94559368273408
from openapi_client.models.pydantic_main_textsummarize_summarize_data_class94559368393536 import PydanticMainTextsummarizeSummarizeDataClass94559368393536
from openapi_client.models.pydantic_main_textsummarize_summarize_data_class94559368914848 import PydanticMainTextsummarizeSummarizeDataClass94559368914848
from typing import Optional, Set
from typing_extensions import Self

class TextsummarizeResponseModel(BaseModel):
    """
    TextsummarizeResponseModel
    """ # noqa: E501
    writesonic: Optional[PydanticMainTextsummarizeSummarizeDataClass94559364428208] = None
    microsoft: Optional[PydanticMainTextsummarizeSummarizeDataClass94559368039472] = None
    emvista: Optional[PydanticMainTextsummarizeSummarizeDataClass94559368393536] = None
    cohere: Optional[PydanticMainTextsummarizeSummarizeDataClass94559368273408] = None
    nlpcloud: Optional[PydanticMainTextsummarizeSummarizeDataClass94559363917488] = None
    oneai: Optional[PydanticMainTextsummarizeSummarizeDataClass94559364661856] = None
    ai21labs: Optional[PydanticMainTextsummarizeSummarizeDataClass94559363614384] = None
    alephalpha: Optional[PydanticMainTextsummarizeSummarizeDataClass94559363895952] = None
    openai: Optional[PydanticMainTextsummarizeSummarizeDataClass94559368914848] = None
    meaningcloud: Optional[PydanticMainTextsummarizeSummarizeDataClass94559367615696] = None
    huggingface: Optional[PydanticMainTextsummarizeSummarizeDataClass94559364620768] = None
    anthropic: Optional[PydanticMainTextsummarizeSummarizeDataClass94559364732896] = None
    connexun: Optional[PydanticMainTextsummarizeSummarizeDataClass94559363928880] = None
    __properties: ClassVar[List[str]] = ["writesonic", "microsoft", "emvista", "cohere", "nlpcloud", "oneai", "ai21labs", "alephalpha", "openai", "meaningcloud", "huggingface", "anthropic", "connexun"]

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
        """Create an instance of TextsummarizeResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of writesonic
        if self.writesonic:
            _dict['writesonic'] = self.writesonic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of microsoft
        if self.microsoft:
            _dict['microsoft'] = self.microsoft.to_dict()
        # override the default output from pydantic by calling `to_dict()` of emvista
        if self.emvista:
            _dict['emvista'] = self.emvista.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cohere
        if self.cohere:
            _dict['cohere'] = self.cohere.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nlpcloud
        if self.nlpcloud:
            _dict['nlpcloud'] = self.nlpcloud.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oneai
        if self.oneai:
            _dict['oneai'] = self.oneai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ai21labs
        if self.ai21labs:
            _dict['ai21labs'] = self.ai21labs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of alephalpha
        if self.alephalpha:
            _dict['alephalpha'] = self.alephalpha.to_dict()
        # override the default output from pydantic by calling `to_dict()` of openai
        if self.openai:
            _dict['openai'] = self.openai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of meaningcloud
        if self.meaningcloud:
            _dict['meaningcloud'] = self.meaningcloud.to_dict()
        # override the default output from pydantic by calling `to_dict()` of huggingface
        if self.huggingface:
            _dict['huggingface'] = self.huggingface.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anthropic
        if self.anthropic:
            _dict['anthropic'] = self.anthropic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of connexun
        if self.connexun:
            _dict['connexun'] = self.connexun.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TextsummarizeResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "writesonic": PydanticMainTextsummarizeSummarizeDataClass94559364428208.from_dict(obj["writesonic"]) if obj.get("writesonic") is not None else None,
            "microsoft": PydanticMainTextsummarizeSummarizeDataClass94559368039472.from_dict(obj["microsoft"]) if obj.get("microsoft") is not None else None,
            "emvista": PydanticMainTextsummarizeSummarizeDataClass94559368393536.from_dict(obj["emvista"]) if obj.get("emvista") is not None else None,
            "cohere": PydanticMainTextsummarizeSummarizeDataClass94559368273408.from_dict(obj["cohere"]) if obj.get("cohere") is not None else None,
            "nlpcloud": PydanticMainTextsummarizeSummarizeDataClass94559363917488.from_dict(obj["nlpcloud"]) if obj.get("nlpcloud") is not None else None,
            "oneai": PydanticMainTextsummarizeSummarizeDataClass94559364661856.from_dict(obj["oneai"]) if obj.get("oneai") is not None else None,
            "ai21labs": PydanticMainTextsummarizeSummarizeDataClass94559363614384.from_dict(obj["ai21labs"]) if obj.get("ai21labs") is not None else None,
            "alephalpha": PydanticMainTextsummarizeSummarizeDataClass94559363895952.from_dict(obj["alephalpha"]) if obj.get("alephalpha") is not None else None,
            "openai": PydanticMainTextsummarizeSummarizeDataClass94559368914848.from_dict(obj["openai"]) if obj.get("openai") is not None else None,
            "meaningcloud": PydanticMainTextsummarizeSummarizeDataClass94559367615696.from_dict(obj["meaningcloud"]) if obj.get("meaningcloud") is not None else None,
            "huggingface": PydanticMainTextsummarizeSummarizeDataClass94559364620768.from_dict(obj["huggingface"]) if obj.get("huggingface") is not None else None,
            "anthropic": PydanticMainTextsummarizeSummarizeDataClass94559364732896.from_dict(obj["anthropic"]) if obj.get("anthropic") is not None else None,
            "connexun": PydanticMainTextsummarizeSummarizeDataClass94559363928880.from_dict(obj["connexun"]) if obj.get("connexun") is not None else None
        })
        return _obj


