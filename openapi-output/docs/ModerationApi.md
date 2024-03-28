# openapi_client.ModerationApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_text_moderation_create**](ModerationApi.md#text_text_moderation_create) | **POST** /text/moderation | Moderation


# **text_text_moderation_create**
> TextmoderationResponseModel text_text_moderation_create(texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request)

Moderation

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**microsoft**|`v1.0`|1.0 (per 1000 request)|1 request |**openai**|`v3.0.0`|free|- |**clarifai**|`8.0.0`|1.2 (per 1000 request)|1 request |**google**|`v1`|5.0 (per 1000000 char)|100 char   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Afrikaans**|`af`| |**Albanian**|`sq`| |**Amharic**|`am`| |**Arabic**|`ar`| |**Aragonese**|`an`| |**Armenian**|`hy`| |**Assamese**|`as`| |**Asturian**|`ast`| |**Azerbaijani**|`az`| |**Bashkir**|`ba`| |**Basque**|`eu`| |**Bavarian**|`bar`| |**Belarusian**|`be`| |**Bengali**|`bn`| |**Bishnupriya**|`bpy`| |**Bosnian**|`bs`| |**Breton**|`br`| |**Bulgarian**|`bg`| |**Burmese**|`my`| |**Catalan**|`ca`| |**Cebuano**|`ceb`| |**Central Khmer**|`km`| |**Central Kurdish**|`ckb`| |**Chechen**|`ce`| |**Cherokee**|`chr`| |**Chinese**|`zh`| |**Chuvash**|`cv`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dutch**|`nl`| |**English**|`en`| |**Estonian**|`et`| |**Filipino**|`fil`| |**Finnish**|`fi`| |**French**|`fr`| |**Fulah**|`ff`| |**Galician**|`gl`| |**Georgian**|`ka`| |**German**|`de`| |**Gujarati**|`gu`| |**Haitian**|`ht`| |**Hausa**|`ha`| |**Hebrew**|`he`| |**Hindi**|`hi`| |**Hungarian**|`hu`| |**Icelandic**|`is`| |**Ido**|`io`| |**Igbo**|`ig`| |**Indonesian**|`id`| |**Inuktitut**|`iu`| |**Irish**|`ga`| |**Italian**|`it`| |**Japanese**|`ja`| |**Javanese**|`jv`| |**Kannada**|`kn`| |**Kazakh**|`kk`| |**Kinyarwanda**|`rw`| |**Kirghiz**|`ky`| |**Konkani (macrolanguage)**|`kok`| |**Korean**|`ko`| |**Lahnda**|`lah`| |**Lao**|`lo`| |**Latin**|`la`| |**Latvian**|`lv`| |**Lithuanian**|`lt`| |**Lombard**|`lmo`| |**Low German**|`nds`| |**Luxembourgish**|`lb`| |**Macedonian**|`mk`| |**Malagasy**|`mg`| |**Malay (macrolanguage)**|`ms`| |**Malayalam**|`ml`| |**Maltese**|`mt`| |**Maori**|`mi`| |**Marathi**|`mr`| |**Minangkabau**|`min`| |**Modern Greek (1453-)**|`el`| |**Mongolian**|`mn`| |**Nepali (macrolanguage)**|`ne`| |**Norwegian**|`no`| |**Norwegian Bokmål**|`nb`| |**Norwegian Nynorsk**|`nn`| |**Occitan (post 1500)**|`oc`| |**Oriya (macrolanguage)**|`or`| |**Panjabi**|`pa`| |**Pedi**|`nso`| |**Persian**|`fa`| |**Piemontese**|`pms`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Pushto**|`ps`| |**Quechua**|`qu`| |**Romanian**|`ro`| |**Russian**|`ru`| |**Scots**|`sco`| |**Scottish Gaelic**|`gd`| |**Serbian**|`sr`| |**Serbo-Croatian**|`sh`| |**Sicilian**|`scn`| |**Sindhi**|`sd`| |**Sinhala**|`si`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**South Azerbaijani**|`azb`| |**Southern Sotho**|`st`| |**Spanish**|`es`| |**Sundanese**|`su`| |**Swahili (macrolanguage)**|`sw`| |**Swedish**|`sv`| |**Tagalog**|`tl`| |**Tajik**|`tg`| |**Tamil**|`ta`| |**Tatar**|`tt`| |**Telugu**|`te`| |**Thai**|`th`| |**Tigrinya**|`ti`| |**Tswana**|`tn`| |**Turkish**|`tr`| |**Turkmen**|`tk`| |**Uighur**|`ug`| |**Ukrainian**|`uk`| |**Urdu**|`ur`| |**Uzbek**|`uz`| |**Vietnamese**|`vi`| |**Volapük**|`vo`| |**Waray (Philippines)**|`war`| |**Welsh**|`cy`| |**Western Frisian**|`fy`| |**Wolof**|`wo`| |**Xhosa**|`xh`| |**Yoruba**|`yo`| |**Zulu**|`zu`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Chinese (Traditional)**|`zh-Hant`| |**Low German (Netherlands)**|`nds-NL`|  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textmoderation_response_model import TextmoderationResponseModel
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
    api_instance = openapi_client.ModerationApi(api_client)
    texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request = {"providers":"google,openai,clarifai,microsoft","language":"en","text":"Is this a crap email abcdef@abcd.com, phone: 0617730730, IP: 255.255.255.255, 1 Microsoft Way, Redmond, WA 98052"} # TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest | 

    try:
        # Moderation
        api_response = await api_instance.text_text_moderation_create(texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request)
        print("The response of ModerationApi->text_text_moderation_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->text_text_moderation_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request** | [**TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest**](TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest.md)|  | 

### Return type

[**TextmoderationResponseModel**](TextmoderationResponseModel.md)

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

