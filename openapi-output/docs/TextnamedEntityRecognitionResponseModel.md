# TextnamedEntityRecognitionResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenstorrent** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368887920**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368887920.md) |  | [optional] 
**microsoft** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368907376**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368907376.md) |  | [optional] 
**ibm** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368935904**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368935904.md) |  | [optional] 
**google** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368892832**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368892832.md) |  | [optional] 
**oneai** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368897200**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368897200.md) |  | [optional] 
**amazon** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368900368**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368900368.md) |  | [optional] 
**neuralspace** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368903536**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368903536.md) |  | [optional] 
**lettria** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368920912**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368920912.md) |  | [optional] 
**nlpcloud** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368925216**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368925216.md) |  | [optional] 
**openai** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368929520**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368929520.md) |  | [optional] 
**eden_ai** | [**PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368942032**](PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368942032.md) |  | [optional] 

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


