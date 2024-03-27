from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doc_parser_create_structure_providers_type_0 import DocParserCreateStructureProvidersType0


T = TypeVar("T", bound="DocParserCreate")


@_attrs_define
class DocParserCreate:
    """
    Attributes:
        project_name (str): The project name
        subfeature (str):
        structure_providers (Union['DocParserCreateStructureProvidersType0', None, Unset]):
    """

    project_name: str
    subfeature: str
    structure_providers: Union["DocParserCreateStructureProvidersType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.doc_parser_create_structure_providers_type_0 import DocParserCreateStructureProvidersType0

        project_name = self.project_name

        subfeature = self.subfeature

        structure_providers: Union[Dict[str, Any], None, Unset]
        if isinstance(self.structure_providers, Unset):
            structure_providers = UNSET
        elif isinstance(self.structure_providers, DocParserCreateStructureProvidersType0):
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

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.doc_parser_create_structure_providers_type_0 import DocParserCreateStructureProvidersType0

        d = src_dict.copy()
        project_name = d.pop("project_name")

        subfeature = d.pop("subfeature")

        def _parse_structure_providers(data: object) -> Union["DocParserCreateStructureProvidersType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                structure_providers_type_0 = DocParserCreateStructureProvidersType0.from_dict(data)

                return structure_providers_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DocParserCreateStructureProvidersType0", None, Unset], data)

        structure_providers = _parse_structure_providers(d.pop("structure_providers", UNSET))

        doc_parser_create = cls(
            project_name=project_name,
            subfeature=subfeature,
            structure_providers=structure_providers,
        )

        doc_parser_create.additional_properties = d
        return doc_parser_create

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