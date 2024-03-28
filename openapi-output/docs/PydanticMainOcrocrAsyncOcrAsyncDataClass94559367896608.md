# PydanticMainOcrocrAsyncOcrAsyncDataClass94559367896608


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
from openapi_client.models.pydantic_main_ocrocr_async_ocr_async_data_class94559367896608 import PydanticMainOcrocrAsyncOcrAsyncDataClass94559367896608

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainOcrocrAsyncOcrAsyncDataClass94559367896608 from a JSON string
pydantic_main_ocrocr_async_ocr_async_data_class94559367896608_instance = PydanticMainOcrocrAsyncOcrAsyncDataClass94559367896608.from_json(json)
# print the JSON string representation of the object
print(PydanticMainOcrocrAsyncOcrAsyncDataClass94559367896608.to_json())

# convert the object into a dict
pydantic_main_ocrocr_async_ocr_async_data_class94559367896608_dict = pydantic_main_ocrocr_async_ocr_async_data_class94559367896608_instance.to_dict()
# create an instance of PydanticMainOcrocrAsyncOcrAsyncDataClass94559367896608 from a dict
pydantic_main_ocrocr_async_ocr_async_data_class94559367896608_form_dict = pydantic_main_ocrocr_async_ocr_async_data_class94559367896608.from_dict(pydantic_main_ocrocr_async_ocr_async_data_class94559367896608_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


