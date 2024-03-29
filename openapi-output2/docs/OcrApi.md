# openapi_client.OcrApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ocr_ocr_ocr_create**](OcrApi.md#ocr_ocr_ocr_create) | **POST** /ocr/ocr | OCR


# **ocr_ocr_ocr_create**
> OcrocrResponseModel ocr_ocr_ocr_create(ocrocr_ocr_request)

OCR

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**amazon**|`boto3 (v1.15.18)`|1.5 (per 1000 page)|1 page |**clarifai**|`8.0.0`|2.0 (per 1000 page)|1 page |**google**|`v1`|1.5 (per 1000 page)|1 page |**microsoft**|`v3.2`|1.0 (per 1000 page)|1 page |**sentisight**|`v3.3.1`|1.0 (per 1000 file)|1 file |**api4ai**|`v1.0.0`|3.0 (per 1000 request)|1 request   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Abaza**|`abq`| |**Adyghe**|`ady`| |**Afrikaans**|`af`| |**Albanian**|`sq`| |**Angika**|`anp`| |**Arabic**|`ar`| |**Assamese**|`as`| |**Asturian**|`ast`| |**Avaric**|`av`| |**Awadhi**|`awa`| |**Azerbaijani**|`az`| |**Bagheli**|`bfy`| |**Basque**|`eu`| |**Belarusian**|`be`| |**Bengali**|`bn`| |**Bhojpuri**|`bho`| |**Bihari languages**|`bh`| |**Bislama**|`bi`| |**Bodo (India)**|`brx`| |**Bosnian**|`bs`| |**Braj**|`bra`| |**Breton**|`br`| |**Bulgarian**|`bg`| |**Bundeli**|`bns`| |**Buriat**|`bua`| |**Camling**|`rab`| |**Catalan**|`ca`| |**Cebuano**|`ceb`| |**Chamorro**|`ch`| |**Chechen**|`ce`| |**Chhattisgarhi**|`hne`| |**Chinese**|`zh`| |**Cornish**|`kw`| |**Corsican**|`co`| |**Crimean Tatar**|`crh`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dargwa**|`dar`| |**Dari**|`prs`| |**Dhimal**|`dhi`| |**Dogri (macrolanguage)**|`doi`| |**Dutch**|`nl`| |**English**|`en`| |**Erzya**|`myv`| |**Estonian**|`et`| |**Faroese**|`fo`| |**Fijian**|`fj`| |**Filipino**|`fil`| |**Finnish**|`fi`| |**French**|`fr`| |**Friulian**|`fur`| |**Gagauz**|`gag`| |**Galician**|`gl`| |**German**|`de`| |**Gilbertese**|`gil`| |**Goan Konkani**|`gom`| |**Gondi**|`gon`| |**Gurung**|`gvr`| |**Haitian**|`ht`| |**Halbi**|`hlb`| |**Hani**|`hni`| |**Haryanvi**|`bgc`| |**Hawaiian**|`haw`| |**Hindi**|`hi`| |**Hmong Daw**|`mww`| |**Ho**|`hoc`| |**Hungarian**|`hu`| |**Icelandic**|`is`| |**Inari Sami**|`smn`| |**Indonesian**|`id`| |**Ingush**|`inh`| |**Interlingua (International Auxiliary Language Association)**|`ia`| |**Inuktitut**|`iu`| |**Irish**|`ga`| |**Italian**|`it`| |**Japanese**|`ja`| |**Jaunsari**|`jns`| |**Javanese**|`jv`| |**K'iche'**|`quc`| |**Kabardian**|`kbd`| |**Kabuverdianu**|`kea`| |**Kachin**|`kac`| |**Kalaallisut**|`kl`| |**Kangri**|`xnr`| |**Kara-Kalpak**|`kaa`| |**Karachay-Balkar**|`krc`| |**Kashubian**|`csb`| |**Kazakh**|`kk`| |**Khaling**|`klr`| |**Khasi**|`kha`| |**Kirghiz**|`ky`| |**Korean**|`ko`| |**Korku**|`kfq`| |**Koryak**|`kpy`| |**Kosraean**|`kos`| |**Kumarbhag Paharia**|`kmj`| |**Kumyk**|`kum`| |**Kurdish**|`ku`| |**Kurukh**|`kru`| |**Kölsch**|`ksh`| |**Lak**|`lbe`| |**Lakota**|`lkt`| |**Latin**|`la`| |**Latvian**|`lv`| |**Lezghian**|`lez`| |**Lithuanian**|`lt`| |**Lower Sorbian**|`dsb`| |**Lule Sami**|`smj`| |**Luxembourgish**|`lb`| |**Mahasu Pahari**|`bfz`| |**Maithili**|`mai`| |**Malay (macrolanguage)**|`ms`| |**Maltese**|`mt`| |**Manx**|`gv`| |**Maori**|`mi`| |**Marathi**|`mr`| |**Marshallese**|`mh`| |**Mongolian**|`mn`| |**Neapolitan**|`nap`| |**Nepali (macrolanguage)**|`ne`| |**Newari**|`new`| |**Niuean**|`niu`| |**Nogai**|`nog`| |**Northern Sami**|`se`| |**Norwegian**|`no`| |**Occitan (post 1500)**|`oc`| |**Old English (ca. 450-1100)**|`ang`| |**Ossetian**|`os`| |**Pali**|`pi`| |**Panjabi**|`pa`| |**Persian**|`fa`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Pushto**|`ps`| |**Romanian**|`ro`| |**Romansh**|`rm`| |**Russian**|`ru`| |**Sadri**|`sck`| |**Samoan**|`sm`| |**Sanskrit**|`sa`| |**Santali**|`sat`| |**Scots**|`sco`| |**Scottish Gaelic**|`gd`| |**Serbian**|`sr`| |**Sherpa**|`xsr`| |**Sirmauri**|`srx`| |**Skolt Sami**|`sms`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**Southern Sami**|`sma`| |**Spanish**|`es`| |**Swahili (macrolanguage)**|`sw`| |**Swedish**|`sv`| |**Tabassaran**|`tab`| |**Tagalog**|`tl`| |**Tajik**|`tg`| |**Tatar**|`tt`| |**Tetum**|`tet`| |**Thangmi**|`thf`| |**Tonga (Tonga Islands)**|`to`| |**Turkish**|`tr`| |**Turkmen**|`tk`| |**Tuvinian**|`tyv`| |**Uighur**|`ug`| |**Ukrainian**|`uk`| |**Upper Sorbian**|`hsb`| |**Urdu**|`ur`| |**Uzbek**|`uz`| |**Vietnamese**|`vi`| |**Volapük**|`vo`| |**Walser**|`wae`| |**Welsh**|`cy`| |**Western Frisian**|`fy`| |**Yucateco**|`yua`| |**Zhuang**|`za`| |**Zulu**|`zu`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Arabic (Pseudo-Accents)**|`ar-XA`| |**Belarusian**|`be-cyrl`| |**Belarusian (Latin)**|`be-latn`| |**Chinese (China)**|`zh-CN`| |**Chinese (Simplified)**|`zh-Hans`| |**Chinese (Taiwan)**|`zh-TW`| |**Chinese (Traditional)**|`zh-Hant`| |**Danish (Denmark)**|`da-DK`| |**Dutch (Netherlands)**|`nl-NL`| |**English (United States)**|`en-US`| |**Finnish (Finland)**|`fi-FI`| |**French (France)**|`fr-FR`| |**German (Germany)**|`de-DE`| |**Hungarian (Hungary)**|`hu-HU`| |**Italian (Italy)**|`it-IT`| |**Japanese (Japan)**|`ja-JP`| |**Kara-Kalpak (Cyrillic)**|`kaa-Cyrl`| |**Kazakh**|`kk-cyrl`| |**Kazakh (Latin)**|`kk-latn`| |**Korean (South Korea)**|`ko-KR`| |**Kurdish (Arabic)**|`ku-arab`| |**Kurdish (Latin)**|`ku-latn`| |**Polish**|`pl-PO`| |**Portuguese (Portugal)**|`pt-PT`| |**Region: Czechia**|`cz-CZ`| |**Region: Greece**|`gr-GR`| |**Russian (Russia)**|`ru-RU`| |**Serbian (Cyrillic, Montenegro)**|`sr-Cyrl-ME`| |**Serbian (Latin)**|`sr-latn`| |**Serbian (Latin, Montenegro)**|`sr-Latn-ME`| |**Serbian (Montenegro)**|`sr-ME`| |**Spanish (Spain)**|`es-ES`| |**Swedish (Sweden)**|`sv-SE`| |**Turkish (Turkey)**|`tr-TR`| |**Uzbek (Arabic)**|`uz-arab`| |**Uzbek (Cyrillic)**|`uz-cyrl`|  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.ocrocr_ocr_request import OcrocrOcrRequest
from openapi_client.models.ocrocr_response_model import OcrocrResponseModel
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
    api_instance = openapi_client.OcrApi(api_client)
    ocrocr_ocr_request = {"providers":"google,clarifai,sentisight,microsoft,api4ai,amazon","language":"en","file_url":"http://edenai-resource-example.png"} # OcrocrOcrRequest | 

    try:
        # OCR
        api_response = api_instance.ocr_ocr_ocr_create(ocrocr_ocr_request)
        print("The response of OcrApi->ocr_ocr_ocr_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OcrApi->ocr_ocr_ocr_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocrocr_ocr_request** | [**OcrocrOcrRequest**](OcrocrOcrRequest.md)|  | 

### Return type

[**OcrocrResponseModel**](OcrocrResponseModel.md)

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

