# ImagefaceCompareResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facepp** | [**PydanticMainImagefaceCompareFaceCompareDataClass94559363598576**](PydanticMainImagefaceCompareFaceCompareDataClass94559363598576.md) |  | [optional] 
**var_base64** | [**PydanticMainImagefaceCompareFaceCompareDataClass94559363599520**](PydanticMainImagefaceCompareFaceCompareDataClass94559363599520.md) |  | [optional] 
**amazon** | [**PydanticMainImagefaceCompareFaceCompareDataClass94559363694992**](PydanticMainImagefaceCompareFaceCompareDataClass94559363694992.md) |  | [optional] 

## Example

```python
from openapi_client.models.imageface_compare_response_model import ImagefaceCompareResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ImagefaceCompareResponseModel from a JSON string
imageface_compare_response_model_instance = ImagefaceCompareResponseModel.from_json(json)
# print the JSON string representation of the object
print(ImagefaceCompareResponseModel.to_json())

# convert the object into a dict
imageface_compare_response_model_dict = imageface_compare_response_model_instance.to_dict()
# create an instance of ImagefaceCompareResponseModel from a dict
imageface_compare_response_model_form_dict = imageface_compare_response_model.from_dict(imageface_compare_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


