from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.row import Row


T = TypeVar("T", bound="Table")


@_attrs_define
class Table:
    """
    Attributes:
        num_rows (int):
        num_cols (int):
        rows (Union[Unset, List['Row']]):
    """

    num_rows: int
    num_cols: int
    rows: Union[Unset, List["Row"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        num_rows = self.num_rows

        num_cols = self.num_cols

        rows: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "num_rows": num_rows,
                "num_cols": num_cols,
            }
        )
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.row import Row

        d = src_dict.copy()
        num_rows = d.pop("num_rows")

        num_cols = d.pop("num_cols")

        rows = []
        _rows = d.pop("rows", UNSET)
        for rows_item_data in _rows or []:
            rows_item = Row.from_dict(rows_item_data)

            rows.append(rows_item)

        table = cls(
            num_rows=num_rows,
            num_cols=num_cols,
            rows=rows,
        )

        table.additional_properties = d
        return table

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
