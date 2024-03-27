import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedUniversalTranslatorCreatetRequest")


@_attrs_define
class PatchedUniversalTranslatorCreatetRequest:
    """
    Attributes:
        source_language (Union[None, Unset, str]): The language code from which the text will be translated
        target_language (Union[None, Unset, str]): The language code in which the text will be translated
        project_name (Union[Unset, str]): The project name
        fall_back_providers (Union[Unset, List[str]]):
        provider (Union[Unset, str]):
    """

    source_language: Union[None, Unset, str] = UNSET
    target_language: Union[None, Unset, str] = UNSET
    project_name: Union[Unset, str] = UNSET
    fall_back_providers: Union[Unset, List[str]] = UNSET
    provider: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_language: Union[None, Unset, str]
        if isinstance(self.source_language, Unset):
            source_language = UNSET
        else:
            source_language = self.source_language

        target_language: Union[None, Unset, str]
        if isinstance(self.target_language, Unset):
            target_language = UNSET
        else:
            target_language = self.target_language

        project_name = self.project_name

        fall_back_providers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.fall_back_providers, Unset):
            fall_back_providers = self.fall_back_providers

        provider = self.provider

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_language is not UNSET:
            field_dict["source_language"] = source_language
        if target_language is not UNSET:
            field_dict["target_language"] = target_language
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if fall_back_providers is not UNSET:
            field_dict["fall_back_providers"] = fall_back_providers
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        source_language: Union[None, Unset, str]
        if isinstance(self.source_language, Unset):
            source_language = UNSET
        else:
            source_language = self.source_language

        target_language: Union[None, Unset, str]
        if isinstance(self.target_language, Unset):
            target_language = UNSET
        else:
            target_language = self.target_language

        project_name = (
            self.project_name
            if isinstance(self.project_name, Unset)
            else (None, str(self.project_name).encode(), "text/plain")
        )

        fall_back_providers: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.fall_back_providers, Unset):
            _temp_fall_back_providers = self.fall_back_providers
            fall_back_providers = (None, json.dumps(_temp_fall_back_providers).encode(), "application/json")

        provider = (
            self.provider if isinstance(self.provider, Unset) else (None, str(self.provider).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if source_language is not UNSET:
            field_dict["source_language"] = source_language
        if target_language is not UNSET:
            field_dict["target_language"] = target_language
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if fall_back_providers is not UNSET:
            field_dict["fall_back_providers"] = fall_back_providers
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_source_language(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_language = _parse_source_language(d.pop("source_language", UNSET))

        def _parse_target_language(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        target_language = _parse_target_language(d.pop("target_language", UNSET))

        project_name = d.pop("project_name", UNSET)

        fall_back_providers = cast(List[str], d.pop("fall_back_providers", UNSET))

        provider = d.pop("provider", UNSET)

        patched_universal_translator_createt_request = cls(
            source_language=source_language,
            target_language=target_language,
            project_name=project_name,
            fall_back_providers=fall_back_providers,
            provider=provider,
        )

        patched_universal_translator_createt_request.additional_properties = d
        return patched_universal_translator_createt_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
