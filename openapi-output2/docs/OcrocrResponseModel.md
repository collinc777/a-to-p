# OcrocrResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**microsoft** | [**PydanticMainOcrocrOcrDataClass94559363407568**](PydanticMainOcrocrOcrDataClass94559363407568.md) |  | [optional] 
**google** | [**PydanticMainOcrocrOcrDataClass94559358866720**](PydanticMainOcrocrOcrDataClass94559358866720.md) |  | [optional] 
**amazon** | [**PydanticMainOcrocrOcrDataClass94559363879168**](PydanticMainOcrocrOcrDataClass94559363879168.md) |  | [optional] 
**clarifai** | [**PydanticMainOcrocrOcrDataClass94559363882336**](PydanticMainOcrocrOcrDataClass94559363882336.md) |  | [optional] 
**var_base64** | [**PydanticMainOcrocrOcrDataClass94559363885504**](PydanticMainOcrocrOcrDataClass94559363885504.md) |  | [optional] 
**api4ai** | [**PydanticMainOcrocrOcrDataClass94559363888672**](PydanticMainOcrocrOcrDataClass94559363888672.md) |  | [optional] 
**sentisight** | [**PydanticMainOcrocrOcrDataClass94559363892976**](PydanticMainOcrocrOcrDataClass94559363892976.md) |  | [optional] 

## Example

```python
from openapi_client.models.ocrocr_response_model import OcrocrResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of OcrocrResponseModel from a JSON string
ocrocr_response_model_instance = OcrocrResponseModel.from_json(json)
# print the JSON string representation of the object
print(OcrocrResponseModel.to_json())

# convert the object into a dict
ocrocr_response_model_dict = ocrocr_response_model_instance.to_dict()
# create an instance of OcrocrResponseModel from a dict
ocrocr_response_model_form_dict = ocrocr_response_model.from_dict(ocrocr_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


