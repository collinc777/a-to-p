import json
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_request_content_item import WorkflowRequestContentItem


T = TypeVar("T", bound="WorkflowRequest")


@_attrs_define
class WorkflowRequest:
    """
    Attributes:
        content (List['WorkflowRequestContentItem']):
        name (Union[None, Unset, str]):
        output_node (Union[None, Unset, str]):
    """

    content: List["WorkflowRequestContentItem"]
    name: Union[None, Unset, str] = UNSET
    output_node: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = []
        for content_item_data in self.content:
            content_item = content_item_data.to_dict()
            content.append(content_item)

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
                "content": content,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if output_node is not UNSET:
            field_dict["output_node"] = output_node

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        _temp_content = []
        for content_item_data in self.content:
            content_item = content_item_data.to_dict()
            _temp_content.append(content_item)
        content = (None, json.dumps(_temp_content).encode(), "application/json")

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
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "content": content,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if output_node is not UNSET:
            field_dict["output_node"] = output_node

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workflow_request_content_item import WorkflowRequestContentItem

        d = src_dict.copy()
        content = []
        _content = d.pop("content")
        for content_item_data in _content:
            content_item = WorkflowRequestContentItem.from_dict(content_item_data)

            content.append(content_item)

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

        workflow_request = cls(
            content=content,
            name=name,
            output_node=output_node,
        )

        workflow_request.additional_properties = d
        return workflow_request

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
