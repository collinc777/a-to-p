# openapi_client.CustomNamedEntityRecognitionApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_text_custom_named_entity_recognition_create**](CustomNamedEntityRecognitionApi.md#text_text_custom_named_entity_recognition_create) | **POST** /text/custom_named_entity_recognition | Custom Named Entity Recognition


# **text_text_custom_named_entity_recognition_create**
> TextcustomNamedEntityRecognitionResponseModel text_text_custom_named_entity_recognition_create(textcustom_named_entity_recognition_custom_named_entity_recognition_request)

Custom Named Entity Recognition

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token |**cohere**|`2022-12-06`|2.0 (per 1000000 token)|1 token   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textcustom_named_entity_recognition_custom_named_entity_recognition_request import TextcustomNamedEntityRecognitionCustomNamedEntityRecognitionRequest
from openapi_client.models.textcustom_named_entity_recognition_response_model import TextcustomNamedEntityRecognitionResponseModel
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
    api_instance = openapi_client.CustomNamedEntityRecognitionApi(api_client)
    textcustom_named_entity_recognition_custom_named_entity_recognition_request = {"providers":"openai,cohere","text":"Barack Hussein Obama is an American politician who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, Obama was the first African-American president of the United States. He previously served as a U.S. senator from Illinois from 2005 to 2008 and as an Illinois state senator from 1997 to 2004.","entities":["Politician","State"],"examples":[{"text":"Steve Jobs was the co-founder of Apple Inc., a multinational technology company based in Cupertino, California. He was born in San Francisco, California in 1955, and studied at Reed College before dropping out to start Apple with Steve Wozniak in 1976","entities":[{"entity":"Steve Jobs","category":"Person"},{"entity":"Apple Inc","category":"Organization"},{"entity":"California","category":"Location"},{"entity":"1955","category":"Date"}]}]} # TextcustomNamedEntityRecognitionCustomNamedEntityRecognitionRequest | 

    try:
        # Custom Named Entity Recognition
        api_response = api_instance.text_text_custom_named_entity_recognition_create(textcustom_named_entity_recognition_custom_named_entity_recognition_request)
        print("The response of CustomNamedEntityRecognitionApi->text_text_custom_named_entity_recognition_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomNamedEntityRecognitionApi->text_text_custom_named_entity_recognition_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **textcustom_named_entity_recognition_custom_named_entity_recognition_request** | [**TextcustomNamedEntityRecognitionCustomNamedEntityRecognitionRequest**](TextcustomNamedEntityRecognitionCustomNamedEntityRecognitionRequest.md)|  | 

### Return type

[**TextcustomNamedEntityRecognitionResponseModel**](TextcustomNamedEntityRecognitionResponseModel.md)

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

