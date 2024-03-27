from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.type_enum import TypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patched_resource_update_request_data import PatchedResourceUpdateRequestData


T = TypeVar("T", bound="PatchedResourceUpdateRequest")


@_attrs_define
class PatchedResourceUpdateRequest:
    """
    Attributes:
        resource (Union[Unset, str]):
        data (Union[Unset, PatchedResourceUpdateRequestData]):
        type (Union[Unset, TypeEnum]): * `db` - Db
            * `bucket` - Bucket
            * `db_vector` - Db Vector
            * `ai` - Ai
        provider (Union[Unset, str]):
    """

    resource: Union[Unset, str] = UNSET
    data: Union[Unset, "PatchedResourceUpdateRequestData"] = UNSET
    type: Union[Unset, TypeEnum] = UNSET
    provider: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource = self.resource

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        provider = self.provider

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource is not UNSET:
            field_dict["resource"] = resource
        if data is not UNSET:
            field_dict["data"] = data
        if type is not UNSET:
            field_dict["type"] = type
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patched_resource_update_request_data import PatchedResourceUpdateRequestData

        d = src_dict.copy()
        resource = d.pop("resource", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PatchedResourceUpdateRequestData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PatchedResourceUpdateRequestData.from_dict(_data)

        _type = d.pop("type", UNSET)
        type: Union[Unset, TypeEnum]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TypeEnum(_type)

        provider = d.pop("provider", UNSET)

        patched_resource_update_request = cls(
            resource=resource,
            data=data,
            type=type,
            provider=provider,
        )

        patched_resource_update_request.additional_properties = d
        return patched_resource_update_request

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
