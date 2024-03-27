# openapi_client.EmotionDetectionApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_text_emotion_detection_create**](EmotionDetectionApi.md#text_text_emotion_detection_create) | **POST** /text/emotion_detection | Emotion Detection


# **text_text_emotion_detection_create**
> TextemotionDetectionResponseModel text_text_emotion_detection_create(textemotion_detection_emotion_detection_request)

Emotion Detection

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**nlpcloud**|`v1`|25.0 (per 1000 request)|1 request |**vernai**|`v1`|2.0 (per 1000 request)|1 request   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textemotion_detection_emotion_detection_request import TextemotionDetectionEmotionDetectionRequest
from openapi_client.models.textemotion_detection_response_model import TextemotionDetectionResponseModel
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
    api_instance = openapi_client.EmotionDetectionApi(api_client)
    textemotion_detection_emotion_detection_request = {"providers":"nlpcloud,vernai","text":"I'm scared!"} # TextemotionDetectionEmotionDetectionRequest | 

    try:
        # Emotion Detection
        api_response = api_instance.text_text_emotion_detection_create(textemotion_detection_emotion_detection_request)
        print("The response of EmotionDetectionApi->text_text_emotion_detection_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmotionDetectionApi->text_text_emotion_detection_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **textemotion_detection_emotion_detection_request** | [**TextemotionDetectionEmotionDetectionRequest**](TextemotionDetectionEmotionDetectionRequest.md)|  | 

### Return type

[**TextemotionDetectionResponseModel**](TextemotionDetectionResponseModel.md)

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

