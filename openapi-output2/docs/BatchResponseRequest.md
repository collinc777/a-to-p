# BatchResponseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_id** | **int** |  | [readonly] 
**status** | [**StatusE80Enum**](StatusE80Enum.md) |  | [optional] 
**name** | **str** |  | [optional] 
**errors** | **Dict[str, object]** |  | [optional] 
**response** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openapi_client.models.batch_response_request import BatchResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchResponseRequest from a JSON string
batch_response_request_instance = BatchResponseRequest.from_json(json)
# print the JSON string representation of the object
print(BatchResponseRequest.to_json())

# convert the object into a dict
batch_response_request_dict = batch_response_request_instance.to_dict()
# create an instance of BatchResponseRequest from a dict
batch_response_request_form_dict = batch_response_request.from_dict(batch_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


