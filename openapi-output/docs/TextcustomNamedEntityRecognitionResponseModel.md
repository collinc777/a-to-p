# TextcustomNamedEntityRecognitionResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cohere** | [**PydanticMainTextcustomNamedEntityRecognitionCustomNamedEntityRecognitionDataClass94559368332544**](PydanticMainTextcustomNamedEntityRecognitionCustomNamedEntityRecognitionDataClass94559368332544.md) |  | [optional] 
**openai** | [**PydanticMainTextcustomNamedEntityRecognitionCustomNamedEntityRecognitionDataClass94559368333488**](PydanticMainTextcustomNamedEntityRecognitionCustomNamedEntityRecognitionDataClass94559368333488.md) |  | [optional] 
**eden_ai** | [**PydanticMainTextcustomNamedEntityRecognitionCustomNamedEntityRecognitionDataClass94559369096592**](PydanticMainTextcustomNamedEntityRecognitionCustomNamedEntityRecognitionDataClass94559369096592.md) |  | [optional] 

## Example

```python
from openapi_client.models.textcustom_named_entity_recognition_response_model import TextcustomNamedEntityRecognitionResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TextcustomNamedEntityRecognitionResponseModel from a JSON string
textcustom_named_entity_recognition_response_model_instance = TextcustomNamedEntityRecognitionResponseModel.from_json(json)
# print the JSON string representation of the object
print(TextcustomNamedEntityRecognitionResponseModel.to_json())

# convert the object into a dict
textcustom_named_entity_recognition_response_model_dict = textcustom_named_entity_recognition_response_model_instance.to_dict()
# create an instance of TextcustomNamedEntityRecognitionResponseModel from a dict
textcustom_named_entity_recognition_response_model_form_dict = textcustom_named_entity_recognition_response_model.from_dict(textcustom_named_entity_recognition_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


