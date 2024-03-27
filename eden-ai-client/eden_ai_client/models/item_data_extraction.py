from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bounding_box import BoundingBox


T = TypeVar("T", bound="ItemDataExtraction")


@_attrs_define
class ItemDataExtraction:
    """
    Attributes:
        key (str):
        value (Any):
        bounding_box (BoundingBox): Bounding box of a word in the image

                Attributes:
                    left (float): Left coordinate of the bounding box
                    top (float): Top coordinate of the bounding box
                    width (float): Width of the bounding box
                    height (float): Height of the bounding box
                    text (str): Text detected in the bounding box

                Constructor:
                    from_json (classmethod): Create a new instance of BoundingBox from a JSON object
                    from_normalized_vertices (classmethod): Create a new instance of BoundingBox from normalized vertices
                    unknown (classmethod): Return a invalid bouding_box with all field filled with `-1`

        confidence_score (int):
    """

    key: str
    value: Any
    bounding_box: "BoundingBox"
    confidence_score: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key

        value = self.value

        bounding_box = self.bounding_box.to_dict()

        confidence_score = self.confidence_score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "value": value,
                "bounding_box": bounding_box,
                "confidence_score": confidence_score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bounding_box import BoundingBox

        d = src_dict.copy()
        key = d.pop("key")

        value = d.pop("value")

        bounding_box = BoundingBox.from_dict(d.pop("bounding_box"))

        confidence_score = d.pop("confidence_score")

        item_data_extraction = cls(
            key=key,
            value=value,
            bounding_box=bounding_box,
            confidence_score=confidence_score,
        )

        item_data_extraction.additional_properties = d
        return item_data_extraction

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
