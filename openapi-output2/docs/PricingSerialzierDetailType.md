# PricingSerialzierDetailType

(Optional) type of extra value, MUST be the same name as the feature parameter name. eg: resolution  * `resolution` - Resolution * `document_type` - Document Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openapi_client.models.pricing_serialzier_detail_type import PricingSerialzierDetailType

# TODO update the JSON string below
json = "{}"
# create an instance of PricingSerialzierDetailType from a JSON string
pricing_serialzier_detail_type_instance = PricingSerialzierDetailType.from_json(json)
# print the JSON string representation of the object
print(PricingSerialzierDetailType.to_json())

# convert the object into a dict
pricing_serialzier_detail_type_dict = pricing_serialzier_detail_type_instance.to_dict()
# create an instance of PricingSerialzierDetailType from a dict
pricing_serialzier_detail_type_form_dict = pricing_serialzier_detail_type.from_dict(pricing_serialzier_detail_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


