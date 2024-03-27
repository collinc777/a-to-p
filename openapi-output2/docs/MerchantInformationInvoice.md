# MerchantInformationInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_name** | **str** |  | 
**merchant_address** | **str** |  | 
**merchant_phone** | **str** |  | 
**merchant_email** | **str** |  | 
**merchant_fax** | **str** |  | 
**merchant_website** | **str** |  | 
**merchant_tax_id** | **str** |  | 
**merchant_siret** | **str** |  | 
**merchant_siren** | **str** |  | 
**abn_number** | **str** |  | 
**gst_number** | **str** |  | 
**pan_number** | **str** |  | 
**vat_number** | **str** |  | 

## Example

```python
from openapi_client.models.merchant_information_invoice import MerchantInformationInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantInformationInvoice from a JSON string
merchant_information_invoice_instance = MerchantInformationInvoice.from_json(json)
# print the JSON string representation of the object
print(MerchantInformationInvoice.to_json())

# convert the object into a dict
merchant_information_invoice_dict = merchant_information_invoice_instance.to_dict()
# create an instance of MerchantInformationInvoice from a dict
merchant_information_invoice_form_dict = merchant_information_invoice.from_dict(merchant_information_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


