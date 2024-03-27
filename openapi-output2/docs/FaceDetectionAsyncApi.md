# openapi_client.FaceDetectionAsyncApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**video_video_face_detection_async_create**](FaceDetectionAsyncApi.md#video_video_face_detection_async_create) | **POST** /video/face_detection_async | Face Detection Launch Job
[**video_video_face_detection_async_destroy**](FaceDetectionAsyncApi.md#video_video_face_detection_async_destroy) | **DELETE** /video/face_detection_async | Face Detection delete Jobs
[**video_video_face_detection_async_retrieve**](FaceDetectionAsyncApi.md#video_video_face_detection_async_retrieve) | **GET** /video/face_detection_async | Face Detection List Jobs
[**video_video_face_detection_async_retrieve2**](FaceDetectionAsyncApi.md#video_video_face_detection_async_retrieve2) | **GET** /video/face_detection_async/{public_id} | Face Detection Get Job Results


# **video_video_face_detection_async_create**
> LaunchAsyncJobResponse video_video_face_detection_async_create(providers, fallback_providers=fallback_providers, show_original_response=show_original_response, webhook_receiver=webhook_receiver, users_webhook_parameters=users_webhook_parameters, file=file, file_url=file_url)

Face Detection Launch Job

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**amazon**|`boto3`|0.1 (per 60 seconde)|60 seconde |**google**|`Video intelligence v1`|0.1 (per 60 seconde)|1 seconde   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.launch_async_job_response import LaunchAsyncJobResponse
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
    api_instance = openapi_client.FaceDetectionAsyncApi(api_client)
    providers = 'providers_example' # str | It can be one (ex: **'amazon'** or **'google'**) or multiple provider(s) (ex: **'amazon,microsoft,google'**)             that the data will be redirected to in order to get the processed results.
    fallback_providers = 'fallback_providers_example' # str | Providers in this list will be used as fallback if the call to provider in `providers` parameter fails.     To use this feature, you must input **only one** provider in the `providers` parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn't fail.   *Doesn't work with async subfeatures.*      (optional)
    show_original_response = False # bool | Optional : Shows the original response of the provider.<br>         When set to **true**, a new attribute *original_response* will appear in the response object. (optional) (default to False)
    webhook_receiver = 'webhook_receiver_example' # str | Webhook receiver should be a valid https URL (ex : https://your.listner.com/endpoint).             After the processing is done, the webhook endpoint will receive a POST request with the result. (optional)
    users_webhook_parameters = None # Dict[str, object] | Json data that contains of additional parameters that will be sent back to the webhook receiver             (ex: api key for security or client's data ID to link the result internally).             Will only be used when webhook_receiver is set. (optional)
    file = None # bytearray | File to analyse in binary format to be used with *content-type*: **multipart/form-data** <br> **Does not work with application/json !** (optional)
    file_url = 'file_url_example' # str | File **URL** to analyse to be used with with *content-type*: **application/json**. (optional)

    try:
        # Face Detection Launch Job
        api_response = api_instance.video_video_face_detection_async_create(providers, fallback_providers=fallback_providers, show_original_response=show_original_response, webhook_receiver=webhook_receiver, users_webhook_parameters=users_webhook_parameters, file=file, file_url=file_url)
        print("The response of FaceDetectionAsyncApi->video_video_face_detection_async_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FaceDetectionAsyncApi->video_video_face_detection_async_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers** | **str**| It can be one (ex: **&#39;amazon&#39;** or **&#39;google&#39;**) or multiple provider(s) (ex: **&#39;amazon,microsoft,google&#39;**)             that the data will be redirected to in order to get the processed results. | 
 **fallback_providers** | **str**| Providers in this list will be used as fallback if the call to provider in &#x60;providers&#x60; parameter fails.     To use this feature, you must input **only one** provider in the &#x60;providers&#x60; parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn&#39;t fail.   *Doesn&#39;t work with async subfeatures.*      | [optional] 
 **show_original_response** | **bool**| Optional : Shows the original response of the provider.&lt;br&gt;         When set to **true**, a new attribute *original_response* will appear in the response object. | [optional] [default to False]
 **webhook_receiver** | **str**| Webhook receiver should be a valid https URL (ex : https://your.listner.com/endpoint).             After the processing is done, the webhook endpoint will receive a POST request with the result. | [optional] 
 **users_webhook_parameters** | [**Dict[str, object]**](Dict.md)| Json data that contains of additional parameters that will be sent back to the webhook receiver             (ex: api key for security or client&#39;s data ID to link the result internally).             Will only be used when webhook_receiver is set. | [optional] 
 **file** | **bytearray**| File to analyse in binary format to be used with *content-type*: **multipart/form-data** &lt;br&gt; **Does not work with application/json !** | [optional] 
 **file_url** | **str**| File **URL** to analyse to be used with with *content-type*: **application/json**. | [optional] 

### Return type

[**LaunchAsyncJobResponse**](LaunchAsyncJobResponse.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_video_face_detection_async_destroy**
> video_video_face_detection_async_destroy()

Face Detection delete Jobs

Generic class to handle method GET all async job for user  Attributes:     feature (str): EdenAI feature     subfeature (str): EdenAI subfeature

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
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
    api_instance = openapi_client.FaceDetectionAsyncApi(api_client)

    try:
        # Face Detection delete Jobs
        api_instance.video_video_face_detection_async_destroy()
    except Exception as e:
        print("Exception when calling FaceDetectionAsyncApi->video_video_face_detection_async_destroy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_video_face_detection_async_retrieve**
> ListAsyncJobResponse video_video_face_detection_async_retrieve()

Face Detection List Jobs

Get a list of all jobs launched for this feature. You'll then be able to use the ID of each one to get its status and results.<br>                         Please note that a **job status doesn't get updated until a get request** is sent.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.list_async_job_response import ListAsyncJobResponse
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
    api_instance = openapi_client.FaceDetectionAsyncApi(api_client)

    try:
        # Face Detection List Jobs
        api_response = api_instance.video_video_face_detection_async_retrieve()
        print("The response of FaceDetectionAsyncApi->video_video_face_detection_async_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FaceDetectionAsyncApi->video_video_face_detection_async_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListAsyncJobResponse**](ListAsyncJobResponse.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_video_face_detection_async_retrieve2**
> AsyncvideofaceDetectionAsyncResponseModel video_video_face_detection_async_retrieve2(public_id, response_as_dict=response_as_dict, show_original_response=show_original_response)

Face Detection Get Job Results

Get the status and results of an async job given its ID.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.asyncvideoface_detection_async_response_model import AsyncvideofaceDetectionAsyncResponseModel
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
    api_instance = openapi_client.FaceDetectionAsyncApi(api_client)
    public_id = 'public_id_example' # str | 
    response_as_dict = True # bool |  (optional) (default to True)
    show_original_response = False # bool |  (optional) (default to False)

    try:
        # Face Detection Get Job Results
        api_response = api_instance.video_video_face_detection_async_retrieve2(public_id, response_as_dict=response_as_dict, show_original_response=show_original_response)
        print("The response of FaceDetectionAsyncApi->video_video_face_detection_async_retrieve2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FaceDetectionAsyncApi->video_video_face_detection_async_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**|  | 
 **response_as_dict** | **bool**|  | [optional] [default to True]
 **show_original_response** | **bool**|  | [optional] [default to False]

### Return type

[**AsyncvideofaceDetectionAsyncResponseModel**](AsyncvideofaceDetectionAsyncResponseModel.md)

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

