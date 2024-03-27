# ImagebackgroundRemovalResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**photoroom** | [**PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363679264**](PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363679264.md) |  | [optional] 
**microsoft** | [**PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363759872**](PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363759872.md) |  | [optional] 
**stabilityai** | [**PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363761360**](PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363761360.md) |  | [optional] 
**api4ai** | [**PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363772656**](PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363772656.md) |  | [optional] 
**sentisight** | [**PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363769888**](PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363769888.md) |  | [optional] 

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


