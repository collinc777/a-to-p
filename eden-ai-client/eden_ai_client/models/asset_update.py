from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.asset_update_data import AssetUpdateData


T = TypeVar("T", bound="AssetUpdate")


@_attrs_define
class AssetUpdate:
    """
    Attributes:
        sub_resource (str):
        data (AssetUpdateData):
    """

    sub_resource: str
    data: "AssetUpdateData"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub_resource = self.sub_resource

        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sub_resource": sub_resource,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.asset_update_data import AssetUpdateData

        d = src_dict.copy()
        sub_resource = d.pop("sub_resource")

        data = AssetUpdateData.from_dict(d.pop("data"))

        asset_update = cls(
            sub_resource=sub_resource,
            data=data,
        )

        asset_update.additional_properties = d
        return asset_update

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
