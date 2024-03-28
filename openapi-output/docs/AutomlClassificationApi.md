# openapi_client.AutomlClassificationApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_image_automl_classification_create_project_create**](AutomlClassificationApi.md#image_image_automl_classification_create_project_create) | **POST** /image/automl_classification/create_project | Automl Classification - Create Project
[**image_image_automl_classification_delete_project_create**](AutomlClassificationApi.md#image_image_automl_classification_delete_project_create) | **POST** /image/automl_classification/delete_project | Automl Classification - Delete Project
[**image_image_automl_classification_list_projects_retrieve**](AutomlClassificationApi.md#image_image_automl_classification_list_projects_retrieve) | **GET** /image/automl_classification/list_projects | Automl Classification - List Projects
[**image_image_automl_classification_predict_async_create**](AutomlClassificationApi.md#image_image_automl_classification_predict_async_create) | **POST** /image/automl_classification/predict_async | Automl Classification Predict Launch Job
[**image_image_automl_classification_predict_async_retrieve**](AutomlClassificationApi.md#image_image_automl_classification_predict_async_retrieve) | **GET** /image/automl_classification/predict_async | Automl Classification Predict List Job
[**image_image_automl_classification_predict_async_retrieve2**](AutomlClassificationApi.md#image_image_automl_classification_predict_async_retrieve2) | **GET** /image/automl_classification/predict_async/{public_id} | Automl Classification - Predict Get Job Results
[**image_image_automl_classification_train_async_create**](AutomlClassificationApi.md#image_image_automl_classification_train_async_create) | **POST** /image/automl_classification/train_async | Automl Classification Train Launch Job
[**image_image_automl_classification_train_async_retrieve**](AutomlClassificationApi.md#image_image_automl_classification_train_async_retrieve) | **GET** /image/automl_classification/train_async | Automl Classification Train List Job
[**image_image_automl_classification_train_async_retrieve2**](AutomlClassificationApi.md#image_image_automl_classification_train_async_retrieve2) | **GET** /image/automl_classification/train_async/{public_id} | Automl Classification - Train Get Job Results
[**image_image_automl_classification_upload_data_async_create**](AutomlClassificationApi.md#image_image_automl_classification_upload_data_async_create) | **POST** /image/automl_classification/upload_data_async | Automl Classification Upload Data Launch Job
[**image_image_automl_classification_upload_data_async_retrieve**](AutomlClassificationApi.md#image_image_automl_classification_upload_data_async_retrieve) | **GET** /image/automl_classification/upload_data_async | Automl Classification Upload Data List Job
[**image_image_automl_classification_upload_data_async_retrieve2**](AutomlClassificationApi.md#image_image_automl_classification_upload_data_async_retrieve2) | **GET** /image/automl_classification/upload_data_async/{public_id} | Automl Classification - Upload Data Get Job Results


# **image_image_automl_classification_create_project_create**
> ImageautomlClassificationResponseModel image_image_automl_classification_create_project_create(imageautoml_classificationcreate_project_automl_classification_create_project_request)

Automl Classification - Create Project

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**nyckel**|`v1.0.0`|free|-   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imageautoml_classification_response_model import ImageautomlClassificationResponseModel
from openapi_client.models.imageautoml_classificationcreate_project_automl_classification_create_project_request import ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest
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
    api_instance = openapi_client.AutomlClassificationApi(api_client)
    imageautoml_classificationcreate_project_automl_classification_create_project_request = {"providers":"nyckel,nyckel,nyckel,nyckel,nyckel"} # ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest | 

    try:
        # Automl Classification - Create Project
        api_response = await api_instance.image_image_automl_classification_create_project_create(imageautoml_classificationcreate_project_automl_classification_create_project_request)
        print("The response of AutomlClassificationApi->image_image_automl_classification_create_project_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomlClassificationApi->image_image_automl_classification_create_project_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageautoml_classificationcreate_project_automl_classification_create_project_request** | [**ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest**](ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest.md)|  | 

### Return type

[**ImageautomlClassificationResponseModel**](ImageautomlClassificationResponseModel.md)

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

# **image_image_automl_classification_delete_project_create**
> ImageautomlClassificationResponseModel image_image_automl_classification_delete_project_create(imageautoml_classificationdelete_project_automl_classification_delete_request)

Automl Classification - Delete Project

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**nyckel**|`v1.0.0`|free|-   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imageautoml_classification_response_model import ImageautomlClassificationResponseModel
from openapi_client.models.imageautoml_classificationdelete_project_automl_classification_delete_request import ImageautomlClassificationdeleteProjectAutomlClassificationDeleteRequest
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
    api_instance = openapi_client.AutomlClassificationApi(api_client)
    imageautoml_classificationdelete_project_automl_classification_delete_request = {"providers":"nyckel,nyckel,nyckel,nyckel,nyckel","project_id":"5d1c7023-c2eb-40ba-a100-e1fdd17cb876"} # ImageautomlClassificationdeleteProjectAutomlClassificationDeleteRequest | 

    try:
        # Automl Classification - Delete Project
        api_response = await api_instance.image_image_automl_classification_delete_project_create(imageautoml_classificationdelete_project_automl_classification_delete_request)
        print("The response of AutomlClassificationApi->image_image_automl_classification_delete_project_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomlClassificationApi->image_image_automl_classification_delete_project_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageautoml_classificationdelete_project_automl_classification_delete_request** | [**ImageautomlClassificationdeleteProjectAutomlClassificationDeleteRequest**](ImageautomlClassificationdeleteProjectAutomlClassificationDeleteRequest.md)|  | 

### Return type

[**ImageautomlClassificationResponseModel**](ImageautomlClassificationResponseModel.md)

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

# **image_image_automl_classification_list_projects_retrieve**
> AutomlClassificationListProjectsResponse image_image_automl_classification_list_projects_retrieve()

Automl Classification - List Projects

List Automl Classification Projects

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.automl_classification_list_projects_response import AutomlClassificationListProjectsResponse
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
    api_instance = openapi_client.AutomlClassificationApi(api_client)

    try:
        # Automl Classification - List Projects
        api_response = await api_instance.image_image_automl_classification_list_projects_retrieve()
        print("The response of AutomlClassificationApi->image_image_automl_classification_list_projects_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomlClassificationApi->image_image_automl_classification_list_projects_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AutomlClassificationListProjectsResponse**](AutomlClassificationListProjectsResponse.md)

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

# **image_image_automl_classification_predict_async_create**
> LaunchAsyncJobResponse image_image_automl_classification_predict_async_create(providers, project_id, fallback_providers=fallback_providers, show_original_response=show_original_response, webhook_receiver=webhook_receiver, users_webhook_parameters=users_webhook_parameters, file=file, file_url=file_url)

Automl Classification Predict Launch Job

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**nyckel**|`v1.0.0`|0.005 (per 1 request)|1 request   </details>  

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
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AutomlClassificationApi(api_client)
    providers = 'providers_example' # str | It can be one (ex: **'amazon'** or **'google'**) or multiple provider(s) (ex: **'amazon,microsoft,google'**)             that the data will be redirected to in order to get the processed results.
    project_id = 'project_id_example' # str | The id of project
    fallback_providers = 'fallback_providers_example' # str | Providers in this list will be used as fallback if the call to provider in `providers` parameter fails.     To use this feature, you must input **only one** provider in the `providers` parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn't fail.   *Doesn't work with async subfeatures.*      (optional)
    show_original_response = False # bool | Optional : Shows the original response of the provider.<br>         When set to **true**, a new attribute *original_response* will appear in the response object. (optional) (default to False)
    webhook_receiver = 'webhook_receiver_example' # str | Webhook receiver should be a valid https URL (ex : https://your.listner.com/endpoint).             After the processing is done, the webhook endpoint will receive a POST request with the result. (optional)
    users_webhook_parameters = None # Dict[str, object] | Json data that contains of additional parameters that will be sent back to the webhook receiver             (ex: api key for security or client's data ID to link the result internally).             Will only be used when webhook_receiver is set. (optional)
    file = None # bytearray | File to analyse in binary format to be used with *content-type*: **multipart/form-data** <br> **Does not work with application/json !** (optional)
    file_url = 'file_url_example' # str | File **URL** to analyse to be used with with *content-type*: **application/json**. (optional)

    try:
        # Automl Classification Predict Launch Job
        api_response = await api_instance.image_image_automl_classification_predict_async_create(providers, project_id, fallback_providers=fallback_providers, show_original_response=show_original_response, webhook_receiver=webhook_receiver, users_webhook_parameters=users_webhook_parameters, file=file, file_url=file_url)
        print("The response of AutomlClassificationApi->image_image_automl_classification_predict_async_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomlClassificationApi->image_image_automl_classification_predict_async_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers** | **str**| It can be one (ex: **&#39;amazon&#39;** or **&#39;google&#39;**) or multiple provider(s) (ex: **&#39;amazon,microsoft,google&#39;**)             that the data will be redirected to in order to get the processed results. | 
 **project_id** | **str**| The id of project | 
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

# **image_image_automl_classification_predict_async_retrieve**
> ListAsyncJobResponse image_image_automl_classification_predict_async_retrieve()

Automl Classification Predict List Job

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
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AutomlClassificationApi(api_client)

    try:
        # Automl Classification Predict List Job
        api_response = await api_instance.image_image_automl_classification_predict_async_retrieve()
        print("The response of AutomlClassificationApi->image_image_automl_classification_predict_async_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomlClassificationApi->image_image_automl_classification_predict_async_retrieve: %s\n" % e)
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

# **image_image_automl_classification_predict_async_retrieve2**
> ImageautomlClassificationResponseModel image_image_automl_classification_predict_async_retrieve2(public_id, response_as_dict=response_as_dict, show_original_response=show_original_response)

Automl Classification - Predict Get Job Results

Get the status and results of an async job given its ID.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imageautoml_classification_response_model import ImageautomlClassificationResponseModel
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
    api_instance = openapi_client.AutomlClassificationApi(api_client)
    public_id = 'public_id_example' # str | 
    response_as_dict = True # bool |  (optional) (default to True)
    show_original_response = False # bool |  (optional) (default to False)

    try:
        # Automl Classification - Predict Get Job Results
        api_response = await api_instance.image_image_automl_classification_predict_async_retrieve2(public_id, response_as_dict=response_as_dict, show_original_response=show_original_response)
        print("The response of AutomlClassificationApi->image_image_automl_classification_predict_async_retrieve2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomlClassificationApi->image_image_automl_classification_predict_async_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**|  | 
 **response_as_dict** | **bool**|  | [optional] [default to True]
 **show_original_response** | **bool**|  | [optional] [default to False]

### Return type

[**ImageautomlClassificationResponseModel**](ImageautomlClassificationResponseModel.md)

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

# **image_image_automl_classification_train_async_create**
> LaunchAsyncJobResponse image_image_automl_classification_train_async_create(providers, project_id, fallback_providers=fallback_providers, show_original_response=show_original_response, webhook_receiver=webhook_receiver, users_webhook_parameters=users_webhook_parameters)

Automl Classification Train Launch Job

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**nyckel**|`v1.0.0`|free|-   </details>  

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
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AutomlClassificationApi(api_client)
    providers = 'providers_example' # str | It can be one (ex: **'amazon'** or **'google'**) or multiple provider(s) (ex: **'amazon,microsoft,google'**)             that the data will be redirected to in order to get the processed results.
    project_id = 'project_id_example' # str | The id of project
    fallback_providers = 'fallback_providers_example' # str | Providers in this list will be used as fallback if the call to provider in `providers` parameter fails.     To use this feature, you must input **only one** provider in the `providers` parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn't fail.   *Doesn't work with async subfeatures.*      (optional)
    show_original_response = False # bool | Optional : Shows the original response of the provider.<br>         When set to **true**, a new attribute *original_response* will appear in the response object. (optional) (default to False)
    webhook_receiver = 'webhook_receiver_example' # str | Webhook receiver should be a valid https URL (ex : https://your.listner.com/endpoint).             After the processing is done, the webhook endpoint will receive a POST request with the result. (optional)
    users_webhook_parameters = None # Dict[str, object] | Json data that contains of additional parameters that will be sent back to the webhook receiver             (ex: api key for security or client's data ID to link the result internally).             Will only be used when webhook_receiver is set. (optional)

    try:
        # Automl Classification Train Launch Job
        api_response = await api_instance.image_image_automl_classification_train_async_create(providers, project_id, fallback_providers=fallback_providers, show_original_response=show_original_response, webhook_receiver=webhook_receiver, users_webhook_parameters=users_webhook_parameters)
        print("The response of AutomlClassificationApi->image_image_automl_classification_train_async_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomlClassificationApi->image_image_automl_classification_train_async_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers** | **str**| It can be one (ex: **&#39;amazon&#39;** or **&#39;google&#39;**) or multiple provider(s) (ex: **&#39;amazon,microsoft,google&#39;**)             that the data will be redirected to in order to get the processed results. | 
 **project_id** | **str**| The id of project | 
 **fallback_providers** | **str**| Providers in this list will be used as fallback if the call to provider in &#x60;providers&#x60; parameter fails.     To use this feature, you must input **only one** provider in the &#x60;providers&#x60; parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn&#39;t fail.   *Doesn&#39;t work with async subfeatures.*      | [optional] 
 **show_original_response** | **bool**| Optional : Shows the original response of the provider.&lt;br&gt;         When set to **true**, a new attribute *original_response* will appear in the response object. | [optional] [default to False]
 **webhook_receiver** | **str**| Webhook receiver should be a valid https URL (ex : https://your.listner.com/endpoint).             After the processing is done, the webhook endpoint will receive a POST request with the result. | [optional] 
 **users_webhook_parameters** | [**Dict[str, object]**](Dict.md)| Json data that contains of additional parameters that will be sent back to the webhook receiver             (ex: api key for security or client&#39;s data ID to link the result internally).             Will only be used when webhook_receiver is set. | [optional] 

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

# **image_image_automl_classification_train_async_retrieve**
> ListAsyncJobResponse image_image_automl_classification_train_async_retrieve()

Automl Classification Train List Job

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
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AutomlClassificationApi(api_client)

    try:
        # Automl Classification Train List Job
        api_response = await api_instance.image_image_automl_classification_train_async_retrieve()
        print("The response of AutomlClassificationApi->image_image_automl_classification_train_async_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomlClassificationApi->image_image_automl_classification_train_async_retrieve: %s\n" % e)
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

# **image_image_automl_classification_train_async_retrieve2**
> ImageautomlClassificationResponseModel image_image_automl_classification_train_async_retrieve2(public_id, response_as_dict=response_as_dict, show_original_response=show_original_response)

Automl Classification - Train Get Job Results

Get the status and results of an async job given its ID.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imageautoml_classification_response_model import ImageautomlClassificationResponseModel
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
    api_instance = openapi_client.AutomlClassificationApi(api_client)
    public_id = 'public_id_example' # str | 
    response_as_dict = True # bool |  (optional) (default to True)
    show_original_response = False # bool |  (optional) (default to False)

    try:
        # Automl Classification - Train Get Job Results
        api_response = await api_instance.image_image_automl_classification_train_async_retrieve2(public_id, response_as_dict=response_as_dict, show_original_response=show_original_response)
        print("The response of AutomlClassificationApi->image_image_automl_classification_train_async_retrieve2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomlClassificationApi->image_image_automl_classification_train_async_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**|  | 
 **response_as_dict** | **bool**|  | [optional] [default to True]
 **show_original_response** | **bool**|  | [optional] [default to False]

### Return type

[**ImageautomlClassificationResponseModel**](ImageautomlClassificationResponseModel.md)

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

# **image_image_automl_classification_upload_data_async_create**
> LaunchAsyncJobResponse image_image_automl_classification_upload_data_async_create(providers, project_id, label, type_of_data, fallback_providers=fallback_providers, show_original_response=show_original_response, webhook_receiver=webhook_receiver, users_webhook_parameters=users_webhook_parameters, file=file, file_url=file_url)

Automl Classification Upload Data Launch Job

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**nyckel**|`v1.0.0`|0.0005 (per 1 file)|1 file   </details>  

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
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AutomlClassificationApi(api_client)
    providers = 'providers_example' # str | It can be one (ex: **'amazon'** or **'google'**) or multiple provider(s) (ex: **'amazon,microsoft,google'**)             that the data will be redirected to in order to get the processed results.
    project_id = 'project_id_example' # str | The id of project
    label = 'label_example' # str | Label of the image
    type_of_data = openapi_client.TypeOfDataEnum() # TypeOfDataEnum | Type of data : TRAINING or TEST  * `TRAINING` - TRAINING * `TEST` - TEST
    fallback_providers = 'fallback_providers_example' # str | Providers in this list will be used as fallback if the call to provider in `providers` parameter fails.     To use this feature, you must input **only one** provider in the `providers` parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn't fail.   *Doesn't work with async subfeatures.*      (optional)
    show_original_response = False # bool | Optional : Shows the original response of the provider.<br>         When set to **true**, a new attribute *original_response* will appear in the response object. (optional) (default to False)
    webhook_receiver = 'webhook_receiver_example' # str | Webhook receiver should be a valid https URL (ex : https://your.listner.com/endpoint).             After the processing is done, the webhook endpoint will receive a POST request with the result. (optional)
    users_webhook_parameters = None # Dict[str, object] | Json data that contains of additional parameters that will be sent back to the webhook receiver             (ex: api key for security or client's data ID to link the result internally).             Will only be used when webhook_receiver is set. (optional)
    file = None # bytearray | File to analyse in binary format to be used with *content-type*: **multipart/form-data** <br> **Does not work with application/json !** (optional)
    file_url = 'file_url_example' # str | File **URL** to analyse to be used with with *content-type*: **application/json**. (optional)

    try:
        # Automl Classification Upload Data Launch Job
        api_response = await api_instance.image_image_automl_classification_upload_data_async_create(providers, project_id, label, type_of_data, fallback_providers=fallback_providers, show_original_response=show_original_response, webhook_receiver=webhook_receiver, users_webhook_parameters=users_webhook_parameters, file=file, file_url=file_url)
        print("The response of AutomlClassificationApi->image_image_automl_classification_upload_data_async_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomlClassificationApi->image_image_automl_classification_upload_data_async_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers** | **str**| It can be one (ex: **&#39;amazon&#39;** or **&#39;google&#39;**) or multiple provider(s) (ex: **&#39;amazon,microsoft,google&#39;**)             that the data will be redirected to in order to get the processed results. | 
 **project_id** | **str**| The id of project | 
 **label** | **str**| Label of the image | 
 **type_of_data** | [**TypeOfDataEnum**](TypeOfDataEnum.md)| Type of data : TRAINING or TEST  * &#x60;TRAINING&#x60; - TRAINING * &#x60;TEST&#x60; - TEST | 
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

# **image_image_automl_classification_upload_data_async_retrieve**
> ListAsyncJobResponse image_image_automl_classification_upload_data_async_retrieve()

Automl Classification Upload Data List Job

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
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AutomlClassificationApi(api_client)

    try:
        # Automl Classification Upload Data List Job
        api_response = await api_instance.image_image_automl_classification_upload_data_async_retrieve()
        print("The response of AutomlClassificationApi->image_image_automl_classification_upload_data_async_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomlClassificationApi->image_image_automl_classification_upload_data_async_retrieve: %s\n" % e)
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

# **image_image_automl_classification_upload_data_async_retrieve2**
> ImageautomlClassificationResponseModel image_image_automl_classification_upload_data_async_retrieve2(public_id, response_as_dict=response_as_dict, show_original_response=show_original_response)

Automl Classification - Upload Data Get Job Results

Get the status and results of an async job given its ID.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imageautoml_classification_response_model import ImageautomlClassificationResponseModel
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
    api_instance = openapi_client.AutomlClassificationApi(api_client)
    public_id = 'public_id_example' # str | 
    response_as_dict = True # bool |  (optional) (default to True)
    show_original_response = False # bool |  (optional) (default to False)

    try:
        # Automl Classification - Upload Data Get Job Results
        api_response = await api_instance.image_image_automl_classification_upload_data_async_retrieve2(public_id, response_as_dict=response_as_dict, show_original_response=show_original_response)
        print("The response of AutomlClassificationApi->image_image_automl_classification_upload_data_async_retrieve2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomlClassificationApi->image_image_automl_classification_upload_data_async_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**|  | 
 **response_as_dict** | **bool**|  | [optional] [default to True]
 **show_original_response** | **bool**|  | [optional] [default to False]

### Return type

[**ImageautomlClassificationResponseModel**](ImageautomlClassificationResponseModel.md)

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

