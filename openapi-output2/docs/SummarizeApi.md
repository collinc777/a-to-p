# openapi_client.SummarizeApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_text_summarize_create**](SummarizeApi.md#text_text_summarize_create) | **POST** /text/summarize | Summarize


# **text_text_summarize_create**
> TextsummarizeResponseModel text_text_summarize_create(textsummarize_summarize_request)

Summarize

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**connexun**|-|`v1.0`|2.0 (per 1000 request)|1 request |**microsoft**|-|`v3.1`|2.0 (per 1000000 char)|1000 char |**openai**|-|`v3.0.0`|60.0 (per 1000000 token)|1 token |**openai**|**gpt-4**|`v3.0.0`|60.0 (per 1000000 token)|1 token |**openai**|**gpt-3.5-turbo-1106**|`v3.0.0`|2.0 (per 1000000 token)|1 token |**openai**|**gpt-3.5-turbo**|`v3.0.0`|2.0 (per 1000000 token)|1 token |**openai**|**gpt-3.5-turbo-16k**|`v3.0.0`|4.0 (per 1000000 token)|1 token |**emvista**|-|`v1.0`|1.0 (per 1000000 char)|1000 char |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token |**alephalpha**|-|`1.12.0`|50.0 (per 1000000 char)|1 char |**alephalpha**|**luminous-base**|`1.12.0`|1.0 (per 1000000 char)|1 char |**alephalpha**|**luminous-extended**|`1.12.0`|1.5 (per 1000000 char)|1 char |**alephalpha**|**luminous-supreme**|`1.12.0`|50.0 (per 1000000 char)|1 char |**alephalpha**|**luminous-base-control**|`1.12.0`|1.25 (per 1000000 char)|1 char |**alephalpha**|**luminous-extended-control**|`1.12.0`|1.8 (per 1000000 char)|1 char |**alephalpha**|**luminous-supreme-control**|`1.12.0`|62.5 (per 1000000 char)|1 char |**nlpcloud**|-|`v1`|25.0 (per 1000 request)|1 request |**nlpcloud**|**bart-large-cnn**|`v1`|25.0 (per 1000 request)|1 request |**nlpcloud**|**fast-gpt-j**|`v1`|25.0 (per 1000 request)|1 request |**nlpcloud**|**finetuned-llama-2-70b**|`v1`|25.0 (per 1000 request)|1 request |**nlpcloud**|**chatdolphin**|`v1`|25.0 (per 1000 request)|1 request |**ai21labs**|-|`v1`|0.005 (per 1000 char)|1000 char |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token |**anthropic**|**claude-v1**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token |**anthropic**|-|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Abkhazian**|`ab`| |**Acoli**|`ach`| |**Afar**|`aa`| |**Afrikaans**|`af`| |**Akan**|`ak`| |**Albanian**|`sq`| |**American Sign Language**|`ase`| |**Amharic**|`am`| |**Arabic**|`ar`| |**Aragonese**|`an`| |**Argentine Sign Language**|`aed`| |**Armenian**|`hy`| |**Assamese**|`as`| |**Avaric**|`av`| |**Avestan**|`ae`| |**Awadhi**|`awa`| |**Aymara**|`ay`| |**Azerbaijani**|`az`| |**Bambara**|`bm`| |**Bashkir**|`ba`| |**Basque**|`eu`| |**Belarusian**|`be`| |**Bemba (Zambia)**|`bem`| |**Bengali**|`bn`| |**Berber languages**|`ber`| |**Bhojpuri**|`bho`| |**Bihari languages**|`bh`| |**Bislama**|`bi`| |**Bosnian**|`bs`| |**Brazilian Sign Language**|`bzs`| |**Breton**|`br`| |**Bulgarian**|`bg`| |**Burmese**|`my`| |**Catalan**|`ca`| |**Cebuano**|`ceb`| |**Celtic languages**|`cel`| |**Central Bikol**|`bcl`| |**Central Khmer**|`km`| |**Chamorro**|`ch`| |**Chechen**|`ce`| |**Chilean Sign Language**|`csg`| |**Chinese**|`zh`| |**Church Slavic**|`cu`| |**Chuukese**|`chk`| |**Chuvash**|`cv`| |**Colombian Sign Language**|`csn`| |**Congo Swahili**|`swc`| |**Cornish**|`kw`| |**Corsican**|`co`| |**Cree**|`cr`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dhivehi**|`dv`| |**Dogri (macrolanguage)**|`doi`| |**Dutch**|`nl`| |**Dzongkha**|`dz`| |**Efik**|`efi`| |**English**|`en`| |**Esperanto**|`eo`| |**Estonian**|`et`| |**Ewe**|`ee`| |**Faroese**|`fo`| |**Fijian**|`fj`| |**Finnish**|`fi`| |**Finnish Sign Language**|`fse`| |**Fon**|`fon`| |**French**|`fr`| |**Fulah**|`ff`| |**Ga**|`gaa`| |**Galician**|`gl`| |**Ganda**|`lg`| |**Georgian**|`ka`| |**German**|`de`| |**Gilbertese**|`gil`| |**Guarani**|`gn`| |**Gujarati**|`gu`| |**Gun**|`guw`| |**Haitian**|`ht`| |**Hausa**|`ha`| |**Hebrew**|`he`| |**Herero**|`hz`| |**Hiligaynon**|`hil`| |**Hindi**|`hi`| |**Hiri Motu**|`ho`| |**Hungarian**|`hu`| |**Icelandic**|`is`| |**Ido**|`io`| |**Igbo**|`ig`| |**Iloko**|`ilo`| |**Indonesian**|`id`| |**Interlingua (International Auxiliary Language Association)**|`ia`| |**Interlingue**|`ie`| |**Inuktitut**|`iu`| |**Inupiaq**|`ik`| |**Irish**|`ga`| |**Isoko**|`iso`| |**Isthmus Zapotec**|`zai`| |**Italian**|`it`| |**Japanese**|`ja`| |**Javanese**|`jv`| |**Kabyle**|`kab`| |**Kalaallisut**|`kl`| |**Kannada**|`kn`| |**Kanuri**|`kr`| |**Kaonde**|`kqn`| |**Kashmiri**|`ks`| |**Kazakh**|`kk`| |**Kikuyu**|`ki`| |**Kinyarwanda**|`rw`| |**Kirghiz**|`ky`| |**Komi**|`kv`| |**Kongo**|`kg`| |**Konkani (macrolanguage)**|`kok`| |**Korean**|`ko`| |**Kuanyama**|`kj`| |**Kurdish**|`ku`| |**Kwangali**|`kwn`| |**Lao**|`lo`| |**Latin**|`la`| |**Latvian**|`lv`| |**Limburgan**|`li`| |**Lingala**|`ln`| |**Lithuanian**|`lt`| |**Lozi**|`loz`| |**Luba-Katanga**|`lu`| |**Luba-Lulua**|`lua`| |**Lunda**|`lun`| |**Luo (Kenya and Tanzania)**|`luo`| |**Lushai**|`lus`| |**Luvale**|`lue`| |**Luxembourgish**|`lb`| |**Macedonian**|`mk`| |**Maithili**|`mai`| |**Malagasy**|`mg`| |**Malay (macrolanguage)**|`ms`| |**Malayalam**|`ml`| |**Maltese**|`mt`| |**Manx**|`gv`| |**Maori**|`mi`| |**Marathi**|`mr`| |**Marshallese**|`mh`| |**Mexican Sign Language**|`mfs`| |**Min Nan Chinese**|`nan`| |**Modern Greek (1453-)**|`el`| |**Mongolian**|`mn`| |**Morisyen**|`mfe`| |**Mossi**|`mos`| |**Nauru**|`na`| |**Navajo**|`nv`| |**Ndonga**|`ng`| |**Nepali (macrolanguage)**|`ne`| |**Niuean**|`niu`| |**North Ndebele**|`nd`| |**Northern Sami**|`se`| |**Norwegian**|`no`| |**Norwegian Bokmål**|`nb`| |**Norwegian Nynorsk**|`nn`| |**Nyaneka**|`nyk`| |**Nyanja**|`ny`| |**Occitan (post 1500)**|`oc`| |**Ojibwa**|`oj`| |**Oriya (macrolanguage)**|`or`| |**Oromo**|`om`| |**Ossetian**|`os`| |**Pali**|`pi`| |**Pangasinan**|`pag`| |**Panjabi**|`pa`| |**Papiamento**|`pap`| |**Pedi**|`nso`| |**Persian**|`fa`| |**Peruvian Sign Language**|`prl`| |**Pijin**|`pis`| |**Pohnpeian**|`pon`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Pushto**|`ps`| |**Quechua**|`qu`| |**Romance languages**|`roa`| |**Romanian**|`mo`| |**Romanian**|`ro`| |**Romansh**|`rm`| |**Rundi**|`rn`| |**Russian**|`ru`| |**Ruund**|`rnd`| |**Samoan**|`sm`| |**San Salvador Kongo**|`kwy`| |**Sango**|`sg`| |**Sanskrit**|`sa`| |**Santali**|`sat`| |**Sardinian**|`sc`| |**Scottish Gaelic**|`gd`| |**Serbian**|`sr`| |**Seselwa Creole French**|`crs`| |**Shan**|`shn`| |**Shona**|`sn`| |**Sichuan Yi**|`ii`| |**Sicilian**|`scn`| |**Sindhi**|`sd`| |**Sinhala**|`si`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**South Ndebele**|`nr`| |**Southern Sotho**|`st`| |**Spanish**|`es`| |**Spanish Sign Language**|`ssp`| |**Sranan Tongo**|`srn`| |**Sundanese**|`su`| |**Swahili (macrolanguage)**|`sw`| |**Swati**|`ss`| |**Swedish**|`sv`| |**Tagalog**|`tl`| |**Tahitian**|`ty`| |**Tajik**|`tg`| |**Tamil**|`ta`| |**Tatar**|`tt`| |**Telugu**|`te`| |**Tetela**|`tll`| |**Tetun Dili**|`tdt`| |**Thai**|`th`| |**Tibetan**|`bo`| |**Tigrinya**|`ti`| |**Tiv**|`tiv`| |**Tok Pisin**|`tpi`| |**Tonga (Tonga Islands)**|`to`| |**Tonga (Zambia)**|`toi`| |**Tsonga**|`ts`| |**Tswana**|`tn`| |**Tumbuka**|`tum`| |**Turkish**|`tr`| |**Turkmen**|`tk`| |**Tuvalu**|`tvl`| |**Twi**|`tw`| |**Tzotzil**|`tzo`| |**Uighur**|`ug`| |**Ukrainian**|`uk`| |**Umbundu**|`umb`| |**Urdu**|`ur`| |**Uzbek**|`uz`| |**Venda**|`ve`| |**Venezuelan Sign Language**|`vsl`| |**Vietnamese**|`vi`| |**Volapük**|`vo`| |**Wallisian**|`wls`| |**Walloon**|`wa`| |**Waray (Philippines)**|`war`| |**Welsh**|`cy`| |**Western Frisian**|`fy`| |**Wolaytta**|`wal`| |**Wolof**|`wo`| |**Wu Chinese**|`wuu`| |**Xhosa**|`xh`| |**Yapese**|`yap`| |**Yiddish**|`yi`| |**Yoruba**|`yo`| |**Yucateco**|`yua`| |**Yue Chinese**|`yue`| |**Zande (individual language)**|`zne`| |**Zhuang**|`za`| |**Zulu**|`zu`| |**me**|`me`| |**ra**|`ra`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Chinese (Simplified)**|`zh-Hans`| |**Portuguese (Brazil)**|`pt-BR`| |**Portuguese (Brazil)**|`pt-br`| |**Portuguese (Portugal)**|`pt-PT`| |**Portuguese (Portugal)**|`pt-pt`|  </details><details><summary>Supported Models</summary><details><summary>openai</summary>      |Name|Value| |----|-----| |**openai**|`gpt-3.5-turbo`| ||`gpt-3.5-turbo-1106`| ||`gpt-3.5-turbo-16k`| ||`gpt-4`|  </details><details><summary>cohere</summary>      |Name|Value| |----|-----| |**cohere**|`summarize-medium`| ||`summarize-xlarge`|  </details><details><summary>alephalpha</summary>      |Name|Value| |----|-----| |**alephalpha**|`luminous-base`| ||`luminous-base-control`| ||`luminous-extended`| ||`luminous-extended-control`| ||`luminous-supreme`| ||`luminous-supreme-control`|  </details><details><summary>nlpcloud</summary>      |Name|Value| |----|-----| |**nlpcloud**|`bart-large-cnn`| ||`chatdolphin`| ||`fast-gpt-j`| ||`finetuned-llama-2-70b`|  </details><details><summary>anthropic</summary>      |Name|Value| |----|-----| |**anthropic**|`claude-3-sonnet-20240229-v1:0`| ||`claude-instant-v1`| ||`claude-v2`|  </details>  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.textsummarize_response_model import TextsummarizeResponseModel
from openapi_client.models.textsummarize_summarize_request import TextsummarizeSummarizeRequest
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
    api_instance = openapi_client.SummarizeApi(api_client)
    textsummarize_summarize_request = {"providers":"microsoft,emvista,openai,ai21labs,anthropic,alephalpha,nlpcloud,connexun,cohere","output_sentences":3,"text":"Barack Hussein Obama is an American politician who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, Obama was the first African-American president of the United States. He previously served as a U.S. senator from Illinois from 2005 to 2008 and as an Illinois state senator from 1997 to 2004.","language":"en"} # TextsummarizeSummarizeRequest | 

    try:
        # Summarize
        api_response = api_instance.text_text_summarize_create(textsummarize_summarize_request)
        print("The response of SummarizeApi->text_text_summarize_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SummarizeApi->text_text_summarize_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **textsummarize_summarize_request** | [**TextsummarizeSummarizeRequest**](TextsummarizeSummarizeRequest.md)|  | 

### Return type

[**TextsummarizeResponseModel**](TextsummarizeResponseModel.md)

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

