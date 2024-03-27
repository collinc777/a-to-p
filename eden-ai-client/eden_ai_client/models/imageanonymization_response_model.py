from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.imageanonymization_anonymization_data_class import ImageanonymizationAnonymizationDataClass


T = TypeVar("T", bound="ImageanonymizationResponseModel")


@_attrs_define
class ImageanonymizationResponseModel:
    """
    Attributes:
        api4ai (Union[Unset, ImageanonymizationAnonymizationDataClass]):
    """

    api4ai: Union[Unset, "ImageanonymizationAnonymizationDataClass"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api4ai: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.api4ai, Unset):
            api4ai = self.api4ai.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api4ai is not UNSET:
            field_dict["api4ai"] = api4ai

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.imageanonymization_anonymization_data_class import ImageanonymizationAnonymizationDataClass

        d = src_dict.copy()
        _api4ai = d.pop("api4ai", UNSET)
        api4ai: Union[Unset, ImageanonymizationAnonymizationDataClass]
        if isinstance(_api4ai, Unset):
            api4ai = UNSET
        else:
            api4ai = ImageanonymizationAnonymizationDataClass.from_dict(_api4ai)

        imageanonymization_response_model = cls(
            api4ai=api4ai,
        )

        imageanonymization_response_model.additional_properties = d
        return imageanonymization_response_model

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
