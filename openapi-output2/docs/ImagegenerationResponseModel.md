# ImagegenerationResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replicate** | [**PydanticMainImagegenerationGenerationDataClass94559363653728**](PydanticMainImagegenerationGenerationDataClass94559363653728.md) |  | [optional] 
**deepai** | [**PydanticMainImagegenerationGenerationDataClass94559363665200**](PydanticMainImagegenerationGenerationDataClass94559363665200.md) |  | [optional] 
**amazon** | [**PydanticMainImagegenerationGenerationDataClass94559363668368**](PydanticMainImagegenerationGenerationDataClass94559363668368.md) |  | [optional] 
**stabilityai** | [**PydanticMainImagegenerationGenerationDataClass94559363672672**](PydanticMainImagegenerationGenerationDataClass94559363672672.md) |  | [optional] 
**openai** | [**PydanticMainImagegenerationGenerationDataClass94559363683680**](PydanticMainImagegenerationGenerationDataClass94559363683680.md) |  | [optional] 

## Example

```python
from openapi_client.models.imagegeneration_response_model import ImagegenerationResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ImagegenerationResponseModel from a JSON string
imagegeneration_response_model_instance = ImagegenerationResponseModel.from_json(json)
# print the JSON string representation of the object
print(ImagegenerationResponseModel.to_json())

# convert the object into a dict
imagegeneration_response_model_dict = imagegeneration_response_model_instance.to_dict()
# create an instance of ImagegenerationResponseModel from a dict
imagegeneration_response_model_form_dict = imagegeneration_response_model.from_dict(imagegeneration_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


