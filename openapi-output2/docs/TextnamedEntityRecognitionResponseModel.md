# TextnamedEntityRecognitionResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenstorrent** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368908400**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368908400.md) |  | [optional] 
**microsoft** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368911920**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368911920.md) |  | [optional] 
**ibm** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368915088**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368915088.md) |  | [optional] 
**google** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368893296**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368893296.md) |  | [optional] 
**oneai** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368894240**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368894240.md) |  | [optional] 
**amazon** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368937232**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368937232.md) |  | [optional] 
**neuralspace** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368921984**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368921984.md) |  | [optional] 
**lettria** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368925152**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368925152.md) |  | [optional] 
**nlpcloud** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368898224**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368898224.md) |  | [optional] 
**openai** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368902528**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368902528.md) |  | [optional] 
**eden_ai** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368943056**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368943056.md) |  | [optional] 

## Example

```python
from openapi_client.models.textnamed_entity_recognition_response_model import TextnamedEntityRecognitionResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TextnamedEntityRecognitionResponseModel from a JSON string
textnamed_entity_recognition_response_model_instance = TextnamedEntityRecognitionResponseModel.from_json(json)
# print the JSON string representation of the object
print(TextnamedEntityRecognitionResponseModel.to_json())

# convert the object into a dict
textnamed_entity_recognition_response_model_dict = textnamed_entity_recognition_response_model_instance.to_dict()
# create an instance of TextnamedEntityRecognitionResponseModel from a dict
textnamed_entity_recognition_response_model_form_dict = textnamed_entity_recognition_response_model.from_dict(textnamed_entity_recognition_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


