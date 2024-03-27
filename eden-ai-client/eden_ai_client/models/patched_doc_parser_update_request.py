import json
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patched_doc_parser_update_request_structure_providers_type_0 import (
        PatchedDocParserUpdateRequestStructureProvidersType0,
    )


T = TypeVar("T", bound="PatchedDocParserUpdateRequest")


@_attrs_define
class PatchedDocParserUpdateRequest:
    """
    Attributes:
        structure_providers (Union['PatchedDocParserUpdateRequestStructureProvidersType0', None, Unset]):
    """

    structure_providers: Union["PatchedDocParserUpdateRequestStructureProvidersType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.patched_doc_parser_update_request_structure_providers_type_0 import (
            PatchedDocParserUpdateRequestStructureProvidersType0,
        )

        structure_providers: Union[Dict[str, Any], None, Unset]
        if isinstance(self.structure_providers, Unset):
            structure_providers = UNSET
        elif isinstance(self.structure_providers, PatchedDocParserUpdateRequestStructureProvidersType0):
            structure_providers = self.structure_providers.to_dict()
        else:
            structure_providers = self.structure_providers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if structure_providers is not UNSET:
            field_dict["structure_providers"] = structure_providers

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        structure_providers: Union[None, Tuple[None, bytes, str], Unset]
        if isinstance(self.structure_providers, Unset):
            structure_providers = UNSET
        elif isinstance(self.structure_providers, PatchedDocParserUpdateRequestStructureProvidersType0):
            structure_providers = (None, json.dumps(self.structure_providers.to_dict()).encode(), "application/json")
        else:
            structure_providers = self.structure_providers

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if structure_providers is not UNSET:
            field_dict["structure_providers"] = structure_providers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patched_doc_parser_update_request_structure_providers_type_0 import (
            PatchedDocParserUpdateRequestStructureProvidersType0,
        )

        d = src_dict.copy()

        def _parse_structure_providers(
            data: object,
        ) -> Union["PatchedDocParserUpdateRequestStructureProvidersType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                structure_providers_type_0 = PatchedDocParserUpdateRequestStructureProvidersType0.from_dict(data)

                return structure_providers_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PatchedDocParserUpdateRequestStructureProvidersType0", None, Unset], data)

        structure_providers = _parse_structure_providers(d.pop("structure_providers", UNSET))

        patched_doc_parser_update_request = cls(
            structure_providers=structure_providers,
        )

        patched_doc_parser_update_request.additional_properties = d
        return patched_doc_parser_update_request

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
