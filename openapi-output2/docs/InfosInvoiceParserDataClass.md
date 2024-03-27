# InfosInvoiceParserDataClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_information** | [**CustomerInformationInvoice**](CustomerInformationInvoice.md) |  | [optional] 
**merchant_information** | [**MerchantInformationInvoice**](MerchantInformationInvoice.md) |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**invoice_total** | **int** |  | [optional] 
**invoice_subtotal** | **int** |  | [optional] 
**gratuity** | **int** |  | [optional] 
**amount_due** | **int** |  | [optional] 
**previous_unpaid_balance** | **int** |  | [optional] 
**discount** | **int** |  | [optional] 
**taxes** | [**List[TaxesInvoice]**](TaxesInvoice.md) |  | [optional] 
**service_charge** | **int** |  | [optional] 
**payment_term** | **str** |  | [optional] 
**purchase_order** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**service_date** | **str** |  | [optional] 
**service_due_date** | **str** |  | [optional] 
**po_number** | **str** |  | [optional] 
**locale** | [**LocaleInvoice**](LocaleInvoice.md) |  | [optional] 
**bank_informations** | [**BankInvoice**](BankInvoice.md) |  | [optional] 
**item_lines** | [**List[ItemLinesInvoice]**](ItemLinesInvoice.md) |  | [optional] 

## Example

```python
from openapi_client.models.infos_invoice_parser_data_class import InfosInvoiceParserDataClass

# TODO update the JSON string below
json = "{}"
# create an instance of InfosInvoiceParserDataClass from a JSON string
infos_invoice_parser_data_class_instance = InfosInvoiceParserDataClass.from_json(json)
# print the JSON string representation of the object
print(InfosInvoiceParserDataClass.to_json())

# convert the object into a dict
infos_invoice_parser_data_class_dict = infos_invoice_parser_data_class_instance.to_dict()
# create an instance of InfosInvoiceParserDataClass from a dict
infos_invoice_parser_data_class_form_dict = infos_invoice_parser_data_class.from_dict(infos_invoice_parser_data_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


