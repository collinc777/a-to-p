# FinancialLocalInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency used in financial transactions. | [optional] 
**currency_code** | **str** | Currency code (e.g., USD, EUR). | [optional] 
**currency_exchange_rate** | **str** | Exchange rate for the specified currency. | [optional] 
**country** | **str** | Country associated with the local financial information. | [optional] 
**language** | **str** | Language used in financial transactions. | [optional] 

## Example

```python
from openapi_client.models.financial_local_information import FinancialLocalInformation

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialLocalInformation from a JSON string
financial_local_information_instance = FinancialLocalInformation.from_json(json)
# print the JSON string representation of the object
print(FinancialLocalInformation.to_json())

# convert the object into a dict
financial_local_information_dict = financial_local_information_instance.to_dict()
# create an instance of FinancialLocalInformation from a dict
financial_local_information_form_dict = financial_local_information.from_dict(financial_local_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


