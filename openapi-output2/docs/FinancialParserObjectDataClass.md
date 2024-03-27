# FinancialParserObjectDataClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_information** | [**FinancialCustomerInformation**](FinancialCustomerInformation.md) |  | 
**merchant_information** | [**FinancialMerchantInformation**](FinancialMerchantInformation.md) |  | 
**payment_information** | [**FinancialPaymentInformation**](FinancialPaymentInformation.md) |  | 
**financial_document_information** | [**FinancialDocumentInformation**](FinancialDocumentInformation.md) |  | 
**local** | [**FinancialLocalInformation**](FinancialLocalInformation.md) |  | 
**bank** | [**FinancialBankInformation**](FinancialBankInformation.md) |  | 
**item_lines** | [**List[FinancialLineItem]**](FinancialLineItem.md) | List of line items associated with the document. | [optional] 
**document_metadata** | [**FinancialDocumentMetadata**](FinancialDocumentMetadata.md) |  | 

## Example

```python
from openapi_client.models.financial_parser_object_data_class import FinancialParserObjectDataClass

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialParserObjectDataClass from a JSON string
financial_parser_object_data_class_instance = FinancialParserObjectDataClass.from_json(json)
# print the JSON string representation of the object
print(FinancialParserObjectDataClass.to_json())

# convert the object into a dict
financial_parser_object_data_class_dict = financial_parser_object_data_class_instance.to_dict()
# create an instance of FinancialParserObjectDataClass from a dict
financial_parser_object_data_class_form_dict = financial_parser_object_data_class.from_dict(financial_parser_object_data_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


