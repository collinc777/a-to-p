from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bounding_box import BoundingBox


T = TypeVar("T", bound="Word")


@_attrs_define
class Word:
    """Word of a document

    Attributes:
        text (str): Text detected in the word
        bounding_boxes (Sequence[BoundingBox]): Bounding boxes of the words in the word
        confidence (float): Confidence score of the word


    Attributes:
        text (str): Text detected in the word
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

        confidence (int): Confidence score of the word
    """

    text: str
    bounding_box: "BoundingBox"
    confidence: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        bounding_box = self.bounding_box.to_dict()

        confidence = self.confidence

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "bounding_box": bounding_box,
                "confidence": confidence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bounding_box import BoundingBox

        d = src_dict.copy()
        text = d.pop("text")

        bounding_box = BoundingBox.from_dict(d.pop("bounding_box"))

        confidence = d.pop("confidence")

        word = cls(
            text=text,
            bounding_box=bounding_box,
            confidence=confidence,
        )

        word.additional_properties = d
        return word

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
