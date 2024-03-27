# CustomerInformationInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_name** | **str** |  | 
**customer_address** | **str** |  | 
**customer_email** | **str** |  | 
**customer_id** | **str** |  | 
**customer_tax_id** | **str** |  | 
**customer_mailing_address** | **str** |  | 
**customer_billing_address** | **str** |  | 
**customer_shipping_address** | **str** |  | 
**customer_service_address** | **str** |  | 
**customer_remittance_address** | **str** |  | 
**abn_number** | **str** |  | 
**gst_number** | **str** |  | 
**pan_number** | **str** |  | 
**vat_number** | **str** |  | 
**siret_number** | **str** |  | [optional] 
**siren_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.customer_information_invoice import CustomerInformationInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerInformationInvoice from a JSON string
customer_information_invoice_instance = CustomerInformationInvoice.from_json(json)
# print the JSON string representation of the object
print(CustomerInformationInvoice.to_json())

# convert the object into a dict
customer_information_invoice_dict = customer_information_invoice_instance.to_dict()
# create an instance of CustomerInformationInvoice from a dict
customer_information_invoice_form_dict = customer_information_invoice.from_dict(customer_information_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


