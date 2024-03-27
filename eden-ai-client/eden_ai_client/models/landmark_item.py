from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.landmark_location import LandmarkLocation
    from ..models.landmark_vertice import LandmarkVertice


T = TypeVar("T", bound="LandmarkItem")


@_attrs_define
class LandmarkItem:
    """
    Attributes:
        description (str):
        confidence (int):
        bounding_box (Union[Unset, List['LandmarkVertice']]):
        locations (Union[Unset, List['LandmarkLocation']]):
    """

    description: str
    confidence: int
    bounding_box: Union[Unset, List["LandmarkVertice"]] = UNSET
    locations: Union[Unset, List["LandmarkLocation"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        confidence = self.confidence

        bounding_box: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bounding_box, Unset):
            bounding_box = []
            for bounding_box_item_data in self.bounding_box:
                bounding_box_item = bounding_box_item_data.to_dict()
                bounding_box.append(bounding_box_item)

        locations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "confidence": confidence,
            }
        )
        if bounding_box is not UNSET:
            field_dict["bounding_box"] = bounding_box
        if locations is not UNSET:
            field_dict["locations"] = locations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.landmark_location import LandmarkLocation
        from ..models.landmark_vertice import LandmarkVertice

        d = src_dict.copy()
        description = d.pop("description")

        confidence = d.pop("confidence")

        bounding_box = []
        _bounding_box = d.pop("bounding_box", UNSET)
        for bounding_box_item_data in _bounding_box or []:
            bounding_box_item = LandmarkVertice.from_dict(bounding_box_item_data)

            bounding_box.append(bounding_box_item)

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = LandmarkLocation.from_dict(locations_item_data)

            locations.append(locations_item)

        landmark_item = cls(
            description=description,
            confidence=confidence,
            bounding_box=bounding_box,
            locations=locations,
        )

        landmark_item.additional_properties = d
        return landmark_item

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
