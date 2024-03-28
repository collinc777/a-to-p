# TextchatChatRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | **str** | It can be one (ex: **&#39;amazon&#39;** or **&#39;google&#39;**) or multiple provider(s) (ex: **&#39;amazon,microsoft,google&#39;**)             that the data will be redirected to in order to get the processed results. | 
**fallback_providers** | **str** | Providers in this list will be used as fallback if the call to provider in &#x60;providers&#x60; parameter fails.     To use this feature, you must input **only one** provider in the &#x60;providers&#x60; parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn&#39;t fail.   *Doesn&#39;t work with async subfeatures.*      | [optional] 
**response_as_dict** | **bool** | Optional : When set to **true** (default), the response is an object of responses with providers names as keys : &lt;br&gt;                    &#x60;&#x60;&#x60; {\&quot;google\&quot; : { \&quot;status\&quot;: \&quot;success\&quot;, ... }, } &#x60;&#x60;&#x60; &lt;br&gt;                 When set to **false** the response structure is a list of response objects : &lt;br&gt;                     &#x60;&#x60;&#x60; [{\&quot;status\&quot;: \&quot;success\&quot;, \&quot;provider\&quot;: \&quot;google\&quot; ... }, ] &#x60;&#x60;&#x60;. &lt;br&gt;                    | [optional] [default to True]
**attributes_as_list** | **bool** | Optional : When set to **false** (default) the structure of the extracted items is list of objects having different attributes : &lt;br&gt;      &#x60;&#x60;&#x60;{&#39;items&#39;: [{\&quot;attribute_1\&quot;: \&quot;x1\&quot;,\&quot;attribute_2\&quot;: \&quot;y2\&quot;}, ... ]}&#x60;&#x60;&#x60; &lt;br&gt;      When it is set to **true**, the response contains an object with each attribute as a list : &lt;br&gt;      &#x60;&#x60;&#x60;{ \&quot;attribute_1\&quot;: [\&quot;x1\&quot;,\&quot;x2\&quot;, ...], \&quot;attribute_2\&quot;: [y1, y2, ...]}&#x60;&#x60;&#x60;  | [optional] [default to False]
**show_original_response** | **bool** | Optional : Shows the original response of the provider.&lt;br&gt;         When set to **true**, a new attribute *original_response* will appear in the response object. | [optional] [default to False]
**settings** | **str** | A dictionnary or a json object to specify specific models to use for some providers. &lt;br&gt;                     It can be in the following format: {\&quot;google\&quot; : \&quot;google_model\&quot;, \&quot;ibm\&quot;: \&quot;ibm_model\&quot;...}.                      **Caution**: setting models can be done only with &#x60;Content-Type&#x60; : &#x60;application/json&#x60;.                       | [optional] 
**text** | **str** | Start your conversation here... | [optional] [default to '']
**chatbot_global_action** | **str** | A system message that helps set the behavior of the assistant. For example, &#39;You are a helpful assistant&#39;. | [optional] [default to '']
**previous_history** | **List[Dict[str, object]]** | A list containing all the previous conversations between the user and the chatbot AI. Each item in the list should be a dictionary with two keys: &#39;role&#39; and &#39;message&#39;. The &#39;role&#39; key specifies the role of the speaker and can have the values &#39;user&#39; or &#39;assistant&#39;. The &#39;message&#39; key contains the text of the conversation from the respective role. For example: [{&#39;role&#39;: &#39;user&#39;, &#39;message&#39;: &#39;Hello&#39;}, {&#39;role&#39;: &#39;assistant&#39;, &#39;message&#39;: &#39;Hi, how can I help you?&#39;}, ...]. This format allows easy identification of the speaker&#39;s role and their corresponding message. | [optional] 
**temperature** | **float** | Higher values mean the model will take more risks and value 0 (argmax sampling) works better for scenarios with a well-defined answer. | [optional] [default to 0.0]
**max_tokens** | **int** | The maximum number of tokens to generate in the completion. The token count of your prompt plus max_tokens cannot exceed the model&#39;s context length. | [optional] [default to 1000]

## Example

```python
from openapi_client.models.textchat_chat_request import TextchatChatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TextchatChatRequest from a JSON string
textchat_chat_request_instance = TextchatChatRequest.from_json(json)
# print the JSON string representation of the object
print(TextchatChatRequest.to_json())

# convert the object into a dict
textchat_chat_request_dict = textchat_chat_request_instance.to_dict()
# create an instance of TextchatChatRequest from a dict
textchat_chat_request_form_dict = textchat_chat_request.from_dict(textchat_chat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


