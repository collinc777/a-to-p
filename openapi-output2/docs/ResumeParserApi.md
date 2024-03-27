# openapi_client.ResumeParserApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ocr_ocr_resume_parser_create**](ResumeParserApi.md#ocr_ocr_resume_parser_create) | **POST** /ocr/resume_parser | Resume Parser


# **ocr_ocr_resume_parser_create**
> OcrresumeParserResponseModel ocr_ocr_resume_parser_create(ocrresume_parser_resume_parser_request)

Resume Parser

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**affinda**|`v3`|0.07 (per 1 file)|1 file |**hireability**|`hireability 1.0.0`|0.05 (per 1 file)|1 file |**klippa**|`v1`|0.1 (per 1 file)|1 file |**senseloaf**|`v3`|0.045 (per 1 file)|1 file |**extracta**|`v1`|0.1 (per 1 page)|1 page   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Afrikaans**|`af`| |**Albanian**|`sq`| |**Arabic**|`ar`| |**Bengali**|`bn`| |**Bulgarian**|`bg`| |**Chinese**|`zh`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dutch**|`nl`| |**English**|`en`| |**Estonian**|`et`| |**Finnish**|`fi`| |**French**|`fr`| |**German**|`de`| |**Gujarati**|`gu`| |**Hebrew**|`he`| |**Hindi**|`hi`| |**Hungarian**|`hu`| |**Indonesian**|`id`| |**Italian**|`it`| |**Japanese**|`ja`| |**Kannada**|`kn`| |**Korean**|`ko`| |**Latvian**|`lv`| |**Lithuanian**|`lt`| |**Macedonian**|`mk`| |**Malayalam**|`ml`| |**Marathi**|`mr`| |**Modern Greek (1453-)**|`el`| |**Nepali (macrolanguage)**|`ne`| |**Norwegian**|`no`| |**Panjabi**|`pa`| |**Persian**|`fa`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Romanian**|`ro`| |**Russian**|`ru`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**Spanish**|`es`| |**Swahili (macrolanguage)**|`sw`| |**Swedish**|`sv`| |**Tagalog**|`tl`| |**Tamil**|`ta`| |**Telugu**|`te`| |**Thai**|`th`| |**Turkish**|`tr`| |**Ukrainian**|`uk`| |**Urdu**|`ur`| |**Vietnamese**|`vi`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Chinese (China)**|`zh-cn`| |**Chinese (Taiwan)**|`zh-tw`|  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.ocrresume_parser_response_model import OcrresumeParserResponseModel
from openapi_client.models.ocrresume_parser_resume_parser_request import OcrresumeParserResumeParserRequest
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
    api_instance = openapi_client.ResumeParserApi(api_client)
    ocrresume_parser_resume_parser_request = {"providers":"senseloaf,affinda,extracta,klippa,hireability","file_url":"http://edenai-resource-example.pdf"} # OcrresumeParserResumeParserRequest | 

    try:
        # Resume Parser
        api_response = api_instance.ocr_ocr_resume_parser_create(ocrresume_parser_resume_parser_request)
        print("The response of ResumeParserApi->ocr_ocr_resume_parser_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResumeParserApi->ocr_ocr_resume_parser_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocrresume_parser_resume_parser_request** | [**OcrresumeParserResumeParserRequest**](OcrresumeParserResumeParserRequest.md)|  | 

### Return type

[**OcrresumeParserResponseModel**](OcrresumeParserResponseModel.md)

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

