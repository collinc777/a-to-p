# openapi_client.SearchApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_image_search_delete_image_create**](SearchApi.md#image_image_search_delete_image_create) | **POST** /image/search/delete_image | Search - Delete phase
[**image_image_search_get_image_retrieve**](SearchApi.md#image_image_search_get_image_retrieve) | **GET** /image/search/get_image | Search - get image
[**image_image_search_get_images_retrieve**](SearchApi.md#image_image_search_get_images_retrieve) | **GET** /image/search/get_images | Search - list all images
[**image_image_search_launch_similarity_create**](SearchApi.md#image_image_search_launch_similarity_create) | **POST** /image/search/launch_similarity | Search - launch similarity
[**image_image_search_upload_image_create**](SearchApi.md#image_image_search_upload_image_create) | **POST** /image/search/upload_image | Search - Upload Phase
[**text_text_search_create**](SearchApi.md#text_text_search_create) | **POST** /text/search | Search


# **image_image_search_delete_image_create**
> ImagesearchResponseModel image_image_search_delete_image_create(imagesearchdelete_image_delete_image_request)

Search - Delete phase

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**sentisight**|`v3.3.1`|free|- |**nyckel**|`v1.0.0`|free|-   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imagesearch_response_model import ImagesearchResponseModel
from openapi_client.models.imagesearchdelete_image_delete_image_request import ImagesearchdeleteImageDeleteImageRequest
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
    api_instance = openapi_client.SearchApi(api_client)
    imagesearchdelete_image_delete_image_request = {"providers":"sentisight,sentisight,sentisight,sentisight,sentisight,nyckel,nyckel,nyckel,nyckel,nyckel","image_name":"test.jpg","project_id":"42874"} # ImagesearchdeleteImageDeleteImageRequest | 

    try:
        # Search - Delete phase
        api_response = await api_instance.image_image_search_delete_image_create(imagesearchdelete_image_delete_image_request)
        print("The response of SearchApi->image_image_search_delete_image_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->image_image_search_delete_image_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imagesearchdelete_image_delete_image_request** | [**ImagesearchdeleteImageDeleteImageRequest**](ImagesearchdeleteImageDeleteImageRequest.md)|  | 

### Return type

[**ImagesearchResponseModel**](ImagesearchResponseModel.md)

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

# **image_image_search_get_image_retrieve**
> ImagesearchResponseModel image_image_search_get_image_retrieve(image_name, providers, attributes_as_list=attributes_as_list, fallback_providers=fallback_providers, response_as_dict=response_as_dict, show_original_response=show_original_response)

Search - get image

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**sentisight**|`v3.3.1`|free|- |**nyckel**|`v1.0.0`|free|-   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imagesearch_response_model import ImagesearchResponseModel
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
    api_instance = openapi_client.SearchApi(api_client)
    image_name = 'image_name_example' # str | 
    providers = 'providers_example' # str | It can be one (ex: **'amazon'** or **'google'**) or multiple provider(s) (ex: **'amazon,microsoft,google'**)             that the data will be redirected to in order to get the processed results.
    attributes_as_list = False # bool | Optional : When set to **false** (default) the structure of the extracted items is list of objects having different attributes : <br>      ```{'items': [{\"attribute_1\": \"x1\",\"attribute_2\": \"y2\"}, ... ]}``` <br>      When it is set to **true**, the response contains an object with each attribute as a list : <br>      ```{ \"attribute_1\": [\"x1\",\"x2\", ...], \"attribute_2\": [y1, y2, ...]}```  (optional) (default to False)
    fallback_providers = 'fallback_providers_example' # str | Providers in this list will be used as fallback if the call to provider in `providers` parameter fails.     To use this feature, you must input **only one** provider in the `providers` parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn't fail.   *Doesn't work with async subfeatures.*      (optional)
    response_as_dict = True # bool | Optional : When set to **true** (default), the response is an object of responses with providers names as keys : <br>                    ``` {\"google\" : { \"status\": \"success\", ... }, } ``` <br>                 When set to **false** the response structure is a list of response objects : <br>                     ``` [{\"status\": \"success\", \"provider\": \"google\" ... }, ] ```. <br>                    (optional) (default to True)
    show_original_response = False # bool | Optional : Shows the original response of the provider.<br>         When set to **true**, a new attribute *original_response* will appear in the response object. (optional) (default to False)

    try:
        # Search - get image
        api_response = await api_instance.image_image_search_get_image_retrieve(image_name, providers, attributes_as_list=attributes_as_list, fallback_providers=fallback_providers, response_as_dict=response_as_dict, show_original_response=show_original_response)
        print("The response of SearchApi->image_image_search_get_image_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->image_image_search_get_image_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_name** | **str**|  | 
 **providers** | **str**| It can be one (ex: **&#39;amazon&#39;** or **&#39;google&#39;**) or multiple provider(s) (ex: **&#39;amazon,microsoft,google&#39;**)             that the data will be redirected to in order to get the processed results. | 
 **attributes_as_list** | **bool**| Optional : When set to **false** (default) the structure of the extracted items is list of objects having different attributes : &lt;br&gt;      &#x60;&#x60;&#x60;{&#39;items&#39;: [{\&quot;attribute_1\&quot;: \&quot;x1\&quot;,\&quot;attribute_2\&quot;: \&quot;y2\&quot;}, ... ]}&#x60;&#x60;&#x60; &lt;br&gt;      When it is set to **true**, the response contains an object with each attribute as a list : &lt;br&gt;      &#x60;&#x60;&#x60;{ \&quot;attribute_1\&quot;: [\&quot;x1\&quot;,\&quot;x2\&quot;, ...], \&quot;attribute_2\&quot;: [y1, y2, ...]}&#x60;&#x60;&#x60;  | [optional] [default to False]
 **fallback_providers** | **str**| Providers in this list will be used as fallback if the call to provider in &#x60;providers&#x60; parameter fails.     To use this feature, you must input **only one** provider in the &#x60;providers&#x60; parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn&#39;t fail.   *Doesn&#39;t work with async subfeatures.*      | [optional] 
 **response_as_dict** | **bool**| Optional : When set to **true** (default), the response is an object of responses with providers names as keys : &lt;br&gt;                    &#x60;&#x60;&#x60; {\&quot;google\&quot; : { \&quot;status\&quot;: \&quot;success\&quot;, ... }, } &#x60;&#x60;&#x60; &lt;br&gt;                 When set to **false** the response structure is a list of response objects : &lt;br&gt;                     &#x60;&#x60;&#x60; [{\&quot;status\&quot;: \&quot;success\&quot;, \&quot;provider\&quot;: \&quot;google\&quot; ... }, ] &#x60;&#x60;&#x60;. &lt;br&gt;                    | [optional] [default to True]
 **show_original_response** | **bool**| Optional : Shows the original response of the provider.&lt;br&gt;         When set to **true**, a new attribute *original_response* will appear in the response object. | [optional] [default to False]

### Return type

[**ImagesearchResponseModel**](ImagesearchResponseModel.md)

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

# **image_image_search_get_images_retrieve**
> ImagesearchResponseModel image_image_search_get_images_retrieve(providers, attributes_as_list=attributes_as_list, fallback_providers=fallback_providers, response_as_dict=response_as_dict, show_original_response=show_original_response)

Search - list all images

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**sentisight**|`v3.3.1`|free|- |**nyckel**|`v1.0.0`|free|-   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imagesearch_response_model import ImagesearchResponseModel
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
    api_instance = openapi_client.SearchApi(api_client)
    providers = 'providers_example' # str | It can be one (ex: **'amazon'** or **'google'**) or multiple provider(s) (ex: **'amazon,microsoft,google'**)             that the data will be redirected to in order to get the processed results.
    attributes_as_list = False # bool | Optional : When set to **false** (default) the structure of the extracted items is list of objects having different attributes : <br>      ```{'items': [{\"attribute_1\": \"x1\",\"attribute_2\": \"y2\"}, ... ]}``` <br>      When it is set to **true**, the response contains an object with each attribute as a list : <br>      ```{ \"attribute_1\": [\"x1\",\"x2\", ...], \"attribute_2\": [y1, y2, ...]}```  (optional) (default to False)
    fallback_providers = 'fallback_providers_example' # str | Providers in this list will be used as fallback if the call to provider in `providers` parameter fails.     To use this feature, you must input **only one** provider in the `providers` parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn't fail.   *Doesn't work with async subfeatures.*      (optional)
    response_as_dict = True # bool | Optional : When set to **true** (default), the response is an object of responses with providers names as keys : <br>                    ``` {\"google\" : { \"status\": \"success\", ... }, } ``` <br>                 When set to **false** the response structure is a list of response objects : <br>                     ``` [{\"status\": \"success\", \"provider\": \"google\" ... }, ] ```. <br>                    (optional) (default to True)
    show_original_response = False # bool | Optional : Shows the original response of the provider.<br>         When set to **true**, a new attribute *original_response* will appear in the response object. (optional) (default to False)

    try:
        # Search - list all images
        api_response = await api_instance.image_image_search_get_images_retrieve(providers, attributes_as_list=attributes_as_list, fallback_providers=fallback_providers, response_as_dict=response_as_dict, show_original_response=show_original_response)
        print("The response of SearchApi->image_image_search_get_images_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->image_image_search_get_images_retrieve: %s\n" % e)
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

[**ImagesearchResponseModel**](ImagesearchResponseModel.md)

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

# **image_image_search_launch_similarity_create**
> ImagesearchResponseModel image_image_search_launch_similarity_create(imagesearchlaunch_similarity_search_image_request)

Search - launch similarity

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**sentisight**|`v3.3.1`|1.0 (per 1000 file)|1 file |**nyckel**|`v1.0.0`|1.0 (per 1000 file)|1 file   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imagesearch_response_model import ImagesearchResponseModel
from openapi_client.models.imagesearchlaunch_similarity_search_image_request import ImagesearchlaunchSimilaritySearchImageRequest
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
    api_instance = openapi_client.SearchApi(api_client)
    imagesearchlaunch_similarity_search_image_request = {"providers":"sentisight,sentisight,sentisight,sentisight,sentisight,nyckel,nyckel,nyckel,nyckel,nyckel","project_id":"42874","file_url":"http://edenai-resource-example.jpg"} # ImagesearchlaunchSimilaritySearchImageRequest | 

    try:
        # Search - launch similarity
        api_response = await api_instance.image_image_search_launch_similarity_create(imagesearchlaunch_similarity_search_image_request)
        print("The response of SearchApi->image_image_search_launch_similarity_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->image_image_search_launch_similarity_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imagesearchlaunch_similarity_search_image_request** | [**ImagesearchlaunchSimilaritySearchImageRequest**](ImagesearchlaunchSimilaritySearchImageRequest.md)|  | 

### Return type

[**ImagesearchResponseModel**](ImagesearchResponseModel.md)

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

# **image_image_search_upload_image_create**
> ImagesearchResponseModel image_image_search_upload_image_create(imagesearchupload_image_upload_image_request)

Search - Upload Phase

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**sentisight**|`v3.3.1`|1.0 (per 1000 file)|1 file |**nyckel**|`v1.0.0`|0.5 (per 1000 file)|1 file   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imagesearch_response_model import ImagesearchResponseModel
from openapi_client.models.imagesearchupload_image_upload_image_request import ImagesearchuploadImageUploadImageRequest
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
    api_instance = openapi_client.SearchApi(api_client)
    imagesearchupload_image_upload_image_request = {"providers":"sentisight,sentisight,sentisight,sentisight,sentisight,nyckel,nyckel,nyckel,nyckel,nyckel","image_name":"test.jpg","project_id":"42874","file_url":"http://edenai-resource-example.jpg"} # ImagesearchuploadImageUploadImageRequest | 

    try:
        # Search - Upload Phase
        api_response = await api_instance.image_image_search_upload_image_create(imagesearchupload_image_upload_image_request)
        print("The response of SearchApi->image_image_search_upload_image_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->image_image_search_upload_image_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imagesearchupload_image_upload_image_request** | [**ImagesearchuploadImageUploadImageRequest**](ImagesearchuploadImageUploadImageRequest.md)|  | 

### Return type

[**ImagesearchResponseModel**](ImagesearchResponseModel.md)

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

# **text_text_search_create**
> TextsearchResponseModel text_text_search_create(textsearch_search_request)

Search

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token |**cohere**|`v1`|0.1 (per 1000000 char)|1 char |**google**|`v1`|0.1 (per 1000000 char)|1 char   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textsearch_response_model import TextsearchResponseModel
from openapi_client.models.textsearch_search_request import TextsearchSearchRequest
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
    api_instance = openapi_client.SearchApi(api_client)
    textsearch_search_request = {"providers":"openai,google,cohere","texts":["In Roman mythology, Romulus and Remus (Latin: [ˈroːmʊlʊs], [ˈrɛmʊs]) are twin brothers whose story tells of the events that led to the founding of the city of Rome and the Roman Kingdom by Romulus.","In ancient Roman religion and myth, Mars (Latin: Mārs, pronounced [maːrs]) was the god of war and also an agricultural guardian, a combination characteristic of early Rome.","Proto-Indo-European mythology is the body of myths and deities associated with the Proto-Indo-Europeans, the hypothetical speakers of the reconstructed Proto-Indo-European language","The Ashvamedha (Sanskrit: अश्वमेध, romanized: aśvamedha) was a horse sacrifice ritual followed by the Śrauta tradition of Vedic religion.","Purusha (puruṣa or Sanskrit: पुरुष) is a complex concept whose meaning evolved in Vedic and Upanishadic times. Depending on source and historical timeline, it means the cosmic being or self, consciousness, and universal principle."],"query":"Rome"} # TextsearchSearchRequest | 

    try:
        # Search
        api_response = await api_instance.text_text_search_create(textsearch_search_request)
        print("The response of SearchApi->text_text_search_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->text_text_search_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **textsearch_search_request** | [**TextsearchSearchRequest**](TextsearchSearchRequest.md)|  | 

### Return type

[**TextsearchResponseModel**](TextsearchResponseModel.md)

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

