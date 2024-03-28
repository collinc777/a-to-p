# openapi_client.ChatApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_text_chat_create**](ChatApi.md#text_text_chat_create) | **POST** /text/chat | Chat
[**text_text_chat_stream_create**](ChatApi.md#text_text_chat_stream_create) | **POST** /text/chat/stream | Chat Stream


# **text_text_chat_create**
> TextchatResponseModel text_text_chat_create(textchat_chat_request)

Chat

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**openai**|**gpt-3.5-turbo**|`v1Beta`|0.002 (per 1000 token)|1 token |**openai**|**gpt-3.5-turbo-1106**|`v1Beta`|0.002 (per 1000 token)|1 token |**openai**|-|`v1Beta`|0.002 (per 1000 token)|1 token |**openai**|**gpt-4**|`v1Beta`|0.06 (per 1000 token)|1 token |**openai**|**gpt-3.5-turbo-0301**|`v1Beta`|0.002 (per 1000 token)|1 token |**openai**|**gpt-4-0314**|`v1Beta`|0.06 (per 1000 token)|1 token |**openai**|**gpt-3.5-turbo-16k**|`v1Beta`|0.004 (per 1000 token)|1 token |**openai**|**gpt-4-1106-preview**|`v1Beta`|0.03 (per 1000 token)|1 token |**openai**|**gpt-4-vision-preview**|`v1Beta`|0.03 (per 1000 token)|1 token |**google**|-|`v1`|0.5 (per 1000000 char)|1000 char |**replicate**|-|`v1`|0.0032 (per 1 exec_time)|1 exec_time |**cohere**|**command**|`2022-12-06`|2.0 (per 1000000 token)|1 token |**cohere**|**command-light**|`2022-12-06`|0.6 (per 1000000 token)|1 token |**cohere**|**command-light-nightly**|`2022-12-06`|0.6 (per 1000000 token)|1 token |**cohere**|**command-nightly**|`2022-12-06`|2.0 (per 1000000 token)|1 token |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token |**meta**|-|`v1`|2.56 (per 1000000 token)|1 token |**meta**|**llama2-13b-chat-v1**|`v1`|1.0 (per 1000000 token)|1 token |**meta**|**llama2-70b-chat-v1**|`v1`|2.56 (per 1000000 token)|1 token |**mistral**|-|`v0.0.1`|0.42 (per 1000000 token)|1 token |**mistral**|**mistral-medium**|`v0.0.1`|8.1 (per 1000000 token)|1 token |**mistral**|**mistral-small**|`v0.0.1`|6.0 (per 1000000 token)|1 token |**mistral**|**mistral-tiny**|`v0.0.1`|0.42 (per 1000000 token)|1 token |**perplexityai**|**mistral-7b-instruct**|`v1.0`|0.28 (per 1000000 token)|1 token |**perplexityai**|**mixtral-8x7b-instruct**|`v1.0`|0.28 (per 1000000 token)|1 token |**perplexityai**|**pplx-7b-chat**|`v1.0`|0.28 (per 1000000 token)|1 token |**perplexityai**|**pplx-7b-online**|`v1.0`|0.28 (per 1000000 token)|1 token |**perplexityai**|**codellama-34b-instruct**|`v1.0`|1.4 (per 1000000 token)|1 token |**perplexityai**|**llama-2-70b-chat**|`v1.0`|2.8 (per 1000000 token)|1 token |**perplexityai**|**pplx-70b-chat**|`v1.0`|2.8 (per 1000000 token)|1 token |**perplexityai**|**pplx-70b-online**|`v1.0`|2.8 (per 1000000 token)|1 token |**perplexityai**|-|`v1.0`|2.8 (per 1000000 token)|1 token |**anthropic**|-|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1 token |**anthropic**|**claude-3-sonnet-20240229-v1:0**|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1 token |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token |**anthropic**|**claude-3-haiku-20240307-v1:0**|`bedrock-2023-05-31`|1.25 (per 1000000 token)|1 token   </details>  <details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`|  </details><details><summary>Supported Models</summary><details><summary>openai</summary>      |Name|Value| |----|-----| |**openai**|`gpt-3.5-turbo`| ||`gpt-3.5-turbo-0301`| ||`gpt-3.5-turbo-1106`| ||`gpt-3.5-turbo-16k`| ||`gpt-4`| ||`gpt-4-0314`| ||`gpt-4-1106-preview`| ||`gpt-4-vision-preview`|  </details><details><summary>google</summary>      |Name|Value| |----|-----| |**google**|`chat-bison`|  </details><details><summary>replicate</summary>      |Name|Value| |----|-----| |**replicate**|`llama-2-70b-chat`|  </details><details><summary>cohere</summary>      |Name|Value| |----|-----| |**cohere**|`command`| ||`command-light`| ||`command-light-nightly`| ||`command-nightly`|  </details><details><summary>meta</summary>      |Name|Value| |----|-----| |**meta**|`llama2-13b-chat-v1`| ||`llama2-70b-chat-v1`|  </details><details><summary>mistral</summary>      |Name|Value| |----|-----| |**mistral**|`large-latest`| ||`medium`| ||`small`| ||`tiny`|  </details><details><summary>perplexityai</summary>      |Name|Value| |----|-----| |**perplexityai**|`codellama-34b-instruct`| ||`llama-2-70b-chat`| ||`mistral-7b-instruct`| ||`mixtral-8x7b-instruct`| ||`pplx-70b-chat`| ||`pplx-70b-online`| ||`pplx-7b-chat`| ||`pplx-7b-online`|  </details><details><summary>anthropic</summary>      |Name|Value| |----|-----| |**anthropic**|`claude-3-sonnet-20240229-v1:0`| ||`claude-instant-v1`| ||`claude-v2`|  </details>  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textchat_chat_request import TextchatChatRequest
from openapi_client.models.textchat_response_model import TextchatResponseModel
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
    api_instance = openapi_client.ChatApi(api_client)
    textchat_chat_request = {"providers":"cohere,meta,replicate,mistral,perplexityai,anthropic,openai,google","text":"Barack Hussein Obama is an American politician who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, Obama was the first African-American president of the United States. He previously served as a U.S. senator from Illinois from 2005 to 2008 and as an Illinois state senator from 1997 to 2004.","chatbot_global_action":"You are a keyword extractor. Extract Only the word from the text provided.","previous_history":[{"role":"user","message":"Steve Jobs was a co-founder of Apple Inc., a multinational technology company headquartered in Cupertino, California. He was also the CEO and a major shareholder of Pixar Animation Studios, which was later acquired by The Walt Disney Company. Jobs was widely recognized as a visionary entrepreneur and a pioneer in the personal computer industry. In addition to his business ventures, he was also known for his charismatic personality, his signature black turtleneck, and his famous keynote presentations at Apple's product launches."},{"role":"assistant","message":"steve jobs, apple inc, pixar, california"}],"temperature":0.0,"max_tokens":100} # TextchatChatRequest | 

    try:
        # Chat
        api_response = await api_instance.text_text_chat_create(textchat_chat_request)
        print("The response of ChatApi->text_text_chat_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->text_text_chat_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **textchat_chat_request** | [**TextchatChatRequest**](TextchatChatRequest.md)|  | 

### Return type

[**TextchatResponseModel**](TextchatResponseModel.md)

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

# **text_text_chat_stream_create**
> str text_text_chat_stream_create(textchat_chat_stream_request)

Chat Stream

Streamed version of Chat feature, the raw text will be streamed chunk by chunk.  NOTE: For this feature, you an only request one provider at a time.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textchat_chat_stream_request import TextchatChatStreamRequest
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
    api_instance = openapi_client.ChatApi(api_client)
    textchat_chat_stream_request = {"providers":"cohere,meta,replicate,mistral,perplexityai,anthropic,openai,google","text":"Barack Hussein Obama is an American politician who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, Obama was the first African-American president of the United States. He previously served as a U.S. senator from Illinois from 2005 to 2008 and as an Illinois state senator from 1997 to 2004.","chatbot_global_action":"You are a keyword extractor. Extract Only the word from the text provided.","previous_history":[{"role":"user","message":"Steve Jobs was a co-founder of Apple Inc., a multinational technology company headquartered in Cupertino, California. He was also the CEO and a major shareholder of Pixar Animation Studios, which was later acquired by The Walt Disney Company. Jobs was widely recognized as a visionary entrepreneur and a pioneer in the personal computer industry. In addition to his business ventures, he was also known for his charismatic personality, his signature black turtleneck, and his famous keynote presentations at Apple's product launches."},{"role":"assistant","message":"steve jobs, apple inc, pixar, california"}],"temperature":0.0,"max_tokens":100} # TextchatChatStreamRequest | 

    try:
        # Chat Stream
        api_response = await api_instance.text_text_chat_stream_create(textchat_chat_stream_request)
        print("The response of ChatApi->text_text_chat_stream_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->text_text_chat_stream_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **textchat_chat_stream_request** | [**TextchatChatStreamRequest**](TextchatChatStreamRequest.md)|  | 

### Return type

**str**

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

