# ImagebackgroundRemovalResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**photoroom** | [**PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363754048**](PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363754048.md) |  | [optional] 
**microsoft** | [**PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363754992**](PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363754992.md) |  | [optional] 
**stabilityai** | [**PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363671792**](PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363671792.md) |  | [optional] 
**api4ai** | [**PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363759392**](PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363759392.md) |  | [optional] 
**sentisight** | [**PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363760880**](PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363760880.md) |  | [optional] 

## Example

```python
from openapi_client.models.imagebackground_removal_response_model import ImagebackgroundRemovalResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ImagebackgroundRemovalResponseModel from a JSON string
imagebackground_removal_response_model_instance = ImagebackgroundRemovalResponseModel.from_json(json)
# print the JSON string representation of the object
print(ImagebackgroundRemovalResponseModel.to_json())

# convert the object into a dict
imagebackground_removal_response_model_dict = imagebackground_removal_response_model_instance.to_dict()
# create an instance of ImagebackgroundRemovalResponseModel from a dict
imagebackground_removal_response_model_form_dict = imagebackground_removal_response_model.from_dict(imagebackground_removal_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


