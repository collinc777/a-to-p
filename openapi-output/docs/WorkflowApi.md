# openapi_client.WorkflowApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflow_workflow_create**](WorkflowApi.md#workflow_workflow_create) | **POST** /workflow/ | 
[**workflow_workflow_destroy**](WorkflowApi.md#workflow_workflow_destroy) | **DELETE** /workflow/{workflow_id}/ | 
[**workflow_workflow_execution_create**](WorkflowApi.md#workflow_workflow_execution_create) | **POST** /workflow/{workflow_id}/execution/ | 
[**workflow_workflow_execution_list**](WorkflowApi.md#workflow_workflow_execution_list) | **GET** /workflow/{workflow_id}/execution/ | 
[**workflow_workflow_execution_retrieve**](WorkflowApi.md#workflow_workflow_execution_retrieve) | **GET** /workflow/{workflow_id}/execution/{execution_id}/ | 
[**workflow_workflow_list**](WorkflowApi.md#workflow_workflow_list) | **GET** /workflow/ | 
[**workflow_workflow_partial_update**](WorkflowApi.md#workflow_workflow_partial_update) | **PATCH** /workflow/{workflow_id}/ | 
[**workflow_workflow_retrieve**](WorkflowApi.md#workflow_workflow_retrieve) | **GET** /workflow/{workflow_id}/ | 
[**workflow_workflow_update**](WorkflowApi.md#workflow_workflow_update) | **PUT** /workflow/{workflow_id}/ | 


# **workflow_workflow_create**
> Workflow workflow_workflow_create(workflow_request)



List all workflows or create a new workflow.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.workflow import Workflow
from openapi_client.models.workflow_request import WorkflowRequest
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
    api_instance = openapi_client.WorkflowApi(api_client)
    workflow_request = openapi_client.WorkflowRequest() # WorkflowRequest | 

    try:
        api_response = await api_instance.workflow_workflow_create(workflow_request)
        print("The response of WorkflowApi->workflow_workflow_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowApi->workflow_workflow_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_request** | [**WorkflowRequest**](WorkflowRequest.md)|  | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_workflow_destroy**
> workflow_workflow_destroy(workflow_id)



Retrieve or update specific workflow.

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
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WorkflowApi(api_client)
    workflow_id = 'workflow_id_example' # str | 

    try:
        await api_instance.workflow_workflow_destroy(workflow_id)
    except Exception as e:
        print("Exception when calling WorkflowApi->workflow_workflow_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**|  | 

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

# **workflow_workflow_execution_create**
> ExecutionList workflow_workflow_execution_create(workflow_id, execution_list_request=execution_list_request)



### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.execution_list import ExecutionList
from openapi_client.models.execution_list_request import ExecutionListRequest
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
    api_instance = openapi_client.WorkflowApi(api_client)
    workflow_id = 'workflow_id_example' # str | 
    execution_list_request = openapi_client.ExecutionListRequest() # ExecutionListRequest |  (optional)

    try:
        api_response = await api_instance.workflow_workflow_execution_create(workflow_id, execution_list_request=execution_list_request)
        print("The response of WorkflowApi->workflow_workflow_execution_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowApi->workflow_workflow_execution_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**|  | 
 **execution_list_request** | [**ExecutionListRequest**](ExecutionListRequest.md)|  | [optional] 

### Return type

[**ExecutionList**](ExecutionList.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_workflow_execution_list**
> PaginatedExecutionListList workflow_workflow_execution_list(workflow_id, page=page, page_size=page_size)



### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.paginated_execution_list_list import PaginatedExecutionListList
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
    api_instance = openapi_client.WorkflowApi(api_client)
    workflow_id = 'workflow_id_example' # str | 
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = await api_instance.workflow_workflow_execution_list(workflow_id, page=page, page_size=page_size)
        print("The response of WorkflowApi->workflow_workflow_execution_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowApi->workflow_workflow_execution_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedExecutionListList**](PaginatedExecutionListList.md)

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

# **workflow_workflow_execution_retrieve**
> Execution workflow_workflow_execution_retrieve(execution_id, workflow_id)



Retrieve a specific execution.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.execution import Execution
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
    api_instance = openapi_client.WorkflowApi(api_client)
    execution_id = 'execution_id_example' # str | 
    workflow_id = 'workflow_id_example' # str | 

    try:
        api_response = await api_instance.workflow_workflow_execution_retrieve(execution_id, workflow_id)
        print("The response of WorkflowApi->workflow_workflow_execution_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowApi->workflow_workflow_execution_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**|  | 
 **workflow_id** | **str**|  | 

### Return type

[**Execution**](Execution.md)

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

# **workflow_workflow_list**
> List[Workflow] workflow_workflow_list()



List all workflows or create a new workflow.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.workflow import Workflow
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
    api_instance = openapi_client.WorkflowApi(api_client)

    try:
        api_response = await api_instance.workflow_workflow_list()
        print("The response of WorkflowApi->workflow_workflow_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowApi->workflow_workflow_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Workflow]**](Workflow.md)

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

# **workflow_workflow_partial_update**
> Workflow workflow_workflow_partial_update(workflow_id, patched_workflow_request=patched_workflow_request)



Retrieve or update specific workflow.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.patched_workflow_request import PatchedWorkflowRequest
from openapi_client.models.workflow import Workflow
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
    api_instance = openapi_client.WorkflowApi(api_client)
    workflow_id = 'workflow_id_example' # str | 
    patched_workflow_request = openapi_client.PatchedWorkflowRequest() # PatchedWorkflowRequest |  (optional)

    try:
        api_response = await api_instance.workflow_workflow_partial_update(workflow_id, patched_workflow_request=patched_workflow_request)
        print("The response of WorkflowApi->workflow_workflow_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowApi->workflow_workflow_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**|  | 
 **patched_workflow_request** | [**PatchedWorkflowRequest**](PatchedWorkflowRequest.md)|  | [optional] 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_workflow_retrieve**
> Workflow workflow_workflow_retrieve(workflow_id)



Retrieve or update specific workflow.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.workflow import Workflow
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
    api_instance = openapi_client.WorkflowApi(api_client)
    workflow_id = 'workflow_id_example' # str | 

    try:
        api_response = await api_instance.workflow_workflow_retrieve(workflow_id)
        print("The response of WorkflowApi->workflow_workflow_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowApi->workflow_workflow_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**|  | 

### Return type

[**Workflow**](Workflow.md)

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

# **workflow_workflow_update**
> Workflow workflow_workflow_update(workflow_id, workflow_request)



Retrieve or update specific workflow.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.workflow import Workflow
from openapi_client.models.workflow_request import WorkflowRequest
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
    api_instance = openapi_client.WorkflowApi(api_client)
    workflow_id = 'workflow_id_example' # str | 
    workflow_request = openapi_client.WorkflowRequest() # WorkflowRequest | 

    try:
        api_response = await api_instance.workflow_workflow_update(workflow_id, workflow_request)
        print("The response of WorkflowApi->workflow_workflow_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowApi->workflow_workflow_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**|  | 
 **workflow_request** | [**WorkflowRequest**](WorkflowRequest.md)|  | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

