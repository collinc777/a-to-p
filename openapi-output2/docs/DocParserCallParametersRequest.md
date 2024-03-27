# DocParserCallParametersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | File to analyse in binary format to be used with *content-type*: **multipart/form-data** &lt;br&gt; **Does not work with application/json !** | [optional] 
**file_url** | **str** | File **URL** to analyse to be used with with *content-type*: **application/json**. | [optional] 
**language** | **str** | Language code of the language the document is written in (ex: fr (French), en (English), es (Spanish)) | [optional] 

## Example

```python
from openapi_client.models.doc_parser_call_parameters_request import DocParserCallParametersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocParserCallParametersRequest from a JSON string
doc_parser_call_parameters_request_instance = DocParserCallParametersRequest.from_json(json)
# print the JSON string representation of the object
print(DocParserCallParametersRequest.to_json())

# convert the object into a dict
doc_parser_call_parameters_request_dict = doc_parser_call_parameters_request_instance.to_dict()
# create an instance of DocParserCallParametersRequest from a dict
doc_parser_call_parameters_request_form_dict = doc_parser_call_parameters_request.from_dict(doc_parser_call_parameters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


