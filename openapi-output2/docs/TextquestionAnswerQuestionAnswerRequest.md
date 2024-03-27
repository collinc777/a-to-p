# TextquestionAnswerQuestionAnswerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | **str** | It can be one (ex: **&#39;amazon&#39;** or **&#39;google&#39;**) or multiple provider(s) (ex: **&#39;amazon,microsoft,google&#39;**)             that the data will be redirected to in order to get the processed results. | 
**fallback_providers** | **str** | Providers in this list will be used as fallback if the call to provider in &#x60;providers&#x60; parameter fails.     To use this feature, you must input **only one** provider in the &#x60;providers&#x60; parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn&#39;t fail.   *Doesn&#39;t work with async subfeatures.*      | [optional] 
**response_as_dict** | **bool** | Optional : When set to **true** (default), the response is an object of responses with providers names as keys : &lt;br&gt;                    &#x60;&#x60;&#x60; {\&quot;google\&quot; : { \&quot;status\&quot;: \&quot;success\&quot;, ... }, } &#x60;&#x60;&#x60; &lt;br&gt;                 When set to **false** the response structure is a list of response objects : &lt;br&gt;                     &#x60;&#x60;&#x60; [{\&quot;status\&quot;: \&quot;success\&quot;, \&quot;provider\&quot;: \&quot;google\&quot; ... }, ] &#x60;&#x60;&#x60;. &lt;br&gt;                    | [optional] [default to True]
**attributes_as_list** | **bool** | Optional : When set to **false** (default) the structure of the extracted items is list of objects having different attributes : &lt;br&gt;      &#x60;&#x60;&#x60;{&#39;items&#39;: [{\&quot;attribute_1\&quot;: \&quot;x1\&quot;,\&quot;attribute_2\&quot;: \&quot;y2\&quot;}, ... ]}&#x60;&#x60;&#x60; &lt;br&gt;      When it is set to **true**, the response contains an object with each attribute as a list : &lt;br&gt;      &#x60;&#x60;&#x60;{ \&quot;attribute_1\&quot;: [\&quot;x1\&quot;,\&quot;x2\&quot;, ...], \&quot;attribute_2\&quot;: [y1, y2, ...]}&#x60;&#x60;&#x60;  | [optional] [default to False]
**show_original_response** | **bool** | Optional : Shows the original response of the provider.&lt;br&gt;         When set to **true**, a new attribute *original_response* will appear in the response object. | [optional] [default to False]
**texts** | **List[str]** | List of texts to analyze | 
**question** | **str** | Question about the text content | 
**temperature** | **float** | Higher values mean the model will take more risks and value 0 (argmax sampling) works better for scenarios with a well-defined answer. | [optional] [default to 0.0]
**examples_context** | **str** | example text serving as context | 
**examples** | **List[List[str]]** | List of question/answer pairs (eg: [[&#39;When was Barack Obama elected president?&#39;, &#39;in 2009.&#39;],] | 

## Example

```python
from openapi_client.models.textquestion_answer_question_answer_request import TextquestionAnswerQuestionAnswerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TextquestionAnswerQuestionAnswerRequest from a JSON string
textquestion_answer_question_answer_request_instance = TextquestionAnswerQuestionAnswerRequest.from_json(json)
# print the JSON string representation of the object
print(TextquestionAnswerQuestionAnswerRequest.to_json())

# convert the object into a dict
textquestion_answer_question_answer_request_dict = textquestion_answer_question_answer_request_instance.to_dict()
# create an instance of TextquestionAnswerQuestionAnswerRequest from a dict
textquestion_answer_question_answer_request_form_dict = textquestion_answer_question_answer_request.from_dict(textquestion_answer_question_answer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


