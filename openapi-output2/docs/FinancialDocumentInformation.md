# FinancialDocumentInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_receipt_id** | **str** | Identifier for the invoice. | [optional] 
**purchase_order** | **str** | Purchase order related to the document. | [optional] 
**invoice_date** | **str** | Date of the invoice. | [optional] 
**time** | **str** | Time associated with the document. | [optional] 
**invoice_due_date** | **str** | Due date for the invoice. | [optional] 
**service_start_date** | **str** | Start date of the service associated with the document. | [optional] 
**service_end_date** | **str** | End date of the service associated with the document. | [optional] 
**reference** | **str** | Reference number associated with the document. | [optional] 
**biller_code** | **str** | Biller code associated with the document. | [optional] 
**order_date** | **str** | Date of the order associated with the document. | [optional] 
**tracking_number** | **str** | Tracking number associated with the document. | [optional] 
**barcodes** | [**List[FinancialBarcode]**](FinancialBarcode.md) | List of barcodes associated with the document. | [optional] 

## Example

```python
from openapi_client.models.financial_document_information import FinancialDocumentInformation

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialDocumentInformation from a JSON string
financial_document_information_instance = FinancialDocumentInformation.from_json(json)
# print the JSON string representation of the object
print(FinancialDocumentInformation.to_json())

# convert the object into a dict
financial_document_information_dict = financial_document_information_instance.to_dict()
# create an instance of FinancialDocumentInformation from a dict
financial_document_information_form_dict = financial_document_information.from_dict(financial_document_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


