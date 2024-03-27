from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.imageembeddings_embeddings_data_class import ImageembeddingsEmbeddingsDataClass


T = TypeVar("T", bound="ImageembeddingsResponseModel")


@_attrs_define
class ImageembeddingsResponseModel:
    """
    Attributes:
        alephalpha (Union[Unset, ImageembeddingsEmbeddingsDataClass]):
    """

    alephalpha: Union[Unset, "ImageembeddingsEmbeddingsDataClass"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alephalpha: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alephalpha, Unset):
            alephalpha = self.alephalpha.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alephalpha is not UNSET:
            field_dict["alephalpha"] = alephalpha

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.imageembeddings_embeddings_data_class import ImageembeddingsEmbeddingsDataClass

        d = src_dict.copy()
        _alephalpha = d.pop("alephalpha", UNSET)
        alephalpha: Union[Unset, ImageembeddingsEmbeddingsDataClass]
        if isinstance(_alephalpha, Unset):
            alephalpha = UNSET
        else:
            alephalpha = ImageembeddingsEmbeddingsDataClass.from_dict(_alephalpha)

        imageembeddings_response_model = cls(
            alephalpha=alephalpha,
        )

        imageembeddings_response_model.additional_properties = d
        return imageembeddings_response_model

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
