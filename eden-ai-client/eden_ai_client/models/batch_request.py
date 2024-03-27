from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_request_requests_item import BatchRequestRequestsItem


T = TypeVar("T", bound="BatchRequest")


@_attrs_define
class BatchRequest:
    """
    Attributes:
        requests (List['BatchRequestRequestsItem']):
        webhook_receiver (Union[Unset, str]):
    """

    requests: List["BatchRequestRequestsItem"]
    webhook_receiver: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        requests = []
        for requests_item_data in self.requests:
            requests_item = requests_item_data.to_dict()
            requests.append(requests_item)

        webhook_receiver = self.webhook_receiver

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requests": requests,
            }
        )
        if webhook_receiver is not UNSET:
            field_dict["webhook_receiver"] = webhook_receiver

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.batch_request_requests_item import BatchRequestRequestsItem

        d = src_dict.copy()
        requests = []
        _requests = d.pop("requests")
        for requests_item_data in _requests:
            requests_item = BatchRequestRequestsItem.from_dict(requests_item_data)

            requests.append(requests_item)

        webhook_receiver = d.pop("webhook_receiver", UNSET)

        batch_request = cls(
            requests=requests,
            webhook_receiver=webhook_receiver,
        )

        batch_request.additional_properties = d
        return batch_request

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
