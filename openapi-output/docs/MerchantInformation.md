# MerchantInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_name** | **str** |  | [optional] 
**merchant_address** | **str** |  | [optional] 
**merchant_phone** | **str** |  | [optional] 
**merchant_url** | **str** |  | [optional] 
**merchant_siret** | **str** |  | [optional] 
**merchant_siren** | **str** |  | [optional] 
**merchant_vat_number** | **str** |  | [optional] 
**merchant_gst_number** | **str** |  | [optional] 
**merchant_abn_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.merchant_information import MerchantInformation

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantInformation from a JSON string
merchant_information_instance = MerchantInformation.from_json(json)
# print the JSON string representation of the object
print(MerchantInformation.to_json())

# convert the object into a dict
merchant_information_dict = merchant_information_instance.to_dict()
# create an instance of MerchantInformation from a dict
merchant_information_form_dict = merchant_information.from_dict(merchant_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


