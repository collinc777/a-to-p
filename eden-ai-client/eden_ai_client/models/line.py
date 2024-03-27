from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bounding_box import BoundingBox
    from ..models.word import Word


T = TypeVar("T", bound="Line")


@_attrs_define
class Line:
    """Line of a document

    Attributes:
        text (str): Text detected in the line
        bounding_boxes (Sequence[BoundingBox]): Bounding boxes of the words in the line
        words (Sequence[Word]): List of words of the line
        confidence (float): Confidence of the line


    Attributes:
        text (str): Text detected in the line
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

        confidence (int): Confidence of the line
        words (Union[Unset, List['Word']]): List of words
    """

    text: str
    bounding_box: "BoundingBox"
    confidence: int
    words: Union[Unset, List["Word"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        bounding_box = self.bounding_box.to_dict()

        confidence = self.confidence

        words: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.words, Unset):
            words = []
            for words_item_data in self.words:
                words_item = words_item_data.to_dict()
                words.append(words_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "bounding_box": bounding_box,
                "confidence": confidence,
            }
        )
        if words is not UNSET:
            field_dict["words"] = words

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bounding_box import BoundingBox
        from ..models.word import Word

        d = src_dict.copy()
        text = d.pop("text")

        bounding_box = BoundingBox.from_dict(d.pop("bounding_box"))

        confidence = d.pop("confidence")

        words = []
        _words = d.pop("words", UNSET)
        for words_item_data in _words or []:
            words_item = Word.from_dict(words_item_data)

            words.append(words_item)

        line = cls(
            text=text,
            bounding_box=bounding_box,
            confidence=confidence,
            words=words,
        )

        line.additional_properties = d
        return line

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
