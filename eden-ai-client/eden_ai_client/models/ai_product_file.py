import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.status_e80_enum import StatusE80Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="AiProductFile")


@_attrs_define
class AiProductFile:
    """
    Attributes:
        file_id (str):
        user (str):
        project (str):
        file_type (str):
        created_at (datetime.datetime):
        status (Union[None, StatusE80Enum, Unset]):
    """

    file_id: str
    user: str
    project: str
    file_type: str
    created_at: datetime.datetime
    status: Union[None, StatusE80Enum, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_id = self.file_id

        user = self.user

        project = self.project

        file_type = self.file_type

        created_at = self.created_at.isoformat()

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, StatusE80Enum):
            status = self.status.value
        else:
            status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_id": file_id,
                "user": user,
                "project": project,
                "file_type": file_type,
                "created_at": created_at,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_id = d.pop("file_id")

        user = d.pop("user")

        project = d.pop("project")

        file_type = d.pop("file_type")

        created_at = isoparse(d.pop("created_at"))

        def _parse_status(data: object) -> Union[None, StatusE80Enum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = StatusE80Enum(data)

                return status_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, StatusE80Enum, Unset], data)

        status = _parse_status(d.pop("status", UNSET))

        ai_product_file = cls(
            file_id=file_id,
            user=user,
            project=project,
            file_type=file_type,
            created_at=created_at,
            status=status,
        )

        ai_product_file.additional_properties = d
        return ai_product_file

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
