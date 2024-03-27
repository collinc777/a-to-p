from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.financial_bank_information import FinancialBankInformation
    from ..models.financial_customer_information import FinancialCustomerInformation
    from ..models.financial_document_information import FinancialDocumentInformation
    from ..models.financial_document_metadata import FinancialDocumentMetadata
    from ..models.financial_line_item import FinancialLineItem
    from ..models.financial_local_information import FinancialLocalInformation
    from ..models.financial_merchant_information import FinancialMerchantInformation
    from ..models.financial_payment_information import FinancialPaymentInformation


T = TypeVar("T", bound="FinancialParserObjectDataClass")


@_attrs_define
class FinancialParserObjectDataClass:
    """
    Attributes:
        customer_information (FinancialCustomerInformation):
        merchant_information (FinancialMerchantInformation):
        payment_information (FinancialPaymentInformation):
        financial_document_information (FinancialDocumentInformation):
        local (FinancialLocalInformation):
        bank (FinancialBankInformation):
        document_metadata (FinancialDocumentMetadata):
        item_lines (Union[Unset, List['FinancialLineItem']]): List of line items associated with the document.
    """

    customer_information: "FinancialCustomerInformation"
    merchant_information: "FinancialMerchantInformation"
    payment_information: "FinancialPaymentInformation"
    financial_document_information: "FinancialDocumentInformation"
    local: "FinancialLocalInformation"
    bank: "FinancialBankInformation"
    document_metadata: "FinancialDocumentMetadata"
    item_lines: Union[Unset, List["FinancialLineItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        customer_information = self.customer_information.to_dict()

        merchant_information = self.merchant_information.to_dict()

        payment_information = self.payment_information.to_dict()

        financial_document_information = self.financial_document_information.to_dict()

        local = self.local.to_dict()

        bank = self.bank.to_dict()

        document_metadata = self.document_metadata.to_dict()

        item_lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.item_lines, Unset):
            item_lines = []
            for item_lines_item_data in self.item_lines:
                item_lines_item = item_lines_item_data.to_dict()
                item_lines.append(item_lines_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer_information": customer_information,
                "merchant_information": merchant_information,
                "payment_information": payment_information,
                "financial_document_information": financial_document_information,
                "local": local,
                "bank": bank,
                "document_metadata": document_metadata,
            }
        )
        if item_lines is not UNSET:
            field_dict["item_lines"] = item_lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.financial_bank_information import FinancialBankInformation
        from ..models.financial_customer_information import FinancialCustomerInformation
        from ..models.financial_document_information import FinancialDocumentInformation
        from ..models.financial_document_metadata import FinancialDocumentMetadata
        from ..models.financial_line_item import FinancialLineItem
        from ..models.financial_local_information import FinancialLocalInformation
        from ..models.financial_merchant_information import FinancialMerchantInformation
        from ..models.financial_payment_information import FinancialPaymentInformation

        d = src_dict.copy()
        customer_information = FinancialCustomerInformation.from_dict(d.pop("customer_information"))

        merchant_information = FinancialMerchantInformation.from_dict(d.pop("merchant_information"))

        payment_information = FinancialPaymentInformation.from_dict(d.pop("payment_information"))

        financial_document_information = FinancialDocumentInformation.from_dict(d.pop("financial_document_information"))

        local = FinancialLocalInformation.from_dict(d.pop("local"))

        bank = FinancialBankInformation.from_dict(d.pop("bank"))

        document_metadata = FinancialDocumentMetadata.from_dict(d.pop("document_metadata"))

        item_lines = []
        _item_lines = d.pop("item_lines", UNSET)
        for item_lines_item_data in _item_lines or []:
            item_lines_item = FinancialLineItem.from_dict(item_lines_item_data)

            item_lines.append(item_lines_item)

        financial_parser_object_data_class = cls(
            customer_information=customer_information,
            merchant_information=merchant_information,
            payment_information=payment_information,
            financial_document_information=financial_document_information,
            local=local,
            bank=bank,
            document_metadata=document_metadata,
            item_lines=item_lines,
        )

        financial_parser_object_data_class.additional_properties = d
        return financial_parser_object_data_class

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
