# TaxesInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** |  | 
**rate** | **int** |  | 

## Example

```python
from openapi_client.models.taxes_invoice import TaxesInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of TaxesInvoice from a JSON string
taxes_invoice_instance = TaxesInvoice.from_json(json)
# print the JSON string representation of the object
print(TaxesInvoice.to_json())

# convert the object into a dict
taxes_invoice_dict = taxes_invoice_instance.to_dict()
# create an instance of TaxesInvoice from a dict
taxes_invoice_form_dict = taxes_invoice.from_dict(taxes_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


