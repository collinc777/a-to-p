# ImageobjectDetectionResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**microsoft** | [**PydanticMainImageobjectDetectionObjectDetectionDataClass94559364505280**](PydanticMainImageobjectDetectionObjectDetectionDataClass94559364505280.md) |  | [optional] 
**google** | [**PydanticMainImageobjectDetectionObjectDetectionDataClass94559364672352**](PydanticMainImageobjectDetectionObjectDetectionDataClass94559364672352.md) |  | [optional] 
**amazon** | [**PydanticMainImageobjectDetectionObjectDetectionDataClass94559363088864**](PydanticMainImageobjectDetectionObjectDetectionDataClass94559363088864.md) |  | [optional] 
**clarifai** | [**PydanticMainImageobjectDetectionObjectDetectionDataClass94559364336912**](PydanticMainImageobjectDetectionObjectDetectionDataClass94559364336912.md) |  | [optional] 
**api4ai** | [**PydanticMainImageobjectDetectionObjectDetectionDataClass94559364500192**](PydanticMainImageobjectDetectionObjectDetectionDataClass94559364500192.md) |  | [optional] 
**sentisight** | [**PydanticMainImageobjectDetectionObjectDetectionDataClass94559359062944**](PydanticMainImageobjectDetectionObjectDetectionDataClass94559359062944.md) |  | [optional] 
**eden_ai** | [**PydanticMainImageobjectDetectionObjectDetectionDataClass94559359068400**](PydanticMainImageobjectDetectionObjectDetectionDataClass94559359068400.md) |  | [optional] 

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


