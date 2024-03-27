from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.micr_model import MicrModel


T = TypeVar("T", bound="ItemBankCheckParsingDataClass")


@_attrs_define
class ItemBankCheckParsingDataClass:
    """
    Attributes:
        amount (int):
        amount_text (str):
        bank_address (str):
        bank_name (str):
        date (str):
        memo (str):
        payer_address (str):
        payer_name (str):
        receiver_address (str):
        receiver_name (str):
        currency (str):
        micr (MicrModel):
    """

    amount: int
    amount_text: str
    bank_address: str
    bank_name: str
    date: str
    memo: str
    payer_address: str
    payer_name: str
    receiver_address: str
    receiver_name: str
    currency: str
    micr: "MicrModel"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        amount_text = self.amount_text

        bank_address = self.bank_address

        bank_name = self.bank_name

        date = self.date

        memo = self.memo

        payer_address = self.payer_address

        payer_name = self.payer_name

        receiver_address = self.receiver_address

        receiver_name = self.receiver_name

        currency = self.currency

        micr = self.micr.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "amount_text": amount_text,
                "bank_address": bank_address,
                "bank_name": bank_name,
                "date": date,
                "memo": memo,
                "payer_address": payer_address,
                "payer_name": payer_name,
                "receiver_address": receiver_address,
                "receiver_name": receiver_name,
                "currency": currency,
                "micr": micr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.micr_model import MicrModel

        d = src_dict.copy()
        amount = d.pop("amount")

        amount_text = d.pop("amount_text")

        bank_address = d.pop("bank_address")

        bank_name = d.pop("bank_name")

        date = d.pop("date")

        memo = d.pop("memo")

        payer_address = d.pop("payer_address")

        payer_name = d.pop("payer_name")

        receiver_address = d.pop("receiver_address")

        receiver_name = d.pop("receiver_name")

        currency = d.pop("currency")

        micr = MicrModel.from_dict(d.pop("micr"))

        item_bank_check_parsing_data_class = cls(
            amount=amount,
            amount_text=amount_text,
            bank_address=bank_address,
            bank_name=bank_name,
            date=date,
            memo=memo,
            payer_address=payer_address,
            payer_name=payer_name,
            receiver_address=receiver_address,
            receiver_name=receiver_name,
            currency=currency,
            micr=micr,
        )

        item_bank_check_parsing_data_class.additional_properties = d
        return item_bank_check_parsing_data_class

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
