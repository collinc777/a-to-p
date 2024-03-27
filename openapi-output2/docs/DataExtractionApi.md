# openapi_client.DataExtractionApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ocr_ocr_data_extraction_create**](DataExtractionApi.md#ocr_ocr_data_extraction_create) | **POST** /ocr/data_extraction | Data Extraction


# **ocr_ocr_data_extraction_create**
> OcrdataExtractionResponseModel ocr_ocr_data_extraction_create(ocrdata_extraction_data_extraction_request)

Data Extraction

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**amazon**|`boto3 (v1.15.18)`|0.05 (per 1 page)|1 page |**base64**|`latest`|0.25 (per 1 page)|1 page   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.ocrdata_extraction_data_extraction_request import OcrdataExtractionDataExtractionRequest
from openapi_client.models.ocrdata_extraction_response_model import OcrdataExtractionResponseModel
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
    api_instance = openapi_client.DataExtractionApi(api_client)
    ocrdata_extraction_data_extraction_request = {"providers":"amazon,base64","file_url":"http://edenai-resource-example.png"} # OcrdataExtractionDataExtractionRequest | 

    try:
        # Data Extraction
        api_response = api_instance.ocr_ocr_data_extraction_create(ocrdata_extraction_data_extraction_request)
        print("The response of DataExtractionApi->ocr_ocr_data_extraction_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataExtractionApi->ocr_ocr_data_extraction_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocrdata_extraction_data_extraction_request** | [**OcrdataExtractionDataExtractionRequest**](OcrdataExtractionDataExtractionRequest.md)|  | 

### Return type

[**OcrdataExtractionResponseModel**](OcrdataExtractionResponseModel.md)

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

