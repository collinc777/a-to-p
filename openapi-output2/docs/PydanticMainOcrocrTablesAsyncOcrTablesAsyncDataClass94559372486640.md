# PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559372486640


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pages** | [**List[Page]**](Page.md) |  | [optional] 
**num_pages** | **int** |  | 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**id** | **str** |  | 
**final_status** | [**FinalStatusEnum**](FinalStatusEnum.md) |  | 
**error** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.pydantic_main_ocrocr_tables_async_ocr_tables_async_data_class94559372486640 import PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559372486640

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559372486640 from a JSON string
pydantic_main_ocrocr_tables_async_ocr_tables_async_data_class94559372486640_instance = PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559372486640.from_json(json)
# print the JSON string representation of the object
print(PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559372486640.to_json())

# convert the object into a dict
pydantic_main_ocrocr_tables_async_ocr_tables_async_data_class94559372486640_dict = pydantic_main_ocrocr_tables_async_ocr_tables_async_data_class94559372486640_instance.to_dict()
# create an instance of PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559372486640 from a dict
pydantic_main_ocrocr_tables_async_ocr_tables_async_data_class94559372486640_form_dict = pydantic_main_ocrocr_tables_async_ocr_tables_async_data_class94559372486640.from_dict(pydantic_main_ocrocr_tables_async_ocr_tables_async_data_class94559372486640_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


