# openapi_client.LandmarkDetectionApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_image_landmark_detection_create**](LandmarkDetectionApi.md#image_image_landmark_detection_create) | **POST** /image/landmark_detection | Landmark Detection


# **image_image_landmark_detection_create**
> ImagelandmarkDetectionResponseModel image_image_landmark_detection_create(imageanonymizationimagelandmark_detectionimageexplicit_content_image_request)

Landmark Detection

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**google**|`v1`|1.5 (per 1000 file)|1 file |**microsoft**|`v3.2`|1.0 (per 1000 file)|1 file   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imageanonymizationimagelandmark_detectionimageexplicit_content_image_request import ImageanonymizationimagelandmarkDetectionimageexplicitContentImageRequest
from openapi_client.models.imagelandmark_detection_response_model import ImagelandmarkDetectionResponseModel
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
    api_instance = openapi_client.LandmarkDetectionApi(api_client)
    imageanonymizationimagelandmark_detectionimageexplicit_content_image_request = {"providers":"google,microsoft","file_url":"http://edenai-resource-example.jpg"} # ImageanonymizationimagelandmarkDetectionimageexplicitContentImageRequest | 

    try:
        # Landmark Detection
        api_response = api_instance.image_image_landmark_detection_create(imageanonymizationimagelandmark_detectionimageexplicit_content_image_request)
        print("The response of LandmarkDetectionApi->image_image_landmark_detection_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LandmarkDetectionApi->image_image_landmark_detection_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageanonymizationimagelandmark_detectionimageexplicit_content_image_request** | [**ImageanonymizationimagelandmarkDetectionimageexplicitContentImageRequest**](ImageanonymizationimagelandmarkDetectionimageexplicitContentImageRequest.md)|  | 

### Return type

[**ImagelandmarkDetectionResponseModel**](ImagelandmarkDetectionResponseModel.md)

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

