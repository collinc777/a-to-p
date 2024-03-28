# openapi_client.PromptOptimizationApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_text_prompt_optimization_create**](PromptOptimizationApi.md#text_text_prompt_optimization_create) | **POST** /text/prompt_optimization | Prompt Optimization


# **text_text_prompt_optimization_create**
> TextpromptOptimizationResponseModel text_text_prompt_optimization_create(textprompt_optimization_prompt_optimization_request)

Prompt Optimization

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**openai**|`v3.0.0`|0.08 (per 1 request)|1 request   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textprompt_optimization_prompt_optimization_request import TextpromptOptimizationPromptOptimizationRequest
from openapi_client.models.textprompt_optimization_response_model import TextpromptOptimizationResponseModel
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
    api_instance = openapi_client.PromptOptimizationApi(api_client)
    textprompt_optimization_prompt_optimization_request = {"providers":"openai","text":"Entity extractor, i give you an entity or multiple entities and a text and i want the entitites extracted from the text","target_provider":"google"} # TextpromptOptimizationPromptOptimizationRequest | 

    try:
        # Prompt Optimization
        api_response = await api_instance.text_text_prompt_optimization_create(textprompt_optimization_prompt_optimization_request)
        print("The response of PromptOptimizationApi->text_text_prompt_optimization_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptOptimizationApi->text_text_prompt_optimization_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **textprompt_optimization_prompt_optimization_request** | [**TextpromptOptimizationPromptOptimizationRequest**](TextpromptOptimizationPromptOptimizationRequest.md)|  | 

### Return type

[**TextpromptOptimizationResponseModel**](TextpromptOptimizationResponseModel.md)

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

