# LocaleInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**language** | **str** |  | 

## Example

```python
from openapi_client.models.locale_invoice import LocaleInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of LocaleInvoice from a JSON string
locale_invoice_instance = LocaleInvoice.from_json(json)
# print the JSON string representation of the object
print(LocaleInvoice.to_json())

# convert the object into a dict
locale_invoice_dict = locale_invoice_instance.to_dict()
# create an instance of LocaleInvoice from a dict
locale_invoice_form_dict = locale_invoice.from_dict(locale_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


