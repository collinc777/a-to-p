# openapi_client.FaceRecognitionApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_image_face_recognition_add_face_create**](FaceRecognitionApi.md#image_image_face_recognition_add_face_create) | **POST** /image/face_recognition/add_face | Face Recognition - Add Face
[**image_image_face_recognition_delete_face_create**](FaceRecognitionApi.md#image_image_face_recognition_delete_face_create) | **POST** /image/face_recognition/delete_face | Face Recognition - Delete Face
[**image_image_face_recognition_list_faces_retrieve**](FaceRecognitionApi.md#image_image_face_recognition_list_faces_retrieve) | **GET** /image/face_recognition/list_faces | Face Recognition - List Faces
[**image_image_face_recognition_recognize_create**](FaceRecognitionApi.md#image_image_face_recognition_recognize_create) | **POST** /image/face_recognition/recognize | Face Recognition - Recognize Face


# **image_image_face_recognition_add_face_create**
> ImagefaceRecognitionResponseModel image_image_face_recognition_add_face_create(imageface_recognitionrecognizeimageface_recognitionadd_face_face_recognition_detect_face_request)

Face Recognition - Add Face

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**amazon**|`boto3 1.26.8`|1.0 (per 1000 file)|1 file |**facepp**|`v3`|0.6 (per 1000 request)|1 request   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imageface_recognition_response_model import ImagefaceRecognitionResponseModel
from openapi_client.models.imageface_recognitionrecognizeimageface_recognitionadd_face_face_recognition_detect_face_request import ImagefaceRecognitionrecognizeimagefaceRecognitionaddFaceFaceRecognitionDetectFaceRequest
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
    api_instance = openapi_client.FaceRecognitionApi(api_client)
    imageface_recognitionrecognizeimageface_recognitionadd_face_face_recognition_detect_face_request = {"providers":"amazon,facepp,facepp,facepp,facepp,amazon,amazon,amazon","file_url":"http://edenai-resource-example.jpg"} # ImagefaceRecognitionrecognizeimagefaceRecognitionaddFaceFaceRecognitionDetectFaceRequest | 

    try:
        # Face Recognition - Add Face
        api_response = await api_instance.image_image_face_recognition_add_face_create(imageface_recognitionrecognizeimageface_recognitionadd_face_face_recognition_detect_face_request)
        print("The response of FaceRecognitionApi->image_image_face_recognition_add_face_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FaceRecognitionApi->image_image_face_recognition_add_face_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageface_recognitionrecognizeimageface_recognitionadd_face_face_recognition_detect_face_request** | [**ImagefaceRecognitionrecognizeimagefaceRecognitionaddFaceFaceRecognitionDetectFaceRequest**](ImagefaceRecognitionrecognizeimagefaceRecognitionaddFaceFaceRecognitionDetectFaceRequest.md)|  | 

### Return type

[**ImagefaceRecognitionResponseModel**](ImagefaceRecognitionResponseModel.md)

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

# **image_image_face_recognition_delete_face_create**
> ImagefaceRecognitionResponseModel image_image_face_recognition_delete_face_create(imageface_recognitiondelete_face_face_recognition_delete_face_request)

Face Recognition - Delete Face

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**amazon**|`boto3 1.26.8`|free|- |**facepp**|`v3`|0.1 (per 1000 request)|1 request   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imageface_recognition_response_model import ImagefaceRecognitionResponseModel
from openapi_client.models.imageface_recognitiondelete_face_face_recognition_delete_face_request import ImagefaceRecognitiondeleteFaceFaceRecognitionDeleteFaceRequest
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
    api_instance = openapi_client.FaceRecognitionApi(api_client)
    imageface_recognitiondelete_face_face_recognition_delete_face_request = {"providers":"amazon,facepp,facepp,facepp,facepp,amazon,amazon,amazon","face_id":"cfe63a35-be87-4741-ae32-eed12f123be5"} # ImagefaceRecognitiondeleteFaceFaceRecognitionDeleteFaceRequest | 

    try:
        # Face Recognition - Delete Face
        api_response = await api_instance.image_image_face_recognition_delete_face_create(imageface_recognitiondelete_face_face_recognition_delete_face_request)
        print("The response of FaceRecognitionApi->image_image_face_recognition_delete_face_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FaceRecognitionApi->image_image_face_recognition_delete_face_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageface_recognitiondelete_face_face_recognition_delete_face_request** | [**ImagefaceRecognitiondeleteFaceFaceRecognitionDeleteFaceRequest**](ImagefaceRecognitiondeleteFaceFaceRecognitionDeleteFaceRequest.md)|  | 

### Return type

[**ImagefaceRecognitionResponseModel**](ImagefaceRecognitionResponseModel.md)

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

# **image_image_face_recognition_list_faces_retrieve**
> ImagefaceRecognitionResponseModel image_image_face_recognition_list_faces_retrieve(providers, attributes_as_list=attributes_as_list, fallback_providers=fallback_providers, response_as_dict=response_as_dict, show_original_response=show_original_response)

Face Recognition - List Faces

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**amazon**|`boto3 1.26.8`|free|- |**facepp**|`v3`|0.1 (per 1000 request)|1 request   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imageface_recognition_response_model import ImagefaceRecognitionResponseModel
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
    api_instance = openapi_client.FaceRecognitionApi(api_client)
    providers = 'providers_example' # str | It can be one (ex: **'amazon'** or **'google'**) or multiple provider(s) (ex: **'amazon,microsoft,google'**)             that the data will be redirected to in order to get the processed results.
    attributes_as_list = False # bool | Optional : When set to **false** (default) the structure of the extracted items is list of objects having different attributes : <br>      ```{'items': [{\"attribute_1\": \"x1\",\"attribute_2\": \"y2\"}, ... ]}``` <br>      When it is set to **true**, the response contains an object with each attribute as a list : <br>      ```{ \"attribute_1\": [\"x1\",\"x2\", ...], \"attribute_2\": [y1, y2, ...]}```  (optional) (default to False)
    fallback_providers = 'fallback_providers_example' # str | Providers in this list will be used as fallback if the call to provider in `providers` parameter fails.     To use this feature, you must input **only one** provider in the `providers` parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn't fail.   *Doesn't work with async subfeatures.*      (optional)
    response_as_dict = True # bool | Optional : When set to **true** (default), the response is an object of responses with providers names as keys : <br>                    ``` {\"google\" : { \"status\": \"success\", ... }, } ``` <br>                 When set to **false** the response structure is a list of response objects : <br>                     ``` [{\"status\": \"success\", \"provider\": \"google\" ... }, ] ```. <br>                    (optional) (default to True)
    show_original_response = False # bool | Optional : Shows the original response of the provider.<br>         When set to **true**, a new attribute *original_response* will appear in the response object. (optional) (default to False)

    try:
        # Face Recognition - List Faces
        api_response = await api_instance.image_image_face_recognition_list_faces_retrieve(providers, attributes_as_list=attributes_as_list, fallback_providers=fallback_providers, response_as_dict=response_as_dict, show_original_response=show_original_response)
        print("The response of FaceRecognitionApi->image_image_face_recognition_list_faces_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FaceRecognitionApi->image_image_face_recognition_list_faces_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers** | **str**| It can be one (ex: **&#39;amazon&#39;** or **&#39;google&#39;**) or multiple provider(s) (ex: **&#39;amazon,microsoft,google&#39;**)             that the data will be redirected to in order to get the processed results. | 
 **attributes_as_list** | **bool**| Optional : When set to **false** (default) the structure of the extracted items is list of objects having different attributes : &lt;br&gt;      &#x60;&#x60;&#x60;{&#39;items&#39;: [{\&quot;attribute_1\&quot;: \&quot;x1\&quot;,\&quot;attribute_2\&quot;: \&quot;y2\&quot;}, ... ]}&#x60;&#x60;&#x60; &lt;br&gt;      When it is set to **true**, the response contains an object with each attribute as a list : &lt;br&gt;      &#x60;&#x60;&#x60;{ \&quot;attribute_1\&quot;: [\&quot;x1\&quot;,\&quot;x2\&quot;, ...], \&quot;attribute_2\&quot;: [y1, y2, ...]}&#x60;&#x60;&#x60;  | [optional] [default to False]
 **fallback_providers** | **str**| Providers in this list will be used as fallback if the call to provider in &#x60;providers&#x60; parameter fails.     To use this feature, you must input **only one** provider in the &#x60;providers&#x60; parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn&#39;t fail.   *Doesn&#39;t work with async subfeatures.*      | [optional] 
 **response_as_dict** | **bool**| Optional : When set to **true** (default), the response is an object of responses with providers names as keys : &lt;br&gt;                    &#x60;&#x60;&#x60; {\&quot;google\&quot; : { \&quot;status\&quot;: \&quot;success\&quot;, ... }, } &#x60;&#x60;&#x60; &lt;br&gt;                 When set to **false** the response structure is a list of response objects : &lt;br&gt;                     &#x60;&#x60;&#x60; [{\&quot;status\&quot;: \&quot;success\&quot;, \&quot;provider\&quot;: \&quot;google\&quot; ... }, ] &#x60;&#x60;&#x60;. &lt;br&gt;                    | [optional] [default to True]
 **show_original_response** | **bool**| Optional : Shows the original response of the provider.&lt;br&gt;         When set to **true**, a new attribute *original_response* will appear in the response object. | [optional] [default to False]

### Return type

[**ImagefaceRecognitionResponseModel**](ImagefaceRecognitionResponseModel.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **image_image_face_recognition_recognize_create**
> ImagefaceRecognitionResponseModel image_image_face_recognition_recognize_create(imageface_recognitionrecognizeimageface_recognitionadd_face_face_recognition_detect_face_request)

Face Recognition - Recognize Face

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**amazon**|`boto3 1.26.8`|1.0 (per 1000 file)|1 file |**facepp**|`v3`|2.0 (per 1000 request)|1 request   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imageface_recognition_response_model import ImagefaceRecognitionResponseModel
from openapi_client.models.imageface_recognitionrecognizeimageface_recognitionadd_face_face_recognition_detect_face_request import ImagefaceRecognitionrecognizeimagefaceRecognitionaddFaceFaceRecognitionDetectFaceRequest
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
    api_instance = openapi_client.FaceRecognitionApi(api_client)
    imageface_recognitionrecognizeimageface_recognitionadd_face_face_recognition_detect_face_request = {"providers":"amazon,facepp,facepp,facepp,facepp,amazon,amazon,amazon","file_url":"http://edenai-resource-example.jpg"} # ImagefaceRecognitionrecognizeimagefaceRecognitionaddFaceFaceRecognitionDetectFaceRequest | 

    try:
        # Face Recognition - Recognize Face
        api_response = await api_instance.image_image_face_recognition_recognize_create(imageface_recognitionrecognizeimageface_recognitionadd_face_face_recognition_detect_face_request)
        print("The response of FaceRecognitionApi->image_image_face_recognition_recognize_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FaceRecognitionApi->image_image_face_recognition_recognize_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageface_recognitionrecognizeimageface_recognitionadd_face_face_recognition_detect_face_request** | [**ImagefaceRecognitionrecognizeimagefaceRecognitionaddFaceFaceRecognitionDetectFaceRequest**](ImagefaceRecognitionrecognizeimagefaceRecognitionaddFaceFaceRecognitionDetectFaceRequest.md)|  | 

### Return type

[**ImagefaceRecognitionResponseModel**](ImagefaceRecognitionResponseModel.md)

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

