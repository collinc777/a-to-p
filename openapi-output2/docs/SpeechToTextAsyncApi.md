# openapi_client.SpeechToTextAsyncApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audio_audio_speech_to_text_async_create**](SpeechToTextAsyncApi.md#audio_audio_speech_to_text_async_create) | **POST** /audio/speech_to_text_async | Speech to Text Launch Job
[**audio_audio_speech_to_text_async_destroy**](SpeechToTextAsyncApi.md#audio_audio_speech_to_text_async_destroy) | **DELETE** /audio/speech_to_text_async | Speech to text delete Jobs
[**audio_audio_speech_to_text_async_retrieve**](SpeechToTextAsyncApi.md#audio_audio_speech_to_text_async_retrieve) | **GET** /audio/speech_to_text_async | Speech to Text List Jobs
[**audio_audio_speech_to_text_async_retrieve2**](SpeechToTextAsyncApi.md#audio_audio_speech_to_text_async_retrieve2) | **GET** /audio/speech_to_text_async/{public_id} | Speech to Text Get Job Results


# **audio_audio_speech_to_text_async_create**
> LaunchAsyncJobResponse audio_audio_speech_to_text_async_create(providers, fallback_providers=fallback_providers, show_original_response=show_original_response, webhook_receiver=webhook_receiver, users_webhook_parameters=users_webhook_parameters, settings=settings, provider_params=provider_params, file=file, file_url=file_url, language=language, speakers=speakers, profanity_filter=profanity_filter, custom_vocabulary=custom_vocabulary, convert_to_wav=convert_to_wav)

Speech to Text Launch Job

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**amazon**|-|`boto3 (v1.15.18)`|0.024 (per 60 seconde)|15 seconde |**google**|-|`v1p1beta1`|0.024 (per 60 seconde)|1 seconde |**ibm**|-|`v1`|0.02 (per 60 seconde)|1 seconde |**microsoft**|-|`v1.0`|0.0168 (per 60 seconde)|1 seconde |**revai**|-|`v1`|0.02 (per 60 seconde)|15 seconde |**symbl**|-|`v1`|0.027 (per 60 seconde)|60 seconde |**voci**|-|`v1`|0.0162 (per 60 seconde)|1 seconde |**neuralspace**|-|`v1`|0.024 (per 60 seconde)|60 seconde |**assembly**|-|`v2`|0.011 (per 60 seconde)|1 seconde |**deepgram**|**enhanced**|`v1`|0.0189 (per 60 seconde)|1 seconde |**deepgram**|-|`v1`|0.0189 (per 60 seconde)|1 seconde |**deepgram**|**base**|`v1`|0.0169 (per 60 seconde)|1 seconde |**openai**|-|`boto3 (v1.15.18)`|0.006 (per 60 seconde)|1 seconde |**speechmatics**|**enhanced**|`v2`|0.022 (per 60 seconde)|1 seconde |**speechmatics**|**standard**|`v2`|0.017 (per 60 seconde)|1 seconde |**speechmatics**|-|`v2`|0.022 (per 60 seconde)|1 seconde |**gladia**|-|`v1`|0.0102 (per 60 seconde)|1 seconde   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Afrikaans**|`af`| |**Albanian**|`sq`| |**Amharic**|`am`| |**Arabic**|`ar`| |**Armenian**|`hy`| |**Azerbaijani**|`az`| |**Bashkir**|`ba`| |**Basque**|`eu`| |**Belarusian**|`be`| |**Bengali**|`bn`| |**Bosnian**|`bs`| |**Breton**|`br`| |**Bulgarian**|`bg`| |**Burmese**|`my`| |**Catalan**|`ca`| |**Central Khmer**|`km`| |**Chinese**|`zh`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dutch**|`nl`| |**English**|`en`| |**Esperanto**|`eo`| |**Estonian**|`et`| |**Filipino**|`fil`| |**Finnish**|`fi`| |**French**|`fr`| |**Galician**|`gl`| |**Georgian**|`ka`| |**German**|`de`| |**Gujarati**|`gu`| |**Haitian**|`ht`| |**Hausa**|`ha`| |**Hebrew**|`he`| |**Hebrew**|`iw`| |**Hindi**|`hi`| |**Hungarian**|`hu`| |**Icelandic**|`is`| |**Indonesian**|`id`| |**Interlingua (International Auxiliary Language Association)**|`ia`| |**Irish**|`ga`| |**Italian**|`it`| |**Japanese**|`ja`| |**Javanese**|`jv`| |**Kannada**|`kn`| |**Kazakh**|`kk`| |**Korean**|`ko`| |**Lao**|`lo`| |**Latvian**|`lv`| |**Lingala**|`ln`| |**Lithuanian**|`lt`| |**Luxembourgish**|`lb`| |**Macedonian**|`mk`| |**Malagasy**|`mg`| |**Malay (macrolanguage)**|`ms`| |**Malayalam**|`ml`| |**Maltese**|`mt`| |**Mandarin Chinese**|`cmn`| |**Maori**|`mi`| |**Marathi**|`mr`| |**Modern Greek (1453-)**|`el`| |**Mongolian**|`mn`| |**Nepali (macrolanguage)**|`ne`| |**Norwegian**|`no`| |**Norwegian Bokmål**|`nb`| |**Occitan (post 1500)**|`oc`| |**Panjabi**|`pa`| |**Persian**|`fa`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Pushto**|`ps`| |**Romanian**|`mo`| |**Romanian**|`ro`| |**Russian**|`ru`| |**Serbian**|`sr`| |**Sindhi**|`sd`| |**Sinhala**|`si`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**Spanish**|`es`| |**Sundanese**|`su`| |**Swahili (macrolanguage)**|`sw`| |**Swedish**|`sv`| |**Tagalog**|`tl`| |**Tamil**|`ta`| |**Telugu**|`te`| |**Thai**|`th`| |**Turkish**|`tr`| |**Uighur**|`ug`| |**Ukrainian**|`uk`| |**Urdu**|`ur`| |**Uzbek**|`uz`| |**Vietnamese**|`vi`| |**Welsh**|`cy`| |**Wu Chinese**|`wuu`| |**Yiddish**|`yi`| |**Yoruba**|`yo`| |**Yue Chinese**|`yue`| |**Zulu**|`zu`| |**at**|`at`| |**jp**|`jp`| |**mymr**|`mymr`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Afrikaans (South Africa)**|`af-ZA`| |**Albanian (Albania)**|`sq-AL`| |**Amharic (Ethiopia)**|`am-ET`| |**Arabic (Algeria)**|`ar-DZ`| |**Arabic (Bahrain)**|`ar-BH`| |**Arabic (Egypt)**|`ar-EG`| |**Arabic (Iraq)**|`ar-IQ`| |**Arabic (Israel)**|`ar-IL`| |**Arabic (Jordan)**|`ar-JO`| |**Arabic (Kuwait)**|`ar-KW`| |**Arabic (Lebanon)**|`ar-LB`| |**Arabic (Libya)**|`ar-LY`| |**Arabic (Mauritania)**|`ar-MR`| |**Arabic (Montserrat)**|`ar-MS`| |**Arabic (Morocco)**|`ar-MA`| |**Arabic (Oman)**|`ar-OM`| |**Arabic (Palestinian Territories)**|`ar-PS`| |**Arabic (Qatar)**|`ar-QA`| |**Arabic (Saudi Arabia)**|`ar-SA`| |**Arabic (Syria)**|`ar-SY`| |**Arabic (Tunisia)**|`ar-TN`| |**Arabic (United Arab Emirates)**|`ar-AE`| |**Arabic (Yemen)**|`ar-YE`| |**Armenian (Armenia)**|`hy-AM`| |**Azerbaijani (Azerbaijan)**|`az-AZ`| |**Bangla (Bangladesh)**|`bn-BD`| |**Bangla (India)**|`bn-IN`| |**Basque (Spain)**|`eu-ES`| |**Bosnian (Bosnia & Herzegovina)**|`bs-BA`| |**Bulgarian (Bulgaria)**|`bg-BG`| |**Burmese (Myanmar (Burma))**|`my-MM`| |**Cantonese (China)**|`yue-CN`| |**Cantonese (Traditional, Hong Kong SAR China)**|`yue-Hant-HK`| |**Catalan (Spain)**|`ca-ES`| |**Chinese (China)**|`zh-CN`| |**Chinese (Hong Kong SAR China)**|`zh-HK`| |**Chinese (Taiwan)**|`zh-TW`| |**Croatian (Croatia)**|`hr-HR`| |**Czech (Czechia)**|`cs-CZ`| |**Danish (Denmark)**|`da-DK`| |**Dutch (Belgium)**|`nl-BE`| |**Dutch (Netherlands)**|`nl-NL`| |**English (Australia)**|`en-AU`| |**English (Canada)**|`en-CA`| |**English (Ghana)**|`en-GH`| |**English (Hong Kong SAR China)**|`en-HK`| |**English (India)**|`en-IN`| |**English (Ireland)**|`en-IE`| |**English (Kenya)**|`en-KE`| |**English (New Zealand)**|`en-NZ`| |**English (Nigeria)**|`en-NG`| |**English (Pakistan)**|`en-PK`| |**English (Philippines)**|`en-PH`| |**English (Singapore)**|`en-SG`| |**English (South Africa)**|`en-ZA`| |**English (Tanzania)**|`en-TZ`| |**English (United Kingdom)**|`en-GB`| |**English (United Kingdom)**|`en-UK`| |**English (United States)**|`en-US`| |**Estonian (Estonia)**|`et-EE`| |**Filipino (Philippines)**|`fil-PH`| |**Finnish (Finland)**|`fi-FI`| |**French (Belgium)**|`fr-BE`| |**French (Canada)**|`fr-CA`| |**French (France)**|`fr-FR`| |**French (Switzerland)**|`fr-CH`| |**Galician (Spain)**|`gl-ES`| |**Georgian (Georgia)**|`ka-GE`| |**German (Austria)**|`de-AT`| |**German (Germany)**|`de-DE`| |**German (Switzerland)**|`de-CH`| |**Greek (Greece)**|`el-GR`| |**Gujarati (India)**|`gu-IN`| |**Hebrew (Israel)**|`he-IL`| |**Hebrew (Israel)**|`iw-IL`| |**Hindi (India)**|`hi-IN`| |**Hindi (Latin)**|`hi-Latn`| |**Hungarian (Hungary)**|`hu-HU`| |**Icelandic (Iceland)**|`is-IS`| |**Indonesian (Indonesia)**|`id-ID`| |**Irish (Ireland)**|`ga-IE`| |**Italian (Italy)**|`it-IT`| |**Italian (Switzerland)**|`it-CH`| |**Japanese (Japan)**|`ja-JP`| |**Javanese (Indonesia)**|`jv-ID`| |**Kannada (India)**|`kn-IN`| |**Kazakh (Kazakhstan)**|`kk-KZ`| |**Khmer (Cambodia)**|`km-KH`| |**Korean (South Korea)**|`ko-KR`| |**Lao (Laos)**|`lo-LA`| |**Latvian (Latvia)**|`lv-LV`| |**Lithuanian (Lithuania)**|`lt-LT`| |**Macedonian (North Macedonia)**|`mk-MK`| |**Malay (Malaysia)**|`ms-MY`| |**Malayalam (India)**|`ml-IN`| |**Maltese (Malta)**|`mt-MT`| |**Marathi (India)**|`mr-IN`| |**Mongolian (Mongolia)**|`mn-MN`| |**Nepali (Nepal)**|`ne-NP`| |**Norwegian (Norway)**|`no-NO`| |**Norwegian Bokmål (Norway)**|`nb-NO`| |**Pashto (Afghanistan)**|`ps-AF`| |**Persian (Iran)**|`fa-IR`| |**Polish (Poland)**|`pl-PL`| |**Portuguese (Brazil)**|`pt-BR`| |**Portuguese (Portugal)**|`pt-PT`| |**Punjabi (India)**|`pa-Guru-IN`| |**Romanian (Romania)**|`ro-RO`| |**Russian (Russia)**|`ru-RU`| |**Serbian (Serbia)**|`sr-RS`| |**Sinhala (Sri Lanka)**|`si-LK`| |**Slovak (Slovakia)**|`sk-SK`| |**Slovenian (Slovenia)**|`sl-SI`| |**Somali (Somalia)**|`so-SO`| |**Spanish (Argentina)**|`es-AR`| |**Spanish (Bolivia)**|`es-BO`| |**Spanish (Chile)**|`es-CL`| |**Spanish (Colombia)**|`es-CO`| |**Spanish (Costa Rica)**|`es-CR`| |**Spanish (Cuba)**|`es-CU`| |**Spanish (Dominican Republic)**|`es-DO`| |**Spanish (Ecuador)**|`es-EC`| |**Spanish (El Salvador)**|`es-SV`| |**Spanish (Equatorial Guinea)**|`es-GQ`| |**Spanish (Guatemala)**|`es-GT`| |**Spanish (Honduras)**|`es-HN`| |**Spanish (Laos)**|`es-LA`| |**Spanish (Latin America)**|`es-419`| |**Spanish (Mexico)**|`es-MX`| |**Spanish (Nicaragua)**|`es-NI`| |**Spanish (Panama)**|`es-PA`| |**Spanish (Paraguay)**|`es-PY`| |**Spanish (Peru)**|`es-PE`| |**Spanish (Puerto Rico)**|`es-PR`| |**Spanish (Spain)**|`es-ES`| |**Spanish (United States)**|`es-US`| |**Spanish (Uruguay)**|`es-UY`| |**Spanish (Venezuela)**|`es-VE`| |**Sundanese (Indonesia)**|`su-ID`| |**Swahili (Kenya)**|`sw-KE`| |**Swahili (Tanzania)**|`sw-TZ`| |**Swedish (Sweden)**|`sv-SE`| |**Tamil (India)**|`ta-IN`| |**Tamil (Malaysia)**|`ta-MY`| |**Tamil (Singapore)**|`ta-SG`| |**Tamil (Sri Lanka)**|`ta-LK`| |**Telugu (India)**|`te-IN`| |**Thai (Thailand)**|`th-TH`| |**Turkish (Turkey)**|`tr-TR`| |**Ukrainian (Ukraine)**|`uk-UA`| |**Urdu (India)**|`ur-IN`| |**Urdu (Pakistan)**|`ur-PK`| |**Uzbek (Uzbekistan)**|`uz-UZ`| |**Vietnamese (Vietnam)**|`vi-VN`| |**Welsh (United Kingdom)**|`cy-GB`| |**Wu Chinese (China)**|`wuu-CN`| |**Zulu (South Africa)**|`zu-ZA`|  </details><details><summary>Supported Models</summary><details><summary>deepgram</summary>      |Name|Value| |----|-----| |**deepgram**|`base`| ||`enhanced`|  </details><details><summary>speechmatics</summary>      |Name|Value| |----|-----| |**speechmatics**|`enhanced`| ||`standard`|  </details>  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.launch_async_job_response import LaunchAsyncJobResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.edenai.run/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.edenai.run/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): FeatureApiAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SpeechToTextAsyncApi(api_client)
    providers = 'providers_example' # str | It can be one (ex: **'amazon'** or **'google'**) or multiple provider(s) (ex: **'amazon,microsoft,google'**)             that the data will be redirected to in order to get the processed results.
    fallback_providers = 'fallback_providers_example' # str | Providers in this list will be used as fallback if the call to provider in `providers` parameter fails.     To use this feature, you must input **only one** provider in the `providers` parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn't fail.   *Doesn't work with async subfeatures.*      (optional)
    show_original_response = False # bool | Optional : Shows the original response of the provider.<br>         When set to **true**, a new attribute *original_response* will appear in the response object. (optional) (default to False)
    webhook_receiver = 'webhook_receiver_example' # str | Webhook receiver should be a valid https URL (ex : https://your.listner.com/endpoint).             After the processing is done, the webhook endpoint will receive a POST request with the result. (optional)
    users_webhook_parameters = None # Dict[str, object] | Json data that contains of additional parameters that will be sent back to the webhook receiver             (ex: api key for security or client's data ID to link the result internally).             Will only be used when webhook_receiver is set. (optional)
    settings = 'settings_example' # str | A dictionnary or a json object to specify specific models to use for some providers. <br>                     It can be in the following format: {\\\"google\\\" : \\\"google_model\\\", \\\"ibm\\\": \\\"ibm_model\\\"...}.                      **Caution**: setting models can be done only with `Content-Type` : `application/json`.                       (optional)
    provider_params = 'provider_params_example' # str |  Parameters specific to the provider that you want to send along the request.  it should take a *provider* name as key and an object of parameters as value.  Example:      {       \\\"deepgram\\\": {         \\\"filler_words\\\": true,         \\\"smart_format\\\": true,         \\\"callback\\\": \\\"https://webhook.site/0000\\\"       },       \\\"assembly\\\": {         \\\"webhook_url\\\": \\\"https://webhook.site/0000\\\"       }     }  Please refer to the documentation of each provider to see which parameters to send.  (optional)
    file = None # bytearray | File to analyse in binary format to be used with *content-type*: **multipart/form-data** <br> **Does not work with application/json !** (optional)
    file_url = 'file_url_example' # str | File **URL** to analyse to be used with with *content-type*: **application/json**. (optional)
    language = 'language_example' # str | Language code expected (ex: en, fr) (optional)
    speakers = 2 # int | Number of speakers in the file audio (optional) (default to 2)
    profanity_filter = False # bool | Boolean value to specify weather or not the service will filter profanity and replace inappropriate words with a series of asterisks (optional) (default to False)
    custom_vocabulary = '' # str | List of words or composed words to be detected by the speech to text engine. (Ex: Word, Mike, Draw, Los Angeles,...) (optional) (default to '')
    convert_to_wav = False # bool | Boolean value to specify weather to convert the audio/video file to wav format to be accepted by a majority of the providers (optional) (default to False)

    try:
        # Speech to Text Launch Job
        api_response = api_instance.audio_audio_speech_to_text_async_create(providers, fallback_providers=fallback_providers, show_original_response=show_original_response, webhook_receiver=webhook_receiver, users_webhook_parameters=users_webhook_parameters, settings=settings, provider_params=provider_params, file=file, file_url=file_url, language=language, speakers=speakers, profanity_filter=profanity_filter, custom_vocabulary=custom_vocabulary, convert_to_wav=convert_to_wav)
        print("The response of SpeechToTextAsyncApi->audio_audio_speech_to_text_async_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpeechToTextAsyncApi->audio_audio_speech_to_text_async_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers** | **str**| It can be one (ex: **&#39;amazon&#39;** or **&#39;google&#39;**) or multiple provider(s) (ex: **&#39;amazon,microsoft,google&#39;**)             that the data will be redirected to in order to get the processed results. | 
 **fallback_providers** | **str**| Providers in this list will be used as fallback if the call to provider in &#x60;providers&#x60; parameter fails.     To use this feature, you must input **only one** provider in the &#x60;providers&#x60; parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn&#39;t fail.   *Doesn&#39;t work with async subfeatures.*      | [optional] 
 **show_original_response** | **bool**| Optional : Shows the original response of the provider.&lt;br&gt;         When set to **true**, a new attribute *original_response* will appear in the response object. | [optional] [default to False]
 **webhook_receiver** | **str**| Webhook receiver should be a valid https URL (ex : https://your.listner.com/endpoint).             After the processing is done, the webhook endpoint will receive a POST request with the result. | [optional] 
 **users_webhook_parameters** | [**Dict[str, object]**](Dict.md)| Json data that contains of additional parameters that will be sent back to the webhook receiver             (ex: api key for security or client&#39;s data ID to link the result internally).             Will only be used when webhook_receiver is set. | [optional] 
 **settings** | **str**| A dictionnary or a json object to specify specific models to use for some providers. &lt;br&gt;                     It can be in the following format: {\\\&quot;google\\\&quot; : \\\&quot;google_model\\\&quot;, \\\&quot;ibm\\\&quot;: \\\&quot;ibm_model\\\&quot;...}.                      **Caution**: setting models can be done only with &#x60;Content-Type&#x60; : &#x60;application/json&#x60;.                       | [optional] 
 **provider_params** | **str**|  Parameters specific to the provider that you want to send along the request.  it should take a *provider* name as key and an object of parameters as value.  Example:      {       \\\&quot;deepgram\\\&quot;: {         \\\&quot;filler_words\\\&quot;: true,         \\\&quot;smart_format\\\&quot;: true,         \\\&quot;callback\\\&quot;: \\\&quot;https://webhook.site/0000\\\&quot;       },       \\\&quot;assembly\\\&quot;: {         \\\&quot;webhook_url\\\&quot;: \\\&quot;https://webhook.site/0000\\\&quot;       }     }  Please refer to the documentation of each provider to see which parameters to send.  | [optional] 
 **file** | **bytearray**| File to analyse in binary format to be used with *content-type*: **multipart/form-data** &lt;br&gt; **Does not work with application/json !** | [optional] 
 **file_url** | **str**| File **URL** to analyse to be used with with *content-type*: **application/json**. | [optional] 
 **language** | **str**| Language code expected (ex: en, fr) | [optional] 
 **speakers** | **int**| Number of speakers in the file audio | [optional] [default to 2]
 **profanity_filter** | **bool**| Boolean value to specify weather or not the service will filter profanity and replace inappropriate words with a series of asterisks | [optional] [default to False]
 **custom_vocabulary** | **str**| List of words or composed words to be detected by the speech to text engine. (Ex: Word, Mike, Draw, Los Angeles,...) | [optional] [default to &#39;&#39;]
 **convert_to_wav** | **bool**| Boolean value to specify weather to convert the audio/video file to wav format to be accepted by a majority of the providers | [optional] [default to False]

### Return type

[**LaunchAsyncJobResponse**](LaunchAsyncJobResponse.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audio_audio_speech_to_text_async_destroy**
> audio_audio_speech_to_text_async_destroy()

Speech to text delete Jobs

Generic class to handle method GET all async job for user  Attributes:     feature (str): EdenAI feature     subfeature (str): EdenAI subfeature

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.edenai.run/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.edenai.run/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): FeatureApiAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SpeechToTextAsyncApi(api_client)

    try:
        # Speech to text delete Jobs
        api_instance.audio_audio_speech_to_text_async_destroy()
    except Exception as e:
        print("Exception when calling SpeechToTextAsyncApi->audio_audio_speech_to_text_async_destroy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audio_audio_speech_to_text_async_retrieve**
> ListAsyncJobResponse audio_audio_speech_to_text_async_retrieve()

Speech to Text List Jobs

Get a list of all jobs launched for this feature. You'll then be able to use the ID of each one to get its status and results.<br>                         Please note that a **job status doesn't get updated until a get request** is sent.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.list_async_job_response import ListAsyncJobResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.edenai.run/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.edenai.run/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): FeatureApiAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SpeechToTextAsyncApi(api_client)

    try:
        # Speech to Text List Jobs
        api_response = api_instance.audio_audio_speech_to_text_async_retrieve()
        print("The response of SpeechToTextAsyncApi->audio_audio_speech_to_text_async_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpeechToTextAsyncApi->audio_audio_speech_to_text_async_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListAsyncJobResponse**](ListAsyncJobResponse.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audio_audio_speech_to_text_async_retrieve2**
> AsyncaudiospeechToTextAsyncResponseModel audio_audio_speech_to_text_async_retrieve2(public_id, response_as_dict=response_as_dict, show_original_response=show_original_response)

Speech to Text Get Job Results

Get the status and results of an async job given its ID.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.asyncaudiospeech_to_text_async_response_model import AsyncaudiospeechToTextAsyncResponseModel
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.edenai.run/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.edenai.run/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): FeatureApiAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SpeechToTextAsyncApi(api_client)
    public_id = 'public_id_example' # str | 
    response_as_dict = True # bool |  (optional) (default to True)
    show_original_response = False # bool |  (optional) (default to False)

    try:
        # Speech to Text Get Job Results
        api_response = api_instance.audio_audio_speech_to_text_async_retrieve2(public_id, response_as_dict=response_as_dict, show_original_response=show_original_response)
        print("The response of SpeechToTextAsyncApi->audio_audio_speech_to_text_async_retrieve2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpeechToTextAsyncApi->audio_audio_speech_to_text_async_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**|  | 
 **response_as_dict** | **bool**|  | [optional] [default to True]
 **show_original_response** | **bool**|  | [optional] [default to False]

### Return type

[**AsyncaudiospeechToTextAsyncResponseModel**](AsyncaudiospeechToTextAsyncResponseModel.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

