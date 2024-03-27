from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cell import Cell


T = TypeVar("T", bound="Row")


@_attrs_define
class Row:
    """
    Attributes:
        cells (Union[Unset, List['Cell']]):
    """

    cells: Union[Unset, List["Cell"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cells: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cells, Unset):
            cells = []
            for cells_item_data in self.cells:
                cells_item = cells_item_data.to_dict()
                cells.append(cells_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cells is not UNSET:
            field_dict["cells"] = cells

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cell import Cell

        d = src_dict.copy()
        cells = []
        _cells = d.pop("cells", UNSET)
        for cells_item_data in _cells or []:
            cells_item = Cell.from_dict(cells_item_data)

            cells.append(cells_item)

        row = cls(
            cells=cells,
        )

        row.additional_properties = d
        return row

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
