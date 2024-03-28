# openapi_client.CustomClassificationApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_text_custom_classification_create**](CustomClassificationApi.md#text_text_custom_classification_create) | **POST** /text/custom_classification | Custom Text Classification


# **text_text_custom_classification_create**
> TextcustomClassificationResponseModel text_text_custom_classification_create(textcustom_classification_custom_classification_request)

Custom Text Classification

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**cohere**|`2022-12-06`|2.0 (per 1000 request)|1 request |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textcustom_classification_custom_classification_request import TextcustomClassificationCustomClassificationRequest
from openapi_client.models.textcustom_classification_response_model import TextcustomClassificationResponseModel
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
    api_instance = openapi_client.CustomClassificationApi(api_client)
    textcustom_classification_custom_classification_request = {"providers":"openai,cohere","texts":["Confirm your email address","hey i need u to send some $"],"labels":["spam","not spam"],"examples":[["I need help please wire me $1000 right now","spam"],["Dermatologists dont like her!","spam"],["Please help me?","spam"],["Pre-read for tomorrow","not spam"],["Your parcel will be delivered today","not spam"],["Review changes to our Terms and Conditions","not spam"]]} # TextcustomClassificationCustomClassificationRequest | 

    try:
        # Custom Text Classification
        api_response = await api_instance.text_text_custom_classification_create(textcustom_classification_custom_classification_request)
        print("The response of CustomClassificationApi->text_text_custom_classification_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomClassificationApi->text_text_custom_classification_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **textcustom_classification_custom_classification_request** | [**TextcustomClassificationCustomClassificationRequest**](TextcustomClassificationCustomClassificationRequest.md)|  | 

### Return type

[**TextcustomClassificationResponseModel**](TextcustomClassificationResponseModel.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

