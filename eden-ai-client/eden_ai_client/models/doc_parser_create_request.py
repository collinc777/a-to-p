import json
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doc_parser_create_request_structure_providers_type_0 import (
        DocParserCreateRequestStructureProvidersType0,
    )


T = TypeVar("T", bound="DocParserCreateRequest")


@_attrs_define
class DocParserCreateRequest:
    """
    Attributes:
        project_name (str): The project name
        subfeature (str):
        structure_providers (Union['DocParserCreateRequestStructureProvidersType0', None, Unset]):
    """

    project_name: str
    subfeature: str
    structure_providers: Union["DocParserCreateRequestStructureProvidersType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.doc_parser_create_request_structure_providers_type_0 import (
            DocParserCreateRequestStructureProvidersType0,
        )

        project_name = self.project_name

        subfeature = self.subfeature

        structure_providers: Union[Dict[str, Any], None, Unset]
        if isinstance(self.structure_providers, Unset):
            structure_providers = UNSET
        elif isinstance(self.structure_providers, DocParserCreateRequestStructureProvidersType0):
            structure_providers = self.structure_providers.to_dict()
        else:
            structure_providers = self.structure_providers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_name": project_name,
                "subfeature": subfeature,
            }
        )
        if structure_providers is not UNSET:
            field_dict["structure_providers"] = structure_providers

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        project_name = (
            self.project_name
            if isinstance(self.project_name, Unset)
            else (None, str(self.project_name).encode(), "text/plain")
        )

        subfeature = (
            self.subfeature
            if isinstance(self.subfeature, Unset)
            else (None, str(self.subfeature).encode(), "text/plain")
        )

        structure_providers: Union[None, Tuple[None, bytes, str], Unset]
        if isinstance(self.structure_providers, Unset):
            structure_providers = UNSET
        elif isinstance(self.structure_providers, DocParserCreateRequestStructureProvidersType0):
            structure_providers = (None, json.dumps(self.structure_providers.to_dict()).encode(), "application/json")
        else:
            structure_providers = self.structure_providers

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "project_name": project_name,
                "subfeature": subfeature,
            }
        )
        if structure_providers is not UNSET:
            field_dict["structure_providers"] = structure_providers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.doc_parser_create_request_structure_providers_type_0 import (
            DocParserCreateRequestStructureProvidersType0,
        )

        d = src_dict.copy()
        project_name = d.pop("project_name")

        subfeature = d.pop("subfeature")

        def _parse_structure_providers(
            data: object,
        ) -> Union["DocParserCreateRequestStructureProvidersType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                structure_providers_type_0 = DocParserCreateRequestStructureProvidersType0.from_dict(data)

                return structure_providers_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DocParserCreateRequestStructureProvidersType0", None, Unset], data)

        structure_providers = _parse_structure_providers(d.pop("structure_providers", UNSET))

        doc_parser_create_request = cls(
            project_name=project_name,
            subfeature=subfeature,
            structure_providers=structure_providers,
        )

        doc_parser_create_request.additional_properties = d
        return doc_parser_create_request

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
