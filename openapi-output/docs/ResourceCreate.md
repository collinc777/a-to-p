# ResourceCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** |  | 
**data** | **Dict[str, object]** |  | 
**type** | [**TypeEnum**](TypeEnum.md) |  | 
**provider** | **str** |  | 

## Example

```python
from openapi_client.models.resource_create import ResourceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCreate from a JSON string
resource_create_instance = ResourceCreate.from_json(json)
# print the JSON string representation of the object
print(ResourceCreate.to_json())

# convert the object into a dict
resource_create_dict = resource_create_instance.to_dict()
# create an instance of ResourceCreate from a dict
resource_create_form_dict = resource_create.from_dict(resource_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


