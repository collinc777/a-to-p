# openapi_client.SentimentAnalysisApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_text_sentiment_analysis_create**](SentimentAnalysisApi.md#text_text_sentiment_analysis_create) | **POST** /text/sentiment_analysis | Sentiment Analysis


# **text_text_sentiment_analysis_create**
> TextsentimentAnalysisResponseModel text_text_sentiment_analysis_create(texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request)

Sentiment Analysis

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char |**connexun**|`v1.0`|2.0 (per 1000 request)|1 request |**google**|`v1`|1.0 (per 1000000 char)|1000 char |**ibm**|`v1 (2021-08-01)`|0.3 (per 1000000 char)|10000 char |**lettria**|`v5.5.2`|2.0 (per 1000000 char)|1000 char |**microsoft**|`v3.1`|1.0 (per 1000000 char)|1000 char |**emvista**|`v1.0`|3.0 (per 1000000 char)|1000 char |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token |**tenstorrent**|`v1.1.0`|0.7 (per 1000000 char)|1000 char |**sapling**|`v1`|20.0 (per 1000000 char)|1000 char |**nlpcloud**|`v1`|25.0 (per 1000 request)|1 request   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Arabic**|`ar`| |**Bengali**|`bn`| |**Chinese**|`zh`| |**Danish**|`da`| |**Dutch**|`nl`| |**English**|`en`| |**Finnish**|`fi`| |**French**|`fr`| |**German**|`de`| |**Hindi**|`hi`| |**Indonesian**|`id`| |**Italian**|`it`| |**Japanese**|`ja`| |**Korean**|`ko`| |**Modern Greek (1453-)**|`el`| |**Norwegian**|`no`| |**Panjabi**|`pa`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Romanian**|`ro`| |**Russian**|`ru`| |**Spanish**|`es`| |**Swedish**|`sv`| |**Tamil**|`ta`| |**Thai**|`th`| |**Turkish**|`tr`| |**Ukrainian**|`uk`| |**Vietnamese**|`vi`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Chinese (Simplified)**|`zh-Hans`| |**Chinese (Taiwan)**|`zh-TW`| |**Chinese (Traditional)**|`zh-Hant`| |**English (United States)**|`en-US`| |**French (France)**|`fr-FR`| |**Portuguese (Brazil)**|`pt-BR`| |**Portuguese (Portugal)**|`pt-PT`|  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textsentiment_analysis_response_model import TextsentimentAnalysisResponseModel
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
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SentimentAnalysisApi(api_client)
    texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request = {"providers":"sapling,google,microsoft,emvista,tenstorrent,connexun,ibm,lettria,openai,amazon,nlpcloud","language":"en","text":"Overall I am satisfied with my experience at Amazon, but two areas of major improvement needed. First is the product reviews and pricing. There are thousands of positive reviews for so many items, and it's clear that the reviews are bogus or not really associated with that product. There needs to be a way to only view products sold by Amazon directly, because many market sellers way overprice items that can be purchased cheaper elsewhere (like Walmart, Target, etc). The second issue is they make it too difficult to get help when there's an issue with an order."} # TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest | 

    try:
        # Sentiment Analysis
        api_response = await api_instance.text_text_sentiment_analysis_create(texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request)
        print("The response of SentimentAnalysisApi->text_text_sentiment_analysis_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SentimentAnalysisApi->text_text_sentiment_analysis_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request** | [**TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest**](TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest.md)|  | 

### Return type

[**TextsentimentAnalysisResponseModel**](TextsentimentAnalysisResponseModel.md)

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

