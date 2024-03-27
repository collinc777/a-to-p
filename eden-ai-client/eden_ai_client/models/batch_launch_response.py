from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.batch_launch_failed_request import BatchLaunchFailedRequest


T = TypeVar("T", bound="BatchLaunchResponse")


@_attrs_define
class BatchLaunchResponse:
    """
    Attributes:
        job_id (str): Job ID/name
        nb_launched (int): Number of successfully launched requests
        nb_failed (int): Number of failed_requests
        total (int): Total number of requests sent
        failed_requests (List['BatchLaunchFailedRequest']): if any requests failed, they will be shown in this list
    """

    job_id: str
    nb_launched: int
    nb_failed: int
    total: int
    failed_requests: List["BatchLaunchFailedRequest"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id

        nb_launched = self.nb_launched

        nb_failed = self.nb_failed

        total = self.total

        failed_requests = []
        for failed_requests_item_data in self.failed_requests:
            failed_requests_item = failed_requests_item_data.to_dict()
            failed_requests.append(failed_requests_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
                "nb_launched": nb_launched,
                "nb_failed": nb_failed,
                "total": total,
                "failed_requests": failed_requests,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.batch_launch_failed_request import BatchLaunchFailedRequest

        d = src_dict.copy()
        job_id = d.pop("job_id")

        nb_launched = d.pop("nb_launched")

        nb_failed = d.pop("nb_failed")

        total = d.pop("total")

        failed_requests = []
        _failed_requests = d.pop("failed_requests")
        for failed_requests_item_data in _failed_requests:
            failed_requests_item = BatchLaunchFailedRequest.from_dict(failed_requests_item_data)

            failed_requests.append(failed_requests_item)

        batch_launch_response = cls(
            job_id=job_id,
            nb_launched=nb_launched,
            nb_failed=nb_failed,
            total=total,
            failed_requests=failed_requests,
        )

        batch_launch_response.additional_properties = d
        return batch_launch_response

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
