from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_f43_enum import StatusF43Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImagebackgroundRemovalBackgroundRemovalDataClass")


@_attrs_define
class ImagebackgroundRemovalBackgroundRemovalDataClass:
    """
    Attributes:
        image_b64 (str): The image in base64 format.
        image_resource_url (str): The image url.
        status (StatusF43Enum):
        original_response (Union[Unset, Any]): original response sent by the provider, hidden by default, show it by
            passing the `show_original_response` field to `true` in your request
    """

    image_b64: str
    image_resource_url: str
    status: StatusF43Enum
    original_response: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image_b64 = self.image_b64

        image_resource_url = self.image_resource_url

        status = self.status.value

        original_response = self.original_response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image_b64": image_b64,
                "image_resource_url": image_resource_url,
                "status": status,
            }
        )
        if original_response is not UNSET:
            field_dict["original_response"] = original_response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        image_b64 = d.pop("image_b64")

        image_resource_url = d.pop("image_resource_url")

        status = StatusF43Enum(d.pop("status"))

        original_response = d.pop("original_response", UNSET)

        imagebackground_removal_background_removal_data_class = cls(
            image_b64=image_b64,
            image_resource_url=image_resource_url,
            status=status,
            original_response=original_response,
        )

        imagebackground_removal_background_removal_data_class.additional_properties = d
        return imagebackground_removal_background_removal_data_class

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