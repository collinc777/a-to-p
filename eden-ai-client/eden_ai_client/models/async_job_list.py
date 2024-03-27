import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.state_enum import StateEnum

T = TypeVar("T", bound="AsyncJobList")


@_attrs_define
class AsyncJobList:
    """
    Attributes:
        providers (str):
        nb (int):
        nb_ok (int):
        public_id (str):
        state (StateEnum): * `finished` - finished
            * `failed` - failed
            * `Timeout error` - Timeout error
            * `processing` - processing
        created_at (datetime.datetime):
    """

    providers: str
    nb: int
    nb_ok: int
    public_id: str
    state: StateEnum
    created_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        providers = self.providers

        nb = self.nb

        nb_ok = self.nb_ok

        public_id = self.public_id

        state = self.state.value

        created_at = self.created_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providers": providers,
                "nb": nb,
                "nb_ok": nb_ok,
                "public_id": public_id,
                "state": state,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        providers = d.pop("providers")

        nb = d.pop("nb")

        nb_ok = d.pop("nb_ok")

        public_id = d.pop("public_id")

        state = StateEnum(d.pop("state"))

        created_at = isoparse(d.pop("created_at"))

        async_job_list = cls(
            providers=providers,
            nb=nb,
            nb_ok=nb_ok,
            public_id=public_id,
            state=state,
            created_at=created_at,
        )

        async_job_list.additional_properties = d
        return async_job_list

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
