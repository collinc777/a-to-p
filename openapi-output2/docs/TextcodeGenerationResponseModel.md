# TextcodeGenerationResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nlpcloud** | [**PydanticMainTextcodeGenerationCodeGenerationDataClass94559368318992**](PydanticMainTextcodeGenerationCodeGenerationDataClass94559368318992.md) |  | [optional] 
**openai** | [**PydanticMainTextcodeGenerationCodeGenerationDataClass94559369110016**](PydanticMainTextcodeGenerationCodeGenerationDataClass94559369110016.md) |  | [optional] 
**google** | [**PydanticMainTextcodeGenerationCodeGenerationDataClass94559369042624**](PydanticMainTextcodeGenerationCodeGenerationDataClass94559369042624.md) |  | [optional] 

## Example

```python
from openapi_client.models.textcode_generation_response_model import TextcodeGenerationResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TextcodeGenerationResponseModel from a JSON string
textcode_generation_response_model_instance = TextcodeGenerationResponseModel.from_json(json)
# print the JSON string representation of the object
print(TextcodeGenerationResponseModel.to_json())

# convert the object into a dict
textcode_generation_response_model_dict = textcode_generation_response_model_instance.to_dict()
# create an instance of TextcodeGenerationResponseModel from a dict
textcode_generation_response_model_form_dict = textcode_generation_response_model.from_dict(textcode_generation_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


