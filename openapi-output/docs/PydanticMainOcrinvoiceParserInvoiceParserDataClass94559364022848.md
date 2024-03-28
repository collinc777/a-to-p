# PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364022848


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extracted_data** | [**List[InfosInvoiceParserDataClass]**](InfosInvoiceParserDataClass.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**status** | [**StatusF43Enum**](StatusF43Enum.md) |  | 

## Example

```python
from openapi_client.models.pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559364022848 import PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364022848

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364022848 from a JSON string
pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559364022848_instance = PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364022848.from_json(json)
# print the JSON string representation of the object
print(PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364022848.to_json())

# convert the object into a dict
pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559364022848_dict = pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559364022848_instance.to_dict()
# create an instance of PydanticMainOcrinvoiceParserInvoiceParserDataClass94559364022848 from a dict
pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559364022848_form_dict = pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559364022848.from_dict(pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559364022848_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


