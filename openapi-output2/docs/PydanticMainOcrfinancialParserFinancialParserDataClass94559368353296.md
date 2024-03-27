# PydanticMainOcrfinancialParserFinancialParserDataClass94559368353296


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extracted_data** | [**List[FinancialParserObjectDataClass]**](FinancialParserObjectDataClass.md) | List of parsed financial data objects (per page). | [optional] 
**original_response** | **object** | original response sent by the provider, hidden by default, show it by passing the &#x60;show_original_response&#x60; field to &#x60;true&#x60; in your request | [optional] 
**status** | [**StatusF43Enum**](StatusF43Enum.md) |  | 

## Example

```python
from openapi_client.models.pydantic_main_ocrfinancial_parser_financial_parser_data_class94559368353296 import PydanticMainOcrfinancialParserFinancialParserDataClass94559368353296

# TODO update the JSON string below
json = "{}"
# create an instance of PydanticMainOcrfinancialParserFinancialParserDataClass94559368353296 from a JSON string
pydantic_main_ocrfinancial_parser_financial_parser_data_class94559368353296_instance = PydanticMainOcrfinancialParserFinancialParserDataClass94559368353296.from_json(json)
# print the JSON string representation of the object
print(PydanticMainOcrfinancialParserFinancialParserDataClass94559368353296.to_json())

# convert the object into a dict
pydantic_main_ocrfinancial_parser_financial_parser_data_class94559368353296_dict = pydantic_main_ocrfinancial_parser_financial_parser_data_class94559368353296_instance.to_dict()
# create an instance of PydanticMainOcrfinancialParserFinancialParserDataClass94559368353296 from a dict
pydantic_main_ocrfinancial_parser_financial_parser_data_class94559368353296_form_dict = pydantic_main_ocrfinancial_parser_financial_parser_data_class94559368353296.from_dict(pydantic_main_ocrfinancial_parser_financial_parser_data_class94559368353296_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


