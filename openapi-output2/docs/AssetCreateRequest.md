# AssetCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_resource** | **str** |  | 
**data** | **Dict[str, object]** |  | 

## Example

```python
from openapi_client.models.asset_create_request import AssetCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssetCreateRequest from a JSON string
asset_create_request_instance = AssetCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AssetCreateRequest.to_json())

# convert the object into a dict
asset_create_request_dict = asset_create_request_instance.to_dict()
# create an instance of AssetCreateRequest from a dict
asset_create_request_form_dict = asset_create_request.from_dict(asset_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


