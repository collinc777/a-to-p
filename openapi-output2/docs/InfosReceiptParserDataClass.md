# InfosReceiptParserDataClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_number** | **str** |  | [optional] 
**invoice_total** | **int** |  | [optional] 
**invoice_subtotal** | **int** |  | [optional] 
**barcodes** | [**List[BarCode]**](BarCode.md) |  | [optional] 
**category** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**time** | **str** |  | [optional] 
**customer_information** | [**CustomerInformation**](CustomerInformation.md) |  | [optional] 
**merchant_information** | [**MerchantInformation**](MerchantInformation.md) |  | [optional] 
**payment_information** | [**PaymentInformation**](PaymentInformation.md) |  | [optional] 
**locale** | [**Locale**](Locale.md) |  | [optional] 
**taxes** | [**List[Taxes]**](Taxes.md) |  | [optional] 
**receipt_infos** | **object** |  | [optional] 
**item_lines** | [**List[ItemLines]**](ItemLines.md) |  | [optional] 

## Example

```python
from openapi_client.models.infos_receipt_parser_data_class import InfosReceiptParserDataClass

# TODO update the JSON string below
json = "{}"
# create an instance of InfosReceiptParserDataClass from a JSON string
infos_receipt_parser_data_class_instance = InfosReceiptParserDataClass.from_json(json)
# print the JSON string representation of the object
print(InfosReceiptParserDataClass.to_json())

# convert the object into a dict
infos_receipt_parser_data_class_dict = infos_receipt_parser_data_class_instance.to_dict()
# create an instance of InfosReceiptParserDataClass from a dict
infos_receipt_parser_data_class_form_dict = infos_receipt_parser_data_class.from_dict(infos_receipt_parser_data_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


