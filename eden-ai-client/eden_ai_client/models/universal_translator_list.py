from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UniversalTranslatorList")


@_attrs_define
class UniversalTranslatorList:
    """
    Attributes:
        source_language (Union[None, str]): The language code from which the text will be translated
        target_language (Union[None, str]): The language code in which the text will be translated
        project_name (str): The project name
        fall_back_providers (Union[None, str]): Providers to use in case of an error
        provider (str):
        project_id (str):
    """

    source_language: Union[None, str]
    target_language: Union[None, str]
    project_name: str
    fall_back_providers: Union[None, str]
    provider: str
    project_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_language: Union[None, str]
        source_language = self.source_language

        target_language: Union[None, str]
        target_language = self.target_language

        project_name = self.project_name

        fall_back_providers: Union[None, str]
        fall_back_providers = self.fall_back_providers

        provider = self.provider

        project_id = self.project_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_language": source_language,
                "target_language": target_language,
                "project_name": project_name,
                "fall_back_providers": fall_back_providers,
                "provider": provider,
                "project_id": project_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_source_language(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        source_language = _parse_source_language(d.pop("source_language"))

        def _parse_target_language(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        target_language = _parse_target_language(d.pop("target_language"))

        project_name = d.pop("project_name")

        def _parse_fall_back_providers(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        fall_back_providers = _parse_fall_back_providers(d.pop("fall_back_providers"))

        provider = d.pop("provider")

        project_id = d.pop("project_id")

        universal_translator_list = cls(
            source_language=source_language,
            target_language=target_language,
            project_name=project_name,
            fall_back_providers=fall_back_providers,
            provider=provider,
            project_id=project_id,
        )

        universal_translator_list.additional_properties = d
        return universal_translator_list

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
