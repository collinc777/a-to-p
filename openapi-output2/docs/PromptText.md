# PromptText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [readonly] 
**text** | **str** |  | 
**feature** | **str** |  | 
**subfeature** | **str** |  | 
**provider** | **str** |  | 
**model** | **str** |  | [optional] 
**params** | **Dict[str, object]** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from openapi_client.models.prompt_text import PromptText

# TODO update the JSON string below
json = "{}"
# create an instance of PromptText from a JSON string
prompt_text_instance = PromptText.from_json(json)
# print the JSON string representation of the object
print(PromptText.to_json())

# convert the object into a dict
prompt_text_dict = prompt_text_instance.to_dict()
# create an instance of PromptText from a dict
prompt_text_form_dict = prompt_text.from_dict(prompt_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


