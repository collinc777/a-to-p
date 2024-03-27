# TextcustomClassificationResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cohere** | [**PydanticMainTextcustomClassificationCustomClassificationDataClass94559369113328**](PydanticMainTextcustomClassificationCustomClassificationDataClass94559369113328.md) |  | [optional] 
**openai** | [**PydanticMainTextcustomClassificationCustomClassificationDataClass94559369141744**](PydanticMainTextcustomClassificationCustomClassificationDataClass94559369141744.md) |  | [optional] 

## Example

```python
from openapi_client.models.textcustom_classification_response_model import TextcustomClassificationResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TextcustomClassificationResponseModel from a JSON string
textcustom_classification_response_model_instance = TextcustomClassificationResponseModel.from_json(json)
# print the JSON string representation of the object
print(TextcustomClassificationResponseModel.to_json())

# convert the object into a dict
textcustom_classification_response_model_dict = textcustom_classification_response_model_instance.to_dict()
# create an instance of TextcustomClassificationResponseModel from a dict
textcustom_classification_response_model_form_dict = textcustom_classification_response_model.from_dict(textcustom_classification_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


