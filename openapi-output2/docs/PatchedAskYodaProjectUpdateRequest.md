# PatchedAskYodaProjectUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ocr_provider** | **str** |  | [optional] 
**speech_to_text_provider** | **str** |  | [optional] 
**llm_provider** | **str** | Select a default LLM provider to use in your project. | [optional] 
**llm_model** | **str** | Select a default Model for LLM provider to use in your project | [optional] 
**chunk_size** | **int** |  | [optional] 
**chunk_separators** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.patched_ask_yoda_project_update_request import PatchedAskYodaProjectUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAskYodaProjectUpdateRequest from a JSON string
patched_ask_yoda_project_update_request_instance = PatchedAskYodaProjectUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedAskYodaProjectUpdateRequest.to_json())

# convert the object into a dict
patched_ask_yoda_project_update_request_dict = patched_ask_yoda_project_update_request_instance.to_dict()
# create an instance of PatchedAskYodaProjectUpdateRequest from a dict
patched_ask_yoda_project_update_request_form_dict = patched_ask_yoda_project_update_request.from_dict(patched_ask_yoda_project_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


