# Subfeature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**fullname** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.subfeature import Subfeature

# TODO update the JSON string below
json = "{}"
# create an instance of Subfeature from a JSON string
subfeature_instance = Subfeature.from_json(json)
# print the JSON string representation of the object
print(Subfeature.to_json())

# convert the object into a dict
subfeature_dict = subfeature_instance.to_dict()
# create an instance of Subfeature from a dict
subfeature_form_dict = subfeature.from_dict(subfeature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


