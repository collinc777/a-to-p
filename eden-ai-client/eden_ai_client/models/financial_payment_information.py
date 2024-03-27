from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialPaymentInformation")


@_attrs_define
class FinancialPaymentInformation:
    """
    Attributes:
        amount_due (Union[Unset, int]): Amount due for payment.
        amount_tip (Union[Unset, int]): Tip amount in a financial transaction.
        amount_shipping (Union[Unset, int]): Shipping cost in a financial transaction.
        amount_change (Union[Unset, int]): Change amount in a financial transaction.
        amount_paid (Union[Unset, int]): Amount already paid in a financial transaction.
        total (Union[Unset, int]): Total amount in the invoice.
        subtotal (Union[Unset, int]): Subtotal amount in a financial transaction.
        total_tax (Union[Unset, int]): Total tax amount in a financial transaction.
        tax_rate (Union[Unset, int]): Tax rate applied in a financial transaction.
        discount (Union[Unset, int]): Discount amount applied in a financial transaction.
        gratuity (Union[Unset, int]): Gratuity amount in a financial transaction.
        service_charge (Union[Unset, int]): Service charge in a financial transaction.
        previous_unpaid_balance (Union[Unset, int]): Previous unpaid balance in a financial transaction.
        prior_balance (Union[Unset, int]): Prior balance before the current financial transaction.
        payment_terms (Union[Unset, str]): Terms and conditions for payment.
        payment_method (Union[Unset, str]): Payment method used in the financial transaction.
        payment_card_number (Union[Unset, str]): Card number used in the payment.
        payment_auth_code (Union[Unset, str]): Authorization code for the payment.
        shipping_handling_charge (Union[Unset, int]): Charge for shipping and handling in a financial transaction.
        transaction_number (Union[Unset, str]): Unique identifier for the financial transaction.
        transaction_reference (Union[Unset, str]): Reference number for the financial transaction.
    """

    amount_due: Union[Unset, int] = UNSET
    amount_tip: Union[Unset, int] = UNSET
    amount_shipping: Union[Unset, int] = UNSET
    amount_change: Union[Unset, int] = UNSET
    amount_paid: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    subtotal: Union[Unset, int] = UNSET
    total_tax: Union[Unset, int] = UNSET
    tax_rate: Union[Unset, int] = UNSET
    discount: Union[Unset, int] = UNSET
    gratuity: Union[Unset, int] = UNSET
    service_charge: Union[Unset, int] = UNSET
    previous_unpaid_balance: Union[Unset, int] = UNSET
    prior_balance: Union[Unset, int] = UNSET
    payment_terms: Union[Unset, str] = UNSET
    payment_method: Union[Unset, str] = UNSET
    payment_card_number: Union[Unset, str] = UNSET
    payment_auth_code: Union[Unset, str] = UNSET
    shipping_handling_charge: Union[Unset, int] = UNSET
    transaction_number: Union[Unset, str] = UNSET
    transaction_reference: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount_due = self.amount_due

        amount_tip = self.amount_tip

        amount_shipping = self.amount_shipping

        amount_change = self.amount_change

        amount_paid = self.amount_paid

        total = self.total

        subtotal = self.subtotal

        total_tax = self.total_tax

        tax_rate = self.tax_rate

        discount = self.discount

        gratuity = self.gratuity

        service_charge = self.service_charge

        previous_unpaid_balance = self.previous_unpaid_balance

        prior_balance = self.prior_balance

        payment_terms = self.payment_terms

        payment_method = self.payment_method

        payment_card_number = self.payment_card_number

        payment_auth_code = self.payment_auth_code

        shipping_handling_charge = self.shipping_handling_charge

        transaction_number = self.transaction_number

        transaction_reference = self.transaction_reference

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_due is not UNSET:
            field_dict["amount_due"] = amount_due
        if amount_tip is not UNSET:
            field_dict["amount_tip"] = amount_tip
        if amount_shipping is not UNSET:
            field_dict["amount_shipping"] = amount_shipping
        if amount_change is not UNSET:
            field_dict["amount_change"] = amount_change
        if amount_paid is not UNSET:
            field_dict["amount_paid"] = amount_paid
        if total is not UNSET:
            field_dict["total"] = total
        if subtotal is not UNSET:
            field_dict["subtotal"] = subtotal
        if total_tax is not UNSET:
            field_dict["total_tax"] = total_tax
        if tax_rate is not UNSET:
            field_dict["tax_rate"] = tax_rate
        if discount is not UNSET:
            field_dict["discount"] = discount
        if gratuity is not UNSET:
            field_dict["gratuity"] = gratuity
        if service_charge is not UNSET:
            field_dict["service_charge"] = service_charge
        if previous_unpaid_balance is not UNSET:
            field_dict["previous_unpaid_balance"] = previous_unpaid_balance
        if prior_balance is not UNSET:
            field_dict["prior_balance"] = prior_balance
        if payment_terms is not UNSET:
            field_dict["payment_terms"] = payment_terms
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method
        if payment_card_number is not UNSET:
            field_dict["payment_card_number"] = payment_card_number
        if payment_auth_code is not UNSET:
            field_dict["payment_auth_code"] = payment_auth_code
        if shipping_handling_charge is not UNSET:
            field_dict["shipping_handling_charge"] = shipping_handling_charge
        if transaction_number is not UNSET:
            field_dict["transaction_number"] = transaction_number
        if transaction_reference is not UNSET:
            field_dict["transaction_reference"] = transaction_reference

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount_due = d.pop("amount_due", UNSET)

        amount_tip = d.pop("amount_tip", UNSET)

        amount_shipping = d.pop("amount_shipping", UNSET)

        amount_change = d.pop("amount_change", UNSET)

        amount_paid = d.pop("amount_paid", UNSET)

        total = d.pop("total", UNSET)

        subtotal = d.pop("subtotal", UNSET)

        total_tax = d.pop("total_tax", UNSET)

        tax_rate = d.pop("tax_rate", UNSET)

        discount = d.pop("discount", UNSET)

        gratuity = d.pop("gratuity", UNSET)

        service_charge = d.pop("service_charge", UNSET)

        previous_unpaid_balance = d.pop("previous_unpaid_balance", UNSET)

        prior_balance = d.pop("prior_balance", UNSET)

        payment_terms = d.pop("payment_terms", UNSET)

        payment_method = d.pop("payment_method", UNSET)

        payment_card_number = d.pop("payment_card_number", UNSET)

        payment_auth_code = d.pop("payment_auth_code", UNSET)

        shipping_handling_charge = d.pop("shipping_handling_charge", UNSET)

        transaction_number = d.pop("transaction_number", UNSET)

        transaction_reference = d.pop("transaction_reference", UNSET)

        financial_payment_information = cls(
            amount_due=amount_due,
            amount_tip=amount_tip,
            amount_shipping=amount_shipping,
            amount_change=amount_change,
            amount_paid=amount_paid,
            total=total,
            subtotal=subtotal,
            total_tax=total_tax,
            tax_rate=tax_rate,
            discount=discount,
            gratuity=gratuity,
            service_charge=service_charge,
            previous_unpaid_balance=previous_unpaid_balance,
            prior_balance=prior_balance,
            payment_terms=payment_terms,
            payment_method=payment_method,
            payment_card_number=payment_card_number,
            payment_auth_code=payment_auth_code,
            shipping_handling_charge=shipping_handling_charge,
            transaction_number=transaction_number,
            transaction_reference=transaction_reference,
        )

        financial_payment_information.additional_properties = d
        return financial_payment_information

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
