# openapi_client.EmbeddingsApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_image_embeddings_create**](EmbeddingsApi.md#image_image_embeddings_create) | **POST** /image/embeddings | Embeddings
[**text_text_embeddings_create**](EmbeddingsApi.md#text_text_embeddings_create) | **POST** /text/embeddings | Embeddings


# **image_image_embeddings_create**
> ImageembeddingsResponseModel image_image_embeddings_create(imageembeddings_embeddings_request)

Embeddings

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**alephalpha**|-|`1.12.0`|0.05 (per 1 file)|1 file   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**English**|`en`| |**French**|`fr`| |**German**|`de`| |**Italian**|`it`| |**Spanish**|`es`|  </details><details><summary>Supported Models</summary><details><summary>alephalpha</summary>      |Name|Value| |----|-----| |**alephalpha**|`luminous-base`|  </details>  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imageembeddings_embeddings_request import ImageembeddingsEmbeddingsRequest
from openapi_client.models.imageembeddings_response_model import ImageembeddingsResponseModel
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
    api_instance = openapi_client.EmbeddingsApi(api_client)
    imageembeddings_embeddings_request = {"providers":"alephalpha","representation":"document","file_url":"http://edenai-resource-example.jpg"} # ImageembeddingsEmbeddingsRequest | 

    try:
        # Embeddings
        api_response = await api_instance.image_image_embeddings_create(imageembeddings_embeddings_request)
        print("The response of EmbeddingsApi->image_image_embeddings_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddingsApi->image_image_embeddings_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageembeddings_embeddings_request** | [**ImageembeddingsEmbeddingsRequest**](ImageembeddingsEmbeddingsRequest.md)|  | 

### Return type

[**ImageembeddingsResponseModel**](ImageembeddingsResponseModel.md)

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

# **text_text_embeddings_create**
> TextembeddingsResponseModel text_text_embeddings_create(textembeddings_embeddings_request)

Embeddings

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**openai**|-|`v3.0.0`|0.1 (per 1000000 token)|1 token |**google**|-|`v1`|0.1 (per 1000000 char)|1 char |**cohere**|-|`v1`|0.1 (per 1000000 char)|1 char |**cohere**|**4096embed-english-v2.0**|`v1`|0.1 (per 1000000 char)|1 char |**cohere**|**1024embed-english-light-v2.0**|`v1`|0.1 (per 1000000 char)|1 char |**cohere**|**768__embed-multilingual-v2.0**|`v1`|0.1 (per 1000000 char)|1 char |**mistral**|-|`v0.0.1`|0.1 (per 1000000 token)|1 token |**jina**|-|`v1`|0.018 (per 1000000 token)|1 token   </details>  <details><summary>Supported Models</summary><details><summary>openai</summary>      |Name|Value| |----|-----| |**openai**|`1536__text-embedding-ada-002`|  </details><details><summary>google</summary>      |Name|Value| |----|-----| |**google**|`768__textembedding-gecko`|  </details><details><summary>cohere</summary>      |Name|Value| |----|-----| |**cohere**|`1024__embed-english-light-v2.0`| ||`4096__embed-english-v2.0`| ||`768__embed-multilingual-v2.0`|  </details><details><summary>mistral</summary>      |Name|Value| |----|-----| |**mistral**|`1024__mistral-embed`|  </details><details><summary>jina</summary>      |Name|Value| |----|-----| |**jina**|`jina-embeddings-v2-base-code`| ||`jina-embeddings-v2-base-de`| ||`jina-embeddings-v2-base-en`| ||`jina-embeddings-v2-base-es`| ||`jina-embeddings-v2-base-zh`|  </details>  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textembeddings_embeddings_request import TextembeddingsEmbeddingsRequest
from openapi_client.models.textembeddings_response_model import TextembeddingsResponseModel
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
    api_instance = openapi_client.EmbeddingsApi(api_client)
    textembeddings_embeddings_request = {"providers":"mistral,jina,cohere,openai,google","texts":["Hello world"]} # TextembeddingsEmbeddingsRequest | 

    try:
        # Embeddings
        api_response = await api_instance.text_text_embeddings_create(textembeddings_embeddings_request)
        print("The response of EmbeddingsApi->text_text_embeddings_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddingsApi->text_text_embeddings_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **textembeddings_embeddings_request** | [**TextembeddingsEmbeddingsRequest**](TextembeddingsEmbeddingsRequest.md)|  | 

### Return type

[**TextembeddingsResponseModel**](TextembeddingsResponseModel.md)

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

