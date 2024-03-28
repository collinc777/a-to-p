# openapi_client.AutomaticTranslationApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translation_translation_automatic_translation_create**](AutomaticTranslationApi.md#translation_translation_automatic_translation_create) | **POST** /translation/automatic_translation | Automatic Translation


# **translation_translation_automatic_translation_create**
> TranslationautomaticTranslationResponseModel translation_translation_automatic_translation_create(translationautomatic_translation_automatic_translation_request)

Automatic Translation

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**amazon**|`boto3 (v1.15.18)`|15.0 (per 1000000 char)|1 char |**google**|`v3`|20.0 (per 1000000 char)|1 char |**ibm**|`v3 (2018-05-01)`|20.0 (per 1000000 char)|1000 char |**microsoft**|`v3.0`|10.0 (per 1000000 char)|1 char |**neuralspace**|`v1`|7.0 (per 1000 request)|1 request |**phedone**|`-`|4.0 (per 1000000 char)|1000 char |**deepl**|`v2`|20.0 (per 1000000 char)|1 char |**modernmt**|`1.2.8`|8.0 (per 1000000 char)|1 char |**openai**|`v1`|20.0 (per 1000000 token)|1 token   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Abkhazian**|`ab`| |**Acoli**|`ach`| |**Afar**|`aa`| |**Afrikaans**|`af`| |**Akan**|`ak`| |**Albanian**|`sq`| |**American Sign Language**|`ase`| |**Amharic**|`am`| |**Arabic**|`ar`| |**Aragonese**|`an`| |**Argentine Sign Language**|`aed`| |**Armenian**|`hy`| |**Assamese**|`as`| |**Avaric**|`av`| |**Avestan**|`ae`| |**Aymara**|`ay`| |**Azerbaijani**|`az`| |**Bambara**|`bm`| |**Bashkir**|`ba`| |**Basque**|`eu`| |**Belarusian**|`be`| |**Bemba (Zambia)**|`bem`| |**Bengali**|`bn`| |**Berber languages**|`ber`| |**Bihari languages**|`bh`| |**Bislama**|`bi`| |**Bosnian**|`bs`| |**Brazilian Sign Language**|`bzs`| |**Breton**|`br`| |**Bulgarian**|`bg`| |**Burmese**|`my`| |**Catalan**|`ca`| |**Cebuano**|`ceb`| |**Celtic languages**|`cel`| |**Central Bikol**|`bcl`| |**Central Khmer**|`km`| |**Chamorro**|`ch`| |**Chechen**|`ce`| |**Chilean Sign Language**|`csg`| |**Chinese**|`zh`| |**Church Slavic**|`cu`| |**Chuukese**|`chk`| |**Chuvash**|`cv`| |**Colombian Sign Language**|`csn`| |**Congo Swahili**|`swc`| |**Cornish**|`kw`| |**Corsican**|`co`| |**Cree**|`cr`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dari**|`prs`| |**Dhivehi**|`dv`| |**Dutch**|`nl`| |**Dzongkha**|`dz`| |**Efik**|`efi`| |**English**|`en`| |**Esperanto**|`eo`| |**Estonian**|`et`| |**Ewe**|`ee`| |**Faroese**|`fo`| |**Fijian**|`fj`| |**Filipino**|`fil`| |**Finnish**|`fi`| |**Finnish Sign Language**|`fse`| |**Fon**|`fon`| |**French**|`fr`| |**Fulah**|`ff`| |**Ga**|`gaa`| |**Galician**|`gl`| |**Ganda**|`lg`| |**Georgian**|`ka`| |**German**|`de`| |**Gilbertese**|`gil`| |**Guarani**|`gn`| |**Gujarati**|`gu`| |**Gun**|`guw`| |**Haitian**|`ht`| |**Hausa**|`ha`| |**Hawaiian**|`haw`| |**Hebrew**|`he`| |**Herero**|`hz`| |**Hiligaynon**|`hil`| |**Hindi**|`hi`| |**Hiri Motu**|`ho`| |**Hmong**|`hmn`| |**Hmong Daw**|`mww`| |**Hungarian**|`hu`| |**Icelandic**|`is`| |**Ido**|`io`| |**Igbo**|`ig`| |**Iloko**|`ilo`| |**Indonesian**|`id`| |**Interlingua (International Auxiliary Language Association)**|`ia`| |**Interlingue**|`ie`| |**Inuinnaqtun**|`ikt`| |**Inuktitut**|`iu`| |**Inupiaq**|`ik`| |**Irish**|`ga`| |**Isoko**|`iso`| |**Isthmus Zapotec**|`zai`| |**Italian**|`it`| |**Japanese**|`ja`| |**Javanese**|`jv`| |**Kabyle**|`kab`| |**Kalaallisut**|`kl`| |**Kannada**|`kn`| |**Kanuri**|`kr`| |**Kaonde**|`kqn`| |**Kashmiri**|`ks`| |**Kazakh**|`kk`| |**Kikuyu**|`ki`| |**Kinyarwanda**|`rw`| |**Kirghiz**|`ky`| |**Klingon**|`tlh`| |**Komi**|`kv`| |**Kongo**|`kg`| |**Korean**|`ko`| |**Kuanyama**|`kj`| |**Kurdish**|`ku`| |**Kwangali**|`kwn`| |**Lao**|`lo`| |**Latin**|`la`| |**Latvian**|`lv`| |**Limburgan**|`li`| |**Lingala**|`ln`| |**Literary Chinese**|`lzh`| |**Lithuanian**|`lt`| |**Lozi**|`loz`| |**Luba-Katanga**|`lu`| |**Luba-Lulua**|`lua`| |**Lunda**|`lun`| |**Luo (Kenya and Tanzania)**|`luo`| |**Lushai**|`lus`| |**Luvale**|`lue`| |**Luxembourgish**|`lb`| |**Macedonian**|`mk`| |**Malagasy**|`mg`| |**Malay (macrolanguage)**|`ms`| |**Malayalam**|`ml`| |**Maltese**|`mt`| |**Manx**|`gv`| |**Maori**|`mi`| |**Marathi**|`mr`| |**Marshallese**|`mh`| |**Mexican Sign Language**|`mfs`| |**Modern Greek (1453-)**|`el`| |**Mongolian**|`mn`| |**Morisyen**|`mfe`| |**Mossi**|`mos`| |**Nauru**|`na`| |**Navajo**|`nv`| |**Ndonga**|`ng`| |**Nepali (macrolanguage)**|`ne`| |**Niuean**|`niu`| |**North Ndebele**|`nd`| |**Northern Kurdish**|`kmr`| |**Northern Sami**|`se`| |**Norwegian**|`no`| |**Norwegian Bokmål**|`nb`| |**Norwegian Nynorsk**|`nn`| |**Nyaneka**|`nyk`| |**Nyanja**|`ny`| |**Occitan (post 1500)**|`oc`| |**Ojibwa**|`oj`| |**Oriya (macrolanguage)**|`or`| |**Oromo**|`om`| |**Ossetian**|`os`| |**Pali**|`pi`| |**Pangasinan**|`pag`| |**Panjabi**|`pa`| |**Papiamento**|`pap`| |**Pedi**|`nso`| |**Persian**|`fa`| |**Peruvian Sign Language**|`prl`| |**Pijin**|`pis`| |**Pohnpeian**|`pon`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Pushto**|`ps`| |**Quechua**|`qu`| |**Querétaro Otomi**|`otq`| |**Romance languages**|`roa`| |**Romanian**|`ro`| |**Romansh**|`rm`| |**Rundi**|`rn`| |**Russian**|`ru`| |**Ruund**|`rnd`| |**Samoan**|`sm`| |**San Salvador Kongo**|`kwy`| |**Sango**|`sg`| |**Sanskrit**|`sa`| |**Sardinian**|`sc`| |**Scottish Gaelic**|`gd`| |**Serbian**|`sr`| |**Serbo-Croatian**|`sh`| |**Seselwa Creole French**|`crs`| |**Shona**|`sn`| |**Sichuan Yi**|`ii`| |**Sindhi**|`sd`| |**Sinhala**|`si`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**South Ndebele**|`nr`| |**Southern Sotho**|`st`| |**Spanish**|`es`| |**Spanish Sign Language**|`ssp`| |**Sranan Tongo**|`srn`| |**Sundanese**|`su`| |**Swahili (macrolanguage)**|`sw`| |**Swati**|`ss`| |**Swedish**|`sv`| |**Tagalog**|`tl`| |**Tahitian**|`ty`| |**Tajik**|`tg`| |**Tamil**|`ta`| |**Tatar**|`tt`| |**Telugu**|`te`| |**Tetela**|`tll`| |**Tetun Dili**|`tdt`| |**Thai**|`th`| |**Tibetan**|`bo`| |**Tigrinya**|`ti`| |**Tiv**|`tiv`| |**Tok Pisin**|`tpi`| |**Tonga (Tonga Islands)**|`to`| |**Tonga (Zambia)**|`toi`| |**Tsonga**|`ts`| |**Tswana**|`tn`| |**Tumbuka**|`tum`| |**Turkish**|`tr`| |**Turkmen**|`tk`| |**Tuvalu**|`tvl`| |**Twi**|`tw`| |**Tzotzil**|`tzo`| |**Uighur**|`ug`| |**Ukrainian**|`uk`| |**Umbundu**|`umb`| |**Upper Sorbian**|`hsb`| |**Urdu**|`ur`| |**Uzbek**|`uz`| |**Venda**|`ve`| |**Venezuelan Sign Language**|`vsl`| |**Vietnamese**|`vi`| |**Volapük**|`vo`| |**Wallisian**|`wls`| |**Walloon**|`wa`| |**Waray (Philippines)**|`war`| |**Welsh**|`cy`| |**Western Frisian**|`fy`| |**Wolaytta**|`wal`| |**Wolof**|`wo`| |**Xhosa**|`xh`| |**Yapese**|`yap`| |**Yiddish**|`yi`| |**Yoruba**|`yo`| |**Yucateco**|`yua`| |**Yue Chinese**|`yue`| |**Zande (individual language)**|`zne`| |**Zhuang**|`za`| |**Zulu**|`zu`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Arabic (Argentina)**|`ar-AR`| |**Bangla (Bangladesh)**|`bn-BD`| |**Basque (Spain)**|`eu-ES`| |**Bosnian (Bosnia & Herzegovina)**|`bs-BA`| |**Bulgarian (Bulgaria)**|`bg-BG`| |**Catalan (Spain)**|`ca-ES`| |**Chinese (China)**|`zh-CN`| |**Chinese (Simplified)**|`zh-Hans`| |**Chinese (Taiwan)**|`zh-TW`| |**Chinese (Traditional)**|`zh-Hant`| |**Croatian (Croatia)**|`hr-HR`| |**Czech (Czechia)**|`cs-CZ`| |**Danish (Denmark)**|`da-DK`| |**Dutch (Netherlands)**|`nl-NL`| |**English (United Kingdom)**|`en-GB`| |**English (United States)**|`en-US`| |**Estonian (Estonia)**|`et-EE`| |**Finnish (Finland)**|`fi-FI`| |**French (Canada)**|`fr-CA`| |**French (France)**|`fr-FR`| |**German (Germany)**|`de-DE`| |**Greek (Greece)**|`el-GR`| |**Gujarati (India)**|`gu-IN`| |**Hebrew (Israel)**|`he-IL`| |**Hindi (India)**|`hi-IN`| |**Hungarian (Hungary)**|`hu-HU`| |**Indonesian (Indonesia)**|`id-ID`| |**Inuktitut (Latin)**|`iu-Latn`| |**Irish (Ireland)**|`ga-IE`| |**Italian (Italy)**|`it-IT`| |**Japanese (Japan)**|`ja-JP`| |**Kannada (India)**|`kn-IN`| |**Klingon (Klingon (KLI pIqaD))**|`tlh-Piqd`| |**Klingon (Latin)**|`tlh-Latn`| |**Korean (South Korea)**|`ko-KR`| |**Latvian (Latvia)**|`lv-LV`| |**Lithuanian (Lithuania)**|`lt-LT`| |**Malay (Malaysia)**|`ms-MY`| |**Malayalam (India)**|`ml-IN`| |**Maltese (Malta)**|`mt-MT`| |**Marathi (India)**|`mr-IN`| |**Mongolian (Cyrillic)**|`mn-Cyrl`| |**Mongolian (Mongolian)**|`mn-Mong`| |**Nepali (Nepal)**|`ne-NP`| |**Norwegian Bokmål (Norway)**|`nb-NO`| |**Persian (Afghanistan)**|`fa-AF`| |**Polish (Poland)**|`pl-PL`| |**Portuguese (Brazil)**|`pt-BR`| |**Portuguese (Portugal)**|`pt-PT`| |**Punjabi (India)**|`pa-IN`| |**Romanian (Romania)**|`ro-RO`| |**Russian (Russia)**|`ru-RU`| |**Serbian (Cyrillic)**|`sr-Cyrl`| |**Serbian (Latin)**|`sr-Latn`| |**Serbian (Montenegro)**|`sr-ME`| |**Serbian (Serbia)**|`sr-RS`| |**Sinhala (Sri Lanka)**|`si-LK`| |**Slovak (Slovakia)**|`sk-SK`| |**Slovenian (Slovenia)**|`sl-SI`| |**Spanish (Latin America)**|`es-419`| |**Spanish (Mexico)**|`es-MX`| |**Spanish (Spain)**|`es-ES`| |**Swedish (Sweden)**|`sv-SE`| |**Tamil (India)**|`ta-IN`| |**Telugu (India)**|`te-IN`| |**Thai (Thailand)**|`th-TH`| |**Turkish (Turkey)**|`tr-TR`| |**Ukrainian (Ukraine)**|`uk-UA`| |**Urdu (Pakistan)**|`ur-PK`| |**Vietnamese (Vietnam)**|`vi-VN`| |**Welsh (United Kingdom)**|`cy-GB`|  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.translationautomatic_translation_automatic_translation_request import TranslationautomaticTranslationAutomaticTranslationRequest
from openapi_client.models.translationautomatic_translation_response_model import TranslationautomaticTranslationResponseModel
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
    api_instance = openapi_client.AutomaticTranslationApi(api_client)
    translationautomatic_translation_automatic_translation_request = {"providers":"microsoft,openai,google,modernmt,ibm,phedone,neuralspace,amazon,deepl","text":"人工智能 亦稱智械、機器智能，指由人製造出來的機器所表現出來的智慧。通常人工智能是指通过普通電腦程式來呈現人類智能的技術。該詞也指出研究這樣的智能系統是否能夠實現，以及如何實現。同时，通過醫學、神經科學、機器人學及統計學等的進步，常態預測則認為人類的很多職業也逐漸被其取代。","source_language":"zh","target_language":"en"} # TranslationautomaticTranslationAutomaticTranslationRequest | 

    try:
        # Automatic Translation
        api_response = await api_instance.translation_translation_automatic_translation_create(translationautomatic_translation_automatic_translation_request)
        print("The response of AutomaticTranslationApi->translation_translation_automatic_translation_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomaticTranslationApi->translation_translation_automatic_translation_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translationautomatic_translation_automatic_translation_request** | [**TranslationautomaticTranslationAutomaticTranslationRequest**](TranslationautomaticTranslationAutomaticTranslationRequest.md)|  | 

### Return type

[**TranslationautomaticTranslationResponseModel**](TranslationautomaticTranslationResponseModel.md)

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

