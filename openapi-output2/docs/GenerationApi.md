# openapi_client.GenerationApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_image_generation_create**](GenerationApi.md#image_image_generation_create) | **POST** /image/generation | Image generation
[**text_text_generation_create**](GenerationApi.md#text_text_generation_create) | **POST** /text/generation | Generation


# **image_image_generation_create**
> ImagegenerationResponseModel image_image_generation_create(imagegeneration_generation_request)

Image generation

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Resolution|Price|Billing unit| |----|----|-------|------|-----|------------| |**deepai**|-|`v1Beta`|-|0.05 (per 1 request)|1 request |**openai**|**dall-e-3**|`v1Beta`|`1024x1024`|0.04 (per 1 image)|1 image |**openai**|**dall-e-2**|`v1Beta`|`256x256`|0.016 (per 1 image)|1 image |**openai**|**dall-e-2**|`v1Beta`|`512x512`|0.018 (per 1 image)|1 image |**openai**|**dall-e-2**|`v1Beta`|`1024x1024`|0.02 (per 1 image)|1 image |**openai**|**dall-e-3**|`v1Beta`|`1024x1792`|0.08 (per 1 image)|1 image |**openai**|**dall-e-3**|`v1Beta`|`1792x1024`|0.08 (per 1 image)|1 image |**openai**|-|`v1Beta`|`1024x1024`|0.04 (per 1 image)|1 image |**openai**|-|`v1Beta`|`512x512`|0.018 (per 1 image)|1 image |**openai**|-|`v1Beta`|`1024x1792`|0.08 (per 1 image)|1 image |**openai**|-|`v1Beta`|`1792x1024`|0.08 (per 1 image)|1 image |**stabilityai**|-|`v1Beta`|`512x512`|0.004 (per 1 image)|1 image |**stabilityai**|**stable-diffusion-xl-1024-v0-9**|`v1Beta`|`1024x1024`|2.0 (per 1 image)|1 image |**stabilityai**|**stable-diffusion-xl-1024-v1-0**|`v1Beta`|`1024x1024`|0.25 (per 1 image)|1 image |**stabilityai**|**stable-diffusion-xl-beta-v2-2-2**|`v1Beta`|`512x512`|0.83 (per 1 image)|1 image |**stabilityai**|**stable-diffusion-v1-6**|`v1Beta`|`1024x1024`|0.0043 (per 1 image)|1 image |**stabilityai**|-|`v1Beta`|`1024x1024`|0.25 (per 1 image)|1 image |**replicate**|**anime-style**|`v1`|-|0.000225 (per 1 exec_time)|1 exec_time |**replicate**|**classic**|`v1`|-|0.00115 (per 1 exec_time)|1 exec_time |**replicate**|-|`v1`|-|0.000225 (per 1 exec_time)|1 exec_time |**replicate**|**vintedois-diffusion**|`v1`|-|0.000225 (per 1 exec_time)|1 exec_time |**amazon**|-|`boto3 (v1.29.6)`|`512x512`|0.01 (per 1 image)|1 image |**amazon**|-|`boto3 (v1.29.6)`|`1024x1024`|0.012 (per 1 image)|1 image |**amazon**|**titan-image-generator-v1_premium**|`boto3 (v1.29.6)`|`512x512`|0.01 (per 1 image)|1 image |**amazon**|**titan-image-generator-v1_premium**|`boto3 (v1.29.6)`|`1024x1024`|0.012 (per 1 image)|1 image |**amazon**|**titan-image-generator-v1_standard**|`boto3 (v1.29.6)`|`512x512`|0.008 (per 1 image)|1 image |**amazon**|**titan-image-generator-v1_standard**|`boto3 (v1.29.6)`|`1024x1024`|0.01 (per 1 image)|1 image   </details>  <details><summary>Supported Models</summary><details><summary>openai</summary>      |Name|Value| |----|-----| |**openai**|`dall-e-2`| ||`dall-e-3`|  </details><details><summary>stabilityai</summary>      |Name|Value| |----|-----| |**stabilityai**|`esrgan-v1-x2plus`| ||`stable-diffusion-v1-6`| ||`stable-diffusion-xl-1024-v0-9`| ||`stable-diffusion-xl-1024-v1-0`| ||`stable-diffusion-xl-beta-v2-2-2`|  </details><details><summary>replicate</summary>      |Name|Value| |----|-----| |**replicate**|`anime-style`| ||`classic`| ||`vintedois-diffusion`|  </details><details><summary>amazon</summary>      |Name|Value| |----|-----| |**amazon**|`titan-image-generator-v1_premium`| ||`titan-image-generator-v1_standard`|  </details>  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imagegeneration_generation_request import ImagegenerationGenerationRequest
from openapi_client.models.imagegeneration_response_model import ImagegenerationResponseModel
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
    api_instance = openapi_client.GenerationApi(api_client)
    imagegeneration_generation_request = {"providers":"stabilityai,amazon,deepai,replicate,openai","text":"A huge red ballon flying outside the city.","resolution":"512x512","num_images":2} # ImagegenerationGenerationRequest | 

    try:
        # Image generation
        api_response = api_instance.image_image_generation_create(imagegeneration_generation_request)
        print("The response of GenerationApi->image_image_generation_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationApi->image_image_generation_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imagegeneration_generation_request** | [**ImagegenerationGenerationRequest**](ImagegenerationGenerationRequest.md)|  | 

### Return type

[**ImagegenerationResponseModel**](ImagegenerationResponseModel.md)

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

# **text_text_generation_create**
> TextgenerationResponseModel text_text_generation_create(textgeneration_generation_request)

Generation

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**cohere**|**command**|`2022-12-06`|2.0 (per 1000000 token)|1 token |**cohere**|**command-light**|`2022-12-06`|0.6 (per 1000000 token)|1 token |**cohere**|**command-light-nightly**|`2022-12-06`|0.6 (per 1000000 token)|1 token |**cohere**|**command-nightly**|`2022-12-06`|2.0 (per 1000000 token)|1 token |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token |**openai**|-|`v1`|2.0 (per 1000000 token)|1 token |**openai**|**gpt-3.5-turbo-instruct**|`v1`|2.0 (per 1000000 token)|1 token |**openai**|**text-babbage-002**|`v1`|0.4 (per 1000000 token)|1 token |**openai**|**text-davinci-002**|`v1`|2.0 (per 1000000 token)|1 token |**google**|-|`v1`|0.375 (per 1000000 char)|1000 char |**google**|**gemini-pro**|`v1`|0.375 (per 1000000 char)|1000 char |**google**|**text-bison**|`v1`|0.5 (per 1000000 char)|1000 char |**ai21labs**|-|`v1`|0.0188 (per 1000 token)|1 token |**ai21labs**|**j2-mid**|`v1`|0.0125 (per 1000 token)|1 token |**ai21labs**|**j2-ultra**|`v1`|0.0188 (per 1000 token)|1 token |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token |**anthropic**|**claude-v1**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token |**anthropic**|-|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token |**mistral**|-|`v0.0.1`|24.0 (per 1000000 token)|1 token |**mistral**|**large-latest**|`v0.0.1`|24.0 (per 1000000 token)|1 token |**mistral**|**mistral-medium**|`v0.0.1`|8.1 (per 1000000 token)|1 token |**mistral**|**mistral-small**|`v0.0.1`|6.0 (per 1000000 token)|1 token |**mistral**|**mistral-tiny**|`v0.0.1`|0.42 (per 1000000 token)|1 token |**amazon**|-|`v1`|1.6 (per 1000000 token)|1 token |**amazon**|**titan-text-express-v1**|`v1`|1.6 (per 1000000 token)|1 token |**amazon**|**titan-text-lite-v1**|`v1`|0.4 (per 1000000 token)|1 token |**amazon**|**titan-tg1-large**|`v1`|1.6 (per 1000000 token)|1 token |**meta**|-|`v1`|2.56 (per 1000000 token)|1 token |**meta**|**llama2-13b-chat-v1**|`v1`|1.0 (per 1000000 token)|1 token |**meta**|**llama2-70b-chat-v1**|`v1`|2.56 (per 1000000 token)|1 token   </details>  <details><summary>Supported Models</summary><details><summary>cohere</summary>      |Name|Value| |----|-----| |**cohere**|`command`| ||`command-light`| ||`command-light-nightly`| ||`command-nightly`|  </details><details><summary>openai</summary>      |Name|Value| |----|-----| |**openai**|`babbage-002`| ||`davinci-002`| ||`gpt-3.5-turbo-instruct`|  </details><details><summary>google</summary>      |Name|Value| |----|-----| |**google**|`gemini-pro`| ||`text-bison`|  </details><details><summary>ai21labs</summary>      |Name|Value| |----|-----| |**ai21labs**|`j2-grande-instruct`| ||`j2-jumbo-instruct`| ||`j2-mid`| ||`j2-ultra`|  </details><details><summary>anthropic</summary>      |Name|Value| |----|-----| |**anthropic**|`claude-instant-v1`| ||`claude-v1`| ||`claude-v2`|  </details><details><summary>mistral</summary>      |Name|Value| |----|-----| |**mistral**|`large-latest`| ||`medium`| ||`small`| ||`tiny`|  </details><details><summary>amazon</summary>      |Name|Value| |----|-----| |**amazon**|`titan-text-express-v1`| ||`titan-text-lite-v1`| ||`titan-tg1-large`|  </details><details><summary>meta</summary>      |Name|Value| |----|-----| |**meta**|`llama2-13b-chat-v1`| ||`llama2-70b-chat-v1`|  </details>  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textgeneration_generation_request import TextgenerationGenerationRequest
from openapi_client.models.textgeneration_response_model import TextgenerationResponseModel
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
    api_instance = openapi_client.GenerationApi(api_client)
    textgeneration_generation_request = {"providers":"amazon,mistral,cohere,anthropic,meta,openai,ai21labs,google","text":"The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?","max_tokens":10,"temperature":0} # TextgenerationGenerationRequest | 

    try:
        # Generation
        api_response = api_instance.text_text_generation_create(textgeneration_generation_request)
        print("The response of GenerationApi->text_text_generation_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerationApi->text_text_generation_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **textgeneration_generation_request** | [**TextgenerationGenerationRequest**](TextgenerationGenerationRequest.md)|  | 

### Return type

[**TextgenerationResponseModel**](TextgenerationResponseModel.md)

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

