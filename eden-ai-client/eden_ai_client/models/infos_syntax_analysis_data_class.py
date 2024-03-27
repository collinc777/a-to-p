from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.infos_syntax_analysis_data_class_others import InfosSyntaxAnalysisDataClassOthers


T = TypeVar("T", bound="InfosSyntaxAnalysisDataClass")


@_attrs_define
class InfosSyntaxAnalysisDataClass:
    """
    Attributes:
        word (str):
        importance (int):
        tag (str):
        lemma (str):
        others (Union[Unset, InfosSyntaxAnalysisDataClassOthers]):
    """

    word: str
    importance: int
    tag: str
    lemma: str
    others: Union[Unset, "InfosSyntaxAnalysisDataClassOthers"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        word = self.word

        importance = self.importance

        tag = self.tag

        lemma = self.lemma

        others: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.others, Unset):
            others = self.others.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "word": word,
                "importance": importance,
                "tag": tag,
                "lemma": lemma,
            }
        )
        if others is not UNSET:
            field_dict["others"] = others

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.infos_syntax_analysis_data_class_others import InfosSyntaxAnalysisDataClassOthers

        d = src_dict.copy()
        word = d.pop("word")

        importance = d.pop("importance")

        tag = d.pop("tag")

        lemma = d.pop("lemma")

        _others = d.pop("others", UNSET)
        others: Union[Unset, InfosSyntaxAnalysisDataClassOthers]
        if isinstance(_others, Unset):
            others = UNSET
        else:
            others = InfosSyntaxAnalysisDataClassOthers.from_dict(_others)

        infos_syntax_analysis_data_class = cls(
            word=word,
            importance=importance,
            tag=tag,
            lemma=lemma,
            others=others,
        )

        infos_syntax_analysis_data_class.additional_properties = d
        return infos_syntax_analysis_data_class

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
