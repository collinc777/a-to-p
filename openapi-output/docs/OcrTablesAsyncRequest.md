# OcrTablesAsyncRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | **str** | It can be one (ex: **&#39;amazon&#39;** or **&#39;google&#39;**) or multiple provider(s) (ex: **&#39;amazon,microsoft,google&#39;**)             that the data will be redirected to in order to get the processed results. | 
**fallback_providers** | **str** | Providers in this list will be used as fallback if the call to provider in &#x60;providers&#x60; parameter fails.     To use this feature, you must input **only one** provider in the &#x60;providers&#x60; parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn&#39;t fail.   *Doesn&#39;t work with async subfeatures.*      | [optional] 
**show_original_response** | **bool** | Optional : Shows the original response of the provider.&lt;br&gt;         When set to **true**, a new attribute *original_response* will appear in the response object. | [optional] [default to False]
**webhook_receiver** | **str** | Webhook receiver should be a valid https URL (ex : https://your.listner.com/endpoint).             After the processing is done, the webhook endpoint will receive a POST request with the result. | [optional] 
**users_webhook_parameters** | **Dict[str, object]** | Json data that contains of additional parameters that will be sent back to the webhook receiver             (ex: api key for security or client&#39;s data ID to link the result internally).             Will only be used when webhook_receiver is set. | [optional] 
**file** | **bytearray** | File to analyse in binary format to be used with *content-type*: **multipart/form-data** &lt;br&gt; **Does not work with application/json !** | [optional] 
**file_url** | **str** | File **URL** to analyse to be used with with *content-type*: **application/json**. | [optional] 
**file_password** | **str** | If your PDF file has a password, you can pass it here! | [optional] 
**language** | **str** | Language code of the language the document is written in (ex: fr (French), en (English), es (Spanish)) | [optional] 

## Example

```python
from openapi_client.models.ocr_tables_async_request import OcrTablesAsyncRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OcrTablesAsyncRequest from a JSON string
ocr_tables_async_request_instance = OcrTablesAsyncRequest.from_json(json)
# print the JSON string representation of the object
print(OcrTablesAsyncRequest.to_json())

# convert the object into a dict
ocr_tables_async_request_dict = ocr_tables_async_request_instance.to_dict()
# create an instance of OcrTablesAsyncRequest from a dict
ocr_tables_async_request_form_dict = ocr_tables_async_request.from_dict(ocr_tables_async_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


