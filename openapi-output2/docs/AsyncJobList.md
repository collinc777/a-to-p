# AsyncJobList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | **str** |  | 
**nb** | **int** |  | 
**nb_ok** | **int** |  | 
**public_id** | **str** |  | 
**state** | [**StateEnum**](StateEnum.md) |  | 
**created_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.async_job_list import AsyncJobList

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncJobList from a JSON string
async_job_list_instance = AsyncJobList.from_json(json)
# print the JSON string representation of the object
print(AsyncJobList.to_json())

# convert the object into a dict
async_job_list_dict = async_job_list_instance.to_dict()
# create an instance of AsyncJobList from a dict
async_job_list_form_dict = async_job_list.from_dict(async_job_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


