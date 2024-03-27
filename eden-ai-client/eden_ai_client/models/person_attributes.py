from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lower_cloth import LowerCloth
    from ..models.upper_cloth import UpperCloth


T = TypeVar("T", bound="PersonAttributes")


@_attrs_define
class PersonAttributes:
    """
    Attributes:
        upper_cloths (Union[Unset, List['UpperCloth']]):
        lower_cloths (Union[Unset, List['LowerCloth']]):
    """

    upper_cloths: Union[Unset, List["UpperCloth"]] = UNSET
    lower_cloths: Union[Unset, List["LowerCloth"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        upper_cloths: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.upper_cloths, Unset):
            upper_cloths = []
            for upper_cloths_item_data in self.upper_cloths:
                upper_cloths_item = upper_cloths_item_data.to_dict()
                upper_cloths.append(upper_cloths_item)

        lower_cloths: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lower_cloths, Unset):
            lower_cloths = []
            for lower_cloths_item_data in self.lower_cloths:
                lower_cloths_item = lower_cloths_item_data.to_dict()
                lower_cloths.append(lower_cloths_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upper_cloths is not UNSET:
            field_dict["upper_cloths"] = upper_cloths
        if lower_cloths is not UNSET:
            field_dict["lower_cloths"] = lower_cloths

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.lower_cloth import LowerCloth
        from ..models.upper_cloth import UpperCloth

        d = src_dict.copy()
        upper_cloths = []
        _upper_cloths = d.pop("upper_cloths", UNSET)
        for upper_cloths_item_data in _upper_cloths or []:
            upper_cloths_item = UpperCloth.from_dict(upper_cloths_item_data)

            upper_cloths.append(upper_cloths_item)

        lower_cloths = []
        _lower_cloths = d.pop("lower_cloths", UNSET)
        for lower_cloths_item_data in _lower_cloths or []:
            lower_cloths_item = LowerCloth.from_dict(lower_cloths_item_data)

            lower_cloths.append(lower_cloths_item)

        person_attributes = cls(
            upper_cloths=upper_cloths,
            lower_cloths=lower_cloths,
        )

        person_attributes.additional_properties = d
        return person_attributes

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
