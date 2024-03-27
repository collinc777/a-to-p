from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.yoda_query_response_item import YodaQueryResponseItem


T = TypeVar("T", bound="YodaQueryResponse")


@_attrs_define
class YodaQueryResponse:
    """
    Attributes:
        result (List['YodaQueryResponseItem']):
    """

    result: List["YodaQueryResponseItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result = []
        for result_item_data in self.result:
            result_item = result_item_data.to_dict()
            result.append(result_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.yoda_query_response_item import YodaQueryResponseItem

        d = src_dict.copy()
        result = []
        _result = d.pop("result")
        for result_item_data in _result:
            result_item = YodaQueryResponseItem.from_dict(result_item_data)

            result.append(result_item)

        yoda_query_response = cls(
            result=result,
        )

        yoda_query_response.additional_properties = d
        return yoda_query_response

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
