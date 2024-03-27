import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ai_project_project_type_enum import AIProjectProjectTypeEnum

T = TypeVar("T", bound="AIProject")


@_attrs_define
class AIProject:
    """
    Attributes:
        project_id (str):
        project_name (str):
        project_type (AIProjectProjectTypeEnum): * `AskYoDa` - Askyoda
            * `Translathor` - Translathor
            * `X-Merge` - X Merge
        created_at (datetime.datetime):
        user (str):
    """

    project_id: str
    project_name: str
    project_type: AIProjectProjectTypeEnum
    created_at: datetime.datetime
    user: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id

        project_name = self.project_name

        project_type = self.project_type.value

        created_at = self.created_at.isoformat()

        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "project_name": project_name,
                "project_type": project_type,
                "created_at": created_at,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        project_type = AIProjectProjectTypeEnum(d.pop("project_type"))

        created_at = isoparse(d.pop("created_at"))

        user = d.pop("user")

        ai_project = cls(
            project_id=project_id,
            project_name=project_name,
            project_type=project_type,
            created_at=created_at,
            user=user,
        )

        ai_project.additional_properties = d
        return ai_project

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
