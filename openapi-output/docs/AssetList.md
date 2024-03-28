# AssetList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_resource** | **str** |  | 
**data** | **bytearray** |  | [readonly] 

## Example

```python
from openapi_client.models.asset_list import AssetList

# TODO update the JSON string below
json = "{}"
# create an instance of AssetList from a JSON string
asset_list_instance = AssetList.from_json(json)
# print the JSON string representation of the object
print(AssetList.to_json())

# convert the object into a dict
asset_list_dict = asset_list_instance.to_dict()
# create an instance of AssetList from a dict
asset_list_form_dict = asset_list.from_dict(asset_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


