# PydanticMainOcrocrAsyncOcrAsyncDataClass94559367918864


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_text** | **str** |  | 
**pages** | [**List[Page]**](Page.md) | List of pages | [optional] 
**number_of_pages** | **int** | Number of pages in the document | 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**id** | **str** |  | 
**final_status** | [**FinalStatusEnum**](FinalStatusEnum.md) |  | 
**error** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.pydantic_main_ocrocr_async_ocr_async_data_class94559367918864 import PydanticMainOcrocrAsyncOcrAsyncDataClass94559367918864

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainOcrocrAsyncOcrAsyncDataClass94559367918864 from a JSON string
pydantic_main_ocrocr_async_ocr_async_data_class94559367918864_instance = PydanticMainOcrocrAsyncOcrAsyncDataClass94559367918864.from_json(json)
# print the JSON string representation of the object
print(PydanticMainOcrocrAsyncOcrAsyncDataClass94559367918864.to_json())

# convert the object into a dict
pydantic_main_ocrocr_async_ocr_async_data_class94559367918864_dict = pydantic_main_ocrocr_async_ocr_async_data_class94559367918864_instance.to_dict()
# create an instance of PydanticMainOcrocrAsyncOcrAsyncDataClass94559367918864 from a dict
pydantic_main_ocrocr_async_ocr_async_data_class94559367918864_form_dict = pydantic_main_ocrocr_async_ocr_async_data_class94559367918864.from_dict(pydantic_main_ocrocr_async_ocr_async_data_class94559367918864_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


