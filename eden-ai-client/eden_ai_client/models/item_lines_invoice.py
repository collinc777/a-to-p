from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemLinesInvoice")


@_attrs_define
class ItemLinesInvoice:
    """
    Attributes:
        description (Union[Unset, str]):
        quantity (Union[Unset, int]):
        amount (Union[Unset, int]):
        unit_price (Union[Unset, int]):
        discount (Union[Unset, int]):
        product_code (Union[Unset, str]):
        date_item (Union[Unset, str]):
        tax_item (Union[Unset, int]):
        tax_rate (Union[Unset, int]):
    """

    description: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    amount: Union[Unset, int] = UNSET
    unit_price: Union[Unset, int] = UNSET
    discount: Union[Unset, int] = UNSET
    product_code: Union[Unset, str] = UNSET
    date_item: Union[Unset, str] = UNSET
    tax_item: Union[Unset, int] = UNSET
    tax_rate: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        quantity = self.quantity

        amount = self.amount

        unit_price = self.unit_price

        discount = self.discount

        product_code = self.product_code

        date_item = self.date_item

        tax_item = self.tax_item

        tax_rate = self.tax_rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if amount is not UNSET:
            field_dict["amount"] = amount
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price
        if discount is not UNSET:
            field_dict["discount"] = discount
        if product_code is not UNSET:
            field_dict["product_code"] = product_code
        if date_item is not UNSET:
            field_dict["date_item"] = date_item
        if tax_item is not UNSET:
            field_dict["tax_item"] = tax_item
        if tax_rate is not UNSET:
            field_dict["tax_rate"] = tax_rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        quantity = d.pop("quantity", UNSET)

        amount = d.pop("amount", UNSET)

        unit_price = d.pop("unit_price", UNSET)

        discount = d.pop("discount", UNSET)

        product_code = d.pop("product_code", UNSET)

        date_item = d.pop("date_item", UNSET)

        tax_item = d.pop("tax_item", UNSET)

        tax_rate = d.pop("tax_rate", UNSET)

        item_lines_invoice = cls(
            description=description,
            quantity=quantity,
            amount=amount,
            unit_price=unit_price,
            discount=discount,
            product_code=product_code,
            date_item=date_item,
            tax_item=tax_item,
            tax_rate=tax_rate,
        )

        item_lines_invoice.additional_properties = d
        return item_lines_invoice

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
