# AssetCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_resource** | **str** |  | 
**data** | **Dict[str, object]** |  | 

## Example

```python
from openapi_client.models.asset_create import AssetCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AssetCreate from a JSON string
asset_create_instance = AssetCreate.from_json(json)
# print the JSON string representation of the object
print(AssetCreate.to_json())

# convert the object into a dict
asset_create_dict = asset_create_instance.to_dict()
# create an instance of AssetCreate from a dict
asset_create_form_dict = asset_create.from_dict(asset_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


