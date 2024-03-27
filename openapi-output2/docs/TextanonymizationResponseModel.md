# TextanonymizationResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**microsoft** | [**PydanticMainTextanonymizationAnonymizationDataClass94559364449008**](PydanticMainTextanonymizationAnonymizationDataClass94559364449008.md) |  | [optional] 
**emvista** | [**PydanticMainTextanonymizationAnonymizationDataClass94559363429776**](PydanticMainTextanonymizationAnonymizationDataClass94559363429776.md) |  | [optional] 
**oneai** | [**PydanticMainTextanonymizationAnonymizationDataClass94559368075168**](PydanticMainTextanonymizationAnonymizationDataClass94559368075168.md) |  | [optional] 
**amazon** | [**PydanticMainTextanonymizationAnonymizationDataClass94559369016496**](PydanticMainTextanonymizationAnonymizationDataClass94559369016496.md) |  | [optional] 
**openai** | [**PydanticMainTextanonymizationAnonymizationDataClass94559364272096**](PydanticMainTextanonymizationAnonymizationDataClass94559364272096.md) |  | [optional] 

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


