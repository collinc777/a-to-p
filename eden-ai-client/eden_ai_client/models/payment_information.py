from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentInformation")


@_attrs_define
class PaymentInformation:
    """
    Attributes:
        card_type (Union[Unset, str]):
        card_number (Union[Unset, str]):
        cash (Union[Unset, str]):
        tip (Union[Unset, str]):
        discount (Union[Unset, str]):
        change (Union[Unset, str]):
    """

    card_type: Union[Unset, str] = UNSET
    card_number: Union[Unset, str] = UNSET
    cash: Union[Unset, str] = UNSET
    tip: Union[Unset, str] = UNSET
    discount: Union[Unset, str] = UNSET
    change: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        card_type = self.card_type

        card_number = self.card_number

        cash = self.cash

        tip = self.tip

        discount = self.discount

        change = self.change

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if card_type is not UNSET:
            field_dict["card_type"] = card_type
        if card_number is not UNSET:
            field_dict["card_number"] = card_number
        if cash is not UNSET:
            field_dict["cash"] = cash
        if tip is not UNSET:
            field_dict["tip"] = tip
        if discount is not UNSET:
            field_dict["discount"] = discount
        if change is not UNSET:
            field_dict["change"] = change

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        card_type = d.pop("card_type", UNSET)

        card_number = d.pop("card_number", UNSET)

        cash = d.pop("cash", UNSET)

        tip = d.pop("tip", UNSET)

        discount = d.pop("discount", UNSET)

        change = d.pop("change", UNSET)

        payment_information = cls(
            card_type=card_type,
            card_number=card_number,
            cash=cash,
            tip=tip,
            discount=discount,
            change=change,
        )

        payment_information.additional_properties = d
        return payment_information

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
