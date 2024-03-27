# openapi_client.LanguageDetectionApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translation_translation_language_detection_create**](LanguageDetectionApi.md#translation_translation_language_detection_create) | **POST** /translation/language_detection | Language Detection


# **translation_translation_language_detection_create**
> TranslationlanguageDetectionResponseModel translation_translation_language_detection_create(translationlanguage_detection_language_detection_request)

Language Detection

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char |**google**|`v1`|20.0 (per 1000000 char)|1 char |**ibm**|`v1 (2021-08-01)`|20.0 (per 1000000 char)|1000 char |**microsoft**|`v3.1`|1.0 (per 1000000 char)|1000 char |**neuralspace**|`v1`|7.0 (per 1000 request)|1 request |**modernmt**|`1.1.0`|8.0 (per 1000000 char)|1 char |**openai**|`v1`|20.0 (per 1000000 token)|1 token   </details>  

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.translationlanguage_detection_language_detection_request import TranslationlanguageDetectionLanguageDetectionRequest
from openapi_client.models.translationlanguage_detection_response_model import TranslationlanguageDetectionResponseModel
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
    api_instance = openapi_client.LanguageDetectionApi(api_client)
    translationlanguage_detection_language_detection_request = {"providers":"amazon,neuralspace,openai,microsoft,google,ibm,modernmt","text":"Ogni individuo ha diritto all'istruzione. L'istruzione deve essere gratuita almeno per quanto riguarda le classi elementari e fondamentali. L'istruzione elementare deve essere obbligatoria. L'istruzione tecnica e professionale deve essere messa alla portata di tutti e l'istruzione superiore deve essere egualmente accessibile a tutti sulla base del merito.\nL'istruzione deve essere indirizzata al pieno sviluppo della personalità umana ed al rafforzamento del rispetto dei diritti umani e delle libertà fondamentali. Essa deve promuovere la comprensione, la tolleranza, l'amicizia fra tutte le Nazioni, i gruppi razziali e religiosi, e deve favorire l'opera delle Nazioni Unite per il mantenimento della pace.\nI genitori hanno diritto di priorità nella scelta del genere di istruzione da impartire ai loro figli."} # TranslationlanguageDetectionLanguageDetectionRequest | 

    try:
        # Language Detection
        api_response = api_instance.translation_translation_language_detection_create(translationlanguage_detection_language_detection_request)
        print("The response of LanguageDetectionApi->translation_translation_language_detection_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LanguageDetectionApi->translation_translation_language_detection_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translationlanguage_detection_language_detection_request** | [**TranslationlanguageDetectionLanguageDetectionRequest**](TranslationlanguageDetectionLanguageDetectionRequest.md)|  | 

### Return type

[**TranslationlanguageDetectionResponseModel**](TranslationlanguageDetectionResponseModel.md)

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

