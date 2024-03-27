# openapi_client.BankCheckParsingApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ocr_ocr_bank_check_parsing_create**](BankCheckParsingApi.md#ocr_ocr_bank_check_parsing_create) | **POST** /ocr/bank_check_parsing | Bank Check Parsing


# **ocr_ocr_bank_check_parsing_create**
> OcrbankCheckParsingResponseModel ocr_ocr_bank_check_parsing_create(ocrbank_check_parsing_bank_check_parsing_request)

Bank Check Parsing

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**base64**|`latest`|0.25 (per 1 page)|1 page |**veryfi**|`v8`|0.16 (per 1 request)|1 request |**mindee**|`v1`|0.1 (per 1 page)|1 page |**extracta**|`v1`|0.1 (per 1 page)|1 page   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.ocrbank_check_parsing_bank_check_parsing_request import OcrbankCheckParsingBankCheckParsingRequest
from openapi_client.models.ocrbank_check_parsing_response_model import OcrbankCheckParsingResponseModel
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
    api_instance = openapi_client.BankCheckParsingApi(api_client)
    ocrbank_check_parsing_bank_check_parsing_request = {"providers":"extracta,veryfi,base64,mindee","file_url":"http://edenai-resource-example.jpg"} # OcrbankCheckParsingBankCheckParsingRequest | 

    try:
        # Bank Check Parsing
        api_response = api_instance.ocr_ocr_bank_check_parsing_create(ocrbank_check_parsing_bank_check_parsing_request)
        print("The response of BankCheckParsingApi->ocr_ocr_bank_check_parsing_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankCheckParsingApi->ocr_ocr_bank_check_parsing_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocrbank_check_parsing_bank_check_parsing_request** | [**OcrbankCheckParsingBankCheckParsingRequest**](OcrbankCheckParsingBankCheckParsingRequest.md)|  | 

### Return type

[**OcrbankCheckParsingResponseModel**](OcrbankCheckParsingResponseModel.md)

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

