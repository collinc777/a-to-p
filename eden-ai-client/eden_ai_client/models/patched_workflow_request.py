import json
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patched_workflow_request_content_item import PatchedWorkflowRequestContentItem


T = TypeVar("T", bound="PatchedWorkflowRequest")


@_attrs_define
class PatchedWorkflowRequest:
    """
    Attributes:
        name (Union[None, Unset, str]):
        content (Union[Unset, List['PatchedWorkflowRequestContentItem']]):
        output_node (Union[None, Unset, str]):
    """

    name: Union[None, Unset, str] = UNSET
    content: Union[Unset, List["PatchedWorkflowRequestContentItem"]] = UNSET
    output_node: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        content: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()
                content.append(content_item)

        output_node: Union[None, Unset, str]
        if isinstance(self.output_node, Unset):
            output_node = UNSET
        else:
            output_node = self.output_node

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if content is not UNSET:
            field_dict["content"] = content
        if output_node is not UNSET:
            field_dict["output_node"] = output_node

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        content: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.content, Unset):
            _temp_content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()
                _temp_content.append(content_item)
            content = (None, json.dumps(_temp_content).encode(), "application/json")

        output_node: Union[None, Unset, str]
        if isinstance(self.output_node, Unset):
            output_node = UNSET
        else:
            output_node = self.output_node

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if content is not UNSET:
            field_dict["content"] = content
        if output_node is not UNSET:
            field_dict["output_node"] = output_node

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patched_workflow_request_content_item import PatchedWorkflowRequestContentItem

        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        content = []
        _content = d.pop("content", UNSET)
        for content_item_data in _content or []:
            content_item = PatchedWorkflowRequestContentItem.from_dict(content_item_data)

            content.append(content_item)

        def _parse_output_node(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        output_node = _parse_output_node(d.pop("output_node", UNSET))

        patched_workflow_request = cls(
            name=name,
            content=content,
            output_node=output_node,
        )

        patched_workflow_request.additional_properties = d
        return patched_workflow_request

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
