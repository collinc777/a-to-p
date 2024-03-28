# openapi_client.PlagiaDetectionApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_text_plagia_detection_create**](PlagiaDetectionApi.md#text_text_plagia_detection_create) | **POST** /text/plagia_detection | Plagia Detection


# **text_text_plagia_detection_create**
> TextplagiaDetectionResponseModel text_text_plagia_detection_create(textplagia_detection_plagia_detection_request)

Plagia Detection

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**originalityai**|`v1`|0.01 (per 400 char)|400 char |**winstonai**|`v2`|14.0 (per 1000000 char)|1 char   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textplagia_detection_plagia_detection_request import TextplagiaDetectionPlagiaDetectionRequest
from openapi_client.models.textplagia_detection_response_model import TextplagiaDetectionResponseModel
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
    api_instance = openapi_client.PlagiaDetectionApi(api_client)
    textplagia_detection_plagia_detection_request = {"providers":"winstonai,originalityai","text":"The Galaxy S23 launch may be far behind us, but Samsung likely has plenty more to announce in 2023.             That's if history repeats itself. Should Samsung stick to its annual routine, we can expect to see new             foldable phones and wearable devices in August. The company also previewed new designs for bendable phones and tablets             earlier this year, hinting that the company may be planning to expand beyond the Z Fold and Z Flip in the near future.             Though Samsung regularly releases new products across many categories, including TVs, home appliances and monitors,             I'm most interested in where its mobile devices are headed. Samsung is one of the world's largest smartphone manufacturers             by market share, meaning it has more influence than most other tech companies on the devices we carry in our pockets each day.             Wearables have also become a large part of how Samsung intends to differentiate its phones from those of other Android device makers.             It's a strategy to create a web of products that keep people hooked, much like Apple's range of devices.","title":"n'importe nawak"} # TextplagiaDetectionPlagiaDetectionRequest | 

    try:
        # Plagia Detection
        api_response = await api_instance.text_text_plagia_detection_create(textplagia_detection_plagia_detection_request)
        print("The response of PlagiaDetectionApi->text_text_plagia_detection_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlagiaDetectionApi->text_text_plagia_detection_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **textplagia_detection_plagia_detection_request** | [**TextplagiaDetectionPlagiaDetectionRequest**](TextplagiaDetectionPlagiaDetectionRequest.md)|  | 

### Return type

[**TextplagiaDetectionResponseModel**](TextplagiaDetectionResponseModel.md)

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

