from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patched_asset_update_request_data import PatchedAssetUpdateRequestData


T = TypeVar("T", bound="PatchedAssetUpdateRequest")


@_attrs_define
class PatchedAssetUpdateRequest:
    """
    Attributes:
        sub_resource (Union[Unset, str]):
        data (Union[Unset, PatchedAssetUpdateRequestData]):
    """

    sub_resource: Union[Unset, str] = UNSET
    data: Union[Unset, "PatchedAssetUpdateRequestData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub_resource = self.sub_resource

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sub_resource is not UNSET:
            field_dict["sub_resource"] = sub_resource
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patched_asset_update_request_data import PatchedAssetUpdateRequestData

        d = src_dict.copy()
        sub_resource = d.pop("sub_resource", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PatchedAssetUpdateRequestData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PatchedAssetUpdateRequestData.from_dict(_data)

        patched_asset_update_request = cls(
            sub_resource=sub_resource,
            data=data,
        )

        patched_asset_update_request.additional_properties = d
        return patched_asset_update_request

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
