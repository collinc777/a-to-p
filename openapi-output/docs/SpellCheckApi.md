# openapi_client.SpellCheckApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_text_spell_check_create**](SpellCheckApi.md#text_text_spell_check_create) | **POST** /text/spell_check | Spell Check


# **text_text_spell_check_create**
> TextspellCheckResponseModel text_text_spell_check_create(textspell_check_spell_check_request)

Spell Check

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**microsoft**|`v7`|0.3 (per 1000 request)|1 request |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token |**prowritingaid**|`v2`|10.0 (per 1000 request)|1 request |**cohere**|`2022-12-06`|2.0 (per 1000000 token)|1 token |**sapling**|`v1`|2.0 (per 1000000 char)|1 char |**nlpcloud**|`v1`|25.0 (per 1000 request)|1 request |**ai21labs**|`v1`|0.0005 (per 1 request)|1 request   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Achinese**|`ace`| |**Afrikaans**|`af`| |**Akan**|`ak`| |**Albanian**|`sq`| |**Amharic**|`am`| |**Arabic**|`ar`| |**Armenian**|`hy`| |**Assamese**|`as`| |**Asturian**|`ast`| |**Awadhi**|`awa`| |**Ayacucho Quechua**|`quy`| |**Azerbaijani**|`az`| |**Balinese**|`ban`| |**Bambara**|`bm`| |**Banjar**|`bjn`| |**Bashkir**|`ba`| |**Basque**|`eu`| |**Belarusian**|`be`| |**Bemba (Zambia)**|`bem`| |**Bengali**|`bn`| |**Bhojpuri**|`bho`| |**Bosnian**|`bs`| |**Buginese**|`bug`| |**Bulgarian**|`bg`| |**Burmese**|`my`| |**Catalan**|`ca`| |**Cebuano**|`ceb`| |**Central Atlas Tamazight**|`tzm`| |**Central Aymara**|`ayr`| |**Central Kanuri**|`knc`| |**Central Khmer**|`km`| |**Central Kurdish**|`ckb`| |**Chhattisgarhi**|`hne`| |**Chinese**|`zh`| |**Chokwe**|`cjk`| |**Corsican**|`co`| |**Crimean Tatar**|`crh`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dutch**|`nl`| |**Dyula**|`dyu`| |**Dzongkha**|`dz`| |**Eastern Yiddish**|`ydd`| |**Egyptian Arabic**|`arz`| |**English**|`en`| |**Esperanto**|`eo`| |**Estonian**|`et`| |**Ewe**|`ee`| |**Faroese**|`fo`| |**Fijian**|`fj`| |**Finnish**|`fi`| |**Fon**|`fon`| |**French**|`fr`| |**Friulian**|`fur`| |**Galician**|`gl`| |**Ganda**|`lg`| |**Georgian**|`ka`| |**German**|`de`| |**Guarani**|`gn`| |**Gujarati**|`gu`| |**Haitian**|`ht`| |**Halh Mongolian**|`khk`| |**Hausa**|`ha`| |**Hawaiian**|`haw`| |**Hebrew**|`he`| |**Hindi**|`hi`| |**Hmong**|`hmn`| |**Hungarian**|`hu`| |**Icelandic**|`is`| |**Igbo**|`ig`| |**Iloko**|`ilo`| |**Indonesian**|`id`| |**Irish**|`ga`| |**Italian**|`it`| |**Japanese**|`ja`| |**Javanese**|`jv`| |**Kabiyè**|`kbp`| |**Kabuverdianu**|`kea`| |**Kabyle**|`kab`| |**Kachin**|`kac`| |**Kamba (Kenya)**|`kam`| |**Kannada**|`kn`| |**Kashmiri**|`ks`| |**Kazakh**|`kk`| |**Kikuyu**|`ki`| |**Kimbundu**|`kmb`| |**Kinyarwanda**|`rw`| |**Kirghiz**|`ky`| |**Kongo**|`kg`| |**Korean**|`ko`| |**Kurdish**|`ku`| |**Lao**|`lo`| |**Latgalian**|`ltg`| |**Latin**|`la`| |**Latvian**|`lv`| |**Ligurian**|`lij`| |**Limburgan**|`li`| |**Lingala**|`ln`| |**Lithuanian**|`lt`| |**Lombard**|`lmo`| |**Luba-Katanga**|`lu`| |**Luo (Kenya and Tanzania)**|`luo`| |**Lushai**|`lus`| |**Luxembourgish**|`lb`| |**Macedonian**|`mk`| |**Magahi**|`mag`| |**Maithili**|`mai`| |**Malagasy**|`mg`| |**Malay (macrolanguage)**|`ms`| |**Malayalam**|`ml`| |**Maltese**|`mt`| |**Manipuri**|`mni`| |**Maori**|`mi`| |**Marathi**|`mr`| |**Mesopotamian Arabic**|`acm`| |**Minangkabau**|`min`| |**Modern Greek (1453-)**|`el`| |**Mongolian**|`mn`| |**Moroccan Arabic**|`ary`| |**Mossi**|`mos`| |**Najdi Arabic**|`ars`| |**Nepali (macrolanguage)**|`ne`| |**Nigerian Fulfulde**|`fuv`| |**North Azerbaijani**|`azj`| |**North Levantine Arabic**|`apc`| |**Northern Kurdish**|`kmr`| |**Northern Uzbek**|`uzn`| |**Norwegian**|`no`| |**Norwegian Bokmål**|`nb`| |**Norwegian Nynorsk**|`nn`| |**Nuer**|`nus`| |**Nyanja**|`ny`| |**Occitan (post 1500)**|`oc`| |**Oriya (macrolanguage)**|`or`| |**Pangasinan**|`pag`| |**Panjabi**|`pa`| |**Papiamento**|`pap`| |**Pedi**|`nso`| |**Persian**|`fa`| |**Plateau Malagasy**|`plt`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Pushto**|`ps`| |**Romanian**|`ro`| |**Rundi**|`rn`| |**Russian**|`ru`| |**Samoan**|`sm`| |**Sango**|`sg`| |**Sanskrit**|`sa`| |**Santali**|`sat`| |**Sardinian**|`sc`| |**Scottish Gaelic**|`gd`| |**Serbian**|`sr`| |**Shan**|`shn`| |**Shona**|`sn`| |**Sicilian**|`scn`| |**Silesian**|`szl`| |**Sindhi**|`sd`| |**Sinhala**|`si`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**South Azerbaijani**|`azb`| |**South Levantine Arabic**|`ajp`| |**Southern Pashto**|`pbt`| |**Southern Sotho**|`st`| |**Southwestern Dinka**|`dik`| |**Spanish**|`es`| |**Standard Latvian**|`lvs`| |**Standard Malay**|`zsm`| |**Sundanese**|`su`| |**Swahili (macrolanguage)**|`sw`| |**Swati**|`ss`| |**Swedish**|`sv`| |**Ta'izzi-Adeni Arabic**|`acq`| |**Tagalog**|`tl`| |**Tajik**|`tg`| |**Tamashek**|`tmh`| |**Tamil**|`ta`| |**Tatar**|`tt`| |**Telugu**|`te`| |**Thai**|`th`| |**Tibetan**|`bo`| |**Tigrinya**|`ti`| |**Tok Pisin**|`tpi`| |**Tosk Albanian**|`als`| |**Tsonga**|`ts`| |**Tswana**|`tn`| |**Tumbuka**|`tum`| |**Tunisian Arabic**|`aeb`| |**Turkish**|`tr`| |**Turkmen**|`tk`| |**Twi**|`tw`| |**Uighur**|`ug`| |**Ukrainian**|`uk`| |**Umbundu**|`umb`| |**Urdu**|`ur`| |**Uzbek**|`uz`| |**Venetian**|`vec`| |**Vietnamese**|`vi`| |**Waray (Philippines)**|`war`| |**Welsh**|`cy`| |**West Central Oromo**|`gaz`| |**Western Frisian**|`fy`| |**Wolof**|`wo`| |**Xhosa**|`xh`| |**Yiddish**|`yi`| |**Yoruba**|`yo`| |**Yue Chinese**|`yue`| |**Zulu**|`zu`| |**jp**|`jp`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Arabic (world)**|`ar-001`| |**Chinese (China)**|`zh-CN`| |**Chinese (Simplified)**|`zh-hans`| |**Chinese (Taiwan)**|`zh-TW`| |**Chinese (Traditional)**|`zh-Hant`| |**Chinese (Traditional)**|`zh-hant`| |**English (United Kingdom)**|`en-gb`| |**Persian (Afghanistan)**|`fa-AF`| |**Portuguese (Brazil)**|`pt-br`| |**Portuguese (Portugal)**|`pt-pt`|  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textspell_check_response_model import TextspellCheckResponseModel
from openapi_client.models.textspell_check_spell_check_request import TextspellCheckSpellCheckRequest
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
    api_instance = openapi_client.SpellCheckApi(api_client)
    textspell_check_spell_check_request = {"providers":"ai21labs,nlpcloud,openai,microsoft,cohere,sapling,prowritingaid","language":"en","text":"Hollo, wrld! How re yu?"} # TextspellCheckSpellCheckRequest | 

    try:
        # Spell Check
        api_response = await api_instance.text_text_spell_check_create(textspell_check_spell_check_request)
        print("The response of SpellCheckApi->text_text_spell_check_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpellCheckApi->text_text_spell_check_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **textspell_check_spell_check_request** | [**TextspellCheckSpellCheckRequest**](TextspellCheckSpellCheckRequest.md)|  | 

### Return type

[**TextspellCheckResponseModel**](TextspellCheckResponseModel.md)

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

