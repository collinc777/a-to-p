from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.boundix_box_ocr_table import BoundixBoxOCRTable


T = TypeVar("T", bound="Cell")


@_attrs_define
class Cell:
    """
    Attributes:
        text (str):
        row_index (int):
        col_index (int):
        row_span (int):
        col_span (int):
        confidence (int):
        bounding_box (BoundixBoxOCRTable):
        is_header (Union[Unset, bool]):  Default: False.
    """

    text: str
    row_index: int
    col_index: int
    row_span: int
    col_span: int
    confidence: int
    bounding_box: "BoundixBoxOCRTable"
    is_header: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        row_index = self.row_index

        col_index = self.col_index

        row_span = self.row_span

        col_span = self.col_span

        confidence = self.confidence

        bounding_box = self.bounding_box.to_dict()

        is_header = self.is_header

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "row_index": row_index,
                "col_index": col_index,
                "row_span": row_span,
                "col_span": col_span,
                "confidence": confidence,
                "bounding_box": bounding_box,
            }
        )
        if is_header is not UNSET:
            field_dict["is_header"] = is_header

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.boundix_box_ocr_table import BoundixBoxOCRTable

        d = src_dict.copy()
        text = d.pop("text")

        row_index = d.pop("row_index")

        col_index = d.pop("col_index")

        row_span = d.pop("row_span")

        col_span = d.pop("col_span")

        confidence = d.pop("confidence")

        bounding_box = BoundixBoxOCRTable.from_dict(d.pop("bounding_box"))

        is_header = d.pop("is_header", UNSET)

        cell = cls(
            text=text,
            row_index=row_index,
            col_index=col_index,
            row_span=row_span,
            col_span=col_span,
            confidence=confidence,
            bounding_box=bounding_box,
            is_header=is_header,
        )

        cell.additional_properties = d
        return cell

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
