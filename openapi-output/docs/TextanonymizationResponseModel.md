# TextanonymizationResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**microsoft** | [**PydanticMainTextanonymizationAnonymizationDataClass94559364102208**](PydanticMainTextanonymizationAnonymizationDataClass94559364102208.md) |  | [optional] 
**emvista** | [**PydanticMainTextanonymizationAnonymizationDataClass94559364103152**](PydanticMainTextanonymizationAnonymizationDataClass94559364103152.md) |  | [optional] 
**oneai** | [**PydanticMainTextanonymizationAnonymizationDataClass94559368088560**](PydanticMainTextanonymizationAnonymizationDataClass94559368088560.md) |  | [optional] 
**amazon** | [**PydanticMainTextanonymizationAnonymizationDataClass94559369000928**](PydanticMainTextanonymizationAnonymizationDataClass94559369000928.md) |  | [optional] 
**openai** | [**PydanticMainTextanonymizationAnonymizationDataClass94559369024192**](PydanticMainTextanonymizationAnonymizationDataClass94559369024192.md) |  | [optional] 

## Example

```python
from openapi_client.models.textanonymization_response_model import TextanonymizationResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TextanonymizationResponseModel from a JSON string
textanonymization_response_model_instance = TextanonymizationResponseModel.from_json(json)
# print the JSON string representation of the object
print(TextanonymizationResponseModel.to_json())

# convert the object into a dict
textanonymization_response_model_dict = textanonymization_response_model_instance.to_dict()
# create an instance of TextanonymizationResponseModel from a dict
textanonymization_response_model_form_dict = textanonymization_response_model.from_dict(textanonymization_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


