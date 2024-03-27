# PydanticMainVideolabelDetectionAsyncLabelDetectionAsyncDataClass94559369147568


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**List[VideoLabel]**](VideoLabel.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**id** | **str** |  | 
**final_status** | [**FinalStatusEnum**](FinalStatusEnum.md) |  | 
**error** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.pydantic_main_videolabel_detection_async_label_detection_async_data_class94559369147568 import PydanticMainVideolabelDetectionAsyncLabelDetectionAsyncDataClass94559369147568

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainVideolabelDetectionAsyncLabelDetectionAsyncDataClass94559369147568 from a JSON string
pydantic_main_videolabel_detection_async_label_detection_async_data_class94559369147568_instance = PydanticMainVideolabelDetectionAsyncLabelDetectionAsyncDataClass94559369147568.from_json(json)
# print the JSON string representation of the object
print(PydanticMainVideolabelDetectionAsyncLabelDetectionAsyncDataClass94559369147568.to_json())

# convert the object into a dict
pydantic_main_videolabel_detection_async_label_detection_async_data_class94559369147568_dict = pydantic_main_videolabel_detection_async_label_detection_async_data_class94559369147568_instance.to_dict()
# create an instance of PydanticMainVideolabelDetectionAsyncLabelDetectionAsyncDataClass94559369147568 from a dict
pydantic_main_videolabel_detection_async_label_detection_async_data_class94559369147568_form_dict = pydantic_main_videolabel_detection_async_label_detection_async_data_class94559369147568.from_dict(pydantic_main_videolabel_detection_async_label_detection_async_data_class94559369147568_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


