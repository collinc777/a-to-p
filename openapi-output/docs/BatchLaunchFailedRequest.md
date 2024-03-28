# BatchLaunchFailedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Request name, if any were given | 
**public_id** | **int** | Request ID | 
**body** | **object** | Parameters passed to the request | 
**errors** | **object** | Error received from the request validator | 

## Example

```python
from openapi_client.models.batch_launch_failed_request import BatchLaunchFailedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchLaunchFailedRequest from a JSON string
batch_launch_failed_request_instance = BatchLaunchFailedRequest.from_json(json)
# print the JSON string representation of the object
print(BatchLaunchFailedRequest.to_json())

# convert the object into a dict
batch_launch_failed_request_dict = batch_launch_failed_request_instance.to_dict()
# create an instance of BatchLaunchFailedRequest from a dict
batch_launch_failed_request_form_dict = batch_launch_failed_request.from_dict(batch_launch_failed_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


