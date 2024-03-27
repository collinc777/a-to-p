from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.textprompt_optimization_prompt_optimization_data_class import (
        TextpromptOptimizationPromptOptimizationDataClass,
    )


T = TypeVar("T", bound="TextpromptOptimizationResponseModel")


@_attrs_define
class TextpromptOptimizationResponseModel:
    """
    Attributes:
        openai (Union[Unset, TextpromptOptimizationPromptOptimizationDataClass]):
    """

    openai: Union[Unset, "TextpromptOptimizationPromptOptimizationDataClass"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        openai: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.openai, Unset):
            openai = self.openai.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if openai is not UNSET:
            field_dict["openai"] = openai

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.textprompt_optimization_prompt_optimization_data_class import (
            TextpromptOptimizationPromptOptimizationDataClass,
        )

        d = src_dict.copy()
        _openai = d.pop("openai", UNSET)
        openai: Union[Unset, TextpromptOptimizationPromptOptimizationDataClass]
        if isinstance(_openai, Unset):
            openai = UNSET
        else:
            openai = TextpromptOptimizationPromptOptimizationDataClass.from_dict(_openai)

        textprompt_optimization_response_model = cls(
            openai=openai,
        )

        textprompt_optimization_response_model.additional_properties = d
        return textprompt_optimization_response_model

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
