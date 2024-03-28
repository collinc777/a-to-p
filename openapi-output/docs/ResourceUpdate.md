# ResourceUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** |  | 
**data** | **Dict[str, object]** |  | 
**type** | [**TypeEnum**](TypeEnum.md) |  | 
**provider** | **str** |  | 
**assets** | [**List[AssetList]**](AssetList.md) |  | [readonly] 

## Example

```python
from openapi_client.models.resource_update import ResourceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceUpdate from a JSON string
resource_update_instance = ResourceUpdate.from_json(json)
# print the JSON string representation of the object
print(ResourceUpdate.to_json())

# convert the object into a dict
resource_update_dict = resource_update_instance.to_dict()
# create an instance of ResourceUpdate from a dict
resource_update_form_dict = resource_update.from_dict(resource_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


