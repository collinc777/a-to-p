# FinancialDocumentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_index** | **int** | Index of the detected document. | [optional] 
**document_page_number** | **int** | Page number within the document. | [optional] 
**document_type** | **str** | Type or category of the document. | [optional] 

## Example

```python
from openapi_client.models.financial_document_metadata import FinancialDocumentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialDocumentMetadata from a JSON string
financial_document_metadata_instance = FinancialDocumentMetadata.from_json(json)
# print the JSON string representation of the object
print(FinancialDocumentMetadata.to_json())

# convert the object into a dict
financial_document_metadata_dict = financial_document_metadata_instance.to_dict()
# create an instance of FinancialDocumentMetadata from a dict
financial_document_metadata_form_dict = financial_document_metadata.from_dict(financial_document_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


