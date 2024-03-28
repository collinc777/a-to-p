# ImagefaceRecognitionResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facepp** | [**PydanticMainImagefaceRecognitionFaceRecognitionAddFaceDataClass94559363584320**](PydanticMainImagefaceRecognitionFaceRecognitionAddFaceDataClass94559363584320.md) |  | [optional] 
**amazon** | [**PydanticMainImagefaceRecognitionFaceRecognitionAddFaceDataClass94559363586448**](PydanticMainImagefaceRecognitionFaceRecognitionAddFaceDataClass94559363586448.md) |  | [optional] 
**microsoft** | [**PydanticMainImagefaceRecognitionFaceRecognitionAddFaceDataClass94559363589408**](PydanticMainImagefaceRecognitionFaceRecognitionAddFaceDataClass94559363589408.md) |  | [optional] 

## Example

```python
from openapi_client.models.imageface_recognition_response_model import ImagefaceRecognitionResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ImagefaceRecognitionResponseModel from a JSON string
imageface_recognition_response_model_instance = ImagefaceRecognitionResponseModel.from_json(json)
# print the JSON string representation of the object
print(ImagefaceRecognitionResponseModel.to_json())

# convert the object into a dict
imageface_recognition_response_model_dict = imageface_recognition_response_model_instance.to_dict()
# create an instance of ImagefaceRecognitionResponseModel from a dict
imageface_recognition_response_model_form_dict = imageface_recognition_response_model.from_dict(imageface_recognition_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


