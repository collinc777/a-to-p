# AddFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | [**DataTypeEnum**](DataTypeEnum.md) |  | 
**file** | **bytearray** | File to analyse in binary format to be used with *content-type*: **multipart/form-data** &lt;br&gt; **Does not work with application/json !** | [optional] 
**file_url** | **str** | File **URL** to analyse to be used with with *content-type*: **application/json**. | [optional] 
**metadata** | **str** | Optional parameter: Attach metadata to the uploaded file data in your database. Provide a stringified JSON with key-value pairs. Useful in &#x60;filter_document&#x60; when querying the language model, it allows you to filter data with your Chatbot by considering only documents that have the specified metadata. | [optional] 
**provider** | **str** | Select a provider to use, only for audio (speech-to-text) &amp; pdf (ocr-async) files. | [optional] 

## Example

```python
from openapi_client.models.add_file_request import AddFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddFileRequest from a JSON string
add_file_request_instance = AddFileRequest.from_json(json)
# print the JSON string representation of the object
print(AddFileRequest.to_json())

# convert the object into a dict
add_file_request_dict = add_file_request_instance.to_dict()
# create an instance of AddFileRequest from a dict
add_file_request_form_dict = add_file_request.from_dict(add_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


