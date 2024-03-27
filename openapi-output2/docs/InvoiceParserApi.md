# openapi_client.InvoiceParserApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ocr_ocr_invoice_parser_create**](InvoiceParserApi.md#ocr_ocr_invoice_parser_create) | **POST** /ocr/invoice_parser | Invoice Parser


# **ocr_ocr_invoice_parser_create**
> OcrinvoiceParserResponseModel ocr_ocr_invoice_parser_create(ocrinvoice_parser_invoice_parser_request)

Invoice Parser

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**affinda**|`v3`|0.08 (per 1 page)|1 page |**base64**|`latest`|0.25 (per 1 page)|1 page |**dataleon**|`v4.0.0`|0.05 (per 1 page)|1 page |**microsoft**|`v2.1-preview.3`|0.01 (per 1 page)|1 page |**mindee**|`v2`|0.1 (per 1 page)|1 page |**amazon**|`boto3 1.26.8`|0.01 (per 1 page)|1 page |**google**|`DocumentAI v1 beta3`|0.01 (per 1 page)|10 page |**klippa**|`v1`|0.1 (per 1 file)|1 file |**veryfi**|`v8`|0.16 (per 1 file)|1 file   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Afrikaans**|`af`| |**Albanian**|`sq`| |**Arabic**|`ar`| |**Bengali**|`bn`| |**Bulgarian**|`bg`| |**Catalan**|`ca`| |**Chinese**|`zh`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dutch**|`nl`| |**English**|`en`| |**Estonian**|`et`| |**Finnish**|`fi`| |**French**|`fr`| |**German**|`de`| |**Gujarati**|`gu`| |**Hebrew**|`he`| |**Hindi**|`hi`| |**Hungarian**|`hu`| |**Indonesian**|`id`| |**Italian**|`it`| |**Japanese**|`ja`| |**Kannada**|`kn`| |**Korean**|`ko`| |**Latvian**|`lv`| |**Lithuanian**|`lt`| |**Macedonian**|`mk`| |**Malayalam**|`ml`| |**Marathi**|`mr`| |**Modern Greek (1453-)**|`el`| |**Nepali (macrolanguage)**|`ne`| |**Norwegian**|`no`| |**Panjabi**|`pa`| |**Persian**|`fa`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Romanian**|`ro`| |**Russian**|`ru`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**Spanish**|`es`| |**Swahili (macrolanguage)**|`sw`| |**Swedish**|`sv`| |**Tagalog**|`tl`| |**Tamil**|`ta`| |**Telugu**|`te`| |**Thai**|`th`| |**Turkish**|`tr`| |**Ukrainian**|`uk`| |**Urdu**|`ur`| |**Vietnamese**|`vi`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Chinese (China)**|`zh-cn`| |**Chinese (Taiwan)**|`zh-tw`| |**Danish (Denmark)**|`da-DK`| |**English (United States)**|`en-US`| |**French (France)**|`fr-FR`| |**German (Germany)**|`de-DE`| |**Italian (Italy)**|`it-IT`| |**Portuguese (Portugal)**|`pt-PT`| |**Spanish (Spain)**|`es-ES`|  </details><strong style='color:red;'>**Note:**</strong> This feature is likely to be deprecated in future releases. It is recommended to use the `financial_parser` feature as an alternative.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.ocrinvoice_parser_invoice_parser_request import OcrinvoiceParserInvoiceParserRequest
from openapi_client.models.ocrinvoice_parser_response_model import OcrinvoiceParserResponseModel
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
    api_instance = openapi_client.InvoiceParserApi(api_client)
    ocrinvoice_parser_invoice_parser_request = {"providers":"affinda,amazon,base64,veryfi,dataleon,mindee,microsoft,klippa,google","language":"en","file_url":"http://edenai-resource-example.png"} # OcrinvoiceParserInvoiceParserRequest | 

    try:
        # Invoice Parser
        api_response = api_instance.ocr_ocr_invoice_parser_create(ocrinvoice_parser_invoice_parser_request)
        print("The response of InvoiceParserApi->ocr_ocr_invoice_parser_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceParserApi->ocr_ocr_invoice_parser_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocrinvoice_parser_invoice_parser_request** | [**OcrinvoiceParserInvoiceParserRequest**](OcrinvoiceParserInvoiceParserRequest.md)|  | 

### Return type

[**OcrinvoiceParserResponseModel**](OcrinvoiceParserResponseModel.md)

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

