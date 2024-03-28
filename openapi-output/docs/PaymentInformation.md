# PaymentInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_type** | **str** |  | [optional] 
**card_number** | **str** |  | [optional] 
**cash** | **str** |  | [optional] 
**tip** | **str** |  | [optional] 
**discount** | **str** |  | [optional] 
**change** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_information import PaymentInformation

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentInformation from a JSON string
payment_information_instance = PaymentInformation.from_json(json)
# print the JSON string representation of the object
print(PaymentInformation.to_json())

# convert the object into a dict
payment_information_dict = payment_information_instance.to_dict()
# create an instance of PaymentInformation from a dict
payment_information_form_dict = payment_information.from_dict(payment_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


