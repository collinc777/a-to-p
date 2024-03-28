# openapi_client.FaceDetectionApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_image_face_detection_create**](FaceDetectionApi.md#image_image_face_detection_create) | **POST** /image/face_detection | Face Detection


# **image_image_face_detection_create**
> ImagefaceDetectionResponseModel image_image_face_detection_create(imageface_detection_face_detection_request)

Face Detection

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000 file)|1 file |**clarifai**|`8.0.0`|2.0 (per 1000 file)|1 file |**google**|`v1`|1.5 (per 1000 file)|1 file |**microsoft**|`v3.2`|1.0 (per 1000 file)|1 file |**api4ai**|`v1.0.0`|0.75 (per 1000 file)|1 file |**picpurify**|`v1.1`|1.2 (per 1000 file)|1 file |**skybiometry**|`v1`|1.0 (per 1000 file)|1 file   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imageface_detection_face_detection_request import ImagefaceDetectionFaceDetectionRequest
from openapi_client.models.imageface_detection_response_model import ImagefaceDetectionResponseModel
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
    api_instance = openapi_client.FaceDetectionApi(api_client)
    imageface_detection_face_detection_request = {"providers":"google,amazon,api4ai,clarifai,microsoft,skybiometry,picpurify","file_url":"http://edenai-resource-example.jpg"} # ImagefaceDetectionFaceDetectionRequest | 

    try:
        # Face Detection
        api_response = await api_instance.image_image_face_detection_create(imageface_detection_face_detection_request)
        print("The response of FaceDetectionApi->image_image_face_detection_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FaceDetectionApi->image_image_face_detection_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageface_detection_face_detection_request** | [**ImagefaceDetectionFaceDetectionRequest**](ImagefaceDetectionFaceDetectionRequest.md)|  | 

### Return type

[**ImagefaceDetectionResponseModel**](ImagefaceDetectionResponseModel.md)

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

