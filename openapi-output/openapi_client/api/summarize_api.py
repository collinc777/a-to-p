# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from openapi_client.models.textsummarize_response_model import TextsummarizeResponseModel
from openapi_client.models.textsummarize_summarize_request import TextsummarizeSummarizeRequest

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class SummarizeApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def text_text_summarize_create(
        self,
        textsummarize_summarize_request: TextsummarizeSummarizeRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> TextsummarizeResponseModel:
        """Summarize

        <details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**connexun**|-|`v1.0`|2.0 (per 1000 request)|1 request |**microsoft**|-|`v3.1`|2.0 (per 1000000 char)|1000 char |**openai**|-|`v3.0.0`|60.0 (per 1000000 token)|1 token |**openai**|**gpt-4**|`v3.0.0`|60.0 (per 1000000 token)|1 token |**openai**|**gpt-3.5-turbo-1106**|`v3.0.0`|2.0 (per 1000000 token)|1 token |**openai**|**gpt-3.5-turbo**|`v3.0.0`|2.0 (per 1000000 token)|1 token |**openai**|**gpt-3.5-turbo-16k**|`v3.0.0`|4.0 (per 1000000 token)|1 token |**emvista**|-|`v1.0`|1.0 (per 1000000 char)|1000 char |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token |**alephalpha**|-|`1.12.0`|50.0 (per 1000000 char)|1 char |**alephalpha**|**luminous-base**|`1.12.0`|1.0 (per 1000000 char)|1 char |**alephalpha**|**luminous-extended**|`1.12.0`|1.5 (per 1000000 char)|1 char |**alephalpha**|**luminous-supreme**|`1.12.0`|50.0 (per 1000000 char)|1 char |**alephalpha**|**luminous-base-control**|`1.12.0`|1.25 (per 1000000 char)|1 char |**alephalpha**|**luminous-extended-control**|`1.12.0`|1.8 (per 1000000 char)|1 char |**alephalpha**|**luminous-supreme-control**|`1.12.0`|62.5 (per 1000000 char)|1 char |**nlpcloud**|-|`v1`|25.0 (per 1000 request)|1 request |**nlpcloud**|**bart-large-cnn**|`v1`|25.0 (per 1000 request)|1 request |**nlpcloud**|**fast-gpt-j**|`v1`|25.0 (per 1000 request)|1 request |**nlpcloud**|**finetuned-llama-2-70b**|`v1`|25.0 (per 1000 request)|1 request |**nlpcloud**|**chatdolphin**|`v1`|25.0 (per 1000 request)|1 request |**ai21labs**|-|`v1`|0.005 (per 1000 char)|1000 char |**anthropic**|**claude-3-haiku-20240307-v1:0**|`bedrock-2023-05-31`|1.25 (per 1000000 token)|1 token |**anthropic**|**claude-3-sonnet-20240229-v1:0**|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1 token |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token |**anthropic**|-|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1 token   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Abkhazian**|`ab`| |**Acoli**|`ach`| |**Afar**|`aa`| |**Afrikaans**|`af`| |**Akan**|`ak`| |**Albanian**|`sq`| |**American Sign Language**|`ase`| |**Amharic**|`am`| |**Arabic**|`ar`| |**Aragonese**|`an`| |**Argentine Sign Language**|`aed`| |**Armenian**|`hy`| |**Assamese**|`as`| |**Avaric**|`av`| |**Avestan**|`ae`| |**Awadhi**|`awa`| |**Aymara**|`ay`| |**Azerbaijani**|`az`| |**Bambara**|`bm`| |**Bashkir**|`ba`| |**Basque**|`eu`| |**Belarusian**|`be`| |**Bemba (Zambia)**|`bem`| |**Bengali**|`bn`| |**Berber languages**|`ber`| |**Bhojpuri**|`bho`| |**Bihari languages**|`bh`| |**Bislama**|`bi`| |**Bosnian**|`bs`| |**Brazilian Sign Language**|`bzs`| |**Breton**|`br`| |**Bulgarian**|`bg`| |**Burmese**|`my`| |**Catalan**|`ca`| |**Cebuano**|`ceb`| |**Celtic languages**|`cel`| |**Central Bikol**|`bcl`| |**Central Khmer**|`km`| |**Chamorro**|`ch`| |**Chechen**|`ce`| |**Chilean Sign Language**|`csg`| |**Chinese**|`zh`| |**Church Slavic**|`cu`| |**Chuukese**|`chk`| |**Chuvash**|`cv`| |**Colombian Sign Language**|`csn`| |**Congo Swahili**|`swc`| |**Cornish**|`kw`| |**Corsican**|`co`| |**Cree**|`cr`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dhivehi**|`dv`| |**Dogri (macrolanguage)**|`doi`| |**Dutch**|`nl`| |**Dzongkha**|`dz`| |**Efik**|`efi`| |**English**|`en`| |**Esperanto**|`eo`| |**Estonian**|`et`| |**Ewe**|`ee`| |**Faroese**|`fo`| |**Fijian**|`fj`| |**Finnish**|`fi`| |**Finnish Sign Language**|`fse`| |**Fon**|`fon`| |**French**|`fr`| |**Fulah**|`ff`| |**Ga**|`gaa`| |**Galician**|`gl`| |**Ganda**|`lg`| |**Georgian**|`ka`| |**German**|`de`| |**Gilbertese**|`gil`| |**Guarani**|`gn`| |**Gujarati**|`gu`| |**Gun**|`guw`| |**Haitian**|`ht`| |**Hausa**|`ha`| |**Hebrew**|`he`| |**Herero**|`hz`| |**Hiligaynon**|`hil`| |**Hindi**|`hi`| |**Hiri Motu**|`ho`| |**Hungarian**|`hu`| |**Icelandic**|`is`| |**Ido**|`io`| |**Igbo**|`ig`| |**Iloko**|`ilo`| |**Indonesian**|`id`| |**Interlingua (International Auxiliary Language Association)**|`ia`| |**Interlingue**|`ie`| |**Inuktitut**|`iu`| |**Inupiaq**|`ik`| |**Irish**|`ga`| |**Isoko**|`iso`| |**Isthmus Zapotec**|`zai`| |**Italian**|`it`| |**Japanese**|`ja`| |**Javanese**|`jv`| |**Kabyle**|`kab`| |**Kalaallisut**|`kl`| |**Kannada**|`kn`| |**Kanuri**|`kr`| |**Kaonde**|`kqn`| |**Kashmiri**|`ks`| |**Kazakh**|`kk`| |**Kikuyu**|`ki`| |**Kinyarwanda**|`rw`| |**Kirghiz**|`ky`| |**Komi**|`kv`| |**Kongo**|`kg`| |**Konkani (macrolanguage)**|`kok`| |**Korean**|`ko`| |**Kuanyama**|`kj`| |**Kurdish**|`ku`| |**Kwangali**|`kwn`| |**Lao**|`lo`| |**Latin**|`la`| |**Latvian**|`lv`| |**Limburgan**|`li`| |**Lingala**|`ln`| |**Lithuanian**|`lt`| |**Lozi**|`loz`| |**Luba-Katanga**|`lu`| |**Luba-Lulua**|`lua`| |**Lunda**|`lun`| |**Luo (Kenya and Tanzania)**|`luo`| |**Lushai**|`lus`| |**Luvale**|`lue`| |**Luxembourgish**|`lb`| |**Macedonian**|`mk`| |**Maithili**|`mai`| |**Malagasy**|`mg`| |**Malay (macrolanguage)**|`ms`| |**Malayalam**|`ml`| |**Maltese**|`mt`| |**Manx**|`gv`| |**Maori**|`mi`| |**Marathi**|`mr`| |**Marshallese**|`mh`| |**Mexican Sign Language**|`mfs`| |**Min Nan Chinese**|`nan`| |**Modern Greek (1453-)**|`el`| |**Mongolian**|`mn`| |**Morisyen**|`mfe`| |**Mossi**|`mos`| |**Nauru**|`na`| |**Navajo**|`nv`| |**Ndonga**|`ng`| |**Nepali (macrolanguage)**|`ne`| |**Niuean**|`niu`| |**North Ndebele**|`nd`| |**Northern Sami**|`se`| |**Norwegian**|`no`| |**Norwegian Bokmål**|`nb`| |**Norwegian Nynorsk**|`nn`| |**Nyaneka**|`nyk`| |**Nyanja**|`ny`| |**Occitan (post 1500)**|`oc`| |**Ojibwa**|`oj`| |**Oriya (macrolanguage)**|`or`| |**Oromo**|`om`| |**Ossetian**|`os`| |**Pali**|`pi`| |**Pangasinan**|`pag`| |**Panjabi**|`pa`| |**Papiamento**|`pap`| |**Pedi**|`nso`| |**Persian**|`fa`| |**Peruvian Sign Language**|`prl`| |**Pijin**|`pis`| |**Pohnpeian**|`pon`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Pushto**|`ps`| |**Quechua**|`qu`| |**Romance languages**|`roa`| |**Romanian**|`mo`| |**Romanian**|`ro`| |**Romansh**|`rm`| |**Rundi**|`rn`| |**Russian**|`ru`| |**Ruund**|`rnd`| |**Samoan**|`sm`| |**San Salvador Kongo**|`kwy`| |**Sango**|`sg`| |**Sanskrit**|`sa`| |**Santali**|`sat`| |**Sardinian**|`sc`| |**Scottish Gaelic**|`gd`| |**Serbian**|`sr`| |**Seselwa Creole French**|`crs`| |**Shan**|`shn`| |**Shona**|`sn`| |**Sichuan Yi**|`ii`| |**Sicilian**|`scn`| |**Sindhi**|`sd`| |**Sinhala**|`si`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**South Ndebele**|`nr`| |**Southern Sotho**|`st`| |**Spanish**|`es`| |**Spanish Sign Language**|`ssp`| |**Sranan Tongo**|`srn`| |**Sundanese**|`su`| |**Swahili (macrolanguage)**|`sw`| |**Swati**|`ss`| |**Swedish**|`sv`| |**Tagalog**|`tl`| |**Tahitian**|`ty`| |**Tajik**|`tg`| |**Tamil**|`ta`| |**Tatar**|`tt`| |**Telugu**|`te`| |**Tetela**|`tll`| |**Tetun Dili**|`tdt`| |**Thai**|`th`| |**Tibetan**|`bo`| |**Tigrinya**|`ti`| |**Tiv**|`tiv`| |**Tok Pisin**|`tpi`| |**Tonga (Tonga Islands)**|`to`| |**Tonga (Zambia)**|`toi`| |**Tsonga**|`ts`| |**Tswana**|`tn`| |**Tumbuka**|`tum`| |**Turkish**|`tr`| |**Turkmen**|`tk`| |**Tuvalu**|`tvl`| |**Twi**|`tw`| |**Tzotzil**|`tzo`| |**Uighur**|`ug`| |**Ukrainian**|`uk`| |**Umbundu**|`umb`| |**Urdu**|`ur`| |**Uzbek**|`uz`| |**Venda**|`ve`| |**Venezuelan Sign Language**|`vsl`| |**Vietnamese**|`vi`| |**Volapük**|`vo`| |**Wallisian**|`wls`| |**Walloon**|`wa`| |**Waray (Philippines)**|`war`| |**Welsh**|`cy`| |**Western Frisian**|`fy`| |**Wolaytta**|`wal`| |**Wolof**|`wo`| |**Wu Chinese**|`wuu`| |**Xhosa**|`xh`| |**Yapese**|`yap`| |**Yiddish**|`yi`| |**Yoruba**|`yo`| |**Yucateco**|`yua`| |**Yue Chinese**|`yue`| |**Zande (individual language)**|`zne`| |**Zhuang**|`za`| |**Zulu**|`zu`| |**me**|`me`| |**ra**|`ra`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Chinese (Simplified)**|`zh-Hans`| |**Portuguese (Brazil)**|`pt-BR`| |**Portuguese (Brazil)**|`pt-br`| |**Portuguese (Portugal)**|`pt-PT`| |**Portuguese (Portugal)**|`pt-pt`|  </details><details><summary>Supported Models</summary><details><summary>openai</summary>      |Name|Value| |----|-----| |**openai**|`gpt-3.5-turbo`| ||`gpt-3.5-turbo-1106`| ||`gpt-3.5-turbo-16k`| ||`gpt-4`|  </details><details><summary>cohere</summary>      |Name|Value| |----|-----| |**cohere**|`summarize-medium`| ||`summarize-xlarge`|  </details><details><summary>alephalpha</summary>      |Name|Value| |----|-----| |**alephalpha**|`luminous-base`| ||`luminous-base-control`| ||`luminous-extended`| ||`luminous-extended-control`| ||`luminous-supreme`| ||`luminous-supreme-control`|  </details><details><summary>nlpcloud</summary>      |Name|Value| |----|-----| |**nlpcloud**|`bart-large-cnn`| ||`chatdolphin`| ||`fast-gpt-j`| ||`finetuned-llama-2-70b`|  </details><details><summary>anthropic</summary>      |Name|Value| |----|-----| |**anthropic**|`claude-3-sonnet-20240229-v1:0`| ||`claude-instant-v1`| ||`claude-v2`|  </details>  </details>

        :param textsummarize_summarize_request: (required)
        :type textsummarize_summarize_request: TextsummarizeSummarizeRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._text_text_summarize_create_serialize(
            textsummarize_summarize_request=textsummarize_summarize_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "TextsummarizeResponseModel",
            '400': "BadRequest",
            '500': "Error",
            '403': "Error",
            '404': "NotFoundResponse",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def text_text_summarize_create_with_http_info(
        self,
        textsummarize_summarize_request: TextsummarizeSummarizeRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[TextsummarizeResponseModel]:
        """Summarize

        <details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**connexun**|-|`v1.0`|2.0 (per 1000 request)|1 request |**microsoft**|-|`v3.1`|2.0 (per 1000000 char)|1000 char |**openai**|-|`v3.0.0`|60.0 (per 1000000 token)|1 token |**openai**|**gpt-4**|`v3.0.0`|60.0 (per 1000000 token)|1 token |**openai**|**gpt-3.5-turbo-1106**|`v3.0.0`|2.0 (per 1000000 token)|1 token |**openai**|**gpt-3.5-turbo**|`v3.0.0`|2.0 (per 1000000 token)|1 token |**openai**|**gpt-3.5-turbo-16k**|`v3.0.0`|4.0 (per 1000000 token)|1 token |**emvista**|-|`v1.0`|1.0 (per 1000000 char)|1000 char |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token |**alephalpha**|-|`1.12.0`|50.0 (per 1000000 char)|1 char |**alephalpha**|**luminous-base**|`1.12.0`|1.0 (per 1000000 char)|1 char |**alephalpha**|**luminous-extended**|`1.12.0`|1.5 (per 1000000 char)|1 char |**alephalpha**|**luminous-supreme**|`1.12.0`|50.0 (per 1000000 char)|1 char |**alephalpha**|**luminous-base-control**|`1.12.0`|1.25 (per 1000000 char)|1 char |**alephalpha**|**luminous-extended-control**|`1.12.0`|1.8 (per 1000000 char)|1 char |**alephalpha**|**luminous-supreme-control**|`1.12.0`|62.5 (per 1000000 char)|1 char |**nlpcloud**|-|`v1`|25.0 (per 1000 request)|1 request |**nlpcloud**|**bart-large-cnn**|`v1`|25.0 (per 1000 request)|1 request |**nlpcloud**|**fast-gpt-j**|`v1`|25.0 (per 1000 request)|1 request |**nlpcloud**|**finetuned-llama-2-70b**|`v1`|25.0 (per 1000 request)|1 request |**nlpcloud**|**chatdolphin**|`v1`|25.0 (per 1000 request)|1 request |**ai21labs**|-|`v1`|0.005 (per 1000 char)|1000 char |**anthropic**|**claude-3-haiku-20240307-v1:0**|`bedrock-2023-05-31`|1.25 (per 1000000 token)|1 token |**anthropic**|**claude-3-sonnet-20240229-v1:0**|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1 token |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token |**anthropic**|-|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1 token   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Abkhazian**|`ab`| |**Acoli**|`ach`| |**Afar**|`aa`| |**Afrikaans**|`af`| |**Akan**|`ak`| |**Albanian**|`sq`| |**American Sign Language**|`ase`| |**Amharic**|`am`| |**Arabic**|`ar`| |**Aragonese**|`an`| |**Argentine Sign Language**|`aed`| |**Armenian**|`hy`| |**Assamese**|`as`| |**Avaric**|`av`| |**Avestan**|`ae`| |**Awadhi**|`awa`| |**Aymara**|`ay`| |**Azerbaijani**|`az`| |**Bambara**|`bm`| |**Bashkir**|`ba`| |**Basque**|`eu`| |**Belarusian**|`be`| |**Bemba (Zambia)**|`bem`| |**Bengali**|`bn`| |**Berber languages**|`ber`| |**Bhojpuri**|`bho`| |**Bihari languages**|`bh`| |**Bislama**|`bi`| |**Bosnian**|`bs`| |**Brazilian Sign Language**|`bzs`| |**Breton**|`br`| |**Bulgarian**|`bg`| |**Burmese**|`my`| |**Catalan**|`ca`| |**Cebuano**|`ceb`| |**Celtic languages**|`cel`| |**Central Bikol**|`bcl`| |**Central Khmer**|`km`| |**Chamorro**|`ch`| |**Chechen**|`ce`| |**Chilean Sign Language**|`csg`| |**Chinese**|`zh`| |**Church Slavic**|`cu`| |**Chuukese**|`chk`| |**Chuvash**|`cv`| |**Colombian Sign Language**|`csn`| |**Congo Swahili**|`swc`| |**Cornish**|`kw`| |**Corsican**|`co`| |**Cree**|`cr`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dhivehi**|`dv`| |**Dogri (macrolanguage)**|`doi`| |**Dutch**|`nl`| |**Dzongkha**|`dz`| |**Efik**|`efi`| |**English**|`en`| |**Esperanto**|`eo`| |**Estonian**|`et`| |**Ewe**|`ee`| |**Faroese**|`fo`| |**Fijian**|`fj`| |**Finnish**|`fi`| |**Finnish Sign Language**|`fse`| |**Fon**|`fon`| |**French**|`fr`| |**Fulah**|`ff`| |**Ga**|`gaa`| |**Galician**|`gl`| |**Ganda**|`lg`| |**Georgian**|`ka`| |**German**|`de`| |**Gilbertese**|`gil`| |**Guarani**|`gn`| |**Gujarati**|`gu`| |**Gun**|`guw`| |**Haitian**|`ht`| |**Hausa**|`ha`| |**Hebrew**|`he`| |**Herero**|`hz`| |**Hiligaynon**|`hil`| |**Hindi**|`hi`| |**Hiri Motu**|`ho`| |**Hungarian**|`hu`| |**Icelandic**|`is`| |**Ido**|`io`| |**Igbo**|`ig`| |**Iloko**|`ilo`| |**Indonesian**|`id`| |**Interlingua (International Auxiliary Language Association)**|`ia`| |**Interlingue**|`ie`| |**Inuktitut**|`iu`| |**Inupiaq**|`ik`| |**Irish**|`ga`| |**Isoko**|`iso`| |**Isthmus Zapotec**|`zai`| |**Italian**|`it`| |**Japanese**|`ja`| |**Javanese**|`jv`| |**Kabyle**|`kab`| |**Kalaallisut**|`kl`| |**Kannada**|`kn`| |**Kanuri**|`kr`| |**Kaonde**|`kqn`| |**Kashmiri**|`ks`| |**Kazakh**|`kk`| |**Kikuyu**|`ki`| |**Kinyarwanda**|`rw`| |**Kirghiz**|`ky`| |**Komi**|`kv`| |**Kongo**|`kg`| |**Konkani (macrolanguage)**|`kok`| |**Korean**|`ko`| |**Kuanyama**|`kj`| |**Kurdish**|`ku`| |**Kwangali**|`kwn`| |**Lao**|`lo`| |**Latin**|`la`| |**Latvian**|`lv`| |**Limburgan**|`li`| |**Lingala**|`ln`| |**Lithuanian**|`lt`| |**Lozi**|`loz`| |**Luba-Katanga**|`lu`| |**Luba-Lulua**|`lua`| |**Lunda**|`lun`| |**Luo (Kenya and Tanzania)**|`luo`| |**Lushai**|`lus`| |**Luvale**|`lue`| |**Luxembourgish**|`lb`| |**Macedonian**|`mk`| |**Maithili**|`mai`| |**Malagasy**|`mg`| |**Malay (macrolanguage)**|`ms`| |**Malayalam**|`ml`| |**Maltese**|`mt`| |**Manx**|`gv`| |**Maori**|`mi`| |**Marathi**|`mr`| |**Marshallese**|`mh`| |**Mexican Sign Language**|`mfs`| |**Min Nan Chinese**|`nan`| |**Modern Greek (1453-)**|`el`| |**Mongolian**|`mn`| |**Morisyen**|`mfe`| |**Mossi**|`mos`| |**Nauru**|`na`| |**Navajo**|`nv`| |**Ndonga**|`ng`| |**Nepali (macrolanguage)**|`ne`| |**Niuean**|`niu`| |**North Ndebele**|`nd`| |**Northern Sami**|`se`| |**Norwegian**|`no`| |**Norwegian Bokmål**|`nb`| |**Norwegian Nynorsk**|`nn`| |**Nyaneka**|`nyk`| |**Nyanja**|`ny`| |**Occitan (post 1500)**|`oc`| |**Ojibwa**|`oj`| |**Oriya (macrolanguage)**|`or`| |**Oromo**|`om`| |**Ossetian**|`os`| |**Pali**|`pi`| |**Pangasinan**|`pag`| |**Panjabi**|`pa`| |**Papiamento**|`pap`| |**Pedi**|`nso`| |**Persian**|`fa`| |**Peruvian Sign Language**|`prl`| |**Pijin**|`pis`| |**Pohnpeian**|`pon`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Pushto**|`ps`| |**Quechua**|`qu`| |**Romance languages**|`roa`| |**Romanian**|`mo`| |**Romanian**|`ro`| |**Romansh**|`rm`| |**Rundi**|`rn`| |**Russian**|`ru`| |**Ruund**|`rnd`| |**Samoan**|`sm`| |**San Salvador Kongo**|`kwy`| |**Sango**|`sg`| |**Sanskrit**|`sa`| |**Santali**|`sat`| |**Sardinian**|`sc`| |**Scottish Gaelic**|`gd`| |**Serbian**|`sr`| |**Seselwa Creole French**|`crs`| |**Shan**|`shn`| |**Shona**|`sn`| |**Sichuan Yi**|`ii`| |**Sicilian**|`scn`| |**Sindhi**|`sd`| |**Sinhala**|`si`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**South Ndebele**|`nr`| |**Southern Sotho**|`st`| |**Spanish**|`es`| |**Spanish Sign Language**|`ssp`| |**Sranan Tongo**|`srn`| |**Sundanese**|`su`| |**Swahili (macrolanguage)**|`sw`| |**Swati**|`ss`| |**Swedish**|`sv`| |**Tagalog**|`tl`| |**Tahitian**|`ty`| |**Tajik**|`tg`| |**Tamil**|`ta`| |**Tatar**|`tt`| |**Telugu**|`te`| |**Tetela**|`tll`| |**Tetun Dili**|`tdt`| |**Thai**|`th`| |**Tibetan**|`bo`| |**Tigrinya**|`ti`| |**Tiv**|`tiv`| |**Tok Pisin**|`tpi`| |**Tonga (Tonga Islands)**|`to`| |**Tonga (Zambia)**|`toi`| |**Tsonga**|`ts`| |**Tswana**|`tn`| |**Tumbuka**|`tum`| |**Turkish**|`tr`| |**Turkmen**|`tk`| |**Tuvalu**|`tvl`| |**Twi**|`tw`| |**Tzotzil**|`tzo`| |**Uighur**|`ug`| |**Ukrainian**|`uk`| |**Umbundu**|`umb`| |**Urdu**|`ur`| |**Uzbek**|`uz`| |**Venda**|`ve`| |**Venezuelan Sign Language**|`vsl`| |**Vietnamese**|`vi`| |**Volapük**|`vo`| |**Wallisian**|`wls`| |**Walloon**|`wa`| |**Waray (Philippines)**|`war`| |**Welsh**|`cy`| |**Western Frisian**|`fy`| |**Wolaytta**|`wal`| |**Wolof**|`wo`| |**Wu Chinese**|`wuu`| |**Xhosa**|`xh`| |**Yapese**|`yap`| |**Yiddish**|`yi`| |**Yoruba**|`yo`| |**Yucateco**|`yua`| |**Yue Chinese**|`yue`| |**Zande (individual language)**|`zne`| |**Zhuang**|`za`| |**Zulu**|`zu`| |**me**|`me`| |**ra**|`ra`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Chinese (Simplified)**|`zh-Hans`| |**Portuguese (Brazil)**|`pt-BR`| |**Portuguese (Brazil)**|`pt-br`| |**Portuguese (Portugal)**|`pt-PT`| |**Portuguese (Portugal)**|`pt-pt`|  </details><details><summary>Supported Models</summary><details><summary>openai</summary>      |Name|Value| |----|-----| |**openai**|`gpt-3.5-turbo`| ||`gpt-3.5-turbo-1106`| ||`gpt-3.5-turbo-16k`| ||`gpt-4`|  </details><details><summary>cohere</summary>      |Name|Value| |----|-----| |**cohere**|`summarize-medium`| ||`summarize-xlarge`|  </details><details><summary>alephalpha</summary>      |Name|Value| |----|-----| |**alephalpha**|`luminous-base`| ||`luminous-base-control`| ||`luminous-extended`| ||`luminous-extended-control`| ||`luminous-supreme`| ||`luminous-supreme-control`|  </details><details><summary>nlpcloud</summary>      |Name|Value| |----|-----| |**nlpcloud**|`bart-large-cnn`| ||`chatdolphin`| ||`fast-gpt-j`| ||`finetuned-llama-2-70b`|  </details><details><summary>anthropic</summary>      |Name|Value| |----|-----| |**anthropic**|`claude-3-sonnet-20240229-v1:0`| ||`claude-instant-v1`| ||`claude-v2`|  </details>  </details>

        :param textsummarize_summarize_request: (required)
        :type textsummarize_summarize_request: TextsummarizeSummarizeRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._text_text_summarize_create_serialize(
            textsummarize_summarize_request=textsummarize_summarize_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "TextsummarizeResponseModel",
            '400': "BadRequest",
            '500': "Error",
            '403': "Error",
            '404': "NotFoundResponse",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def text_text_summarize_create_without_preload_content(
        self,
        textsummarize_summarize_request: TextsummarizeSummarizeRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Summarize

        <details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**connexun**|-|`v1.0`|2.0 (per 1000 request)|1 request |**microsoft**|-|`v3.1`|2.0 (per 1000000 char)|1000 char |**openai**|-|`v3.0.0`|60.0 (per 1000000 token)|1 token |**openai**|**gpt-4**|`v3.0.0`|60.0 (per 1000000 token)|1 token |**openai**|**gpt-3.5-turbo-1106**|`v3.0.0`|2.0 (per 1000000 token)|1 token |**openai**|**gpt-3.5-turbo**|`v3.0.0`|2.0 (per 1000000 token)|1 token |**openai**|**gpt-3.5-turbo-16k**|`v3.0.0`|4.0 (per 1000000 token)|1 token |**emvista**|-|`v1.0`|1.0 (per 1000000 char)|1000 char |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token |**alephalpha**|-|`1.12.0`|50.0 (per 1000000 char)|1 char |**alephalpha**|**luminous-base**|`1.12.0`|1.0 (per 1000000 char)|1 char |**alephalpha**|**luminous-extended**|`1.12.0`|1.5 (per 1000000 char)|1 char |**alephalpha**|**luminous-supreme**|`1.12.0`|50.0 (per 1000000 char)|1 char |**alephalpha**|**luminous-base-control**|`1.12.0`|1.25 (per 1000000 char)|1 char |**alephalpha**|**luminous-extended-control**|`1.12.0`|1.8 (per 1000000 char)|1 char |**alephalpha**|**luminous-supreme-control**|`1.12.0`|62.5 (per 1000000 char)|1 char |**nlpcloud**|-|`v1`|25.0 (per 1000 request)|1 request |**nlpcloud**|**bart-large-cnn**|`v1`|25.0 (per 1000 request)|1 request |**nlpcloud**|**fast-gpt-j**|`v1`|25.0 (per 1000 request)|1 request |**nlpcloud**|**finetuned-llama-2-70b**|`v1`|25.0 (per 1000 request)|1 request |**nlpcloud**|**chatdolphin**|`v1`|25.0 (per 1000 request)|1 request |**ai21labs**|-|`v1`|0.005 (per 1000 char)|1000 char |**anthropic**|**claude-3-haiku-20240307-v1:0**|`bedrock-2023-05-31`|1.25 (per 1000000 token)|1 token |**anthropic**|**claude-3-sonnet-20240229-v1:0**|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1 token |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token |**anthropic**|-|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1 token   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Abkhazian**|`ab`| |**Acoli**|`ach`| |**Afar**|`aa`| |**Afrikaans**|`af`| |**Akan**|`ak`| |**Albanian**|`sq`| |**American Sign Language**|`ase`| |**Amharic**|`am`| |**Arabic**|`ar`| |**Aragonese**|`an`| |**Argentine Sign Language**|`aed`| |**Armenian**|`hy`| |**Assamese**|`as`| |**Avaric**|`av`| |**Avestan**|`ae`| |**Awadhi**|`awa`| |**Aymara**|`ay`| |**Azerbaijani**|`az`| |**Bambara**|`bm`| |**Bashkir**|`ba`| |**Basque**|`eu`| |**Belarusian**|`be`| |**Bemba (Zambia)**|`bem`| |**Bengali**|`bn`| |**Berber languages**|`ber`| |**Bhojpuri**|`bho`| |**Bihari languages**|`bh`| |**Bislama**|`bi`| |**Bosnian**|`bs`| |**Brazilian Sign Language**|`bzs`| |**Breton**|`br`| |**Bulgarian**|`bg`| |**Burmese**|`my`| |**Catalan**|`ca`| |**Cebuano**|`ceb`| |**Celtic languages**|`cel`| |**Central Bikol**|`bcl`| |**Central Khmer**|`km`| |**Chamorro**|`ch`| |**Chechen**|`ce`| |**Chilean Sign Language**|`csg`| |**Chinese**|`zh`| |**Church Slavic**|`cu`| |**Chuukese**|`chk`| |**Chuvash**|`cv`| |**Colombian Sign Language**|`csn`| |**Congo Swahili**|`swc`| |**Cornish**|`kw`| |**Corsican**|`co`| |**Cree**|`cr`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dhivehi**|`dv`| |**Dogri (macrolanguage)**|`doi`| |**Dutch**|`nl`| |**Dzongkha**|`dz`| |**Efik**|`efi`| |**English**|`en`| |**Esperanto**|`eo`| |**Estonian**|`et`| |**Ewe**|`ee`| |**Faroese**|`fo`| |**Fijian**|`fj`| |**Finnish**|`fi`| |**Finnish Sign Language**|`fse`| |**Fon**|`fon`| |**French**|`fr`| |**Fulah**|`ff`| |**Ga**|`gaa`| |**Galician**|`gl`| |**Ganda**|`lg`| |**Georgian**|`ka`| |**German**|`de`| |**Gilbertese**|`gil`| |**Guarani**|`gn`| |**Gujarati**|`gu`| |**Gun**|`guw`| |**Haitian**|`ht`| |**Hausa**|`ha`| |**Hebrew**|`he`| |**Herero**|`hz`| |**Hiligaynon**|`hil`| |**Hindi**|`hi`| |**Hiri Motu**|`ho`| |**Hungarian**|`hu`| |**Icelandic**|`is`| |**Ido**|`io`| |**Igbo**|`ig`| |**Iloko**|`ilo`| |**Indonesian**|`id`| |**Interlingua (International Auxiliary Language Association)**|`ia`| |**Interlingue**|`ie`| |**Inuktitut**|`iu`| |**Inupiaq**|`ik`| |**Irish**|`ga`| |**Isoko**|`iso`| |**Isthmus Zapotec**|`zai`| |**Italian**|`it`| |**Japanese**|`ja`| |**Javanese**|`jv`| |**Kabyle**|`kab`| |**Kalaallisut**|`kl`| |**Kannada**|`kn`| |**Kanuri**|`kr`| |**Kaonde**|`kqn`| |**Kashmiri**|`ks`| |**Kazakh**|`kk`| |**Kikuyu**|`ki`| |**Kinyarwanda**|`rw`| |**Kirghiz**|`ky`| |**Komi**|`kv`| |**Kongo**|`kg`| |**Konkani (macrolanguage)**|`kok`| |**Korean**|`ko`| |**Kuanyama**|`kj`| |**Kurdish**|`ku`| |**Kwangali**|`kwn`| |**Lao**|`lo`| |**Latin**|`la`| |**Latvian**|`lv`| |**Limburgan**|`li`| |**Lingala**|`ln`| |**Lithuanian**|`lt`| |**Lozi**|`loz`| |**Luba-Katanga**|`lu`| |**Luba-Lulua**|`lua`| |**Lunda**|`lun`| |**Luo (Kenya and Tanzania)**|`luo`| |**Lushai**|`lus`| |**Luvale**|`lue`| |**Luxembourgish**|`lb`| |**Macedonian**|`mk`| |**Maithili**|`mai`| |**Malagasy**|`mg`| |**Malay (macrolanguage)**|`ms`| |**Malayalam**|`ml`| |**Maltese**|`mt`| |**Manx**|`gv`| |**Maori**|`mi`| |**Marathi**|`mr`| |**Marshallese**|`mh`| |**Mexican Sign Language**|`mfs`| |**Min Nan Chinese**|`nan`| |**Modern Greek (1453-)**|`el`| |**Mongolian**|`mn`| |**Morisyen**|`mfe`| |**Mossi**|`mos`| |**Nauru**|`na`| |**Navajo**|`nv`| |**Ndonga**|`ng`| |**Nepali (macrolanguage)**|`ne`| |**Niuean**|`niu`| |**North Ndebele**|`nd`| |**Northern Sami**|`se`| |**Norwegian**|`no`| |**Norwegian Bokmål**|`nb`| |**Norwegian Nynorsk**|`nn`| |**Nyaneka**|`nyk`| |**Nyanja**|`ny`| |**Occitan (post 1500)**|`oc`| |**Ojibwa**|`oj`| |**Oriya (macrolanguage)**|`or`| |**Oromo**|`om`| |**Ossetian**|`os`| |**Pali**|`pi`| |**Pangasinan**|`pag`| |**Panjabi**|`pa`| |**Papiamento**|`pap`| |**Pedi**|`nso`| |**Persian**|`fa`| |**Peruvian Sign Language**|`prl`| |**Pijin**|`pis`| |**Pohnpeian**|`pon`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Pushto**|`ps`| |**Quechua**|`qu`| |**Romance languages**|`roa`| |**Romanian**|`mo`| |**Romanian**|`ro`| |**Romansh**|`rm`| |**Rundi**|`rn`| |**Russian**|`ru`| |**Ruund**|`rnd`| |**Samoan**|`sm`| |**San Salvador Kongo**|`kwy`| |**Sango**|`sg`| |**Sanskrit**|`sa`| |**Santali**|`sat`| |**Sardinian**|`sc`| |**Scottish Gaelic**|`gd`| |**Serbian**|`sr`| |**Seselwa Creole French**|`crs`| |**Shan**|`shn`| |**Shona**|`sn`| |**Sichuan Yi**|`ii`| |**Sicilian**|`scn`| |**Sindhi**|`sd`| |**Sinhala**|`si`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**South Ndebele**|`nr`| |**Southern Sotho**|`st`| |**Spanish**|`es`| |**Spanish Sign Language**|`ssp`| |**Sranan Tongo**|`srn`| |**Sundanese**|`su`| |**Swahili (macrolanguage)**|`sw`| |**Swati**|`ss`| |**Swedish**|`sv`| |**Tagalog**|`tl`| |**Tahitian**|`ty`| |**Tajik**|`tg`| |**Tamil**|`ta`| |**Tatar**|`tt`| |**Telugu**|`te`| |**Tetela**|`tll`| |**Tetun Dili**|`tdt`| |**Thai**|`th`| |**Tibetan**|`bo`| |**Tigrinya**|`ti`| |**Tiv**|`tiv`| |**Tok Pisin**|`tpi`| |**Tonga (Tonga Islands)**|`to`| |**Tonga (Zambia)**|`toi`| |**Tsonga**|`ts`| |**Tswana**|`tn`| |**Tumbuka**|`tum`| |**Turkish**|`tr`| |**Turkmen**|`tk`| |**Tuvalu**|`tvl`| |**Twi**|`tw`| |**Tzotzil**|`tzo`| |**Uighur**|`ug`| |**Ukrainian**|`uk`| |**Umbundu**|`umb`| |**Urdu**|`ur`| |**Uzbek**|`uz`| |**Venda**|`ve`| |**Venezuelan Sign Language**|`vsl`| |**Vietnamese**|`vi`| |**Volapük**|`vo`| |**Wallisian**|`wls`| |**Walloon**|`wa`| |**Waray (Philippines)**|`war`| |**Welsh**|`cy`| |**Western Frisian**|`fy`| |**Wolaytta**|`wal`| |**Wolof**|`wo`| |**Wu Chinese**|`wuu`| |**Xhosa**|`xh`| |**Yapese**|`yap`| |**Yiddish**|`yi`| |**Yoruba**|`yo`| |**Yucateco**|`yua`| |**Yue Chinese**|`yue`| |**Zande (individual language)**|`zne`| |**Zhuang**|`za`| |**Zulu**|`zu`| |**me**|`me`| |**ra**|`ra`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Chinese (Simplified)**|`zh-Hans`| |**Portuguese (Brazil)**|`pt-BR`| |**Portuguese (Brazil)**|`pt-br`| |**Portuguese (Portugal)**|`pt-PT`| |**Portuguese (Portugal)**|`pt-pt`|  </details><details><summary>Supported Models</summary><details><summary>openai</summary>      |Name|Value| |----|-----| |**openai**|`gpt-3.5-turbo`| ||`gpt-3.5-turbo-1106`| ||`gpt-3.5-turbo-16k`| ||`gpt-4`|  </details><details><summary>cohere</summary>      |Name|Value| |----|-----| |**cohere**|`summarize-medium`| ||`summarize-xlarge`|  </details><details><summary>alephalpha</summary>      |Name|Value| |----|-----| |**alephalpha**|`luminous-base`| ||`luminous-base-control`| ||`luminous-extended`| ||`luminous-extended-control`| ||`luminous-supreme`| ||`luminous-supreme-control`|  </details><details><summary>nlpcloud</summary>      |Name|Value| |----|-----| |**nlpcloud**|`bart-large-cnn`| ||`chatdolphin`| ||`fast-gpt-j`| ||`finetuned-llama-2-70b`|  </details><details><summary>anthropic</summary>      |Name|Value| |----|-----| |**anthropic**|`claude-3-sonnet-20240229-v1:0`| ||`claude-instant-v1`| ||`claude-v2`|  </details>  </details>

        :param textsummarize_summarize_request: (required)
        :type textsummarize_summarize_request: TextsummarizeSummarizeRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._text_text_summarize_create_serialize(
            textsummarize_summarize_request=textsummarize_summarize_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "TextsummarizeResponseModel",
            '400': "BadRequest",
            '500': "Error",
            '403': "Error",
            '404': "NotFoundResponse",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _text_text_summarize_create_serialize(
        self,
        textsummarize_summarize_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if textsummarize_summarize_request is not None:
            _body_params = textsummarize_summarize_request


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'FeatureApiAuth'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/text/summarize',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


