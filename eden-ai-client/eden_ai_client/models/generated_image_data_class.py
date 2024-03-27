from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GeneratedImageDataClass")


@_attrs_define
class GeneratedImageDataClass:
    """
    Attributes:
        image (str):
        image_resource_url (str):
    """

    image: str
    image_resource_url: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image = self.image

        image_resource_url = self.image_resource_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
                "image_resource_url": image_resource_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        image = d.pop("image")

        image_resource_url = d.pop("image_resource_url")

        generated_image_data_class = cls(
            image=image,
            image_resource_url=image_resource_url,
        )

        generated_image_data_class.additional_properties = d
        return generated_image_data_class

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
