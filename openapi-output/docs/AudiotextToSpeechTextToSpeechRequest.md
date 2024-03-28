# AudiotextToSpeechTextToSpeechRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | **str** | It can be one (ex: **&#39;amazon&#39;** or **&#39;google&#39;**) or multiple provider(s) (ex: **&#39;amazon,microsoft,google&#39;**)             that the data will be redirected to in order to get the processed results. | 
**fallback_providers** | **str** | Providers in this list will be used as fallback if the call to provider in &#x60;providers&#x60; parameter fails.     To use this feature, you must input **only one** provider in the &#x60;providers&#x60; parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn&#39;t fail.   *Doesn&#39;t work with async subfeatures.*      | [optional] 
**response_as_dict** | **bool** | Optional : When set to **true** (default), the response is an object of responses with providers names as keys : &lt;br&gt;                    &#x60;&#x60;&#x60; {\&quot;google\&quot; : { \&quot;status\&quot;: \&quot;success\&quot;, ... }, } &#x60;&#x60;&#x60; &lt;br&gt;                 When set to **false** the response structure is a list of response objects : &lt;br&gt;                     &#x60;&#x60;&#x60; [{\&quot;status\&quot;: \&quot;success\&quot;, \&quot;provider\&quot;: \&quot;google\&quot; ... }, ] &#x60;&#x60;&#x60;. &lt;br&gt;                    | [optional] [default to True]
**attributes_as_list** | **bool** | Optional : When set to **false** (default) the structure of the extracted items is list of objects having different attributes : &lt;br&gt;      &#x60;&#x60;&#x60;{&#39;items&#39;: [{\&quot;attribute_1\&quot;: \&quot;x1\&quot;,\&quot;attribute_2\&quot;: \&quot;y2\&quot;}, ... ]}&#x60;&#x60;&#x60; &lt;br&gt;      When it is set to **true**, the response contains an object with each attribute as a list : &lt;br&gt;      &#x60;&#x60;&#x60;{ \&quot;attribute_1\&quot;: [\&quot;x1\&quot;,\&quot;x2\&quot;, ...], \&quot;attribute_2\&quot;: [y1, y2, ...]}&#x60;&#x60;&#x60;  | [optional] [default to False]
**show_original_response** | **bool** | Optional : Shows the original response of the provider.&lt;br&gt;         When set to **true**, a new attribute *original_response* will appear in the response object. | [optional] [default to False]
**settings** | **str** | A dictionnary or a json object to specify specific models to use for some providers. &lt;br&gt;                     It can be in the following format: {\&quot;google\&quot; : \&quot;google_model\&quot;, \&quot;ibm\&quot;: \&quot;ibm_model\&quot;...}.                      **Caution**: setting models can be done only with &#x60;Content-Type&#x60; : &#x60;application/json&#x60;.                       | [optional] 
**text** | **str** | Text to analyze | 
**language** | **str** | Language code expected (ex: en, fr) | [optional] [default to '']
**option** | [**TextToSpeechAsyncRequestOption**](TextToSpeechAsyncRequestOption.md) |  | [optional] 
**rate** | **int** | Increase or decrease the speaking rate by expressing a positif or negatif number ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%) | [optional] [default to 0]
**pitch** | **int** | Increase or decrease the speaking pitch by expressing a positif or negatif number ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%) | [optional] [default to 0]
**volume** | **int** | Increase or decrease the audio volume by expressing a positif or negatif number ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%) | [optional] [default to 0]
**audio_format** | **str** | Optional parameter to specify the audio format in which the audio will be generated. By default,             audios are encoded in MP3, except for lovoai which use the wav container. | [optional] [default to '']
**sampling_rate** | **int** | Optional. The synthesis sample rate (in hertz) for this audio. When this is specified, the audio will be converted             either to the right passed value, or to a the nearest value acceptable by the provider | [optional] [default to 0]

## Example

```python
from openapi_client.models.audiotext_to_speech_text_to_speech_request import AudiotextToSpeechTextToSpeechRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AudiotextToSpeechTextToSpeechRequest from a JSON string
audiotext_to_speech_text_to_speech_request_instance = AudiotextToSpeechTextToSpeechRequest.from_json(json)
# print the JSON string representation of the object
print(AudiotextToSpeechTextToSpeechRequest.to_json())

# convert the object into a dict
audiotext_to_speech_text_to_speech_request_dict = audiotext_to_speech_text_to_speech_request_instance.to_dict()
# create an instance of AudiotextToSpeechTextToSpeechRequest from a dict
audiotext_to_speech_text_to_speech_request_form_dict = audiotext_to_speech_text_to_speech_request.from_dict(audiotext_to_speech_text_to_speech_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


