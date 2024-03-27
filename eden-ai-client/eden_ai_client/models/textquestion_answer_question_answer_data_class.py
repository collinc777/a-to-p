from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_f43_enum import StatusF43Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="TextquestionAnswerQuestionAnswerDataClass")


@_attrs_define
class TextquestionAnswerQuestionAnswerDataClass:
    """
    Attributes:
        status (StatusF43Enum):
        answers (Union[Unset, List[str]]):
        original_response (Union[Unset, Any]): original response sent by the provider, hidden by default, show it by
            passing the `show_original_response` field to `true` in your request
    """

    status: StatusF43Enum
    answers: Union[Unset, List[str]] = UNSET
    original_response: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        answers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.answers, Unset):
            answers = self.answers

        original_response = self.original_response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if answers is not UNSET:
            field_dict["answers"] = answers
        if original_response is not UNSET:
            field_dict["original_response"] = original_response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = StatusF43Enum(d.pop("status"))

        answers = cast(List[str], d.pop("answers", UNSET))

        original_response = d.pop("original_response", UNSET)

        textquestion_answer_question_answer_data_class = cls(
            status=status,
            answers=answers,
            original_response=original_response,
        )

        textquestion_answer_question_answer_data_class.additional_properties = d
        return textquestion_answer_question_answer_data_class

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
