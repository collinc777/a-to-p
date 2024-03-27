# AssetUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_resource** | **str** |  | 
**data** | **Dict[str, object]** |  | 

## Example

```python
from openapi_client.models.asset_update_request import AssetUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssetUpdateRequest from a JSON string
asset_update_request_instance = AssetUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AssetUpdateRequest.to_json())

# convert the object into a dict
asset_update_request_dict = asset_update_request_instance.to_dict()
# create an instance of AssetUpdateRequest from a dict
asset_update_request_form_dict = asset_update_request.from_dict(asset_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


