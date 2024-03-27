from enum import Enum


class FinancialInformationSubCategoryType(str, Enum):
    BANKACCOUNTNUMBER = "BankAccountNumber"
    BANKROUTINGNUMBER = "BankRoutingNumber"
    CARDEXPIRY = "CardExpiry"
    CREDITCARD = "CreditCard"
    SWIFTCODE = "SwiftCode"
    TAXIDENTIFICATIONNUMBER = "TaxIdentificationNumber"

    def __str__(self) -> str:
        return str(self.value)
