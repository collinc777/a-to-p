# openapi_client.NamedEntityRecognitionApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_text_named_entity_recognition_create**](NamedEntityRecognitionApi.md#text_text_named_entity_recognition_create) | **POST** /text/named_entity_recognition | Named Entity Recognition


# **text_text_named_entity_recognition_create**
> TextnamedEntityRecognitionResponseModel text_text_named_entity_recognition_create(texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request)

Named Entity Recognition

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char |**google**|`v1`|1.0 (per 1000000 char)|1000 char |**ibm**|`v1 (2021-08-01)`|0.3 (per 1000000 char)|10000 char |**lettria**|`v5.5.2`|2.0 (per 1000000 char)|1000 char |**microsoft**|`v3.1`|1.0 (per 1000000 char)|1000 char |**neuralspace**|`v1`|0.007 (per 1 request)|1 request |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token |**tenstorrent**|`v1.0.0`|1.0 (per 1000000 char)|1000 char |**nlpcloud**|`v1`|25.0 (per 1000 request)|1 request   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Afrikaans**|`af`| |**Albanian**|`sq`| |**Arabic**|`ar`| |**Aragonese**|`an`| |**Armenian**|`hy`| |**Assamese**|`as`| |**Azerbaijani**|`az`| |**Bashkir**|`ba`| |**Basque**|`eu`| |**Belarusian**|`be`| |**Bengali**|`bn`| |**Bosnian**|`bs`| |**Breton**|`br`| |**Bulgarian**|`bg`| |**Burmese**|`my`| |**Catalan**|`ca`| |**Chechen**|`ce`| |**Chinese**|`zh`| |**Chuvash**|`cv`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dutch**|`nl`| |**English**|`en`| |**Estonian**|`et`| |**Finnish**|`fi`| |**French**|`fr`| |**Galician**|`gl`| |**Georgian**|`ka`| |**German**|`de`| |**Gujarati**|`gu`| |**Haitian**|`ht`| |**Hebrew**|`he`| |**Hindi**|`hi`| |**Hungarian**|`hu`| |**Icelandic**|`is`| |**Indonesian**|`id`| |**Irish**|`ga`| |**Italian**|`it`| |**Japanese**|`ja`| |**Javanese**|`jv`| |**Kannada**|`kn`| |**Kazakh**|`kk`| |**Kirghiz**|`ky`| |**Korean**|`ko`| |**Latin**|`la`| |**Latvian**|`lv`| |**Lithuanian**|`lt`| |**Luxembourgish**|`lb`| |**Macedonian**|`mk`| |**Malagasy**|`mg`| |**Malay (macrolanguage)**|`ms`| |**Malayalam**|`ml`| |**Maltese**|`mt`| |**Marathi**|`mr`| |**Modern Greek (1453-)**|`el`| |**Nepali (macrolanguage)**|`ne`| |**Norwegian**|`no`| |**Norwegian Bokmål**|`nb`| |**Occitan (post 1500)**|`oc`| |**Panjabi**|`pa`| |**Persian**|`fa`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Romanian**|`ro`| |**Russian**|`ru`| |**Serbian**|`sr`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Spanish**|`es`| |**Sundanese**|`su`| |**Swahili (macrolanguage)**|`sw`| |**Swedish**|`sv`| |**Tagalog**|`tl`| |**Tajik**|`tg`| |**Tamil**|`ta`| |**Tatar**|`tt`| |**Telugu**|`te`| |**Turkish**|`tr`| |**Uighur**|`ug`| |**Ukrainian**|`uk`| |**Urdu**|`ur`| |**Uzbek**|`uz`| |**Vietnamese**|`vi`| |**Welsh**|`cy`| |**Yoruba**|`yo`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Chinese (Simplified)**|`zh-Hans`| |**Chinese (Taiwan)**|`zh-TW`| |**Chinese (Traditional)**|`zh-Hant`| |**English (United States)**|`en-US`| |**French (France)**|`fr-FR`| |**Portuguese (Brazil)**|`pt-BR`| |**Portuguese (Portugal)**|`pt-PT`|  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textnamed_entity_recognition_response_model import TextnamedEntityRecognitionResponseModel
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
    api_instance = openapi_client.NamedEntityRecognitionApi(api_client)
    texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request = {"providers":"microsoft,amazon,google,neuralspace,lettria,tenstorrent,ibm,openai,nlpcloud","language":"en","text":"Barack Hussein Obama is an American politician who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, Obama was the first African-American president of the United States. He previously served as a U.S. senator from Illinois from 2005 to 2008 and as an Illinois state senator from 1997 to 2004."} # TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest | 

    try:
        # Named Entity Recognition
        api_response = api_instance.text_text_named_entity_recognition_create(texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request)
        print("The response of NamedEntityRecognitionApi->text_text_named_entity_recognition_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamedEntityRecognitionApi->text_text_named_entity_recognition_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request** | [**TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest**](TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest.md)|  | 

### Return type

[**TextnamedEntityRecognitionResponseModel**](TextnamedEntityRecognitionResponseModel.md)

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

