# PatchedPromptTextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**feature** | **str** |  | [optional] 
**subfeature** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**params** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openapi_client.models.patched_prompt_text_request import PatchedPromptTextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPromptTextRequest from a JSON string
patched_prompt_text_request_instance = PatchedPromptTextRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedPromptTextRequest.to_json())

# convert the object into a dict
patched_prompt_text_request_dict = patched_prompt_text_request_instance.to_dict()
# create an instance of PatchedPromptTextRequest from a dict
patched_prompt_text_request_form_dict = patched_prompt_text_request.from_dict(patched_prompt_text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


