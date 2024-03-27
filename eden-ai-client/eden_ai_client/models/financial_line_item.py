from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialLineItem")


@_attrs_define
class FinancialLineItem:
    """
    Attributes:
        tax (Union[Unset, int]): Tax amount for the line item.
        amount_line (Union[Unset, int]): Total amount for the line item.
        description (Union[Unset, str]): Description of the line item.
        quantity (Union[Unset, int]): Quantity of units for the line item.
        unit_price (Union[Unset, int]): Unit price for each unit in the line item.
        unit_type (Union[Unset, str]): Type of unit (e.g., hours, items).
        date (Union[Unset, str]): Date associated with the line item.
        product_code (Union[Unset, str]): Product code or identifier for the line item.
        purchase_order (Union[Unset, str]): Purchase order related to the line item.
        tax_rate (Union[Unset, int]): Tax rate applied to the line item.
        base_total (Union[Unset, int]): Base total amount before any discounts or taxes.
        sub_total (Union[Unset, int]): Subtotal amount for the line item.
        discount_amount (Union[Unset, int]): Amount of discount applied to the line item.
        discount_rate (Union[Unset, int]): Rate of discount applied to the line item.
        discount_code (Union[Unset, str]): Code associated with any discount applied to the line item.
        order_number (Union[Unset, str]): Order number associated with the line item.
        title (Union[Unset, str]): Title or name of the line item.
    """

    tax: Union[Unset, int] = UNSET
    amount_line: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    unit_price: Union[Unset, int] = UNSET
    unit_type: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    product_code: Union[Unset, str] = UNSET
    purchase_order: Union[Unset, str] = UNSET
    tax_rate: Union[Unset, int] = UNSET
    base_total: Union[Unset, int] = UNSET
    sub_total: Union[Unset, int] = UNSET
    discount_amount: Union[Unset, int] = UNSET
    discount_rate: Union[Unset, int] = UNSET
    discount_code: Union[Unset, str] = UNSET
    order_number: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tax = self.tax

        amount_line = self.amount_line

        description = self.description

        quantity = self.quantity

        unit_price = self.unit_price

        unit_type = self.unit_type

        date = self.date

        product_code = self.product_code

        purchase_order = self.purchase_order

        tax_rate = self.tax_rate

        base_total = self.base_total

        sub_total = self.sub_total

        discount_amount = self.discount_amount

        discount_rate = self.discount_rate

        discount_code = self.discount_code

        order_number = self.order_number

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tax is not UNSET:
            field_dict["tax"] = tax
        if amount_line is not UNSET:
            field_dict["amount_line"] = amount_line
        if description is not UNSET:
            field_dict["description"] = description
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price
        if unit_type is not UNSET:
            field_dict["unit_type"] = unit_type
        if date is not UNSET:
            field_dict["date"] = date
        if product_code is not UNSET:
            field_dict["product_code"] = product_code
        if purchase_order is not UNSET:
            field_dict["purchase_order"] = purchase_order
        if tax_rate is not UNSET:
            field_dict["tax_rate"] = tax_rate
        if base_total is not UNSET:
            field_dict["base_total"] = base_total
        if sub_total is not UNSET:
            field_dict["sub_total"] = sub_total
        if discount_amount is not UNSET:
            field_dict["discount_amount"] = discount_amount
        if discount_rate is not UNSET:
            field_dict["discount_rate"] = discount_rate
        if discount_code is not UNSET:
            field_dict["discount_code"] = discount_code
        if order_number is not UNSET:
            field_dict["order_number"] = order_number
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tax = d.pop("tax", UNSET)

        amount_line = d.pop("amount_line", UNSET)

        description = d.pop("description", UNSET)

        quantity = d.pop("quantity", UNSET)

        unit_price = d.pop("unit_price", UNSET)

        unit_type = d.pop("unit_type", UNSET)

        date = d.pop("date", UNSET)

        product_code = d.pop("product_code", UNSET)

        purchase_order = d.pop("purchase_order", UNSET)

        tax_rate = d.pop("tax_rate", UNSET)

        base_total = d.pop("base_total", UNSET)

        sub_total = d.pop("sub_total", UNSET)

        discount_amount = d.pop("discount_amount", UNSET)

        discount_rate = d.pop("discount_rate", UNSET)

        discount_code = d.pop("discount_code", UNSET)

        order_number = d.pop("order_number", UNSET)

        title = d.pop("title", UNSET)

        financial_line_item = cls(
            tax=tax,
            amount_line=amount_line,
            description=description,
            quantity=quantity,
            unit_price=unit_price,
            unit_type=unit_type,
            date=date,
            product_code=product_code,
            purchase_order=purchase_order,
            tax_rate=tax_rate,
            base_total=base_total,
            sub_total=sub_total,
            discount_amount=discount_amount,
            discount_rate=discount_rate,
            discount_code=discount_code,
            order_number=order_number,
            title=title,
        )

        financial_line_item.additional_properties = d
        return financial_line_item

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
