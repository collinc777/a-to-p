# openapi_client.DocumentTranslationApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translation_translation_document_translation_create**](DocumentTranslationApi.md#translation_translation_document_translation_create) | **POST** /translation/document_translation | Document Translation


# **translation_translation_document_translation_create**
> TranslationdocumentTranslationResponseModel translation_translation_document_translation_create(translationdocument_translation_document_translation_request)

Document Translation

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**deepl**|`v2`|2.0 (per 20 page)|20 page |**google**|`v3`|0.08 (per 1 page)|1 page   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Afrikaans**|`af`| |**Albanian**|`sq`| |**Amharic**|`am`| |**Arabic**|`ar`| |**Armenian**|`hy`| |**Azerbaijani**|`az`| |**Basque**|`eu`| |**Belarusian**|`be`| |**Bengali**|`bn`| |**Bosnian**|`bs`| |**Bulgarian**|`bg`| |**Burmese**|`my`| |**Catalan**|`ca`| |**Cebuano**|`ceb`| |**Central Khmer**|`km`| |**Chinese**|`zh`| |**Corsican**|`co`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dutch**|`nl`| |**English**|`en`| |**Esperanto**|`eo`| |**Estonian**|`et`| |**Finnish**|`fi`| |**French**|`fr`| |**Galician**|`gl`| |**Georgian**|`ka`| |**German**|`de`| |**Gujarati**|`gu`| |**Haitian**|`ht`| |**Hausa**|`ha`| |**Hawaiian**|`haw`| |**Hebrew**|`he`| |**Hindi**|`hi`| |**Hmong**|`hmn`| |**Hungarian**|`hu`| |**Icelandic**|`is`| |**Igbo**|`ig`| |**Indonesian**|`id`| |**Irish**|`ga`| |**Italian**|`it`| |**Japanese**|`ja`| |**Javanese**|`jv`| |**Kannada**|`kn`| |**Kazakh**|`kk`| |**Kinyarwanda**|`rw`| |**Kirghiz**|`ky`| |**Korean**|`ko`| |**Kurdish**|`ku`| |**Lao**|`lo`| |**Latin**|`la`| |**Latvian**|`lv`| |**Lithuanian**|`lt`| |**Luxembourgish**|`lb`| |**Macedonian**|`mk`| |**Malagasy**|`mg`| |**Malay (macrolanguage)**|`ms`| |**Malayalam**|`ml`| |**Maltese**|`mt`| |**Maori**|`mi`| |**Marathi**|`mr`| |**Modern Greek (1453-)**|`el`| |**Mongolian**|`mn`| |**Nepali (macrolanguage)**|`ne`| |**Norwegian**|`no`| |**Nyanja**|`ny`| |**Oriya (macrolanguage)**|`or`| |**Panjabi**|`pa`| |**Persian**|`fa`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Pushto**|`ps`| |**Romanian**|`ro`| |**Russian**|`ru`| |**Samoan**|`sm`| |**Scottish Gaelic**|`gd`| |**Serbian**|`sr`| |**Shona**|`sn`| |**Sindhi**|`sd`| |**Sinhala**|`si`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**Southern Sotho**|`st`| |**Spanish**|`es`| |**Sundanese**|`su`| |**Swahili (macrolanguage)**|`sw`| |**Swedish**|`sv`| |**Tagalog**|`tl`| |**Tajik**|`tg`| |**Tamil**|`ta`| |**Tatar**|`tt`| |**Telugu**|`te`| |**Thai**|`th`| |**Turkish**|`tr`| |**Turkmen**|`tk`| |**Uighur**|`ug`| |**Ukrainian**|`uk`| |**Urdu**|`ur`| |**Uzbek**|`uz`| |**Vietnamese**|`vi`| |**Welsh**|`cy`| |**Western Frisian**|`fy`| |**Xhosa**|`xh`| |**Yiddish**|`yi`| |**Yoruba**|`yo`| |**Zulu**|`zu`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Chinese (China)**|`zh-CN`| |**Chinese (Taiwan)**|`zh-TW`|  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.translationdocument_translation_document_translation_request import TranslationdocumentTranslationDocumentTranslationRequest
from openapi_client.models.translationdocument_translation_response_model import TranslationdocumentTranslationResponseModel
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
    api_instance = openapi_client.DocumentTranslationApi(api_client)
    translationdocument_translation_document_translation_request = {"providers":"google,deepl","source_language":"en","target_language":"fr","file_url":"http://edenai-resource-example.pdf"} # TranslationdocumentTranslationDocumentTranslationRequest | 

    try:
        # Document Translation
        api_response = await api_instance.translation_translation_document_translation_create(translationdocument_translation_document_translation_request)
        print("The response of DocumentTranslationApi->translation_translation_document_translation_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentTranslationApi->translation_translation_document_translation_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translationdocument_translation_document_translation_request** | [**TranslationdocumentTranslationDocumentTranslationRequest**](TranslationdocumentTranslationDocumentTranslationRequest.md)|  | 

### Return type

[**TranslationdocumentTranslationResponseModel**](TranslationdocumentTranslationResponseModel.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
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

