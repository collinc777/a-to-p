# BankInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | 
**iban** | **str** |  | 
**bsb** | **str** |  | 
**sort_code** | **str** |  | 
**vat_number** | **str** |  | 
**rooting_number** | **str** |  | 
**swift** | **str** |  | 

## Example

```python
from openapi_client.models.bank_invoice import BankInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of BankInvoice from a JSON string
bank_invoice_instance = BankInvoice.from_json(json)
# print the JSON string representation of the object
print(BankInvoice.to_json())

# convert the object into a dict
bank_invoice_dict = bank_invoice_instance.to_dict()
# create an instance of BankInvoice from a dict
bank_invoice_form_dict = bank_invoice.from_dict(bank_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


