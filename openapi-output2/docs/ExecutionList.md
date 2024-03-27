# ExecutionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from openapi_client.models.execution_list import ExecutionList

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionList from a JSON string
execution_list_instance = ExecutionList.from_json(json)
# print the JSON string representation of the object
print(ExecutionList.to_json())

# convert the object into a dict
execution_list_dict = execution_list_instance.to_dict()
# create an instance of ExecutionList from a dict
execution_list_form_dict = execution_list.from_dict(execution_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


