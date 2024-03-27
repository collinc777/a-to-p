from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAskYodaProjectUpdateRequest")


@_attrs_define
class PatchedAskYodaProjectUpdateRequest:
    """
    Attributes:
        ocr_provider (Union[Unset, str]):
        speech_to_text_provider (Union[Unset, str]):
        llm_provider (Union[Unset, str]): Select a default LLM provider to use in your project.
        llm_model (Union[Unset, str]): Select a default Model for LLM provider to use in your project
        chunk_size (Union[None, Unset, int]):
        chunk_separators (Union[List[str], None, Unset]):
    """

    ocr_provider: Union[Unset, str] = UNSET
    speech_to_text_provider: Union[Unset, str] = UNSET
    llm_provider: Union[Unset, str] = UNSET
    llm_model: Union[Unset, str] = UNSET
    chunk_size: Union[None, Unset, int] = UNSET
    chunk_separators: Union[List[str], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ocr_provider = self.ocr_provider

        speech_to_text_provider = self.speech_to_text_provider

        llm_provider = self.llm_provider

        llm_model = self.llm_model

        chunk_size: Union[None, Unset, int]
        if isinstance(self.chunk_size, Unset):
            chunk_size = UNSET
        else:
            chunk_size = self.chunk_size

        chunk_separators: Union[List[str], None, Unset]
        if isinstance(self.chunk_separators, Unset):
            chunk_separators = UNSET
        elif isinstance(self.chunk_separators, list):
            chunk_separators = self.chunk_separators

        else:
            chunk_separators = self.chunk_separators

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ocr_provider is not UNSET:
            field_dict["ocr_provider"] = ocr_provider
        if speech_to_text_provider is not UNSET:
            field_dict["speech_to_text_provider"] = speech_to_text_provider
        if llm_provider is not UNSET:
            field_dict["llm_provider"] = llm_provider
        if llm_model is not UNSET:
            field_dict["llm_model"] = llm_model
        if chunk_size is not UNSET:
            field_dict["chunk_size"] = chunk_size
        if chunk_separators is not UNSET:
            field_dict["chunk_separators"] = chunk_separators

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ocr_provider = d.pop("ocr_provider", UNSET)

        speech_to_text_provider = d.pop("speech_to_text_provider", UNSET)

        llm_provider = d.pop("llm_provider", UNSET)

        llm_model = d.pop("llm_model", UNSET)

        def _parse_chunk_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        chunk_size = _parse_chunk_size(d.pop("chunk_size", UNSET))

        def _parse_chunk_separators(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                chunk_separators_type_0 = cast(List[str], data)

                return chunk_separators_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        chunk_separators = _parse_chunk_separators(d.pop("chunk_separators", UNSET))

        patched_ask_yoda_project_update_request = cls(
            ocr_provider=ocr_provider,
            speech_to_text_provider=speech_to_text_provider,
            llm_provider=llm_provider,
            llm_model=llm_model,
            chunk_size=chunk_size,
            chunk_separators=chunk_separators,
        )

        patched_ask_yoda_project_update_request.additional_properties = d
        return patched_ask_yoda_project_update_request

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
