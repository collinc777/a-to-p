# FinancialCustomerInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the invoiced customer. | [optional] 
**id_reference** | **str** | Unique reference ID for the customer. | [optional] 
**mailling_address** | **str** | The mailing address of the customer. | [optional] 
**billing_address** | **str** | The explicit billing address for the customer. | [optional] 
**shipping_address** | **str** | The shipping address for the customer. | [optional] 
**service_address** | **str** | The service address associated with the customer. | [optional] 
**remittance_address** | **str** | The address to which payments should be remitted. | [optional] 
**email** | **str** | The email address of the customer. | [optional] 
**phone** | **str** | The phone number associated with the customer. | [optional] 
**vat_number** | **str** | VAT (Value Added Tax) number of the customer. | [optional] 
**abn_number** | **str** | ABN (Australian Business Number) of the customer. | [optional] 
**gst_number** | **str** | GST (Goods and Services Tax) number of the customer. | [optional] 
**pan_number** | **str** | PAN (Permanent Account Number) of the customer. | [optional] 
**business_number** | **str** | Business registration number of the customer. | [optional] 
**siret_number** | **str** | SIRET (Système d&#39;Identification du Répertoire des Entreprises et de leurs Établissements) number of the customer. | [optional] 
**siren_number** | **str** | SIREN (Système d&#39;Identification du Répertoire des Entreprises) number of the customer. | [optional] 
**customer_number** | **str** | Customer identification number. | [optional] 
**coc_number** | **str** | Chamber of Commerce registration number. | [optional] 
**fiscal_number** | **str** | Fiscal identification number of the customer. | [optional] 
**registration_number** | **str** | Official registration number of the customer. | [optional] 
**tax_id** | **str** | Tax identification number of the customer. | [optional] 
**website** | **str** | The website associated with the customer. | [optional] 
**remit_to_name** | **str** | The name associated with the customer&#39;s remittance address. | [optional] 
**city** | **str** | The city associated with the customer&#39;s address. | [optional] 
**country** | **str** | The country associated with the customer&#39;s address. | [optional] 
**house_number** | **str** | The house number associated with the customer&#39;s address. | [optional] 
**province** | **str** | The province associated with the customer&#39;s address. | [optional] 
**street_name** | **str** | The street name associated with the customer&#39;s address. | [optional] 
**zip_code** | **str** | The ZIP code associated with the customer&#39;s address. | [optional] 
**municipality** | **str** | The municipality associated with the customer&#39;s address. | [optional] 

## Example

```python
from openapi_client.models.financial_customer_information import FinancialCustomerInformation

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialCustomerInformation from a JSON string
financial_customer_information_instance = FinancialCustomerInformation.from_json(json)
# print the JSON string representation of the object
print(FinancialCustomerInformation.to_json())

# convert the object into a dict
financial_customer_information_dict = financial_customer_information_instance.to_dict()
# create an instance of FinancialCustomerInformation from a dict
financial_customer_information_form_dict = financial_customer_information.from_dict(financial_customer_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


