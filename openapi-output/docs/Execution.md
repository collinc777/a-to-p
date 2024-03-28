# Execution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**content** | **Dict[str, object]** |  | 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from openapi_client.models.execution import Execution

# TODO update the JSON string below
json = "{}"
# create an instance of Execution from a JSON string
execution_instance = Execution.from_json(json)
# print the JSON string representation of the object
print(Execution.to_json())

# convert the object into a dict
execution_dict = execution_instance.to_dict()
# create an instance of Execution from a dict
execution_form_dict = execution.from_dict(execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


