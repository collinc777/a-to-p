# PydanticMainVideologoDetectionAsyncLogoDetectionAsyncDataClass94559370779840


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logos** | [**List[LogoTrack]**](LogoTrack.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**id** | **str** |  | 
**final_status** | [**FinalStatusEnum**](FinalStatusEnum.md) |  | 
**error** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.pydantic_main_videologo_detection_async_logo_detection_async_data_class94559370779840 import PydanticMainVideologoDetectionAsyncLogoDetectionAsyncDataClass94559370779840

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainVideologoDetectionAsyncLogoDetectionAsyncDataClass94559370779840 from a JSON string
pydantic_main_videologo_detection_async_logo_detection_async_data_class94559370779840_instance = PydanticMainVideologoDetectionAsyncLogoDetectionAsyncDataClass94559370779840.from_json(json)
# print the JSON string representation of the object
print(PydanticMainVideologoDetectionAsyncLogoDetectionAsyncDataClass94559370779840.to_json())

# convert the object into a dict
pydantic_main_videologo_detection_async_logo_detection_async_data_class94559370779840_dict = pydantic_main_videologo_detection_async_logo_detection_async_data_class94559370779840_instance.to_dict()
# create an instance of PydanticMainVideologoDetectionAsyncLogoDetectionAsyncDataClass94559370779840 from a dict
pydantic_main_videologo_detection_async_logo_detection_async_data_class94559370779840_form_dict = pydantic_main_videologo_detection_async_logo_detection_async_data_class94559370779840.from_dict(pydantic_main_videologo_detection_async_logo_detection_async_data_class94559370779840_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


