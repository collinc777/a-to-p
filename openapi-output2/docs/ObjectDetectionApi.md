# openapi_client.ObjectDetectionApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_image_object_detection_create**](ObjectDetectionApi.md#image_image_object_detection_create) | **POST** /image/object_detection | Object Detection


# **image_image_object_detection_create**
> ImageobjectDetectionResponseModel image_image_object_detection_create(imageobject_detection_object_detection_request)

Object Detection

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**amazon**|-|`boto3 (v1.15.18)`|1.0 (per 1000 file)|1 file |**api4ai**|-|`1.9.2`|0.5 (per 1000 file)|1 file |**clarifai**|-|`8.0.0`|2.0 (per 1000 file)|1 file |**google**|-|`v1`|2.25 (per 1000 file)|1 file |**microsoft**|-|`v3.2`|1.0 (per 1000 file)|1 file |**sentisight**|-|`v3.3.1`|1.0 (per 1000 file)|1 file   </details>  <details><summary>Supported Models</summary><details><summary>clarifai</summary>      |Name|Value| |----|-----| |**clarifai**|`apparel-detection`| ||`general-image-detection`| ||`hate-symbol-detection`| ||`people-detection-yolov5`| ||`weapon-detection`|  </details>  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imageobject_detection_object_detection_request import ImageobjectDetectionObjectDetectionRequest
from openapi_client.models.imageobject_detection_response_model import ImageobjectDetectionResponseModel
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
    api_instance = openapi_client.ObjectDetectionApi(api_client)
    imageobject_detection_object_detection_request = {"providers":"amazon,google,clarifai,api4ai,microsoft,sentisight","file_url":"http://edenai-resource-example.png"} # ImageobjectDetectionObjectDetectionRequest | 

    try:
        # Object Detection
        api_response = api_instance.image_image_object_detection_create(imageobject_detection_object_detection_request)
        print("The response of ObjectDetectionApi->image_image_object_detection_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDetectionApi->image_image_object_detection_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageobject_detection_object_detection_request** | [**ImageobjectDetectionObjectDetectionRequest**](ImageobjectDetectionObjectDetectionRequest.md)|  | 

### Return type

[**ImageobjectDetectionResponseModel**](ImageobjectDetectionResponseModel.md)

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

