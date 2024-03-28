# PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363912992


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extracted_data** | [**List[InfosInvoiceParserDataClass]**](InfosInvoiceParserDataClass.md) |  | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**status** | [**StatusF43Enum**](StatusF43Enum.md) |  | 

## Example

```python
from openapi_client.models.pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559363912992 import PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363912992

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363912992 from a JSON string
pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559363912992_instance = PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363912992.from_json(json)
# print the JSON string representation of the object
print(PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363912992.to_json())

# convert the object into a dict
pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559363912992_dict = pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559363912992_instance.to_dict()
# create an instance of PydanticMainOcrinvoiceParserInvoiceParserDataClass94559363912992 from a dict
pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559363912992_form_dict = pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559363912992.from_dict(pydantic_main_ocrinvoice_parser_invoice_parser_data_class94559363912992_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


