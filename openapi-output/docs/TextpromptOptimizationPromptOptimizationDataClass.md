# TextpromptOptimizationPromptOptimizationDataClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**missing_information** | **str** |  | 
**items** | [**List[PromptDataClass]**](PromptDataClass.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**status** | [**StatusF43Enum**](StatusF43Enum.md) |  | 

## Example

```python
from openapi_client.models.textprompt_optimization_prompt_optimization_data_class import TextpromptOptimizationPromptOptimizationDataClass

# TODO update the JSON string below
json = "{}"
# create an instance of TextpromptOptimizationPromptOptimizationDataClass from a JSON string
textprompt_optimization_prompt_optimization_data_class_instance = TextpromptOptimizationPromptOptimizationDataClass.from_json(json)
# print the JSON string representation of the object
print(TextpromptOptimizationPromptOptimizationDataClass.to_json())

# convert the object into a dict
textprompt_optimization_prompt_optimization_data_class_dict = textprompt_optimization_prompt_optimization_data_class_instance.to_dict()
# create an instance of TextpromptOptimizationPromptOptimizationDataClass from a dict
textprompt_optimization_prompt_optimization_data_class_form_dict = textprompt_optimization_prompt_optimization_data_class.from_dict(textprompt_optimization_prompt_optimization_data_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


