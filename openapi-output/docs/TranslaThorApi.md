# openapi_client.TranslaThorApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aiproducts_aiproducts_delete_destroy**](TranslaThorApi.md#aiproducts_aiproducts_delete_destroy) | **DELETE** /aiproducts/delete/{project_id} | Delete Project
[**aiproducts_aiproducts_list**](TranslaThorApi.md#aiproducts_aiproducts_list) | **GET** /aiproducts/ | List Projects
[**aiproducts_aiproducts_retrieve**](TranslaThorApi.md#aiproducts_aiproducts_retrieve) | **GET** /aiproducts/{project_id} | Retrieve Project
[**aiproducts_aiproducts_translathor_create**](TranslaThorApi.md#aiproducts_aiproducts_translathor_create) | **POST** /aiproducts/translathor/ | Create Language Provider Pair
[**aiproducts_aiproducts_translathor_destroy**](TranslaThorApi.md#aiproducts_aiproducts_translathor_destroy) | **DELETE** /aiproducts/translathor/{project_id} | Delete language
[**aiproducts_aiproducts_translathor_list**](TranslaThorApi.md#aiproducts_aiproducts_translathor_list) | **GET** /aiproducts/translathor/ | List all TranslaThor Projects
[**aiproducts_aiproducts_translathor_partial_update**](TranslaThorApi.md#aiproducts_aiproducts_translathor_partial_update) | **PATCH** /aiproducts/translathor/{project_id} | Update language
[**aiproducts_aiproducts_translathor_retrieve**](TranslaThorApi.md#aiproducts_aiproducts_translathor_retrieve) | **GET** /aiproducts/translathor/{project_id} | List languages
[**aiproducts_aiproducts_translathor_translate_create**](TranslaThorApi.md#aiproducts_aiproducts_translathor_translate_create) | **POST** /aiproducts/translathor/translate/{project_name} | Translate
[**aiproducts_aiproducts_translathor_translate_create2**](TranslaThorApi.md#aiproducts_aiproducts_translathor_translate_create2) | **POST** /aiproducts/translathor/{project_id}/translate | Translate


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
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslaThorApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Delete Project
        await api_instance.aiproducts_aiproducts_delete_destroy(project_id)
    except Exception as e:
        print("Exception when calling TranslaThorApi->aiproducts_aiproducts_delete_destroy: %s\n" % e)
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
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslaThorApi(api_client)
    project_type = 'project_type_example' # str |  (optional)

    try:
        # List Projects
        api_response = await api_instance.aiproducts_aiproducts_list(project_type=project_type)
        print("The response of TranslaThorApi->aiproducts_aiproducts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslaThorApi->aiproducts_aiproducts_list: %s\n" % e)
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
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslaThorApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Retrieve Project
        api_response = await api_instance.aiproducts_aiproducts_retrieve(project_id)
        print("The response of TranslaThorApi->aiproducts_aiproducts_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslaThorApi->aiproducts_aiproducts_retrieve: %s\n" % e)
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

# **aiproducts_aiproducts_translathor_create**
> UniversalTranslatorCreatet aiproducts_aiproducts_translathor_create(universal_translator_createt_request)

Create Language Provider Pair

Create a new language pair, and associate it to an existing project. If the project does not exist, a new project will be         created

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.universal_translator_createt import UniversalTranslatorCreatet
from openapi_client.models.universal_translator_createt_request import UniversalTranslatorCreatetRequest
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
    api_instance = openapi_client.TranslaThorApi(api_client)
    universal_translator_createt_request = openapi_client.UniversalTranslatorCreatetRequest() # UniversalTranslatorCreatetRequest | 

    try:
        # Create Language Provider Pair
        api_response = await api_instance.aiproducts_aiproducts_translathor_create(universal_translator_createt_request)
        print("The response of TranslaThorApi->aiproducts_aiproducts_translathor_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslaThorApi->aiproducts_aiproducts_translathor_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **universal_translator_createt_request** | [**UniversalTranslatorCreatetRequest**](UniversalTranslatorCreatetRequest.md)|  | 

### Return type

[**UniversalTranslatorCreatet**](UniversalTranslatorCreatet.md)

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

# **aiproducts_aiproducts_translathor_destroy**
> aiproducts_aiproducts_translathor_destroy(project_id, source_lang, target_lang)

Delete language

Delete a language pair withing a `project_name`. Both `source_lang` and `target_lang` query parameters should be provided.         **NB**: If  your source or target language references `any language`, use `all` as value for the query parameter

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
    api_instance = openapi_client.TranslaThorApi(api_client)
    project_id = 'project_id_example' # str | 
    source_lang = 'source_lang_example' # str | 
    target_lang = 'target_lang_example' # str | 

    try:
        # Delete language
        await api_instance.aiproducts_aiproducts_translathor_destroy(project_id, source_lang, target_lang)
    except Exception as e:
        print("Exception when calling TranslaThorApi->aiproducts_aiproducts_translathor_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **source_lang** | **str**|  | 
 **target_lang** | **str**|  | 

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

# **aiproducts_aiproducts_translathor_list**
> List[UniversalTranslatorList] aiproducts_aiproducts_translathor_list()

List all TranslaThor Projects

List all language pairs of all projects created by the user

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.universal_translator_list import UniversalTranslatorList
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
    api_instance = openapi_client.TranslaThorApi(api_client)

    try:
        # List all TranslaThor Projects
        api_response = await api_instance.aiproducts_aiproducts_translathor_list()
        print("The response of TranslaThorApi->aiproducts_aiproducts_translathor_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslaThorApi->aiproducts_aiproducts_translathor_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UniversalTranslatorList]**](UniversalTranslatorList.md)

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

# **aiproducts_aiproducts_translathor_partial_update**
> UniversalTranslatorCreatet aiproducts_aiproducts_translathor_partial_update(project_id, source_lang, target_lang, patched_universal_translator_createt_request=patched_universal_translator_createt_request)

Update language

Update a language pair withing a `project_name`. Both `source_lang` and `target_lang` query parameters should be provided.         **NB**: If  your source or target language references `any language`, use `all` as value for the query parameter

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.patched_universal_translator_createt_request import PatchedUniversalTranslatorCreatetRequest
from openapi_client.models.universal_translator_createt import UniversalTranslatorCreatet
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
    api_instance = openapi_client.TranslaThorApi(api_client)
    project_id = 'project_id_example' # str | 
    source_lang = 'source_lang_example' # str | 
    target_lang = 'target_lang_example' # str | 
    patched_universal_translator_createt_request = openapi_client.PatchedUniversalTranslatorCreatetRequest() # PatchedUniversalTranslatorCreatetRequest |  (optional)

    try:
        # Update language
        api_response = await api_instance.aiproducts_aiproducts_translathor_partial_update(project_id, source_lang, target_lang, patched_universal_translator_createt_request=patched_universal_translator_createt_request)
        print("The response of TranslaThorApi->aiproducts_aiproducts_translathor_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslaThorApi->aiproducts_aiproducts_translathor_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **source_lang** | **str**|  | 
 **target_lang** | **str**|  | 
 **patched_universal_translator_createt_request** | [**PatchedUniversalTranslatorCreatetRequest**](PatchedUniversalTranslatorCreatetRequest.md)|  | [optional] 

### Return type

[**UniversalTranslatorCreatet**](UniversalTranslatorCreatet.md)

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

# **aiproducts_aiproducts_translathor_retrieve**
> UniversalTranslatorList aiproducts_aiproducts_translathor_retrieve(project_id, source_lang, target_lang)

List languages

List all language pairs withing a `project_name`. You should at leat provide one or both of `source_lang` and `target_lang`         query parameters.           **Example**: to retreive this language pair (Any, Enlish):  aiproducts/translathor/{project_name}?source_lang=`all`&target_lang=`en`

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.universal_translator_list import UniversalTranslatorList
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
    api_instance = openapi_client.TranslaThorApi(api_client)
    project_id = 'project_id_example' # str | 
    source_lang = 'source_lang_example' # str | 
    target_lang = 'target_lang_example' # str | 

    try:
        # List languages
        api_response = await api_instance.aiproducts_aiproducts_translathor_retrieve(project_id, source_lang, target_lang)
        print("The response of TranslaThorApi->aiproducts_aiproducts_translathor_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslaThorApi->aiproducts_aiproducts_translathor_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **source_lang** | **str**|  | 
 **target_lang** | **str**|  | 

### Return type

[**UniversalTranslatorList**](UniversalTranslatorList.md)

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

# **aiproducts_aiproducts_translathor_translate_create**
> Dict[str, object] aiproducts_aiproducts_translathor_translate_create(project_name, universal_translator_call_request)

Translate

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.universal_translator_call_request import UniversalTranslatorCallRequest
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
    api_instance = openapi_client.TranslaThorApi(api_client)
    project_name = 'project_name_example' # str | 
    universal_translator_call_request = openapi_client.UniversalTranslatorCallRequest() # UniversalTranslatorCallRequest | 

    try:
        # Translate
        api_response = await api_instance.aiproducts_aiproducts_translathor_translate_create(project_name, universal_translator_call_request)
        print("The response of TranslaThorApi->aiproducts_aiproducts_translathor_translate_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslaThorApi->aiproducts_aiproducts_translathor_translate_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **universal_translator_call_request** | [**UniversalTranslatorCallRequest**](UniversalTranslatorCallRequest.md)|  | 

### Return type

**Dict[str, object]**

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

# **aiproducts_aiproducts_translathor_translate_create2**
> Dict[str, object] aiproducts_aiproducts_translathor_translate_create2(project_id, universal_translator_call_request)

Translate

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.universal_translator_call_request import UniversalTranslatorCallRequest
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
    api_instance = openapi_client.TranslaThorApi(api_client)
    project_id = 'project_id_example' # str | 
    universal_translator_call_request = openapi_client.UniversalTranslatorCallRequest() # UniversalTranslatorCallRequest | 

    try:
        # Translate
        api_response = await api_instance.aiproducts_aiproducts_translathor_translate_create2(project_id, universal_translator_call_request)
        print("The response of TranslaThorApi->aiproducts_aiproducts_translathor_translate_create2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslaThorApi->aiproducts_aiproducts_translathor_translate_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **universal_translator_call_request** | [**UniversalTranslatorCallRequest**](UniversalTranslatorCallRequest.md)|  | 

### Return type

**Dict[str, object]**

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

