# openapi_client.FinancialParserApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ocr_ocr_financial_parser_create**](FinancialParserApi.md#ocr_ocr_financial_parser_create) | **POST** /ocr/financial_parser | Financial Parser


# **ocr_ocr_financial_parser_create**
> OcrfinancialParserResponseModel ocr_ocr_financial_parser_create(ocrfinancial_parser_financial_parser_request)

Financial Parser

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Document Type|Price|Billing unit| |----|-------|------|-----|------------| |**affinda**|`v3`|`invoice`|0.08 (per 1 page)|1 page |**affinda**|`v3`|`receipt`|0.07 (per 1 page)|1 page |**amazon**|`boto3 1.26.8`|-|0.01 (per 1 page)|1 page |**base64**|`latest`|-|0.25 (per 1 page)|1 page |**dataleon**|`v4.0.0`|-|0.05 (per 1 page)|1 page |**google**|`DocumentAI v1 beta3`|-|0.01 (per 1 page)|10 page |**klippa**|`v1`|-|0.1 (per 1 file)|1 file |**microsoft**|`v2.1-preview.3`|-|0.01 (per 1 page)|1 page |**mindee**|`v1.2`|-|0.1 (per 1 page)|1 page |**tabscanner**|`latest`|-|0.08 (per 1 page)|1 page |**veryfi**|`v8`|`receipt`|0.08 (per 1 file)|1 file |**veryfi**|`v8`|`invoice`|0.16 (per 1 file)|1 file   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Afrikaans**|`af`| |**Albanian**|`sq`| |**Arabic**|`ar`| |**Bengali**|`bn`| |**Bulgarian**|`bg`| |**Catalan**|`ca`| |**Chinese**|`zh`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dutch**|`nl`| |**English**|`en`| |**Estonian**|`et`| |**Finnish**|`fi`| |**French**|`fr`| |**German**|`de`| |**Gujarati**|`gu`| |**Hebrew**|`he`| |**Hindi**|`hi`| |**Hungarian**|`hu`| |**Indonesian**|`id`| |**Italian**|`it`| |**Japanese**|`ja`| |**Kannada**|`kn`| |**Korean**|`ko`| |**Latvian**|`lv`| |**Lithuanian**|`lt`| |**Macedonian**|`mk`| |**Malayalam**|`ml`| |**Marathi**|`mr`| |**Modern Greek (1453-)**|`el`| |**Nepali (macrolanguage)**|`ne`| |**Norwegian**|`no`| |**Panjabi**|`pa`| |**Persian**|`fa`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Romanian**|`ro`| |**Russian**|`ru`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**Spanish**|`es`| |**Swahili (macrolanguage)**|`sw`| |**Swedish**|`sv`| |**Tagalog**|`tl`| |**Tamil**|`ta`| |**Telugu**|`te`| |**Thai**|`th`| |**Turkish**|`tr`| |**Ukrainian**|`uk`| |**Urdu**|`ur`| |**Vietnamese**|`vi`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Catalan (Spain)**|`ca-ES`| |**Chinese (China)**|`zh-cn`| |**Chinese (Taiwan)**|`zh-tw`| |**Danish (Denmark)**|`da-DK`| |**Dutch (Netherlands)**|`nl-NL`| |**English (United Kingdom)**|`en-GB`| |**English (United States)**|`en-US`| |**French (Canada)**|`fr-CA`| |**French (France)**|`fr-FR`| |**French (Switzerland)**|`fr-CH`| |**German (Germany)**|`de-DE`| |**German (Switzerland)**|`de-CH`| |**Italian (Italy)**|`it-IT`| |**Italian (Switzerland)**|`it-CH`| |**Portuguese (Portugal)**|`pt-PT`| |**Spanish (Spain)**|`es-ES`|  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.ocrfinancial_parser_financial_parser_request import OcrfinancialParserFinancialParserRequest
from openapi_client.models.ocrfinancial_parser_response_model import OcrfinancialParserResponseModel
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
    api_instance = openapi_client.FinancialParserApi(api_client)
    ocrfinancial_parser_financial_parser_request = {"providers":"tabscanner,veryfi,affinda,amazon,base64,dataleon,google,klippa,microsoft,mindee","language":"en","document_type":"invoice","file_url":"http://edenai-resource-example.png"} # OcrfinancialParserFinancialParserRequest | 

    try:
        # Financial Parser
        api_response = api_instance.ocr_ocr_financial_parser_create(ocrfinancial_parser_financial_parser_request)
        print("The response of FinancialParserApi->ocr_ocr_financial_parser_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinancialParserApi->ocr_ocr_financial_parser_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocrfinancial_parser_financial_parser_request** | [**OcrfinancialParserFinancialParserRequest**](OcrfinancialParserFinancialParserRequest.md)|  | 

### Return type

[**OcrfinancialParserResponseModel**](OcrfinancialParserResponseModel.md)

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

