import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_content_item import WorkflowContentItem


T = TypeVar("T", bound="Workflow")


@_attrs_define
class Workflow:
    """
    Attributes:
        id (str):
        content (List['WorkflowContentItem']):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (Union[None, Unset, str]):
        output_node (Union[None, Unset, str]):
    """

    id: str
    content: List["WorkflowContentItem"]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: Union[None, Unset, str] = UNSET
    output_node: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        content = []
        for content_item_data in self.content:
            content_item = content_item_data.to_dict()
            content.append(content_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        output_node: Union[None, Unset, str]
        if isinstance(self.output_node, Unset):
            output_node = UNSET
        else:
            output_node = self.output_node

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "content": content,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if output_node is not UNSET:
            field_dict["output_node"] = output_node

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workflow_content_item import WorkflowContentItem

        d = src_dict.copy()
        id = d.pop("id")

        content = []
        _content = d.pop("content")
        for content_item_data in _content:
            content_item = WorkflowContentItem.from_dict(content_item_data)

            content.append(content_item)

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_output_node(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        output_node = _parse_output_node(d.pop("output_node", UNSET))

        workflow = cls(
            id=id,
            content=content,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            output_node=output_node,
        )

        workflow.additional_properties = d
        return workflow

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
