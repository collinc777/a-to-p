# WorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**content** | **List[Dict[str, object]]** |  | 
**output_node** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.workflow_request import WorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRequest from a JSON string
workflow_request_instance = WorkflowRequest.from_json(json)
# print the JSON string representation of the object
print(WorkflowRequest.to_json())

# convert the object into a dict
workflow_request_dict = workflow_request_instance.to_dict()
# create an instance of WorkflowRequest from a dict
workflow_request_form_dict = workflow_request.from_dict(workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


