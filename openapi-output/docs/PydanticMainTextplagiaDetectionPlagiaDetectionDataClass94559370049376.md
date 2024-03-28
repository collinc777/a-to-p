# PydanticMainTextplagiaDetectionPlagiaDetectionDataClass94559370049376


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plagia_score** | **int** |  | 
**items** | [**List[PlagiaDetectionItem]**](PlagiaDetectionItem.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**status** | [**StatusF43Enum**](StatusF43Enum.md) |  | 

## Example

```python
from openapi_client.models.pydantic_main_textplagia_detection_plagia_detection_data_class94559370049376 import PydanticMainTextplagiaDetectionPlagiaDetectionDataClass94559370049376

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainTextplagiaDetectionPlagiaDetectionDataClass94559370049376 from a JSON string
pydantic_main_textplagia_detection_plagia_detection_data_class94559370049376_instance = PydanticMainTextplagiaDetectionPlagiaDetectionDataClass94559370049376.from_json(json)
# print the JSON string representation of the object
print(PydanticMainTextplagiaDetectionPlagiaDetectionDataClass94559370049376.to_json())

# convert the object into a dict
pydantic_main_textplagia_detection_plagia_detection_data_class94559370049376_dict = pydantic_main_textplagia_detection_plagia_detection_data_class94559370049376_instance.to_dict()
# create an instance of PydanticMainTextplagiaDetectionPlagiaDetectionDataClass94559370049376 from a dict
pydantic_main_textplagia_detection_plagia_detection_data_class94559370049376_form_dict = pydantic_main_textplagia_detection_plagia_detection_data_class94559370049376.from_dict(pydantic_main_textplagia_detection_plagia_detection_data_class94559370049376_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


