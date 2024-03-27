# PatchedWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**content** | **List[Dict[str, object]]** |  | [optional] 
**output_node** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.patched_workflow_request import PatchedWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedWorkflowRequest from a JSON string
patched_workflow_request_instance = PatchedWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedWorkflowRequest.to_json())

# convert the object into a dict
patched_workflow_request_dict = patched_workflow_request_instance.to_dict()
# create an instance of PatchedWorkflowRequest from a dict
patched_workflow_request_form_dict = patched_workflow_request.from_dict(patched_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


