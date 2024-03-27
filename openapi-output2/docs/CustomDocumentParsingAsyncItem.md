# CustomDocumentParsingAsyncItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **int** |  | 
**value** | **str** |  | 
**query** | **str** |  | 
**bounding_box** | [**CustomDocumentParsingAsyncBoundingBox**](CustomDocumentParsingAsyncBoundingBox.md) |  | 
**page** | **int** |  | 

## Example

```python
from openapi_client.models.custom_document_parsing_async_item import CustomDocumentParsingAsyncItem

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDocumentParsingAsyncItem from a JSON string
custom_document_parsing_async_item_instance = CustomDocumentParsingAsyncItem.from_json(json)
# print the JSON string representation of the object
print(CustomDocumentParsingAsyncItem.to_json())

# convert the object into a dict
custom_document_parsing_async_item_dict = custom_document_parsing_async_item_instance.to_dict()
# create an instance of CustomDocumentParsingAsyncItem from a dict
custom_document_parsing_async_item_form_dict = custom_document_parsing_async_item.from_dict(custom_document_parsing_async_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


