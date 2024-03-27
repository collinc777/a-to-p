# openapi_client.IdentityParserApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ocr_ocr_identity_parser_create**](IdentityParserApi.md#ocr_ocr_identity_parser_create) | **POST** /ocr/identity_parser | Identity Parser


# **ocr_ocr_identity_parser_create**
> OcridentityParserResponseModel ocr_ocr_identity_parser_create(ocridentity_parser_identity_parser_request)

Identity Parser

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**amazon**|`boto3 (v1.15.18)`|0.025 (per 1 page)|1 page |**base64**|`latest`|0.2 (per 1 page)|1 page |**microsoft**|`rest API 3.0`|0.01 (per 1 page)|1 page |**mindee**|`v2`|0.1 (per 1 page)|1 page |**klippa**|`v1`|0.1 (per 1 file)|1 file |**affinda**|`v3`|0.07 (per 1 file)|1 file   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Afrikaans**|`af`| |**Albanian**|`sq`| |**Arabic**|`ar`| |**Bengali**|`bn`| |**Bulgarian**|`bg`| |**Chinese**|`zh`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dutch**|`nl`| |**English**|`en`| |**Estonian**|`et`| |**Finnish**|`fi`| |**French**|`fr`| |**German**|`de`| |**Gujarati**|`gu`| |**Hebrew**|`he`| |**Hindi**|`hi`| |**Hungarian**|`hu`| |**Indonesian**|`id`| |**Italian**|`it`| |**Japanese**|`ja`| |**Kannada**|`kn`| |**Korean**|`ko`| |**Latvian**|`lv`| |**Lithuanian**|`lt`| |**Macedonian**|`mk`| |**Malayalam**|`ml`| |**Marathi**|`mr`| |**Modern Greek (1453-)**|`el`| |**Nepali (macrolanguage)**|`ne`| |**Norwegian**|`no`| |**Panjabi**|`pa`| |**Persian**|`fa`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Romanian**|`ro`| |**Russian**|`ru`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**Spanish**|`es`| |**Swahili (macrolanguage)**|`sw`| |**Swedish**|`sv`| |**Tagalog**|`tl`| |**Tamil**|`ta`| |**Telugu**|`te`| |**Thai**|`th`| |**Turkish**|`tr`| |**Ukrainian**|`uk`| |**Urdu**|`ur`| |**Vietnamese**|`vi`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Chinese (China)**|`zh-cn`| |**Chinese (Taiwan)**|`zh-tw`| |**English (United States)**|`en-US`| |**French (France)**|`fr-FR`| |**German (Germany)**|`de-DE`| |**Italian (Italy)**|`it-IT`| |**Portuguese (Portugal)**|`pt-PT`| |**Spanish (Spain)**|`es-ES`|  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.ocridentity_parser_identity_parser_request import OcridentityParserIdentityParserRequest
from openapi_client.models.ocridentity_parser_response_model import OcridentityParserResponseModel
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
    api_instance = openapi_client.IdentityParserApi(api_client)
    ocridentity_parser_identity_parser_request = {"providers":"amazon,microsoft,mindee,klippa,base64,affinda","file_url":"http://edenai-resource-example.pdf"} # OcridentityParserIdentityParserRequest | 

    try:
        # Identity Parser
        api_response = api_instance.ocr_ocr_identity_parser_create(ocridentity_parser_identity_parser_request)
        print("The response of IdentityParserApi->ocr_ocr_identity_parser_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityParserApi->ocr_ocr_identity_parser_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocridentity_parser_identity_parser_request** | [**OcridentityParserIdentityParserRequest**](OcridentityParserIdentityParserRequest.md)|  | 

### Return type

[**OcridentityParserResponseModel**](OcridentityParserResponseModel.md)

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

