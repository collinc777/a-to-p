# ImageobjectDetectionResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**microsoft** | [**PydanticMainImageobjectDetectionObjectDetectionDataClass94559356777168**](PydanticMainImageobjectDetectionObjectDetectionDataClass94559356777168.md) |  | [optional] 
**google** | [**PydanticMainImageobjectDetectionObjectDetectionDataClass94559364798448**](PydanticMainImageobjectDetectionObjectDetectionDataClass94559364798448.md) |  | [optional] 
**amazon** | [**PydanticMainImageobjectDetectionObjectDetectionDataClass94559359158000**](PydanticMainImageobjectDetectionObjectDetectionDataClass94559359158000.md) |  | [optional] 
**clarifai** | [**PydanticMainImageobjectDetectionObjectDetectionDataClass94559364766336**](PydanticMainImageobjectDetectionObjectDetectionDataClass94559364766336.md) |  | [optional] 
**api4ai** | [**PydanticMainImageobjectDetectionObjectDetectionDataClass94559364464608**](PydanticMainImageobjectDetectionObjectDetectionDataClass94559364464608.md) |  | [optional] 
**sentisight** | [**PydanticMainImageobjectDetectionObjectDetectionDataClass94559364476928**](PydanticMainImageobjectDetectionObjectDetectionDataClass94559364476928.md) |  | [optional] 
**eden_ai** | [**PydanticMainImageobjectDetectionObjectDetectionDataClass94559364877712**](PydanticMainImageobjectDetectionObjectDetectionDataClass94559364877712.md) |  | [optional] 

## Example

```python
from openapi_client.models.imageobject_detection_response_model import ImageobjectDetectionResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ImageobjectDetectionResponseModel from a JSON string
imageobject_detection_response_model_instance = ImageobjectDetectionResponseModel.from_json(json)
# print the JSON string representation of the object
print(ImageobjectDetectionResponseModel.to_json())

# convert the object into a dict
imageobject_detection_response_model_dict = imageobject_detection_response_model_instance.to_dict()
# create an instance of ImageobjectDetectionResponseModel from a dict
imageobject_detection_response_model_form_dict = imageobject_detection_response_model.from_dict(imageobject_detection_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


