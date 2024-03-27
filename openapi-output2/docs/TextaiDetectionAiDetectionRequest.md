# TextaiDetectionAiDetectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | **str** | It can be one (ex: **&#39;amazon&#39;** or **&#39;google&#39;**) or multiple provider(s) (ex: **&#39;amazon,microsoft,google&#39;**)             that the data will be redirected to in order to get the processed results. | 
**fallback_providers** | **str** | Providers in this list will be used as fallback if the call to provider in &#x60;providers&#x60; parameter fails.     To use this feature, you must input **only one** provider in the &#x60;providers&#x60; parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn&#39;t fail.   *Doesn&#39;t work with async subfeatures.*      | [optional] 
**response_as_dict** | **bool** | Optional : When set to **true** (default), the response is an object of responses with providers names as keys : &lt;br&gt;                    &#x60;&#x60;&#x60; {\&quot;google\&quot; : { \&quot;status\&quot;: \&quot;success\&quot;, ... }, } &#x60;&#x60;&#x60; &lt;br&gt;                 When set to **false** the response structure is a list of response objects : &lt;br&gt;                     &#x60;&#x60;&#x60; [{\&quot;status\&quot;: \&quot;success\&quot;, \&quot;provider\&quot;: \&quot;google\&quot; ... }, ] &#x60;&#x60;&#x60;. &lt;br&gt;                    | [optional] [default to True]
**attributes_as_list** | **bool** | Optional : When set to **false** (default) the structure of the extracted items is list of objects having different attributes : &lt;br&gt;      &#x60;&#x60;&#x60;{&#39;items&#39;: [{\&quot;attribute_1\&quot;: \&quot;x1\&quot;,\&quot;attribute_2\&quot;: \&quot;y2\&quot;}, ... ]}&#x60;&#x60;&#x60; &lt;br&gt;      When it is set to **true**, the response contains an object with each attribute as a list : &lt;br&gt;      &#x60;&#x60;&#x60;{ \&quot;attribute_1\&quot;: [\&quot;x1\&quot;,\&quot;x2\&quot;, ...], \&quot;attribute_2\&quot;: [y1, y2, ...]}&#x60;&#x60;&#x60;  | [optional] [default to False]
**show_original_response** | **bool** | Optional : Shows the original response of the provider.&lt;br&gt;         When set to **true**, a new attribute *original_response* will appear in the response object. | [optional] [default to False]
**text** | **str** | Text to analyze | 
**language** | **str** | Language code for the language the input text is written in (eg: en, fr). | [optional] 
**provider_params** | **str** |  Parameters specific to the provider that you want to send along the request.  it should take a *provider* name as key and an object of parameters as value.  Example:      {       \&quot;deepgram\&quot;: {         \&quot;filler_words\&quot;: true,         \&quot;smart_format\&quot;: true,         \&quot;callback\&quot;: \&quot;https://webhook.site/0000\&quot;       },       \&quot;assembly\&quot;: {         \&quot;webhook_url\&quot;: \&quot;https://webhook.site/0000\&quot;       }     }  Please refer to the documentation of each provider to see which parameters to send.  | [optional] 

## Example

```python
from openapi_client.models.textai_detection_ai_detection_request import TextaiDetectionAiDetectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TextaiDetectionAiDetectionRequest from a JSON string
textai_detection_ai_detection_request_instance = TextaiDetectionAiDetectionRequest.from_json(json)
# print the JSON string representation of the object
print(TextaiDetectionAiDetectionRequest.to_json())

# convert the object into a dict
textai_detection_ai_detection_request_dict = textai_detection_ai_detection_request_instance.to_dict()
# create an instance of TextaiDetectionAiDetectionRequest from a dict
textai_detection_ai_detection_request_form_dict = textai_detection_ai_detection_request.from_dict(textai_detection_ai_detection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


