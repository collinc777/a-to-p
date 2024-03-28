# TextmoderationResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openai** | [**PydanticMainTextmoderationModerationDataClass94559368951360**](PydanticMainTextmoderationModerationDataClass94559368951360.md) |  | [optional] 
**microsoft** | [**PydanticMainTextmoderationModerationDataClass94559368980912**](PydanticMainTextmoderationModerationDataClass94559368980912.md) |  | [optional] 
**clarifai** | [**PydanticMainTextmoderationModerationDataClass94559368971952**](PydanticMainTextmoderationModerationDataClass94559368971952.md) |  | [optional] 
**google** | [**PydanticMainTextmoderationModerationDataClass94559368916096**](PydanticMainTextmoderationModerationDataClass94559368916096.md) |  | [optional] 

## Example

```python
from openapi_client.models.textmoderation_response_model import TextmoderationResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TextmoderationResponseModel from a JSON string
textmoderation_response_model_instance = TextmoderationResponseModel.from_json(json)
# print the JSON string representation of the object
print(TextmoderationResponseModel.to_json())

# convert the object into a dict
textmoderation_response_model_dict = textmoderation_response_model_instance.to_dict()
# create an instance of TextmoderationResponseModel from a dict
textmoderation_response_model_form_dict = textmoderation_response_model.from_dict(textmoderation_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


