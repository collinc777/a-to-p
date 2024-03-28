# PydanticMainOcrreceiptParserReceiptParserDataClass94559367677312


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extracted_data** | [**List[InfosReceiptParserDataClass]**](InfosReceiptParserDataClass.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**status** | [**StatusF43Enum**](StatusF43Enum.md) |  | 

## Example

```python
from openapi_client.models.pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367677312 import PydanticMainOcrreceiptParserReceiptParserDataClass94559367677312

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainOcrreceiptParserReceiptParserDataClass94559367677312 from a JSON string
pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367677312_instance = PydanticMainOcrreceiptParserReceiptParserDataClass94559367677312.from_json(json)
# print the JSON string representation of the object
print(PydanticMainOcrreceiptParserReceiptParserDataClass94559367677312.to_json())

# convert the object into a dict
pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367677312_dict = pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367677312_instance.to_dict()
# create an instance of PydanticMainOcrreceiptParserReceiptParserDataClass94559367677312 from a dict
pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367677312_form_dict = pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367677312.from_dict(pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367677312_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


