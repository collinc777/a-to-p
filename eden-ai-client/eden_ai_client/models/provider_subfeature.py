from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature import Feature
    from ..models.pricing_serialzier import PricingSerialzier
    from ..models.provider import Provider
    from ..models.provider_subfeature_constraints import ProviderSubfeatureConstraints
    from ..models.provider_subfeature_languages_item import ProviderSubfeatureLanguagesItem
    from ..models.provider_subfeature_models import ProviderSubfeatureModels
    from ..models.subfeature import Subfeature


T = TypeVar("T", bound="ProviderSubfeature")


@_attrs_define
class ProviderSubfeature:
    """
    Attributes:
        name (str):
        version (str):
        pricings (List['PricingSerialzier']):
        provider (Provider):
        feature (Feature):
        subfeature (Subfeature):
        constraints (ProviderSubfeatureConstraints):
        models (ProviderSubfeatureModels):
        languages (List['ProviderSubfeatureLanguagesItem']):
        phase (str):
        is_working (Union[Unset, bool]):
        description_title (Union[None, Unset, str]):
        description_content (Union[None, Unset, str]):
    """

    name: str
    version: str
    pricings: List["PricingSerialzier"]
    provider: "Provider"
    feature: "Feature"
    subfeature: "Subfeature"
    constraints: "ProviderSubfeatureConstraints"
    models: "ProviderSubfeatureModels"
    languages: List["ProviderSubfeatureLanguagesItem"]
    phase: str
    is_working: Union[Unset, bool] = UNSET
    description_title: Union[None, Unset, str] = UNSET
    description_content: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        version = self.version

        pricings = []
        for pricings_item_data in self.pricings:
            pricings_item = pricings_item_data.to_dict()
            pricings.append(pricings_item)

        provider = self.provider.to_dict()

        feature = self.feature.to_dict()

        subfeature = self.subfeature.to_dict()

        constraints = self.constraints.to_dict()

        models = self.models.to_dict()

        languages = []
        for languages_item_data in self.languages:
            languages_item = languages_item_data.to_dict()
            languages.append(languages_item)

        phase = self.phase

        is_working = self.is_working

        description_title: Union[None, Unset, str]
        if isinstance(self.description_title, Unset):
            description_title = UNSET
        else:
            description_title = self.description_title

        description_content: Union[None, Unset, str]
        if isinstance(self.description_content, Unset):
            description_content = UNSET
        else:
            description_content = self.description_content

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "version": version,
                "pricings": pricings,
                "provider": provider,
                "feature": feature,
                "subfeature": subfeature,
                "constraints": constraints,
                "models": models,
                "languages": languages,
                "phase": phase,
            }
        )
        if is_working is not UNSET:
            field_dict["is_working"] = is_working
        if description_title is not UNSET:
            field_dict["description_title"] = description_title
        if description_content is not UNSET:
            field_dict["description_content"] = description_content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.feature import Feature
        from ..models.pricing_serialzier import PricingSerialzier
        from ..models.provider import Provider
        from ..models.provider_subfeature_constraints import ProviderSubfeatureConstraints
        from ..models.provider_subfeature_languages_item import ProviderSubfeatureLanguagesItem
        from ..models.provider_subfeature_models import ProviderSubfeatureModels
        from ..models.subfeature import Subfeature

        d = src_dict.copy()
        name = d.pop("name")

        version = d.pop("version")

        pricings = []
        _pricings = d.pop("pricings")
        for pricings_item_data in _pricings:
            pricings_item = PricingSerialzier.from_dict(pricings_item_data)

            pricings.append(pricings_item)

        provider = Provider.from_dict(d.pop("provider"))

        feature = Feature.from_dict(d.pop("feature"))

        subfeature = Subfeature.from_dict(d.pop("subfeature"))

        constraints = ProviderSubfeatureConstraints.from_dict(d.pop("constraints"))

        models = ProviderSubfeatureModels.from_dict(d.pop("models"))

        languages = []
        _languages = d.pop("languages")
        for languages_item_data in _languages:
            languages_item = ProviderSubfeatureLanguagesItem.from_dict(languages_item_data)

            languages.append(languages_item)

        phase = d.pop("phase")

        is_working = d.pop("is_working", UNSET)

        def _parse_description_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description_title = _parse_description_title(d.pop("description_title", UNSET))

        def _parse_description_content(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description_content = _parse_description_content(d.pop("description_content", UNSET))

        provider_subfeature = cls(
            name=name,
            version=version,
            pricings=pricings,
            provider=provider,
            feature=feature,
            subfeature=subfeature,
            constraints=constraints,
            models=models,
            languages=languages,
            phase=phase,
            is_working=is_working,
            description_title=description_title,
            description_content=description_content,
        )

        provider_subfeature.additional_properties = d
        return provider_subfeature

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
