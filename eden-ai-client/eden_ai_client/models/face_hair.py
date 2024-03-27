from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.face_hair_color import FaceHairColor


T = TypeVar("T", bound="FaceHair")


@_attrs_define
class FaceHair:
    """
    Attributes:
        bald (int):
        invisible (bool):
        hair_color (Union[Unset, List['FaceHairColor']]):
    """

    bald: int
    invisible: bool
    hair_color: Union[Unset, List["FaceHairColor"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bald = self.bald

        invisible = self.invisible

        hair_color: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hair_color, Unset):
            hair_color = []
            for hair_color_item_data in self.hair_color:
                hair_color_item = hair_color_item_data.to_dict()
                hair_color.append(hair_color_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bald": bald,
                "invisible": invisible,
            }
        )
        if hair_color is not UNSET:
            field_dict["hair_color"] = hair_color

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.face_hair_color import FaceHairColor

        d = src_dict.copy()
        bald = d.pop("bald")

        invisible = d.pop("invisible")

        hair_color = []
        _hair_color = d.pop("hair_color", UNSET)
        for hair_color_item_data in _hair_color or []:
            hair_color_item = FaceHairColor.from_dict(hair_color_item_data)

            hair_color.append(hair_color_item)

        face_hair = cls(
            bald=bald,
            invisible=invisible,
            hair_color=hair_color,
        )

        face_hair.additional_properties = d
        return face_hair

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
