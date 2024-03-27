# FinancialBankInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iban** | **str** | International Bank Account Number. | [optional] 
**swift** | **str** | Society for Worldwide Interbank Financial Telecommunication code. | [optional] 
**bsb** | **str** | Bank State Branch code (Australia). | [optional] 
**sort_code** | **str** | Sort code for UK banks. | [optional] 
**account_number** | **str** | Bank account number. | [optional] 
**routing_number** | **str** | Routing number for banks in the United States. | [optional] 
**bic** | **str** | Bank Identifier Code. | [optional] 

## Example

```python
from openapi_client.models.financial_bank_information import FinancialBankInformation

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialBankInformation from a JSON string
financial_bank_information_instance = FinancialBankInformation.from_json(json)
# print the JSON string representation of the object
print(FinancialBankInformation.to_json())

# convert the object into a dict
financial_bank_information_dict = financial_bank_information_instance.to_dict()
# create an instance of FinancialBankInformation from a dict
financial_bank_information_form_dict = financial_bank_information.from_dict(financial_bank_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


