from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.type_enum import TypeEnum

if TYPE_CHECKING:
    from ..models.asset_list import AssetList


T = TypeVar("T", bound="ResourceList")


@_attrs_define
class ResourceList:
    """
    Attributes:
        resource (str):
        data (str):
        type (TypeEnum): * `db` - Db
            * `bucket` - Bucket
            * `db_vector` - Db Vector
            * `ai` - Ai
        provider (str):
        assets (List['AssetList']):
    """

    resource: str
    data: str
    type: TypeEnum
    provider: str
    assets: List["AssetList"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource = self.resource

        data = self.data

        type = self.type.value

        provider = self.provider

        assets = []
        for assets_item_data in self.assets:
            assets_item = assets_item_data.to_dict()
            assets.append(assets_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
                "data": data,
                "type": type,
                "provider": provider,
                "assets": assets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.asset_list import AssetList

        d = src_dict.copy()
        resource = d.pop("resource")

        data = d.pop("data")

        type = TypeEnum(d.pop("type"))

        provider = d.pop("provider")

        assets = []
        _assets = d.pop("assets")
        for assets_item_data in _assets:
            assets_item = AssetList.from_dict(assets_item_data)

            assets.append(assets_item)

        resource_list = cls(
            resource=resource,
            data=data,
            type=type,
            provider=provider,
            assets=assets,
        )

        resource_list.additional_properties = d
        return resource_list

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
