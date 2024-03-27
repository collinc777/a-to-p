from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.imageautoml_classification_automl_classification_create_project_data_class import (
        ImageautomlClassificationAutomlClassificationCreateProjectDataClass,
    )


T = TypeVar("T", bound="ImageautomlClassificationResponseModel")


@_attrs_define
class ImageautomlClassificationResponseModel:
    """
    Attributes:
        nyckel (Union[Unset, ImageautomlClassificationAutomlClassificationCreateProjectDataClass]):
    """

    nyckel: Union[Unset, "ImageautomlClassificationAutomlClassificationCreateProjectDataClass"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nyckel: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.nyckel, Unset):
            nyckel = self.nyckel.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nyckel is not UNSET:
            field_dict["nyckel"] = nyckel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.imageautoml_classification_automl_classification_create_project_data_class import (
            ImageautomlClassificationAutomlClassificationCreateProjectDataClass,
        )

        d = src_dict.copy()
        _nyckel = d.pop("nyckel", UNSET)
        nyckel: Union[Unset, ImageautomlClassificationAutomlClassificationCreateProjectDataClass]
        if isinstance(_nyckel, Unset):
            nyckel = UNSET
        else:
            nyckel = ImageautomlClassificationAutomlClassificationCreateProjectDataClass.from_dict(_nyckel)

        imageautoml_classification_response_model = cls(
            nyckel=nyckel,
        )

        imageautoml_classification_response_model.additional_properties = d
        return imageautoml_classification_response_model

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
