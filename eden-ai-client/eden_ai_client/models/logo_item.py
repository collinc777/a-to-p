from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.logo_bounding_poly import LogoBoundingPoly


T = TypeVar("T", bound="LogoItem")


@_attrs_define
class LogoItem:
    """
    Attributes:
        bounding_poly (LogoBoundingPoly):
        description (str):
        score (int):
    """

    bounding_poly: "LogoBoundingPoly"
    description: str
    score: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bounding_poly = self.bounding_poly.to_dict()

        description = self.description

        score = self.score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bounding_poly": bounding_poly,
                "description": description,
                "score": score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.logo_bounding_poly import LogoBoundingPoly

        d = src_dict.copy()
        bounding_poly = LogoBoundingPoly.from_dict(d.pop("bounding_poly"))

        description = d.pop("description")

        score = d.pop("score")

        logo_item = cls(
            bounding_poly=bounding_poly,
            description=description,
            score=score,
        )

        logo_item.additional_properties = d
        return logo_item

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
