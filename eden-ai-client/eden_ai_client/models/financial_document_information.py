from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.financial_barcode import FinancialBarcode


T = TypeVar("T", bound="FinancialDocumentInformation")


@_attrs_define
class FinancialDocumentInformation:
    """
    Attributes:
        invoice_receipt_id (Union[Unset, str]): Identifier for the invoice.
        purchase_order (Union[Unset, str]): Purchase order related to the document.
        invoice_date (Union[Unset, str]): Date of the invoice.
        time (Union[Unset, str]): Time associated with the document.
        invoice_due_date (Union[Unset, str]): Due date for the invoice.
        service_start_date (Union[Unset, str]): Start date of the service associated with the document.
        service_end_date (Union[Unset, str]): End date of the service associated with the document.
        reference (Union[Unset, str]): Reference number associated with the document.
        biller_code (Union[Unset, str]): Biller code associated with the document.
        order_date (Union[Unset, str]): Date of the order associated with the document.
        tracking_number (Union[Unset, str]): Tracking number associated with the document.
        barcodes (Union[Unset, List['FinancialBarcode']]): List of barcodes associated with the document.
    """

    invoice_receipt_id: Union[Unset, str] = UNSET
    purchase_order: Union[Unset, str] = UNSET
    invoice_date: Union[Unset, str] = UNSET
    time: Union[Unset, str] = UNSET
    invoice_due_date: Union[Unset, str] = UNSET
    service_start_date: Union[Unset, str] = UNSET
    service_end_date: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    biller_code: Union[Unset, str] = UNSET
    order_date: Union[Unset, str] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    barcodes: Union[Unset, List["FinancialBarcode"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_receipt_id = self.invoice_receipt_id

        purchase_order = self.purchase_order

        invoice_date = self.invoice_date

        time = self.time

        invoice_due_date = self.invoice_due_date

        service_start_date = self.service_start_date

        service_end_date = self.service_end_date

        reference = self.reference

        biller_code = self.biller_code

        order_date = self.order_date

        tracking_number = self.tracking_number

        barcodes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.barcodes, Unset):
            barcodes = []
            for barcodes_item_data in self.barcodes:
                barcodes_item = barcodes_item_data.to_dict()
                barcodes.append(barcodes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoice_receipt_id is not UNSET:
            field_dict["invoice_receipt_id"] = invoice_receipt_id
        if purchase_order is not UNSET:
            field_dict["purchase_order"] = purchase_order
        if invoice_date is not UNSET:
            field_dict["invoice_date"] = invoice_date
        if time is not UNSET:
            field_dict["time"] = time
        if invoice_due_date is not UNSET:
            field_dict["invoice_due_date"] = invoice_due_date
        if service_start_date is not UNSET:
            field_dict["service_start_date"] = service_start_date
        if service_end_date is not UNSET:
            field_dict["service_end_date"] = service_end_date
        if reference is not UNSET:
            field_dict["reference"] = reference
        if biller_code is not UNSET:
            field_dict["biller_code"] = biller_code
        if order_date is not UNSET:
            field_dict["order_date"] = order_date
        if tracking_number is not UNSET:
            field_dict["tracking_number"] = tracking_number
        if barcodes is not UNSET:
            field_dict["barcodes"] = barcodes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.financial_barcode import FinancialBarcode

        d = src_dict.copy()
        invoice_receipt_id = d.pop("invoice_receipt_id", UNSET)

        purchase_order = d.pop("purchase_order", UNSET)

        invoice_date = d.pop("invoice_date", UNSET)

        time = d.pop("time", UNSET)

        invoice_due_date = d.pop("invoice_due_date", UNSET)

        service_start_date = d.pop("service_start_date", UNSET)

        service_end_date = d.pop("service_end_date", UNSET)

        reference = d.pop("reference", UNSET)

        biller_code = d.pop("biller_code", UNSET)

        order_date = d.pop("order_date", UNSET)

        tracking_number = d.pop("tracking_number", UNSET)

        barcodes = []
        _barcodes = d.pop("barcodes", UNSET)
        for barcodes_item_data in _barcodes or []:
            barcodes_item = FinancialBarcode.from_dict(barcodes_item_data)

            barcodes.append(barcodes_item)

        financial_document_information = cls(
            invoice_receipt_id=invoice_receipt_id,
            purchase_order=purchase_order,
            invoice_date=invoice_date,
            time=time,
            invoice_due_date=invoice_due_date,
            service_start_date=service_start_date,
            service_end_date=service_end_date,
            reference=reference,
            biller_code=biller_code,
            order_date=order_date,
            tracking_number=tracking_number,
            barcodes=barcodes,
        )

        financial_document_information.additional_properties = d
        return financial_document_information

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
