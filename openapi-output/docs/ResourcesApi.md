# openapi_client.ResourcesApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resources_resources_asset_create**](ResourcesApi.md#resources_resources_asset_create) | **POST** /resources/{resource}/asset/ | 
[**resources_resources_asset_destroy**](ResourcesApi.md#resources_resources_asset_destroy) | **DELETE** /resources/{resource}/asset/{asset}/ | 
[**resources_resources_asset_partial_update**](ResourcesApi.md#resources_resources_asset_partial_update) | **PATCH** /resources/{resource}/asset/{asset}/ | 
[**resources_resources_asset_retrieve**](ResourcesApi.md#resources_resources_asset_retrieve) | **GET** /resources/{resource}/asset/{asset}/ | 
[**resources_resources_asset_update**](ResourcesApi.md#resources_resources_asset_update) | **PUT** /resources/{resource}/asset/{asset}/ | 
[**resources_resources_create**](ResourcesApi.md#resources_resources_create) | **POST** /resources/ | 
[**resources_resources_destroy**](ResourcesApi.md#resources_resources_destroy) | **DELETE** /resources/{resource}/ | 
[**resources_resources_list**](ResourcesApi.md#resources_resources_list) | **GET** /resources/ | 
[**resources_resources_partial_update**](ResourcesApi.md#resources_resources_partial_update) | **PATCH** /resources/{resource}/ | 
[**resources_resources_retrieve**](ResourcesApi.md#resources_resources_retrieve) | **GET** /resources/{resource}/ | 
[**resources_resources_update**](ResourcesApi.md#resources_resources_update) | **PUT** /resources/{resource}/ | 


# **resources_resources_asset_create**
> AssetCreate resources_resources_asset_create(resource, asset_create_request)



### Example

* Bearer (JWT) Authentication (jwtAuth):

```python
import openapi_client
from openapi_client.models.asset_create import AssetCreate
from openapi_client.models.asset_create_request import AssetCreateRequest
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

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApi(api_client)
    resource = 'resource_example' # str | 
    asset_create_request = openapi_client.AssetCreateRequest() # AssetCreateRequest | 

    try:
        api_response = await api_instance.resources_resources_asset_create(resource, asset_create_request)
        print("The response of ResourcesApi->resources_resources_asset_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resources_resources_asset_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 
 **asset_create_request** | [**AssetCreateRequest**](AssetCreateRequest.md)|  | 

### Return type

[**AssetCreate**](AssetCreate.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_resources_asset_destroy**
> resources_resources_asset_destroy(asset, resource)



### Example

* Bearer (JWT) Authentication (jwtAuth):

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

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApi(api_client)
    asset = 'asset_example' # str | 
    resource = 'resource_example' # str | 

    try:
        await api_instance.resources_resources_asset_destroy(asset, resource)
    except Exception as e:
        print("Exception when calling ResourcesApi->resources_resources_asset_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **resource** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_resources_asset_partial_update**
> AssetUpdate resources_resources_asset_partial_update(asset, resource, patched_asset_update_request=patched_asset_update_request)



### Example

* Bearer (JWT) Authentication (jwtAuth):

```python
import openapi_client
from openapi_client.models.asset_update import AssetUpdate
from openapi_client.models.patched_asset_update_request import PatchedAssetUpdateRequest
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

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApi(api_client)
    asset = 'asset_example' # str | 
    resource = 'resource_example' # str | 
    patched_asset_update_request = openapi_client.PatchedAssetUpdateRequest() # PatchedAssetUpdateRequest |  (optional)

    try:
        api_response = await api_instance.resources_resources_asset_partial_update(asset, resource, patched_asset_update_request=patched_asset_update_request)
        print("The response of ResourcesApi->resources_resources_asset_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resources_resources_asset_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **resource** | **str**|  | 
 **patched_asset_update_request** | [**PatchedAssetUpdateRequest**](PatchedAssetUpdateRequest.md)|  | [optional] 

### Return type

[**AssetUpdate**](AssetUpdate.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_resources_asset_retrieve**
> AssetUpdate resources_resources_asset_retrieve(asset, resource)



### Example

* Bearer (JWT) Authentication (jwtAuth):

```python
import openapi_client
from openapi_client.models.asset_update import AssetUpdate
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

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApi(api_client)
    asset = 'asset_example' # str | 
    resource = 'resource_example' # str | 

    try:
        api_response = await api_instance.resources_resources_asset_retrieve(asset, resource)
        print("The response of ResourcesApi->resources_resources_asset_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resources_resources_asset_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **resource** | **str**|  | 

### Return type

[**AssetUpdate**](AssetUpdate.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_resources_asset_update**
> AssetUpdate resources_resources_asset_update(asset, resource, asset_update_request)



### Example

* Bearer (JWT) Authentication (jwtAuth):

```python
import openapi_client
from openapi_client.models.asset_update import AssetUpdate
from openapi_client.models.asset_update_request import AssetUpdateRequest
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

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApi(api_client)
    asset = 'asset_example' # str | 
    resource = 'resource_example' # str | 
    asset_update_request = openapi_client.AssetUpdateRequest() # AssetUpdateRequest | 

    try:
        api_response = await api_instance.resources_resources_asset_update(asset, resource, asset_update_request)
        print("The response of ResourcesApi->resources_resources_asset_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resources_resources_asset_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **resource** | **str**|  | 
 **asset_update_request** | [**AssetUpdateRequest**](AssetUpdateRequest.md)|  | 

### Return type

[**AssetUpdate**](AssetUpdate.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_resources_create**
> ResourceCreate resources_resources_create(resource_create_request)



### Example

* Bearer (JWT) Authentication (jwtAuth):

```python
import openapi_client
from openapi_client.models.resource_create import ResourceCreate
from openapi_client.models.resource_create_request import ResourceCreateRequest
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

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApi(api_client)
    resource_create_request = openapi_client.ResourceCreateRequest() # ResourceCreateRequest | 

    try:
        api_response = await api_instance.resources_resources_create(resource_create_request)
        print("The response of ResourcesApi->resources_resources_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resources_resources_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_create_request** | [**ResourceCreateRequest**](ResourceCreateRequest.md)|  | 

### Return type

[**ResourceCreate**](ResourceCreate.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_resources_destroy**
> resources_resources_destroy(resource)



### Example

* Bearer (JWT) Authentication (jwtAuth):

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

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApi(api_client)
    resource = 'resource_example' # str | 

    try:
        await api_instance.resources_resources_destroy(resource)
    except Exception as e:
        print("Exception when calling ResourcesApi->resources_resources_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_resources_list**
> List[ResourceList] resources_resources_list()



### Example

* Bearer (JWT) Authentication (jwtAuth):

```python
import openapi_client
from openapi_client.models.resource_list import ResourceList
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

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApi(api_client)

    try:
        api_response = await api_instance.resources_resources_list()
        print("The response of ResourcesApi->resources_resources_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resources_resources_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ResourceList]**](ResourceList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_resources_partial_update**
> ResourceUpdate resources_resources_partial_update(resource, patched_resource_update_request=patched_resource_update_request)



### Example

* Bearer (JWT) Authentication (jwtAuth):

```python
import openapi_client
from openapi_client.models.patched_resource_update_request import PatchedResourceUpdateRequest
from openapi_client.models.resource_update import ResourceUpdate
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

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApi(api_client)
    resource = 'resource_example' # str | 
    patched_resource_update_request = openapi_client.PatchedResourceUpdateRequest() # PatchedResourceUpdateRequest |  (optional)

    try:
        api_response = await api_instance.resources_resources_partial_update(resource, patched_resource_update_request=patched_resource_update_request)
        print("The response of ResourcesApi->resources_resources_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resources_resources_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 
 **patched_resource_update_request** | [**PatchedResourceUpdateRequest**](PatchedResourceUpdateRequest.md)|  | [optional] 

### Return type

[**ResourceUpdate**](ResourceUpdate.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_resources_retrieve**
> ResourceUpdate resources_resources_retrieve(resource)



### Example

* Bearer (JWT) Authentication (jwtAuth):

```python
import openapi_client
from openapi_client.models.resource_update import ResourceUpdate
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

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApi(api_client)
    resource = 'resource_example' # str | 

    try:
        api_response = await api_instance.resources_resources_retrieve(resource)
        print("The response of ResourcesApi->resources_resources_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resources_resources_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 

### Return type

[**ResourceUpdate**](ResourceUpdate.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_resources_update**
> ResourceUpdate resources_resources_update(resource, resource_update_request)



### Example

* Bearer (JWT) Authentication (jwtAuth):

```python
import openapi_client
from openapi_client.models.resource_update import ResourceUpdate
from openapi_client.models.resource_update_request import ResourceUpdateRequest
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

# Configure Bearer authorization (JWT): jwtAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApi(api_client)
    resource = 'resource_example' # str | 
    resource_update_request = openapi_client.ResourceUpdateRequest() # ResourceUpdateRequest | 

    try:
        api_response = await api_instance.resources_resources_update(resource, resource_update_request)
        print("The response of ResourcesApi->resources_resources_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->resources_resources_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 
 **resource_update_request** | [**ResourceUpdateRequest**](ResourceUpdateRequest.md)|  | 

### Return type

[**ResourceUpdate**](ResourceUpdate.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

