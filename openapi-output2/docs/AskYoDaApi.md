# openapi_client.AskYoDaApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aiproducts_aiproducts_askyoda_v2_add_file_create**](AskYoDaApi.md#aiproducts_aiproducts_askyoda_v2_add_file_create) | **POST** /aiproducts/askyoda/v2/{project_id}/add_file | Add File
[**aiproducts_aiproducts_askyoda_v2_add_text_create**](AskYoDaApi.md#aiproducts_aiproducts_askyoda_v2_add_text_create) | **POST** /aiproducts/askyoda/v2/{project_id}/add_text | Add Texts
[**aiproducts_aiproducts_askyoda_v2_add_url_create**](AskYoDaApi.md#aiproducts_aiproducts_askyoda_v2_add_url_create) | **POST** /aiproducts/askyoda/v2/{project_id}/add_url | Add Urls
[**aiproducts_aiproducts_askyoda_v2_ask_llm_create**](AskYoDaApi.md#aiproducts_aiproducts_askyoda_v2_ask_llm_create) | **POST** /aiproducts/askyoda/v2/{project_id}/ask_llm | Ask LLM
[**aiproducts_aiproducts_askyoda_v2_create**](AskYoDaApi.md#aiproducts_aiproducts_askyoda_v2_create) | **POST** /aiproducts/askyoda/v2/ | Create Project
[**aiproducts_aiproducts_askyoda_v2_delete_chunk_destroy**](AskYoDaApi.md#aiproducts_aiproducts_askyoda_v2_delete_chunk_destroy) | **DELETE** /aiproducts/askyoda/v2/{project_id}/delete_chunk | Delete Chunk
[**aiproducts_aiproducts_askyoda_v2_files_destroy**](AskYoDaApi.md#aiproducts_aiproducts_askyoda_v2_files_destroy) | **DELETE** /aiproducts/askyoda/v2/{project_id}/files/{file_id}/ | Delete File
[**aiproducts_aiproducts_askyoda_v2_files_list**](AskYoDaApi.md#aiproducts_aiproducts_askyoda_v2_files_list) | **GET** /aiproducts/askyoda/v2/{project_id}/files/ | List Files
[**aiproducts_aiproducts_askyoda_v2_files_retrieve**](AskYoDaApi.md#aiproducts_aiproducts_askyoda_v2_files_retrieve) | **GET** /aiproducts/askyoda/v2/{project_id}/files/{file_id}/ | Get File
[**aiproducts_aiproducts_askyoda_v2_info_retrieve**](AskYoDaApi.md#aiproducts_aiproducts_askyoda_v2_info_retrieve) | **GET** /aiproducts/askyoda/v2/{project_id}/info | Get info
[**aiproducts_aiproducts_askyoda_v2_query_create**](AskYoDaApi.md#aiproducts_aiproducts_askyoda_v2_query_create) | **POST** /aiproducts/askyoda/v2/{project_id}/query | Query
[**aiproducts_aiproducts_askyoda_v2_update_project_partial_update**](AskYoDaApi.md#aiproducts_aiproducts_askyoda_v2_update_project_partial_update) | **PATCH** /aiproducts/askyoda/v2/{project_id}/update_project | Update Project
[**aiproducts_aiproducts_delete_destroy**](AskYoDaApi.md#aiproducts_aiproducts_delete_destroy) | **DELETE** /aiproducts/delete/{project_id} | Delete Project
[**aiproducts_aiproducts_list**](AskYoDaApi.md#aiproducts_aiproducts_list) | **GET** /aiproducts/ | List Projects
[**aiproducts_aiproducts_retrieve**](AskYoDaApi.md#aiproducts_aiproducts_retrieve) | **GET** /aiproducts/{project_id} | Retrieve Project


# **aiproducts_aiproducts_askyoda_v2_add_file_create**
> aiproducts_aiproducts_askyoda_v2_add_file_create(project_id, data_type, file=file, file_url=file_url, metadata=metadata, provider=provider)

Add File

Upload a file (csv, audio, pdf) into your project, it wil be processed and stored as text embeddings within your database project.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.data_type_enum import DataTypeEnum
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
    api_instance = openapi_client.AskYoDaApi(api_client)
    project_id = 'project_id_example' # str | 
    data_type = openapi_client.DataTypeEnum() # DataTypeEnum | 
    file = None # bytearray | File to analyse in binary format to be used with *content-type*: **multipart/form-data** <br> **Does not work with application/json !** (optional)
    file_url = 'file_url_example' # str | File **URL** to analyse to be used with with *content-type*: **application/json**. (optional)
    metadata = 'metadata_example' # str | Optional parameter: Attach metadata to the uploaded file data in your database. Provide a stringified JSON with key-value pairs. Useful in `filter_document` when querying the language model, it allows you to filter data with your Chatbot by considering only documents that have the specified metadata. (optional)
    provider = 'provider_example' # str | Select a provider to use, only for audio (speech-to-text) & pdf (ocr-async) files. (optional)

    try:
        # Add File
        api_instance.aiproducts_aiproducts_askyoda_v2_add_file_create(project_id, data_type, file=file, file_url=file_url, metadata=metadata, provider=provider)
    except Exception as e:
        print("Exception when calling AskYoDaApi->aiproducts_aiproducts_askyoda_v2_add_file_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type** | [**DataTypeEnum**](DataTypeEnum.md)|  | 
 **file** | **bytearray**| File to analyse in binary format to be used with *content-type*: **multipart/form-data** &lt;br&gt; **Does not work with application/json !** | [optional] 
 **file_url** | **str**| File **URL** to analyse to be used with with *content-type*: **application/json**. | [optional] 
 **metadata** | **str**| Optional parameter: Attach metadata to the uploaded file data in your database. Provide a stringified JSON with key-value pairs. Useful in &#x60;filter_document&#x60; when querying the language model, it allows you to filter data with your Chatbot by considering only documents that have the specified metadata. | [optional] 
 **provider** | **str**| Select a provider to use, only for audio (speech-to-text) &amp; pdf (ocr-async) files. | [optional] 

### Return type

void (empty response body)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aiproducts_aiproducts_askyoda_v2_add_text_create**
> aiproducts_aiproducts_askyoda_v2_add_text_create(project_id, add_text_request)

Add Texts

Add text data in your project, which will be stored as embeddings within your chosen database provider.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.add_text_request import AddTextRequest
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
    api_instance = openapi_client.AskYoDaApi(api_client)
    project_id = 'project_id_example' # str | 
    add_text_request = openapi_client.AddTextRequest() # AddTextRequest | 

    try:
        # Add Texts
        api_instance.aiproducts_aiproducts_askyoda_v2_add_text_create(project_id, add_text_request)
    except Exception as e:
        print("Exception when calling AskYoDaApi->aiproducts_aiproducts_askyoda_v2_add_text_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **add_text_request** | [**AddTextRequest**](AddTextRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aiproducts_aiproducts_askyoda_v2_add_url_create**
> aiproducts_aiproducts_askyoda_v2_add_url_create(project_id, add_url_request)

Add Urls

Add a list of URLs into your projects, they will be processed and stored as text embeddings within your project.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.add_url_request import AddUrlRequest
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
    api_instance = openapi_client.AskYoDaApi(api_client)
    project_id = 'project_id_example' # str | 
    add_url_request = openapi_client.AddUrlRequest() # AddUrlRequest | 

    try:
        # Add Urls
        api_instance.aiproducts_aiproducts_askyoda_v2_add_url_create(project_id, add_url_request)
    except Exception as e:
        print("Exception when calling AskYoDaApi->aiproducts_aiproducts_askyoda_v2_add_url_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **add_url_request** | [**AddUrlRequest**](AddUrlRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aiproducts_aiproducts_askyoda_v2_ask_llm_create**
> YodaQueryResponse aiproducts_aiproducts_askyoda_v2_ask_llm_create(project_id, ask_llm_request)

Ask LLM

Retrieve a list of search query responses and compare them to your input. Provide a query, and in return, receive scores for the most relevant items from your project, ranked by their proximity to your query.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.ask_llm_request import AskLLMRequest
from openapi_client.models.yoda_query_response import YodaQueryResponse
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
    api_instance = openapi_client.AskYoDaApi(api_client)
    project_id = 'project_id_example' # str | 
    ask_llm_request = openapi_client.AskLLMRequest() # AskLLMRequest | 

    try:
        # Ask LLM
        api_response = api_instance.aiproducts_aiproducts_askyoda_v2_ask_llm_create(project_id, ask_llm_request)
        print("The response of AskYoDaApi->aiproducts_aiproducts_askyoda_v2_ask_llm_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AskYoDaApi->aiproducts_aiproducts_askyoda_v2_ask_llm_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **ask_llm_request** | [**AskLLMRequest**](AskLLMRequest.md)|  | 

### Return type

[**YodaQueryResponse**](YodaQueryResponse.md)

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

# **aiproducts_aiproducts_askyoda_v2_create**
> YodaCreateProjectResponse aiproducts_aiproducts_askyoda_v2_create(ask_your_data_project_request)

Create Project

Allows you to create a new Ask YODA project with specified details.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.ask_your_data_project_request import AskYourDataProjectRequest
from openapi_client.models.yoda_create_project_response import YodaCreateProjectResponse
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
    api_instance = openapi_client.AskYoDaApi(api_client)
    ask_your_data_project_request = openapi_client.AskYourDataProjectRequest() # AskYourDataProjectRequest | 

    try:
        # Create Project
        api_response = api_instance.aiproducts_aiproducts_askyoda_v2_create(ask_your_data_project_request)
        print("The response of AskYoDaApi->aiproducts_aiproducts_askyoda_v2_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AskYoDaApi->aiproducts_aiproducts_askyoda_v2_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ask_your_data_project_request** | [**AskYourDataProjectRequest**](AskYourDataProjectRequest.md)|  | 

### Return type

[**YodaCreateProjectResponse**](YodaCreateProjectResponse.md)

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

# **aiproducts_aiproducts_askyoda_v2_delete_chunk_destroy**
> YodaDeleteResponse aiproducts_aiproducts_askyoda_v2_delete_chunk_destroy(id, project_id)

Delete Chunk

Delete a query from your project by its ID.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.yoda_delete_response import YodaDeleteResponse
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
    api_instance = openapi_client.AskYoDaApi(api_client)
    id = 'id_example' # str | chunk_id
    project_id = 'project_id_example' # str | 

    try:
        # Delete Chunk
        api_response = api_instance.aiproducts_aiproducts_askyoda_v2_delete_chunk_destroy(id, project_id)
        print("The response of AskYoDaApi->aiproducts_aiproducts_askyoda_v2_delete_chunk_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AskYoDaApi->aiproducts_aiproducts_askyoda_v2_delete_chunk_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| chunk_id | 
 **project_id** | **str**|  | 

### Return type

[**YodaDeleteResponse**](YodaDeleteResponse.md)

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

# **aiproducts_aiproducts_askyoda_v2_files_destroy**
> aiproducts_aiproducts_askyoda_v2_files_destroy(file_id, project_id)

Delete File

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
    api_instance = openapi_client.AskYoDaApi(api_client)
    file_id = 'file_id_example' # str | 
    project_id = 'project_id_example' # str | 

    try:
        # Delete File
        api_instance.aiproducts_aiproducts_askyoda_v2_files_destroy(file_id, project_id)
    except Exception as e:
        print("Exception when calling AskYoDaApi->aiproducts_aiproducts_askyoda_v2_files_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **project_id** | **str**|  | 

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

# **aiproducts_aiproducts_askyoda_v2_files_list**
> List[AiProductFile] aiproducts_aiproducts_askyoda_v2_files_list(project_id)

List Files

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.ai_product_file import AiProductFile
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
    api_instance = openapi_client.AskYoDaApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # List Files
        api_response = api_instance.aiproducts_aiproducts_askyoda_v2_files_list(project_id)
        print("The response of AskYoDaApi->aiproducts_aiproducts_askyoda_v2_files_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AskYoDaApi->aiproducts_aiproducts_askyoda_v2_files_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**List[AiProductFile]**](AiProductFile.md)

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

# **aiproducts_aiproducts_askyoda_v2_files_retrieve**
> AiProductFile aiproducts_aiproducts_askyoda_v2_files_retrieve(file_id, project_id)

Get File

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.ai_product_file import AiProductFile
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
    api_instance = openapi_client.AskYoDaApi(api_client)
    file_id = 'file_id_example' # str | 
    project_id = 'project_id_example' # str | 

    try:
        # Get File
        api_response = api_instance.aiproducts_aiproducts_askyoda_v2_files_retrieve(file_id, project_id)
        print("The response of AskYoDaApi->aiproducts_aiproducts_askyoda_v2_files_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AskYoDaApi->aiproducts_aiproducts_askyoda_v2_files_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **project_id** | **str**|  | 

### Return type

[**AiProductFile**](AiProductFile.md)

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

# **aiproducts_aiproducts_askyoda_v2_info_retrieve**
> YodaInfoResponse aiproducts_aiproducts_askyoda_v2_info_retrieve(project_id)

Get info

Retrieve details about your project within your Ask YODA project, including the total number of items stored in your project collection and default models

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.yoda_info_response import YodaInfoResponse
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
    api_instance = openapi_client.AskYoDaApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Get info
        api_response = api_instance.aiproducts_aiproducts_askyoda_v2_info_retrieve(project_id)
        print("The response of AskYoDaApi->aiproducts_aiproducts_askyoda_v2_info_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AskYoDaApi->aiproducts_aiproducts_askyoda_v2_info_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**YodaInfoResponse**](YodaInfoResponse.md)

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

# **aiproducts_aiproducts_askyoda_v2_query_create**
> YodaAskLlmResponse aiproducts_aiproducts_askyoda_v2_query_create(project_id, ask_llm_request)

Query

Interact with your data by selecting your preferred Language Model  provider. The chosen provider will then respond to queries based on the data you have added to your collection

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.ask_llm_request import AskLLMRequest
from openapi_client.models.yoda_ask_llm_response import YodaAskLlmResponse
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
    api_instance = openapi_client.AskYoDaApi(api_client)
    project_id = 'project_id_example' # str | 
    ask_llm_request = openapi_client.AskLLMRequest() # AskLLMRequest | 

    try:
        # Query
        api_response = api_instance.aiproducts_aiproducts_askyoda_v2_query_create(project_id, ask_llm_request)
        print("The response of AskYoDaApi->aiproducts_aiproducts_askyoda_v2_query_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AskYoDaApi->aiproducts_aiproducts_askyoda_v2_query_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **ask_llm_request** | [**AskLLMRequest**](AskLLMRequest.md)|  | 

### Return type

[**YodaAskLlmResponse**](YodaAskLlmResponse.md)

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

# **aiproducts_aiproducts_askyoda_v2_update_project_partial_update**
> aiproducts_aiproducts_askyoda_v2_update_project_partial_update(project_id, patched_ask_yoda_project_update_request=patched_ask_yoda_project_update_request)

Update Project

Update the default settings of the Yoda project. It allows you to modify the project's default settings, specifically changing the llm_provider (language model provider), llm_model (language model), ocr_provider (upload pdf), speech_to_text provider (upload audio) and the default chunks parameter associated with the default project.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.patched_ask_yoda_project_update_request import PatchedAskYodaProjectUpdateRequest
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
    api_instance = openapi_client.AskYoDaApi(api_client)
    project_id = 'project_id_example' # str | 
    patched_ask_yoda_project_update_request = openapi_client.PatchedAskYodaProjectUpdateRequest() # PatchedAskYodaProjectUpdateRequest |  (optional)

    try:
        # Update Project
        api_instance.aiproducts_aiproducts_askyoda_v2_update_project_partial_update(project_id, patched_ask_yoda_project_update_request=patched_ask_yoda_project_update_request)
    except Exception as e:
        print("Exception when calling AskYoDaApi->aiproducts_aiproducts_askyoda_v2_update_project_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **patched_ask_yoda_project_update_request** | [**PatchedAskYodaProjectUpdateRequest**](PatchedAskYodaProjectUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aiproducts_aiproducts_delete_destroy**
> aiproducts_aiproducts_delete_destroy(project_id)

Delete Project

View to delete an AI project.

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
    api_instance = openapi_client.AskYoDaApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Delete Project
        api_instance.aiproducts_aiproducts_delete_destroy(project_id)
    except Exception as e:
        print("Exception when calling AskYoDaApi->aiproducts_aiproducts_delete_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

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

# **aiproducts_aiproducts_list**
> List[AIProject] aiproducts_aiproducts_list(project_type=project_type)

List Projects

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.ai_project import AIProject
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
    api_instance = openapi_client.AskYoDaApi(api_client)
    project_type = 'project_type_example' # str |  (optional)

    try:
        # List Projects
        api_response = api_instance.aiproducts_aiproducts_list(project_type=project_type)
        print("The response of AskYoDaApi->aiproducts_aiproducts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AskYoDaApi->aiproducts_aiproducts_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_type** | **str**|  | [optional] 

### Return type

[**List[AIProject]**](AIProject.md)

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

# **aiproducts_aiproducts_retrieve**
> AIProject aiproducts_aiproducts_retrieve(project_id)

Retrieve Project

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.ai_project import AIProject
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
    api_instance = openapi_client.AskYoDaApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Retrieve Project
        api_response = api_instance.aiproducts_aiproducts_retrieve(project_id)
        print("The response of AskYoDaApi->aiproducts_aiproducts_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AskYoDaApi->aiproducts_aiproducts_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**AIProject**](AIProject.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

