# openapi_client.OcrTablesAsyncApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ocr_ocr_ocr_tables_async_create**](OcrTablesAsyncApi.md#ocr_ocr_ocr_tables_async_create) | **POST** /ocr/ocr_tables_async | OCR Tables Launch Job
[**ocr_ocr_ocr_tables_async_destroy**](OcrTablesAsyncApi.md#ocr_ocr_ocr_tables_async_destroy) | **DELETE** /ocr/ocr_tables_async | OCR Tables delete Jobs
[**ocr_ocr_ocr_tables_async_retrieve**](OcrTablesAsyncApi.md#ocr_ocr_ocr_tables_async_retrieve) | **GET** /ocr/ocr_tables_async | OCR Tables List Job
[**ocr_ocr_ocr_tables_async_retrieve2**](OcrTablesAsyncApi.md#ocr_ocr_ocr_tables_async_retrieve2) | **GET** /ocr/ocr_tables_async/{public_id} | OCR Tables Get Job Results


# **ocr_ocr_ocr_tables_async_create**
> LaunchAsyncJobResponse ocr_ocr_ocr_tables_async_create(providers, fallback_providers=fallback_providers, show_original_response=show_original_response, webhook_receiver=webhook_receiver, users_webhook_parameters=users_webhook_parameters, file=file, file_url=file_url, file_password=file_password, language=language)

OCR Tables Launch Job

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**amazon**|`boto3 (v1.15.18)`|15.0 (per 1000 page)|1 page |**google**|`DocumentAI v1 beta3`|65.0 (per 1000 page)|1 page |**microsoft**|`rest API 3.0`|10.0 (per 1000 page)|1 page   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Afrikaans**|`af`| |**Albanian**|`sq`| |**Angika**|`anp`| |**Arabic**|`ar`| |**Asturian**|`ast`| |**Awadhi**|`awa`| |**Azerbaijani**|`az`| |**Bagheli**|`bfy`| |**Basque**|`eu`| |**Belarusian**|`be`| |**Bhojpuri**|`bho`| |**Bislama**|`bi`| |**Bodo (India)**|`brx`| |**Bosnian**|`bs`| |**Braj**|`bra`| |**Breton**|`br`| |**Bulgarian**|`bg`| |**Bundeli**|`bns`| |**Buriat**|`bua`| |**Camling**|`rab`| |**Catalan**|`ca`| |**Cebuano**|`ceb`| |**Chamorro**|`ch`| |**Chhattisgarhi**|`hne`| |**Chinese**|`zh`| |**Cornish**|`kw`| |**Corsican**|`co`| |**Crimean Tatar**|`crh`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dari**|`prs`| |**Dhimal**|`dhi`| |**Dogri (macrolanguage)**|`doi`| |**Dutch**|`nl`| |**English**|`en`| |**Erzya**|`myv`| |**Estonian**|`et`| |**Faroese**|`fo`| |**Fijian**|`fj`| |**Filipino**|`fil`| |**Finnish**|`fi`| |**French**|`fr`| |**Friulian**|`fur`| |**Gagauz**|`gag`| |**Galician**|`gl`| |**German**|`de`| |**Gilbertese**|`gil`| |**Gondi**|`gon`| |**Gurung**|`gvr`| |**Haitian**|`ht`| |**Halbi**|`hlb`| |**Hani**|`hni`| |**Haryanvi**|`bgc`| |**Hawaiian**|`haw`| |**Hindi**|`hi`| |**Hmong Daw**|`mww`| |**Ho**|`hoc`| |**Hungarian**|`hu`| |**Icelandic**|`is`| |**Inari Sami**|`smn`| |**Indonesian**|`id`| |**Interlingua (International Auxiliary Language Association)**|`ia`| |**Inuktitut**|`iu`| |**Irish**|`ga`| |**Italian**|`it`| |**Japanese**|`ja`| |**Jaunsari**|`jns`| |**Javanese**|`jv`| |**K'iche'**|`quc`| |**Kabuverdianu**|`kea`| |**Kachin**|`kac`| |**Kalaallisut**|`kl`| |**Kangri**|`xnr`| |**Kara-Kalpak**|`kaa`| |**Karachay-Balkar**|`krc`| |**Kashubian**|`csb`| |**Kazakh**|`kk`| |**Khaling**|`klr`| |**Khasi**|`kha`| |**Kirghiz**|`ky`| |**Korean**|`ko`| |**Korku**|`kfq`| |**Koryak**|`kpy`| |**Kosraean**|`kos`| |**Kumarbhag Paharia**|`kmj`| |**Kumyk**|`kum`| |**Kurdish**|`ku`| |**Kurukh**|`kru`| |**Kölsch**|`ksh`| |**Lakota**|`lkt`| |**Latin**|`la`| |**Latvian**|`lv`| |**Lithuanian**|`lt`| |**Lower Sorbian**|`dsb`| |**Lule Sami**|`smj`| |**Luxembourgish**|`lb`| |**Mahasu Pahari**|`bfz`| |**Malay (macrolanguage)**|`ms`| |**Maltese**|`mt`| |**Manx**|`gv`| |**Maori**|`mi`| |**Marathi**|`mr`| |**Mongolian**|`mn`| |**Neapolitan**|`nap`| |**Nepali (macrolanguage)**|`ne`| |**Niuean**|`niu`| |**Nogai**|`nog`| |**Northern Sami**|`se`| |**Norwegian**|`no`| |**Occitan (post 1500)**|`oc`| |**Ossetian**|`os`| |**Panjabi**|`pa`| |**Persian**|`fa`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Pushto**|`ps`| |**Romanian**|`ro`| |**Romansh**|`rm`| |**Russian**|`ru`| |**Sadri**|`sck`| |**Samoan**|`sm`| |**Sanskrit**|`sa`| |**Santali**|`sat`| |**Scots**|`sco`| |**Scottish Gaelic**|`gd`| |**Serbian**|`sr`| |**Sherpa**|`xsr`| |**Sirmauri**|`srx`| |**Skolt Sami**|`sms`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**Southern Sami**|`sma`| |**Spanish**|`es`| |**Swahili (macrolanguage)**|`sw`| |**Swedish**|`sv`| |**Tagalog**|`tl`| |**Tajik**|`tg`| |**Tatar**|`tt`| |**Tetum**|`tet`| |**Thangmi**|`thf`| |**Tonga (Tonga Islands)**|`to`| |**Turkish**|`tr`| |**Turkmen**|`tk`| |**Tuvinian**|`tyv`| |**Uighur**|`ug`| |**Upper Sorbian**|`hsb`| |**Urdu**|`ur`| |**Uzbek**|`uz`| |**Vietnamese**|`vi`| |**Volapük**|`vo`| |**Walser**|`wae`| |**Welsh**|`cy`| |**Western Frisian**|`fy`| |**Yucateco**|`yua`| |**Zhuang**|`za`| |**Zulu**|`zu`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Belarusian**|`be-Cyrl`| |**Belarusian (Latin)**|`be-Latn`| |**Chinese (Simplified)**|`zh-Hans`| |**Chinese (Traditional)**|`zh-Hant`| |**Kara-Kalpak (Cyrillic)**|`kaa-Cyrl`| |**Kazakh**|`kk-Cyrl`| |**Kazakh (Latin)**|`kk-Latn`| |**Kurdish (Arabic)**|`ku-Arab`| |**Kurdish (Latin)**|`ku-Latn`| |**Serbian (Cyrillic)**|`sr-Cyrl`| |**Serbian (Cyrillic, Montenegro)**|`sr-Cyrl-ME`| |**Serbian (Latin)**|`sr-Latn`| |**Serbian (Latin, Montenegro)**|`sr-Latn-ME`| |**Serbian (Montenegro)**|`sr-ME`| |**Uzbek (Arabic)**|`uz-Arab`| |**Uzbek (Cyrillic)**|`uz-cyrl`|  </details>

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
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OcrTablesAsyncApi(api_client)
    providers = 'providers_example' # str | It can be one (ex: **'amazon'** or **'google'**) or multiple provider(s) (ex: **'amazon,microsoft,google'**)             that the data will be redirected to in order to get the processed results.
    fallback_providers = 'fallback_providers_example' # str | Providers in this list will be used as fallback if the call to provider in `providers` parameter fails.     To use this feature, you must input **only one** provider in the `providers` parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn't fail.   *Doesn't work with async subfeatures.*      (optional)
    show_original_response = False # bool | Optional : Shows the original response of the provider.<br>         When set to **true**, a new attribute *original_response* will appear in the response object. (optional) (default to False)
    webhook_receiver = 'webhook_receiver_example' # str | Webhook receiver should be a valid https URL (ex : https://your.listner.com/endpoint).             After the processing is done, the webhook endpoint will receive a POST request with the result. (optional)
    users_webhook_parameters = None # Dict[str, object] | Json data that contains of additional parameters that will be sent back to the webhook receiver             (ex: api key for security or client's data ID to link the result internally).             Will only be used when webhook_receiver is set. (optional)
    file = None # bytearray | File to analyse in binary format to be used with *content-type*: **multipart/form-data** <br> **Does not work with application/json !** (optional)
    file_url = 'file_url_example' # str | File **URL** to analyse to be used with with *content-type*: **application/json**. (optional)
    file_password = 'file_password_example' # str | If your PDF file has a password, you can pass it here! (optional)
    language = 'language_example' # str | Language code of the language the document is written in (ex: fr (French), en (English), es (Spanish)) (optional)

    try:
        # OCR Tables Launch Job
        api_response = await api_instance.ocr_ocr_ocr_tables_async_create(providers, fallback_providers=fallback_providers, show_original_response=show_original_response, webhook_receiver=webhook_receiver, users_webhook_parameters=users_webhook_parameters, file=file, file_url=file_url, file_password=file_password, language=language)
        print("The response of OcrTablesAsyncApi->ocr_ocr_ocr_tables_async_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OcrTablesAsyncApi->ocr_ocr_ocr_tables_async_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers** | **str**| It can be one (ex: **&#39;amazon&#39;** or **&#39;google&#39;**) or multiple provider(s) (ex: **&#39;amazon,microsoft,google&#39;**)             that the data will be redirected to in order to get the processed results. | 
 **fallback_providers** | **str**| Providers in this list will be used as fallback if the call to provider in &#x60;providers&#x60; parameter fails.     To use this feature, you must input **only one** provider in the &#x60;providers&#x60; parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn&#39;t fail.   *Doesn&#39;t work with async subfeatures.*      | [optional] 
 **show_original_response** | **bool**| Optional : Shows the original response of the provider.&lt;br&gt;         When set to **true**, a new attribute *original_response* will appear in the response object. | [optional] [default to False]
 **webhook_receiver** | **str**| Webhook receiver should be a valid https URL (ex : https://your.listner.com/endpoint).             After the processing is done, the webhook endpoint will receive a POST request with the result. | [optional] 
 **users_webhook_parameters** | [**Dict[str, object]**](Dict.md)| Json data that contains of additional parameters that will be sent back to the webhook receiver             (ex: api key for security or client&#39;s data ID to link the result internally).             Will only be used when webhook_receiver is set. | [optional] 
 **file** | **bytearray**| File to analyse in binary format to be used with *content-type*: **multipart/form-data** &lt;br&gt; **Does not work with application/json !** | [optional] 
 **file_url** | **str**| File **URL** to analyse to be used with with *content-type*: **application/json**. | [optional] 
 **file_password** | **str**| If your PDF file has a password, you can pass it here! | [optional] 
 **language** | **str**| Language code of the language the document is written in (ex: fr (French), en (English), es (Spanish)) | [optional] 

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

# **ocr_ocr_ocr_tables_async_destroy**
> ocr_ocr_ocr_tables_async_destroy()

OCR Tables delete Jobs

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
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OcrTablesAsyncApi(api_client)

    try:
        # OCR Tables delete Jobs
        await api_instance.ocr_ocr_ocr_tables_async_destroy()
    except Exception as e:
        print("Exception when calling OcrTablesAsyncApi->ocr_ocr_ocr_tables_async_destroy: %s\n" % e)
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

# **ocr_ocr_ocr_tables_async_retrieve**
> ListAsyncJobResponse ocr_ocr_ocr_tables_async_retrieve()

OCR Tables List Job

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
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OcrTablesAsyncApi(api_client)

    try:
        # OCR Tables List Job
        api_response = await api_instance.ocr_ocr_ocr_tables_async_retrieve()
        print("The response of OcrTablesAsyncApi->ocr_ocr_ocr_tables_async_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OcrTablesAsyncApi->ocr_ocr_ocr_tables_async_retrieve: %s\n" % e)
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

# **ocr_ocr_ocr_tables_async_retrieve2**
> AsyncocrocrTablesAsyncResponseModel ocr_ocr_ocr_tables_async_retrieve2(public_id, response_as_dict=response_as_dict, show_original_response=show_original_response)

OCR Tables Get Job Results

Get the status and results of an async job given its ID.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.asyncocrocr_tables_async_response_model import AsyncocrocrTablesAsyncResponseModel
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
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OcrTablesAsyncApi(api_client)
    public_id = 'public_id_example' # str | 
    response_as_dict = True # bool |  (optional) (default to True)
    show_original_response = False # bool |  (optional) (default to False)

    try:
        # OCR Tables Get Job Results
        api_response = await api_instance.ocr_ocr_ocr_tables_async_retrieve2(public_id, response_as_dict=response_as_dict, show_original_response=show_original_response)
        print("The response of OcrTablesAsyncApi->ocr_ocr_ocr_tables_async_retrieve2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OcrTablesAsyncApi->ocr_ocr_ocr_tables_async_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**|  | 
 **response_as_dict** | **bool**|  | [optional] [default to True]
 **show_original_response** | **bool**|  | [optional] [default to False]

### Return type

[**AsyncocrocrTablesAsyncResponseModel**](AsyncocrocrTablesAsyncResponseModel.md)

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

