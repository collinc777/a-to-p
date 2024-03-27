# openapi_client.AnonymizationApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_image_anonymization_create**](AnonymizationApi.md#image_image_anonymization_create) | **POST** /image/anonymization | Anonymization
[**text_text_anonymization_create**](AnonymizationApi.md#text_text_anonymization_create) | **POST** /text/anonymization | Anonymization


# **image_image_anonymization_create**
> ImageanonymizationResponseModel image_image_anonymization_create(imageanonymizationimagelandmark_detectionimageexplicit_content_image_request)

Anonymization

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**api4ai**|`v1.0.0`|25.0 (per 1000 file)|1 file   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.imageanonymization_response_model import ImageanonymizationResponseModel
from openapi_client.models.imageanonymizationimagelandmark_detectionimageexplicit_content_image_request import ImageanonymizationimagelandmarkDetectionimageexplicitContentImageRequest
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
    api_instance = openapi_client.AnonymizationApi(api_client)
    imageanonymizationimagelandmark_detectionimageexplicit_content_image_request = {"providers":"api4ai","file_url":"http://edenai-resource-example.jpg"} # ImageanonymizationimagelandmarkDetectionimageexplicitContentImageRequest | 

    try:
        # Anonymization
        api_response = api_instance.image_image_anonymization_create(imageanonymizationimagelandmark_detectionimageexplicit_content_image_request)
        print("The response of AnonymizationApi->image_image_anonymization_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnonymizationApi->image_image_anonymization_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageanonymizationimagelandmark_detectionimageexplicit_content_image_request** | [**ImageanonymizationimagelandmarkDetectionimageexplicitContentImageRequest**](ImageanonymizationimagelandmarkDetectionimageexplicitContentImageRequest.md)|  | 

### Return type

[**ImageanonymizationResponseModel**](ImageanonymizationResponseModel.md)

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

# **text_text_anonymization_create**
> TextanonymizationResponseModel text_text_anonymization_create(texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request)

Anonymization

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**emvista**|`v1.0`|3.0 (per 1000000 char)|1 char |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char |**microsoft**|`v3.1`|0.25 (per 1000000 char)|1000 char   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Arabic**|`ar`| |**Chinese**|`zh`| |**Danish**|`da`| |**Dutch**|`nl`| |**English**|`en`| |**Finnish**|`fi`| |**French**|`fr`| |**German**|`de`| |**Hindi**|`hi`| |**Italian**|`it`| |**Japanese**|`ja`| |**Korean**|`ko`| |**Modern Greek (1453-)**|`el`| |**Norwegian**|`no`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Russian**|`ru`| |**Spanish**|`es`| |**Swedish**|`sv`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Chinese (Simplified)**|`zh-Hans`| |**Chinese (Traditional)**|`zh-Hant`| |**Portuguese (Brazil)**|`pt-BR`| |**Portuguese (Portugal)**|`pt-PT`|  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textanonymization_response_model import TextanonymizationResponseModel
from openapi_client.models.texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request import TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest
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
    api_instance = openapi_client.AnonymizationApi(api_client)
    texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request = {"providers":"amazon,emvista,openai,microsoft","language":"en","text":"Overall I am satisfied with my experience at Amazon, but two areas of major improvement needed. First is the product reviews and pricing. There are thousands of positive reviews for so many items, and it's clear that the reviews are bogus or not really associated with that product. There needs to be a way to only view products sold by Amazon directly, because many market sellers way overprice items that can be purchased cheaper elsewhere (like Walmart, Target, etc). The second issue is they make it too difficult to get help when there's an issue with an order."} # TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest | 

    try:
        # Anonymization
        api_response = api_instance.text_text_anonymization_create(texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request)
        print("The response of AnonymizationApi->text_text_anonymization_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnonymizationApi->text_text_anonymization_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request** | [**TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest**](TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest.md)|  | 

### Return type

[**TextanonymizationResponseModel**](TextanonymizationResponseModel.md)

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

