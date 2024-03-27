from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResumePersonalName")


@_attrs_define
class ResumePersonalName:
    """
    Attributes:
        first_name (str):
        last_name (str):
        raw_name (str):
        middle (str):
        title (str):
        prefix (str):
        sufix (str):
    """

    first_name: str
    last_name: str
    raw_name: str
    middle: str
    title: str
    prefix: str
    sufix: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        raw_name = self.raw_name

        middle = self.middle

        title = self.title

        prefix = self.prefix

        sufix = self.sufix

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "first_name": first_name,
                "last_name": last_name,
                "raw_name": raw_name,
                "middle": middle,
                "title": title,
                "prefix": prefix,
                "sufix": sufix,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        raw_name = d.pop("raw_name")

        middle = d.pop("middle")

        title = d.pop("title")

        prefix = d.pop("prefix")

        sufix = d.pop("sufix")

        resume_personal_name = cls(
            first_name=first_name,
            last_name=last_name,
            raw_name=raw_name,
            middle=middle,
            title=title,
            prefix=prefix,
            sufix=sufix,
        )

        resume_personal_name.additional_properties = d
        return resume_personal_name

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
