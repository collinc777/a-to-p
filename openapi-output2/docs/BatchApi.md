# openapi_client.BatchApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_batch_list**](BatchApi.md#batch_batch_list) | **GET** /batch | List Batch Jobs
[**feature_batch_create**](BatchApi.md#feature_batch_create) | **POST** /{feature}/{subfeature}/batch/{name}/ | Launch Batch Job
[**feature_batch_destroy**](BatchApi.md#feature_batch_destroy) | **DELETE** /{feature}/{subfeature}/batch/{name}/ | Delete Batch Job
[**feature_batch_retrieve**](BatchApi.md#feature_batch_retrieve) | **GET** /{feature}/{subfeature}/batch/{name}/ | Get Batch Job Result


# **batch_batch_list**
> List[BatchList] batch_batch_list()

List Batch Jobs

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.batch_list import BatchList
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
    api_instance = openapi_client.BatchApi(api_client)

    try:
        # List Batch Jobs
        api_response = api_instance.batch_batch_list()
        print("The response of BatchApi->batch_batch_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_batch_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BatchList]**](BatchList.md)

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

# **feature_batch_create**
> BatchLaunchResponse feature_batch_create(feature, name, subfeature, batch_request)

Launch Batch Job

 Launch a async Batch job, given a job name that will be used as its id.  Each request should have the same parameters as you would normally pass to a feature.   You can also pass an optional paramater `name` to help better identify each requests you send.   Example with `text`/`sentiment_analysis`:  ```json \"requests\": [     {         \"text\": \"It's -25 outside and I am so hot.\",         \"language\": \"en\",         \"providers\": \"google,amazon\"     },     {         \"name\": \"mixed\",         \"text\": \"Overall I am satisfied with my experience at Amazon, but two areas of major improvement needed.\",         \"language\": \"en\",         \"providers\": \"google\"     },     ... ] ```   ### Limitations: You can have up to `5` concurrent running Jobs & input up to `500` requests per Batch           <details><summary><strong style='color: #0072a3; cursor: pointer'>Available Features</strong></summary>    |Feature Name|Subfeature Name| |------------|---------------| |`text`|`moderation`| |`text`|`chat`| |`text`|`question_answer`| |`image`|`logo_detection`| |`image`|`anonymization`| |`text`|`anonymization`| |`text`|`embeddings`| |`text`|`spell_check`| |`audio`|`speech_to_text_async`| |`image`|`landmark_detection`| |`audio`|`text_to_speech`| |`text`|`custom_named_entity_recognition`| |`image`|`face_detection`| |`text`|`custom_classification`| |`translation`|`automatic_translation`| |`translation`|`document_translation`| |`text`|`topic_extraction`| |`text`|`generation`| |`text`|`code_generation`| |`image`|`generation`| |`video`|`text_detection_async`| |`text`|`sentiment_analysis`| |`text`|`syntax_analysis`| |`text`|`keyword_extraction`| |`text`|`named_entity_recognition`| |`text`|`search`| |`text`|`summarize`| |`translation`|`language_detection`| |`image`|`object_detection`| |`image`|`explicit_content`| |`ocr`|`invoice_parser`| |`ocr`|`resume_parser`| |`ocr`|`receipt_parser`| |`ocr`|`identity_parser`|  </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.batch_launch_response import BatchLaunchResponse
from openapi_client.models.batch_request import BatchRequest
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
    api_instance = openapi_client.BatchApi(api_client)
    feature = 'feature_example' # str | 
    name = 'name_example' # str | 
    subfeature = 'subfeature_example' # str | 
    batch_request = openapi_client.BatchRequest() # BatchRequest | 

    try:
        # Launch Batch Job
        api_response = api_instance.feature_batch_create(feature, name, subfeature, batch_request)
        print("The response of BatchApi->feature_batch_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->feature_batch_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | **str**|  | 
 **name** | **str**|  | 
 **subfeature** | **str**|  | 
 **batch_request** | [**BatchRequest**](BatchRequest.md)|  | 

### Return type

[**BatchLaunchResponse**](BatchLaunchResponse.md)

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

# **feature_batch_destroy**
> feature_batch_destroy(feature, name, subfeature)

Delete Batch Job

Api view with custom pagination method to return paginated response from any queryset

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
    api_instance = openapi_client.BatchApi(api_client)
    feature = 'feature_example' # str | 
    name = 'name_example' # str | 
    subfeature = 'subfeature_example' # str | 

    try:
        # Delete Batch Job
        api_instance.feature_batch_destroy(feature, name, subfeature)
    except Exception as e:
        print("Exception when calling BatchApi->feature_batch_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | **str**|  | 
 **name** | **str**|  | 
 **subfeature** | **str**|  | 

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

# **feature_batch_retrieve**
> PaginatedBatchResponse feature_batch_retrieve(feature, name, subfeature, name2=name2, page=page, public_id=public_id, status=status)

Get Batch Job Result

Return paginated response of requests with their status and their responses if the request succeeded or errror if failed

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.paginated_batch_response import PaginatedBatchResponse
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
    api_instance = openapi_client.BatchApi(api_client)
    feature = 'feature_example' # str | 
    name = 'name_example' # str | 
    subfeature = 'subfeature_example' # str | 
    name2 = 'name_example' # str |  (optional)
    page = 56 # int |  (optional)
    public_id = 56 # int |  (optional)
    status = 'status_example' # str | * `succeeded` - Status Succeeded * `failed` - Status Failed * `finished` - Status Finished * `processing` - Status Processing (optional)

    try:
        # Get Batch Job Result
        api_response = api_instance.feature_batch_retrieve(feature, name, subfeature, name2=name2, page=page, public_id=public_id, status=status)
        print("The response of BatchApi->feature_batch_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->feature_batch_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | **str**|  | 
 **name** | **str**|  | 
 **subfeature** | **str**|  | 
 **name2** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **public_id** | **int**|  | [optional] 
 **status** | **str**| * &#x60;succeeded&#x60; - Status Succeeded * &#x60;failed&#x60; - Status Failed * &#x60;finished&#x60; - Status Finished * &#x60;processing&#x60; - Status Processing | [optional] 

### Return type

[**PaginatedBatchResponse**](PaginatedBatchResponse.md)

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

