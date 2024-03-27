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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.db_provider_enum import DbProviderEnum
from typing import Set
from typing_extensions import Self


class AskYourDataProjectRequest(BaseModel):
    """
    AskYourDataProjectRequest
    """  # noqa: E501

    credential: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(
        default=None, description="The credential resource name"
    )
    asset: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(
        default=None, description="The asset sub_resource name"
    )
    ocr_provider: Annotated[str, Field(min_length=1, strict=True)]
    speech_to_text_provider: Annotated[str, Field(min_length=1, strict=True)]
    llm_provider: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="Select a default LLM provider to use in your project.",
    )
    llm_model: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="Select a default Model for LLM provider to use in your project",
    )
    chunk_size: Optional[Annotated[int, Field(le=10000, strict=True, ge=1)]] = None
    chunk_separators: Optional[List[StrictStr]] = None
    project_name: Annotated[str, Field(min_length=1, strict=True)] = Field(
        description="Project name"
    )
    collection_name: Annotated[str, Field(min_length=1, strict=True)] = Field(
        description="Database Collection Name"
    )
    db_provider: Optional[DbProviderEnum] = Field(
        default=None,
        description="Database Provider  * `qdrant` - qdrant * `supabase` - supabase",
    )
    embeddings_provider: Optional[Annotated[str, Field(min_length=1, strict=True)]] = (
        Field(
            default="cohere",
            description="Select an embedding provider to use in your search database. Leave empty for default.",
        )
    )
    __properties: ClassVar[List[str]] = [
        "credential",
        "asset",
        "ocr_provider",
        "speech_to_text_provider",
        "llm_provider",
        "llm_model",
        "chunk_size",
        "chunk_separators",
        "project_name",
        "collection_name",
        "db_provider",
        "embeddings_provider",
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
        """Create an instance of AskYourDataProjectRequest from a JSON string"""
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
        # set to None if credential (nullable) is None
        # and model_fields_set contains the field
        if self.credential is None and "credential" in self.model_fields_set:
            _dict["credential"] = None

        # set to None if asset (nullable) is None
        # and model_fields_set contains the field
        if self.asset is None and "asset" in self.model_fields_set:
            _dict["asset"] = None

        # set to None if chunk_size (nullable) is None
        # and model_fields_set contains the field
        if self.chunk_size is None and "chunk_size" in self.model_fields_set:
            _dict["chunk_size"] = None

        # set to None if chunk_separators (nullable) is None
        # and model_fields_set contains the field
        if (
            self.chunk_separators is None
            and "chunk_separators" in self.model_fields_set
        ):
            _dict["chunk_separators"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AskYourDataProjectRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "credential": obj.get("credential"),
                "asset": obj.get("asset"),
                "ocr_provider": obj.get("ocr_provider"),
                "speech_to_text_provider": obj.get("speech_to_text_provider"),
                "llm_provider": obj.get("llm_provider"),
                "llm_model": obj.get("llm_model"),
                "chunk_size": obj.get("chunk_size"),
                "chunk_separators": obj.get("chunk_separators"),
                "project_name": obj.get("project_name"),
                "collection_name": obj.get("collection_name"),
                "db_provider": obj.get("db_provider"),
                "embeddings_provider": obj.get("embeddings_provider")
                if obj.get("embeddings_provider") is not None
                else "cohere",
            }
        )
        return _obj
