from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.type_enum import TypeEnum

if TYPE_CHECKING:
    from ..models.resource_create_request_data import ResourceCreateRequestData


T = TypeVar("T", bound="ResourceCreateRequest")


@_attrs_define
class ResourceCreateRequest:
    """
    Attributes:
        resource (str):
        data (ResourceCreateRequestData):
        type (TypeEnum): * `db` - Db
            * `bucket` - Bucket
            * `db_vector` - Db Vector
            * `ai` - Ai
        provider (str):
    """

    resource: str
    data: "ResourceCreateRequestData"
    type: TypeEnum
    provider: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource = self.resource

        data = self.data.to_dict()

        type = self.type.value

        provider = self.provider

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
                "data": data,
                "type": type,
                "provider": provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.resource_create_request_data import ResourceCreateRequestData

        d = src_dict.copy()
        resource = d.pop("resource")

        data = ResourceCreateRequestData.from_dict(d.pop("data"))

        type = TypeEnum(d.pop("type"))

        provider = d.pop("provider")

        resource_create_request = cls(
            resource=resource,
            data=data,
            type=type,
            provider=provider,
        )

        resource_create_request.additional_properties = d
        return resource_create_request

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
