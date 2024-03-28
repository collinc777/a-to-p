# ImagelogoDetectionResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**microsoft** | [**PydanticMainImagelogoDetectionLogoDetectionDataClass94559364220800**](PydanticMainImagelogoDetectionLogoDetectionDataClass94559364220800.md) |  | [optional] 
**google** | [**PydanticMainImagelogoDetectionLogoDetectionDataClass94559364386944**](PydanticMainImagelogoDetectionLogoDetectionDataClass94559364386944.md) |  | [optional] 
**clarifai** | [**PydanticMainImagelogoDetectionLogoDetectionDataClass94559363427872**](PydanticMainImagelogoDetectionLogoDetectionDataClass94559363427872.md) |  | [optional] 
**api4ai** | [**PydanticMainImagelogoDetectionLogoDetectionDataClass94559363441296**](PydanticMainImagelogoDetectionLogoDetectionDataClass94559363441296.md) |  | [optional] 
**smartclick** | [**PydanticMainImagelogoDetectionLogoDetectionDataClass94559363452160**](PydanticMainImagelogoDetectionLogoDetectionDataClass94559363452160.md) |  | [optional] 

## Example

```python
from openapi_client.models.imagelogo_detection_response_model import ImagelogoDetectionResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ImagelogoDetectionResponseModel from a JSON string
imagelogo_detection_response_model_instance = ImagelogoDetectionResponseModel.from_json(json)
# print the JSON string representation of the object
print(ImagelogoDetectionResponseModel.to_json())

# convert the object into a dict
imagelogo_detection_response_model_dict = imagelogo_detection_response_model_instance.to_dict()
# create an instance of ImagelogoDetectionResponseModel from a dict
imagelogo_detection_response_model_form_dict = imagelogo_detection_response_model.from_dict(imagelogo_detection_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


