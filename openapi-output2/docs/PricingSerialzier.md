# PricingSerialzier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_name** | **str** | Model name, default to &#39;default&#39; if no models to chose from | [optional] 
**price** | **decimal.Decimal** |  | [optional] 
**price_unit_quantity** | **int** |  | [optional] 
**min_price_quantity** | **int** |  | [optional] 
**price_unit_type** | [**PriceUnitTypeEnum**](PriceUnitTypeEnum.md) |  | [optional] 
**detail_type** | [**PricingSerialzierDetailType**](PricingSerialzierDetailType.md) |  | [optional] 
**detail_value** | **str** | (Optional) extra value for detailed pricing, eg: 250x250 for resolution | [optional] 
**get_detail_type_display** | **str** |  | [readonly] 
**is_post_call** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.pricing_serialzier import PricingSerialzier

# TODO update the JSON string below
json = "{}"
# create an instance of PricingSerialzier from a JSON string
pricing_serialzier_instance = PricingSerialzier.from_json(json)
# print the JSON string representation of the object
print(PricingSerialzier.to_json())

# convert the object into a dict
pricing_serialzier_dict = pricing_serialzier_instance.to_dict()
# create an instance of PricingSerialzier from a dict
pricing_serialzier_form_dict = pricing_serialzier.from_dict(pricing_serialzier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


