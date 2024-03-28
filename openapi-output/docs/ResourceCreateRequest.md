# ResourceCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** |  | 
**data** | **Dict[str, object]** |  | 
**type** | [**TypeEnum**](TypeEnum.md) |  | 
**provider** | **str** |  | 

## Example

```python
from openapi_client.models.resource_create_request import ResourceCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCreateRequest from a JSON string
resource_create_request_instance = ResourceCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ResourceCreateRequest.to_json())

# convert the object into a dict
resource_create_request_dict = resource_create_request_instance.to_dict()
# create an instance of ResourceCreateRequest from a dict
resource_create_request_form_dict = resource_create_request.from_dict(resource_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


