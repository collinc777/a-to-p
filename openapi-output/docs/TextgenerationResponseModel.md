# TextgenerationResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PydanticMainTextgenerationGenerationDataClass94559368042544**](PydanticMainTextgenerationGenerationDataClass94559368042544.md) |  | [optional] 
**google** | [**PydanticMainTextgenerationGenerationDataClass94559369063440**](PydanticMainTextgenerationGenerationDataClass94559369063440.md) |  | [optional] 
**cohere** | [**PydanticMainTextgenerationGenerationDataClass94559369064384**](PydanticMainTextgenerationGenerationDataClass94559369064384.md) |  | [optional] 
**mistral** | [**PydanticMainTextgenerationGenerationDataClass94559369052128**](PydanticMainTextgenerationGenerationDataClass94559369052128.md) |  | [optional] 
**amazon** | [**PydanticMainTextgenerationGenerationDataClass94559369056400**](PydanticMainTextgenerationGenerationDataClass94559369056400.md) |  | [optional] 
**ai21labs** | [**PydanticMainTextgenerationGenerationDataClass94559369067424**](PydanticMainTextgenerationGenerationDataClass94559369067424.md) |  | [optional] 
**clarifai** | [**PydanticMainTextgenerationGenerationDataClass94559369068368**](PydanticMainTextgenerationGenerationDataClass94559369068368.md) |  | [optional] 
**openai** | [**PydanticMainTextgenerationGenerationDataClass94559369074208**](PydanticMainTextgenerationGenerationDataClass94559369074208.md) |  | [optional] 
**anthropic** | [**PydanticMainTextgenerationGenerationDataClass94559369075152**](PydanticMainTextgenerationGenerationDataClass94559369075152.md) |  | [optional] 

## Example

```python
from openapi_client.models.textgeneration_response_model import TextgenerationResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TextgenerationResponseModel from a JSON string
textgeneration_response_model_instance = TextgenerationResponseModel.from_json(json)
# print the JSON string representation of the object
print(TextgenerationResponseModel.to_json())

# convert the object into a dict
textgeneration_response_model_dict = textgeneration_response_model_instance.to_dict()
# create an instance of TextgenerationResponseModel from a dict
textgeneration_response_model_form_dict = textgeneration_response_model.from_dict(textgeneration_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


