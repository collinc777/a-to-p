# openapi_client.XMergeApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aiproducts_aiproducts_x_merge_doc_parser_create**](XMergeApi.md#aiproducts_aiproducts_x_merge_doc_parser_create) | **POST** /aiproducts/x_merge/doc_parser/ | Create doc_parser project
[**aiproducts_aiproducts_x_merge_doc_parser_launch_call_create**](XMergeApi.md#aiproducts_aiproducts_x_merge_doc_parser_launch_call_create) | **POST** /aiproducts/x_merge/doc_parser/{project_id}/launch_call | Doc Parser launch call
[**aiproducts_aiproducts_x_merge_doc_parser_list**](XMergeApi.md#aiproducts_aiproducts_x_merge_doc_parser_list) | **GET** /aiproducts/x_merge/doc_parser/ | List doc_parser projects
[**aiproducts_aiproducts_x_merge_doc_parser_partial_update**](XMergeApi.md#aiproducts_aiproducts_x_merge_doc_parser_partial_update) | **PATCH** /aiproducts/x_merge/doc_parser/{project_id} | Update doc_parser project
[**aiproducts_aiproducts_x_merge_doc_parser_retrieve**](XMergeApi.md#aiproducts_aiproducts_x_merge_doc_parser_retrieve) | **GET** /aiproducts/x_merge/doc_parser/{project_id} | Retrieve doc_parser project
[**aiproducts_aiproducts_x_merge_list**](XMergeApi.md#aiproducts_aiproducts_x_merge_list) | **GET** /aiproducts/x_merge/ | List XMerge project


# **aiproducts_aiproducts_x_merge_doc_parser_create**
> DocParserCreate aiproducts_aiproducts_x_merge_doc_parser_create(doc_parser_create_request)

Create doc_parser project

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.doc_parser_create import DocParserCreate
from openapi_client.models.doc_parser_create_request import DocParserCreateRequest
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
    api_instance = openapi_client.XMergeApi(api_client)
    doc_parser_create_request = openapi_client.DocParserCreateRequest() # DocParserCreateRequest | 

    try:
        # Create doc_parser project
        api_response = await api_instance.aiproducts_aiproducts_x_merge_doc_parser_create(doc_parser_create_request)
        print("The response of XMergeApi->aiproducts_aiproducts_x_merge_doc_parser_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling XMergeApi->aiproducts_aiproducts_x_merge_doc_parser_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_parser_create_request** | [**DocParserCreateRequest**](DocParserCreateRequest.md)|  | 

### Return type

[**DocParserCreate**](DocParserCreate.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aiproducts_aiproducts_x_merge_doc_parser_launch_call_create**
> aiproducts_aiproducts_x_merge_doc_parser_launch_call_create(project_id, doc_parser_call_parameters_request=doc_parser_call_parameters_request)

Doc Parser launch call

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.doc_parser_call_parameters_request import DocParserCallParametersRequest
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
    api_instance = openapi_client.XMergeApi(api_client)
    project_id = 'project_id_example' # str | 
    doc_parser_call_parameters_request = openapi_client.DocParserCallParametersRequest() # DocParserCallParametersRequest |  (optional)

    try:
        # Doc Parser launch call
        await api_instance.aiproducts_aiproducts_x_merge_doc_parser_launch_call_create(project_id, doc_parser_call_parameters_request=doc_parser_call_parameters_request)
    except Exception as e:
        print("Exception when calling XMergeApi->aiproducts_aiproducts_x_merge_doc_parser_launch_call_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **doc_parser_call_parameters_request** | [**DocParserCallParametersRequest**](DocParserCallParametersRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aiproducts_aiproducts_x_merge_doc_parser_list**
> List[DocParserList] aiproducts_aiproducts_x_merge_doc_parser_list()

List doc_parser projects

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.doc_parser_list import DocParserList
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
    api_instance = openapi_client.XMergeApi(api_client)

    try:
        # List doc_parser projects
        api_response = await api_instance.aiproducts_aiproducts_x_merge_doc_parser_list()
        print("The response of XMergeApi->aiproducts_aiproducts_x_merge_doc_parser_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling XMergeApi->aiproducts_aiproducts_x_merge_doc_parser_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DocParserList]**](DocParserList.md)

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

# **aiproducts_aiproducts_x_merge_doc_parser_partial_update**
> DocParserUpdate aiproducts_aiproducts_x_merge_doc_parser_partial_update(project_id, patched_doc_parser_update_request=patched_doc_parser_update_request)

Update doc_parser project

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.doc_parser_update import DocParserUpdate
from openapi_client.models.patched_doc_parser_update_request import PatchedDocParserUpdateRequest
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
    api_instance = openapi_client.XMergeApi(api_client)
    project_id = 'project_id_example' # str | 
    patched_doc_parser_update_request = openapi_client.PatchedDocParserUpdateRequest() # PatchedDocParserUpdateRequest |  (optional)

    try:
        # Update doc_parser project
        api_response = await api_instance.aiproducts_aiproducts_x_merge_doc_parser_partial_update(project_id, patched_doc_parser_update_request=patched_doc_parser_update_request)
        print("The response of XMergeApi->aiproducts_aiproducts_x_merge_doc_parser_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling XMergeApi->aiproducts_aiproducts_x_merge_doc_parser_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **patched_doc_parser_update_request** | [**PatchedDocParserUpdateRequest**](PatchedDocParserUpdateRequest.md)|  | [optional] 

### Return type

[**DocParserUpdate**](DocParserUpdate.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aiproducts_aiproducts_x_merge_doc_parser_retrieve**
> DocParserList aiproducts_aiproducts_x_merge_doc_parser_retrieve(project_id)

Retrieve doc_parser project

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.doc_parser_list import DocParserList
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
    api_instance = openapi_client.XMergeApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Retrieve doc_parser project
        api_response = await api_instance.aiproducts_aiproducts_x_merge_doc_parser_retrieve(project_id)
        print("The response of XMergeApi->aiproducts_aiproducts_x_merge_doc_parser_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling XMergeApi->aiproducts_aiproducts_x_merge_doc_parser_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**DocParserList**](DocParserList.md)

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

# **aiproducts_aiproducts_x_merge_list**
> List[XMergeList] aiproducts_aiproducts_x_merge_list()

List XMerge project

List all user XMerge projects

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.x_merge_list import XMergeList
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
    api_instance = openapi_client.XMergeApi(api_client)

    try:
        # List XMerge project
        api_response = await api_instance.aiproducts_aiproducts_x_merge_list()
        print("The response of XMergeApi->aiproducts_aiproducts_x_merge_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling XMergeApi->aiproducts_aiproducts_x_merge_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[XMergeList]**](XMergeList.md)

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

