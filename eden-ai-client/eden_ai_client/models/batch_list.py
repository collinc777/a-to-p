from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_e80_enum import StatusE80Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchList")


@_attrs_define
class BatchList:
    """
    Attributes:
        feature (str):
        subfeature (str):
        total_requests (int):
        nb_processing (int):
        nb_succeeded (int):
        nb_failed (int):
        get_response_url (str):
        name (Union[Unset, str]):
        status (Union[Unset, StatusE80Enum]): * `succeeded` - Status Succeeded
            * `failed` - Status Failed
            * `finished` - Status Finished
            * `processing` - Status Processing
    """

    feature: str
    subfeature: str
    total_requests: int
    nb_processing: int
    nb_succeeded: int
    nb_failed: int
    get_response_url: str
    name: Union[Unset, str] = UNSET
    status: Union[Unset, StatusE80Enum] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        feature = self.feature

        subfeature = self.subfeature

        total_requests = self.total_requests

        nb_processing = self.nb_processing

        nb_succeeded = self.nb_succeeded

        nb_failed = self.nb_failed

        get_response_url = self.get_response_url

        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feature": feature,
                "subfeature": subfeature,
                "total_requests": total_requests,
                "nb_processing": nb_processing,
                "nb_succeeded": nb_succeeded,
                "nb_failed": nb_failed,
                "get_response_url": get_response_url,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        feature = d.pop("feature")

        subfeature = d.pop("subfeature")

        total_requests = d.pop("total_requests")

        nb_processing = d.pop("nb_processing")

        nb_succeeded = d.pop("nb_succeeded")

        nb_failed = d.pop("nb_failed")

        get_response_url = d.pop("get_response_url")

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, StatusE80Enum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusE80Enum(_status)

        batch_list = cls(
            feature=feature,
            subfeature=subfeature,
            total_requests=total_requests,
            nb_processing=nb_processing,
            nb_succeeded=nb_succeeded,
            nb_failed=nb_failed,
            get_response_url=get_response_url,
            name=name,
            status=status,
        )

        batch_list.additional_properties = d
        return batch_list

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
