# PydanticMainOcrocrOcrDataClass94559363875232


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**bounding_boxes** | [**List[BoundingBox]**](BoundingBox.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**status** | [**StatusF43Enum**](StatusF43Enum.md) |  | 

## Example

```python
from openapi_client.models.pydantic_main_ocrocr_ocr_data_class94559363875232 import PydanticMainOcrocrOcrDataClass94559363875232

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainOcrocrOcrDataClass94559363875232 from a JSON string
pydantic_main_ocrocr_ocr_data_class94559363875232_instance = PydanticMainOcrocrOcrDataClass94559363875232.from_json(json)
# print the JSON string representation of the object
print(PydanticMainOcrocrOcrDataClass94559363875232.to_json())

# convert the object into a dict
pydantic_main_ocrocr_ocr_data_class94559363875232_dict = pydantic_main_ocrocr_ocr_data_class94559363875232_instance.to_dict()
# create an instance of PydanticMainOcrocrOcrDataClass94559363875232 from a dict
pydantic_main_ocrocr_ocr_data_class94559363875232_form_dict = pydantic_main_ocrocr_ocr_data_class94559363875232.from_dict(pydantic_main_ocrocr_ocr_data_class94559363875232_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

