import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.x_merge_list_project_type_enum import XMergeListProjectTypeEnum

T = TypeVar("T", bound="XMergeList")


@_attrs_define
class XMergeList:
    """
    Attributes:
        project_name (str):
        project_type (XMergeListProjectTypeEnum): * `DOC_PARSER` - Doc Parser
            * `TEXT` - Text
        created (datetime.datetime):
        subfeature (str):
        project_id (str):
    """

    project_name: str
    project_type: XMergeListProjectTypeEnum
    created: datetime.datetime
    subfeature: str
    project_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_name = self.project_name

        project_type = self.project_type.value

        created = self.created.isoformat()

        subfeature = self.subfeature

        project_id = self.project_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_name": project_name,
                "project_type": project_type,
                "created": created,
                "subfeature": subfeature,
                "project_id": project_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_name = d.pop("project_name")

        project_type = XMergeListProjectTypeEnum(d.pop("project_type"))

        created = isoparse(d.pop("created"))

        subfeature = d.pop("subfeature")

        project_id = d.pop("project_id")

        x_merge_list = cls(
            project_name=project_name,
            project_type=project_type,
            created=created,
            subfeature=subfeature,
            project_id=project_id,
        )

        x_merge_list.additional_properties = d
        return x_merge_list

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
