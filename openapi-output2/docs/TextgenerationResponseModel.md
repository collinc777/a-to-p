# TextgenerationResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**PydanticMainTextgenerationGenerationDataClass94559369073472**](PydanticMainTextgenerationGenerationDataClass94559369073472.md) |  | [optional] 
**google** | [**PydanticMainTextgenerationGenerationDataClass94559369074416**](PydanticMainTextgenerationGenerationDataClass94559369074416.md) |  | [optional] 
**cohere** | [**PydanticMainTextgenerationGenerationDataClass94559369053024**](PydanticMainTextgenerationGenerationDataClass94559369053024.md) |  | [optional] 
**mistral** | [**PydanticMainTextgenerationGenerationDataClass94559369053968**](PydanticMainTextgenerationGenerationDataClass94559369053968.md) |  | [optional] 
**amazon** | [**PydanticMainTextgenerationGenerationDataClass94559369055456**](PydanticMainTextgenerationGenerationDataClass94559369055456.md) |  | [optional] 
**ai21labs** | [**PydanticMainTextgenerationGenerationDataClass94559369058896**](PydanticMainTextgenerationGenerationDataClass94559369058896.md) |  | [optional] 
**clarifai** | [**PydanticMainTextgenerationGenerationDataClass94559369066432**](PydanticMainTextgenerationGenerationDataClass94559369066432.md) |  | [optional] 
**openai** | [**PydanticMainTextgenerationGenerationDataClass94559369067376**](PydanticMainTextgenerationGenerationDataClass94559369067376.md) |  | [optional] 
**anthropic** | [**PydanticMainTextgenerationGenerationDataClass94559369078400**](PydanticMainTextgenerationGenerationDataClass94559369078400.md) |  | [optional] 

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


