from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FaceAccessories")


@_attrs_define
class FaceAccessories:
    """
    Attributes:
        sunglasses (int):
        reading_glasses (int):
        swimming_goggles (int):
        face_mask (int):
        eyeglasses (int):
        headwear (int):
    """

    sunglasses: int
    reading_glasses: int
    swimming_goggles: int
    face_mask: int
    eyeglasses: int
    headwear: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sunglasses = self.sunglasses

        reading_glasses = self.reading_glasses

        swimming_goggles = self.swimming_goggles

        face_mask = self.face_mask

        eyeglasses = self.eyeglasses

        headwear = self.headwear

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sunglasses": sunglasses,
                "reading_glasses": reading_glasses,
                "swimming_goggles": swimming_goggles,
                "face_mask": face_mask,
                "eyeglasses": eyeglasses,
                "headwear": headwear,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sunglasses = d.pop("sunglasses")

        reading_glasses = d.pop("reading_glasses")

        swimming_goggles = d.pop("swimming_goggles")

        face_mask = d.pop("face_mask")

        eyeglasses = d.pop("eyeglasses")

        headwear = d.pop("headwear")

        face_accessories = cls(
            sunglasses=sunglasses,
            reading_glasses=reading_glasses,
            swimming_goggles=swimming_goggles,
            face_mask=face_mask,
            eyeglasses=eyeglasses,
            headwear=headwear,
        )

        face_accessories.additional_properties = d
        return face_accessories

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
