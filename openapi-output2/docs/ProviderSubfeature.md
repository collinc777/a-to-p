# ProviderSubfeature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [readonly] 
**version** | **str** |  | [readonly] 
**pricings** | [**List[PricingSerialzier]**](PricingSerialzier.md) |  | 
**is_working** | **bool** |  | [optional] 
**description_title** | **str** |  | [optional] 
**description_content** | **str** |  | [optional] 
**provider** | [**Provider**](Provider.md) |  | 
**feature** | [**Feature**](Feature.md) |  | 
**subfeature** | [**Subfeature**](Subfeature.md) |  | 
**constraints** | **Dict[str, object]** |  | [readonly] 
**models** | **Dict[str, object]** |  | [readonly] 
**languages** | [**List[ProviderSubfeatureLanguagesInner]**](ProviderSubfeatureLanguagesInner.md) |  | [readonly] 
**phase** | **str** |  | [readonly] 

## Example

```python
from openapi_client.models.provider_subfeature import ProviderSubfeature

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderSubfeature from a JSON string
provider_subfeature_instance = ProviderSubfeature.from_json(json)
# print the JSON string representation of the object
print(ProviderSubfeature.to_json())

# convert the object into a dict
provider_subfeature_dict = provider_subfeature_instance.to_dict()
# create an instance of ProviderSubfeature from a dict
provider_subfeature_form_dict = provider_subfeature.from_dict(provider_subfeature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


