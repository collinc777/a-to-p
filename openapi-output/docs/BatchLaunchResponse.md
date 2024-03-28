# BatchLaunchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Job ID/name | 
**nb_launched** | **int** | Number of successfully launched requests | 
**nb_failed** | **int** | Number of failed_requests | 
**total** | **int** | Total number of requests sent | 
**failed_requests** | [**List[BatchLaunchFailedRequest]**](BatchLaunchFailedRequest.md) | if any requests failed, they will be shown in this list | 

## Example

```python
from openapi_client.models.batch_launch_response import BatchLaunchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchLaunchResponse from a JSON string
batch_launch_response_instance = BatchLaunchResponse.from_json(json)
# print the JSON string representation of the object
print(BatchLaunchResponse.to_json())

# convert the object into a dict
batch_launch_response_dict = batch_launch_response_instance.to_dict()
# create an instance of BatchLaunchResponse from a dict
batch_launch_response_form_dict = batch_launch_response.from_dict(batch_launch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


