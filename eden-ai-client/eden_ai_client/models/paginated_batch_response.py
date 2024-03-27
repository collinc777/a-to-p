import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.status_e80_enum import StatusE80Enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_response_request import BatchResponseRequest


T = TypeVar("T", bound="PaginatedBatchResponse")


@_attrs_define
class PaginatedBatchResponse:
    """
    Attributes:
        total (int): Total requests made
        current_page (int): Current page number
        last_page (int):
        per_page (int): Number of requests per page
        from_ (int):
        to (int):
        requests (List['BatchResponseRequest']):
        created (datetime.datetime):
        updated (datetime.datetime):
        prev_page_url (Union[Unset, str]):
        next_page_url (Union[Unset, str]):
        status (Union[Unset, StatusE80Enum]): * `succeeded` - Status Succeeded
            * `failed` - Status Failed
            * `finished` - Status Finished
            * `processing` - Status Processing
    """

    total: int
    current_page: int
    last_page: int
    per_page: int
    from_: int
    to: int
    requests: List["BatchResponseRequest"]
    created: datetime.datetime
    updated: datetime.datetime
    prev_page_url: Union[Unset, str] = UNSET
    next_page_url: Union[Unset, str] = UNSET
    status: Union[Unset, StatusE80Enum] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total

        current_page = self.current_page

        last_page = self.last_page

        per_page = self.per_page

        from_ = self.from_

        to = self.to

        requests = []
        for requests_item_data in self.requests:
            requests_item = requests_item_data.to_dict()
            requests.append(requests_item)

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        prev_page_url = self.prev_page_url

        next_page_url = self.next_page_url

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "current_page": current_page,
                "last_page": last_page,
                "per_page": per_page,
                "From": from_,
                "to": to,
                "requests": requests,
                "created": created,
                "updated": updated,
            }
        )
        if prev_page_url is not UNSET:
            field_dict["prev_page_url"] = prev_page_url
        if next_page_url is not UNSET:
            field_dict["next_page_url"] = next_page_url
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.batch_response_request import BatchResponseRequest

        d = src_dict.copy()
        total = d.pop("total")

        current_page = d.pop("current_page")

        last_page = d.pop("last_page")

        per_page = d.pop("per_page")

        from_ = d.pop("From")

        to = d.pop("to")

        requests = []
        _requests = d.pop("requests")
        for requests_item_data in _requests:
            requests_item = BatchResponseRequest.from_dict(requests_item_data)

            requests.append(requests_item)

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        prev_page_url = d.pop("prev_page_url", UNSET)

        next_page_url = d.pop("next_page_url", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, StatusE80Enum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusE80Enum(_status)

        paginated_batch_response = cls(
            total=total,
            current_page=current_page,
            last_page=last_page,
            per_page=per_page,
            from_=from_,
            to=to,
            requests=requests,
            created=created,
            updated=updated,
            prev_page_url=prev_page_url,
            next_page_url=next_page_url,
            status=status,
        )

        paginated_batch_response.additional_properties = d
        return paginated_batch_response

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
