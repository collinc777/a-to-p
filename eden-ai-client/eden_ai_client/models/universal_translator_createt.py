from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UniversalTranslatorCreatet")


@_attrs_define
class UniversalTranslatorCreatet:
    """
    Attributes:
        project_name (str): The project name
        provider (str):
        source_language (Union[None, Unset, str]): The language code from which the text will be translated
        target_language (Union[None, Unset, str]): The language code in which the text will be translated
        fall_back_providers (Union[Unset, List[str]]):
    """

    project_name: str
    provider: str
    source_language: Union[None, Unset, str] = UNSET
    target_language: Union[None, Unset, str] = UNSET
    fall_back_providers: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_name = self.project_name

        provider = self.provider

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

        fall_back_providers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.fall_back_providers, Unset):
            fall_back_providers = self.fall_back_providers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_name": project_name,
                "provider": provider,
            }
        )
        if source_language is not UNSET:
            field_dict["source_language"] = source_language
        if target_language is not UNSET:
            field_dict["target_language"] = target_language
        if fall_back_providers is not UNSET:
            field_dict["fall_back_providers"] = fall_back_providers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_name = d.pop("project_name")

        provider = d.pop("provider")

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

        fall_back_providers = cast(List[str], d.pop("fall_back_providers", UNSET))

        universal_translator_createt = cls(
            project_name=project_name,
            provider=provider,
            source_language=source_language,
            target_language=target_language,
            fall_back_providers=fall_back_providers,
        )

        universal_translator_createt.additional_properties = d
        return universal_translator_createt

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
