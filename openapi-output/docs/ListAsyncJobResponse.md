# ListAsyncJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[AsyncJobList]**](AsyncJobList.md) |  | 

## Example

```python
from openapi_client.models.list_async_job_response import ListAsyncJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAsyncJobResponse from a JSON string
list_async_job_response_instance = ListAsyncJobResponse.from_json(json)
# print the JSON string representation of the object
print(ListAsyncJobResponse.to_json())

# convert the object into a dict
list_async_job_response_dict = list_async_job_response_instance.to_dict()
# create an instance of ListAsyncJobResponse from a dict
list_async_job_response_form_dict = list_async_job_response.from_dict(list_async_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


