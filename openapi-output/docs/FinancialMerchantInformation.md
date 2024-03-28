# FinancialMerchantInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the merchant. | [optional] 
**address** | **str** | Address of the merchant. | [optional] 
**phone** | **str** | Phone number of the merchant. | [optional] 
**tax_id** | **str** | Tax identification number of the merchant. | [optional] 
**id_reference** | **str** | Unique reference ID for the merchant. | [optional] 
**vat_number** | **str** | VAT (Value Added Tax) number of the merchant. | [optional] 
**abn_number** | **str** | ABN (Australian Business Number) of the merchant. | [optional] 
**gst_number** | **str** | GST (Goods and Services Tax) number of the merchant. | [optional] 
**business_number** | **str** | Business registration number of the merchant. | [optional] 
**siret_number** | **str** | SIRET (Système d&#39;Identification du Répertoire des Entreprises et de leurs Établissements) number of the merchant. | [optional] 
**siren_number** | **str** | SIREN (Système d&#39;Identification du Répertoire des Entreprises) number of the merchant. | [optional] 
**pan_number** | **str** | PAN (Permanent Account Number) of the merchant. | [optional] 
**coc_number** | **str** | Chamber of Commerce registration number of the merchant. | [optional] 
**fiscal_number** | **str** | Fiscal identification number of the merchant. | [optional] 
**email** | **str** | Email address of the merchant. | [optional] 
**fax** | **str** | Fax number of the merchant. | [optional] 
**website** | **str** | Website of the merchant. | [optional] 
**registration** | **str** | Official registration information of the merchant. | [optional] 
**city** | **str** | City associated with the merchant&#39;s address. | [optional] 
**country** | **str** | Country associated with the merchant&#39;s address. | [optional] 
**house_number** | **str** | House number associated with the merchant&#39;s address. | [optional] 
**province** | **str** | Province associated with the merchant&#39;s address. | [optional] 
**street_name** | **str** | Street name associated with the merchant&#39;s address. | [optional] 
**zip_code** | **str** | ZIP code associated with the merchant&#39;s address. | [optional] 
**country_code** | **str** | Country code associated with the merchant&#39;s location. | [optional] 

## Example

```python
from openapi_client.models.financial_merchant_information import FinancialMerchantInformation

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialMerchantInformation from a JSON string
financial_merchant_information_instance = FinancialMerchantInformation.from_json(json)
# print the JSON string representation of the object
print(FinancialMerchantInformation.to_json())

# convert the object into a dict
financial_merchant_information_dict = financial_merchant_information_instance.to_dict()
# create an instance of FinancialMerchantInformation from a dict
financial_merchant_information_form_dict = financial_merchant_information.from_dict(financial_merchant_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


