# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from openapi_client.models.textspell_check_response_model import (
    TextspellCheckResponseModel,
)
from openapi_client.models.textspell_check_spell_check_request import (
    TextspellCheckSpellCheckRequest,
)

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class SpellCheckApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def text_text_spell_check_create(
        self,
        textspell_check_spell_check_request: TextspellCheckSpellCheckRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> TextspellCheckResponseModel:
        """Spell Check

        <details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**microsoft**|`v7`|0.3 (per 1000 request)|1 request |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token |**prowritingaid**|`v2`|10.0 (per 1000 request)|1 request |**cohere**|`2022-12-06`|2.0 (per 1000000 token)|1 token |**sapling**|`v1`|2.0 (per 1000000 char)|1 char |**nlpcloud**|`v1`|25.0 (per 1000 request)|1 request |**ai21labs**|`v1`|0.0005 (per 1 request)|1 request   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Achinese**|`ace`| |**Afrikaans**|`af`| |**Akan**|`ak`| |**Albanian**|`sq`| |**Amharic**|`am`| |**Arabic**|`ar`| |**Armenian**|`hy`| |**Assamese**|`as`| |**Asturian**|`ast`| |**Awadhi**|`awa`| |**Ayacucho Quechua**|`quy`| |**Azerbaijani**|`az`| |**Balinese**|`ban`| |**Bambara**|`bm`| |**Banjar**|`bjn`| |**Bashkir**|`ba`| |**Basque**|`eu`| |**Belarusian**|`be`| |**Bemba (Zambia)**|`bem`| |**Bengali**|`bn`| |**Bhojpuri**|`bho`| |**Bosnian**|`bs`| |**Buginese**|`bug`| |**Bulgarian**|`bg`| |**Burmese**|`my`| |**Catalan**|`ca`| |**Cebuano**|`ceb`| |**Central Atlas Tamazight**|`tzm`| |**Central Aymara**|`ayr`| |**Central Kanuri**|`knc`| |**Central Khmer**|`km`| |**Central Kurdish**|`ckb`| |**Chhattisgarhi**|`hne`| |**Chinese**|`zh`| |**Chokwe**|`cjk`| |**Corsican**|`co`| |**Crimean Tatar**|`crh`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dutch**|`nl`| |**Dyula**|`dyu`| |**Dzongkha**|`dz`| |**Eastern Yiddish**|`ydd`| |**Egyptian Arabic**|`arz`| |**English**|`en`| |**Esperanto**|`eo`| |**Estonian**|`et`| |**Ewe**|`ee`| |**Faroese**|`fo`| |**Fijian**|`fj`| |**Finnish**|`fi`| |**Fon**|`fon`| |**French**|`fr`| |**Friulian**|`fur`| |**Galician**|`gl`| |**Ganda**|`lg`| |**Georgian**|`ka`| |**German**|`de`| |**Guarani**|`gn`| |**Gujarati**|`gu`| |**Haitian**|`ht`| |**Halh Mongolian**|`khk`| |**Hausa**|`ha`| |**Hawaiian**|`haw`| |**Hebrew**|`he`| |**Hindi**|`hi`| |**Hmong**|`hmn`| |**Hungarian**|`hu`| |**Icelandic**|`is`| |**Igbo**|`ig`| |**Iloko**|`ilo`| |**Indonesian**|`id`| |**Irish**|`ga`| |**Italian**|`it`| |**Japanese**|`ja`| |**Javanese**|`jv`| |**Kabiyè**|`kbp`| |**Kabuverdianu**|`kea`| |**Kabyle**|`kab`| |**Kachin**|`kac`| |**Kamba (Kenya)**|`kam`| |**Kannada**|`kn`| |**Kashmiri**|`ks`| |**Kazakh**|`kk`| |**Kikuyu**|`ki`| |**Kimbundu**|`kmb`| |**Kinyarwanda**|`rw`| |**Kirghiz**|`ky`| |**Kongo**|`kg`| |**Korean**|`ko`| |**Kurdish**|`ku`| |**Lao**|`lo`| |**Latgalian**|`ltg`| |**Latin**|`la`| |**Latvian**|`lv`| |**Ligurian**|`lij`| |**Limburgan**|`li`| |**Lingala**|`ln`| |**Lithuanian**|`lt`| |**Lombard**|`lmo`| |**Luba-Katanga**|`lu`| |**Luo (Kenya and Tanzania)**|`luo`| |**Lushai**|`lus`| |**Luxembourgish**|`lb`| |**Macedonian**|`mk`| |**Magahi**|`mag`| |**Maithili**|`mai`| |**Malagasy**|`mg`| |**Malay (macrolanguage)**|`ms`| |**Malayalam**|`ml`| |**Maltese**|`mt`| |**Manipuri**|`mni`| |**Maori**|`mi`| |**Marathi**|`mr`| |**Mesopotamian Arabic**|`acm`| |**Minangkabau**|`min`| |**Modern Greek (1453-)**|`el`| |**Mongolian**|`mn`| |**Moroccan Arabic**|`ary`| |**Mossi**|`mos`| |**Najdi Arabic**|`ars`| |**Nepali (macrolanguage)**|`ne`| |**Nigerian Fulfulde**|`fuv`| |**North Azerbaijani**|`azj`| |**North Levantine Arabic**|`apc`| |**Northern Kurdish**|`kmr`| |**Northern Uzbek**|`uzn`| |**Norwegian**|`no`| |**Norwegian Bokmål**|`nb`| |**Norwegian Nynorsk**|`nn`| |**Nuer**|`nus`| |**Nyanja**|`ny`| |**Occitan (post 1500)**|`oc`| |**Oriya (macrolanguage)**|`or`| |**Pangasinan**|`pag`| |**Panjabi**|`pa`| |**Papiamento**|`pap`| |**Pedi**|`nso`| |**Persian**|`fa`| |**Plateau Malagasy**|`plt`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Pushto**|`ps`| |**Romanian**|`ro`| |**Rundi**|`rn`| |**Russian**|`ru`| |**Samoan**|`sm`| |**Sango**|`sg`| |**Sanskrit**|`sa`| |**Santali**|`sat`| |**Sardinian**|`sc`| |**Scottish Gaelic**|`gd`| |**Serbian**|`sr`| |**Shan**|`shn`| |**Shona**|`sn`| |**Sicilian**|`scn`| |**Silesian**|`szl`| |**Sindhi**|`sd`| |**Sinhala**|`si`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**South Azerbaijani**|`azb`| |**South Levantine Arabic**|`ajp`| |**Southern Pashto**|`pbt`| |**Southern Sotho**|`st`| |**Southwestern Dinka**|`dik`| |**Spanish**|`es`| |**Standard Latvian**|`lvs`| |**Standard Malay**|`zsm`| |**Sundanese**|`su`| |**Swahili (macrolanguage)**|`sw`| |**Swati**|`ss`| |**Swedish**|`sv`| |**Ta'izzi-Adeni Arabic**|`acq`| |**Tagalog**|`tl`| |**Tajik**|`tg`| |**Tamashek**|`tmh`| |**Tamil**|`ta`| |**Tatar**|`tt`| |**Telugu**|`te`| |**Thai**|`th`| |**Tibetan**|`bo`| |**Tigrinya**|`ti`| |**Tok Pisin**|`tpi`| |**Tosk Albanian**|`als`| |**Tsonga**|`ts`| |**Tswana**|`tn`| |**Tumbuka**|`tum`| |**Tunisian Arabic**|`aeb`| |**Turkish**|`tr`| |**Turkmen**|`tk`| |**Twi**|`tw`| |**Uighur**|`ug`| |**Ukrainian**|`uk`| |**Umbundu**|`umb`| |**Urdu**|`ur`| |**Uzbek**|`uz`| |**Venetian**|`vec`| |**Vietnamese**|`vi`| |**Waray (Philippines)**|`war`| |**Welsh**|`cy`| |**West Central Oromo**|`gaz`| |**Western Frisian**|`fy`| |**Wolof**|`wo`| |**Xhosa**|`xh`| |**Yiddish**|`yi`| |**Yoruba**|`yo`| |**Yue Chinese**|`yue`| |**Zulu**|`zu`| |**jp**|`jp`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Arabic (world)**|`ar-001`| |**Chinese (China)**|`zh-CN`| |**Chinese (Simplified)**|`zh-hans`| |**Chinese (Taiwan)**|`zh-TW`| |**Chinese (Traditional)**|`zh-Hant`| |**Chinese (Traditional)**|`zh-hant`| |**English (United Kingdom)**|`en-gb`| |**Persian (Afghanistan)**|`fa-AF`| |**Portuguese (Brazil)**|`pt-br`| |**Portuguese (Portugal)**|`pt-pt`|  </details>

        :param textspell_check_spell_check_request: (required)
        :type textspell_check_spell_check_request: TextspellCheckSpellCheckRequest
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
        """  # noqa: E501

        _param = self._text_text_spell_check_create_serialize(
            textspell_check_spell_check_request=textspell_check_spell_check_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "TextspellCheckResponseModel",
            "400": "BadRequest",
            "500": "Error",
            "403": "Error",
            "404": "NotFoundResponse",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def text_text_spell_check_create_with_http_info(
        self,
        textspell_check_spell_check_request: TextspellCheckSpellCheckRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[TextspellCheckResponseModel]:
        """Spell Check

        <details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**microsoft**|`v7`|0.3 (per 1000 request)|1 request |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token |**prowritingaid**|`v2`|10.0 (per 1000 request)|1 request |**cohere**|`2022-12-06`|2.0 (per 1000000 token)|1 token |**sapling**|`v1`|2.0 (per 1000000 char)|1 char |**nlpcloud**|`v1`|25.0 (per 1000 request)|1 request |**ai21labs**|`v1`|0.0005 (per 1 request)|1 request   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Achinese**|`ace`| |**Afrikaans**|`af`| |**Akan**|`ak`| |**Albanian**|`sq`| |**Amharic**|`am`| |**Arabic**|`ar`| |**Armenian**|`hy`| |**Assamese**|`as`| |**Asturian**|`ast`| |**Awadhi**|`awa`| |**Ayacucho Quechua**|`quy`| |**Azerbaijani**|`az`| |**Balinese**|`ban`| |**Bambara**|`bm`| |**Banjar**|`bjn`| |**Bashkir**|`ba`| |**Basque**|`eu`| |**Belarusian**|`be`| |**Bemba (Zambia)**|`bem`| |**Bengali**|`bn`| |**Bhojpuri**|`bho`| |**Bosnian**|`bs`| |**Buginese**|`bug`| |**Bulgarian**|`bg`| |**Burmese**|`my`| |**Catalan**|`ca`| |**Cebuano**|`ceb`| |**Central Atlas Tamazight**|`tzm`| |**Central Aymara**|`ayr`| |**Central Kanuri**|`knc`| |**Central Khmer**|`km`| |**Central Kurdish**|`ckb`| |**Chhattisgarhi**|`hne`| |**Chinese**|`zh`| |**Chokwe**|`cjk`| |**Corsican**|`co`| |**Crimean Tatar**|`crh`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dutch**|`nl`| |**Dyula**|`dyu`| |**Dzongkha**|`dz`| |**Eastern Yiddish**|`ydd`| |**Egyptian Arabic**|`arz`| |**English**|`en`| |**Esperanto**|`eo`| |**Estonian**|`et`| |**Ewe**|`ee`| |**Faroese**|`fo`| |**Fijian**|`fj`| |**Finnish**|`fi`| |**Fon**|`fon`| |**French**|`fr`| |**Friulian**|`fur`| |**Galician**|`gl`| |**Ganda**|`lg`| |**Georgian**|`ka`| |**German**|`de`| |**Guarani**|`gn`| |**Gujarati**|`gu`| |**Haitian**|`ht`| |**Halh Mongolian**|`khk`| |**Hausa**|`ha`| |**Hawaiian**|`haw`| |**Hebrew**|`he`| |**Hindi**|`hi`| |**Hmong**|`hmn`| |**Hungarian**|`hu`| |**Icelandic**|`is`| |**Igbo**|`ig`| |**Iloko**|`ilo`| |**Indonesian**|`id`| |**Irish**|`ga`| |**Italian**|`it`| |**Japanese**|`ja`| |**Javanese**|`jv`| |**Kabiyè**|`kbp`| |**Kabuverdianu**|`kea`| |**Kabyle**|`kab`| |**Kachin**|`kac`| |**Kamba (Kenya)**|`kam`| |**Kannada**|`kn`| |**Kashmiri**|`ks`| |**Kazakh**|`kk`| |**Kikuyu**|`ki`| |**Kimbundu**|`kmb`| |**Kinyarwanda**|`rw`| |**Kirghiz**|`ky`| |**Kongo**|`kg`| |**Korean**|`ko`| |**Kurdish**|`ku`| |**Lao**|`lo`| |**Latgalian**|`ltg`| |**Latin**|`la`| |**Latvian**|`lv`| |**Ligurian**|`lij`| |**Limburgan**|`li`| |**Lingala**|`ln`| |**Lithuanian**|`lt`| |**Lombard**|`lmo`| |**Luba-Katanga**|`lu`| |**Luo (Kenya and Tanzania)**|`luo`| |**Lushai**|`lus`| |**Luxembourgish**|`lb`| |**Macedonian**|`mk`| |**Magahi**|`mag`| |**Maithili**|`mai`| |**Malagasy**|`mg`| |**Malay (macrolanguage)**|`ms`| |**Malayalam**|`ml`| |**Maltese**|`mt`| |**Manipuri**|`mni`| |**Maori**|`mi`| |**Marathi**|`mr`| |**Mesopotamian Arabic**|`acm`| |**Minangkabau**|`min`| |**Modern Greek (1453-)**|`el`| |**Mongolian**|`mn`| |**Moroccan Arabic**|`ary`| |**Mossi**|`mos`| |**Najdi Arabic**|`ars`| |**Nepali (macrolanguage)**|`ne`| |**Nigerian Fulfulde**|`fuv`| |**North Azerbaijani**|`azj`| |**North Levantine Arabic**|`apc`| |**Northern Kurdish**|`kmr`| |**Northern Uzbek**|`uzn`| |**Norwegian**|`no`| |**Norwegian Bokmål**|`nb`| |**Norwegian Nynorsk**|`nn`| |**Nuer**|`nus`| |**Nyanja**|`ny`| |**Occitan (post 1500)**|`oc`| |**Oriya (macrolanguage)**|`or`| |**Pangasinan**|`pag`| |**Panjabi**|`pa`| |**Papiamento**|`pap`| |**Pedi**|`nso`| |**Persian**|`fa`| |**Plateau Malagasy**|`plt`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Pushto**|`ps`| |**Romanian**|`ro`| |**Rundi**|`rn`| |**Russian**|`ru`| |**Samoan**|`sm`| |**Sango**|`sg`| |**Sanskrit**|`sa`| |**Santali**|`sat`| |**Sardinian**|`sc`| |**Scottish Gaelic**|`gd`| |**Serbian**|`sr`| |**Shan**|`shn`| |**Shona**|`sn`| |**Sicilian**|`scn`| |**Silesian**|`szl`| |**Sindhi**|`sd`| |**Sinhala**|`si`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**South Azerbaijani**|`azb`| |**South Levantine Arabic**|`ajp`| |**Southern Pashto**|`pbt`| |**Southern Sotho**|`st`| |**Southwestern Dinka**|`dik`| |**Spanish**|`es`| |**Standard Latvian**|`lvs`| |**Standard Malay**|`zsm`| |**Sundanese**|`su`| |**Swahili (macrolanguage)**|`sw`| |**Swati**|`ss`| |**Swedish**|`sv`| |**Ta'izzi-Adeni Arabic**|`acq`| |**Tagalog**|`tl`| |**Tajik**|`tg`| |**Tamashek**|`tmh`| |**Tamil**|`ta`| |**Tatar**|`tt`| |**Telugu**|`te`| |**Thai**|`th`| |**Tibetan**|`bo`| |**Tigrinya**|`ti`| |**Tok Pisin**|`tpi`| |**Tosk Albanian**|`als`| |**Tsonga**|`ts`| |**Tswana**|`tn`| |**Tumbuka**|`tum`| |**Tunisian Arabic**|`aeb`| |**Turkish**|`tr`| |**Turkmen**|`tk`| |**Twi**|`tw`| |**Uighur**|`ug`| |**Ukrainian**|`uk`| |**Umbundu**|`umb`| |**Urdu**|`ur`| |**Uzbek**|`uz`| |**Venetian**|`vec`| |**Vietnamese**|`vi`| |**Waray (Philippines)**|`war`| |**Welsh**|`cy`| |**West Central Oromo**|`gaz`| |**Western Frisian**|`fy`| |**Wolof**|`wo`| |**Xhosa**|`xh`| |**Yiddish**|`yi`| |**Yoruba**|`yo`| |**Yue Chinese**|`yue`| |**Zulu**|`zu`| |**jp**|`jp`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Arabic (world)**|`ar-001`| |**Chinese (China)**|`zh-CN`| |**Chinese (Simplified)**|`zh-hans`| |**Chinese (Taiwan)**|`zh-TW`| |**Chinese (Traditional)**|`zh-Hant`| |**Chinese (Traditional)**|`zh-hant`| |**English (United Kingdom)**|`en-gb`| |**Persian (Afghanistan)**|`fa-AF`| |**Portuguese (Brazil)**|`pt-br`| |**Portuguese (Portugal)**|`pt-pt`|  </details>

        :param textspell_check_spell_check_request: (required)
        :type textspell_check_spell_check_request: TextspellCheckSpellCheckRequest
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
        """  # noqa: E501

        _param = self._text_text_spell_check_create_serialize(
            textspell_check_spell_check_request=textspell_check_spell_check_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "TextspellCheckResponseModel",
            "400": "BadRequest",
            "500": "Error",
            "403": "Error",
            "404": "NotFoundResponse",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def text_text_spell_check_create_without_preload_content(
        self,
        textspell_check_spell_check_request: TextspellCheckSpellCheckRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Spell Check

        <details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**microsoft**|`v7`|0.3 (per 1000 request)|1 request |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token |**prowritingaid**|`v2`|10.0 (per 1000 request)|1 request |**cohere**|`2022-12-06`|2.0 (per 1000000 token)|1 token |**sapling**|`v1`|2.0 (per 1000000 char)|1 char |**nlpcloud**|`v1`|25.0 (per 1000 request)|1 request |**ai21labs**|`v1`|0.0005 (per 1 request)|1 request   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Achinese**|`ace`| |**Afrikaans**|`af`| |**Akan**|`ak`| |**Albanian**|`sq`| |**Amharic**|`am`| |**Arabic**|`ar`| |**Armenian**|`hy`| |**Assamese**|`as`| |**Asturian**|`ast`| |**Awadhi**|`awa`| |**Ayacucho Quechua**|`quy`| |**Azerbaijani**|`az`| |**Balinese**|`ban`| |**Bambara**|`bm`| |**Banjar**|`bjn`| |**Bashkir**|`ba`| |**Basque**|`eu`| |**Belarusian**|`be`| |**Bemba (Zambia)**|`bem`| |**Bengali**|`bn`| |**Bhojpuri**|`bho`| |**Bosnian**|`bs`| |**Buginese**|`bug`| |**Bulgarian**|`bg`| |**Burmese**|`my`| |**Catalan**|`ca`| |**Cebuano**|`ceb`| |**Central Atlas Tamazight**|`tzm`| |**Central Aymara**|`ayr`| |**Central Kanuri**|`knc`| |**Central Khmer**|`km`| |**Central Kurdish**|`ckb`| |**Chhattisgarhi**|`hne`| |**Chinese**|`zh`| |**Chokwe**|`cjk`| |**Corsican**|`co`| |**Crimean Tatar**|`crh`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dutch**|`nl`| |**Dyula**|`dyu`| |**Dzongkha**|`dz`| |**Eastern Yiddish**|`ydd`| |**Egyptian Arabic**|`arz`| |**English**|`en`| |**Esperanto**|`eo`| |**Estonian**|`et`| |**Ewe**|`ee`| |**Faroese**|`fo`| |**Fijian**|`fj`| |**Finnish**|`fi`| |**Fon**|`fon`| |**French**|`fr`| |**Friulian**|`fur`| |**Galician**|`gl`| |**Ganda**|`lg`| |**Georgian**|`ka`| |**German**|`de`| |**Guarani**|`gn`| |**Gujarati**|`gu`| |**Haitian**|`ht`| |**Halh Mongolian**|`khk`| |**Hausa**|`ha`| |**Hawaiian**|`haw`| |**Hebrew**|`he`| |**Hindi**|`hi`| |**Hmong**|`hmn`| |**Hungarian**|`hu`| |**Icelandic**|`is`| |**Igbo**|`ig`| |**Iloko**|`ilo`| |**Indonesian**|`id`| |**Irish**|`ga`| |**Italian**|`it`| |**Japanese**|`ja`| |**Javanese**|`jv`| |**Kabiyè**|`kbp`| |**Kabuverdianu**|`kea`| |**Kabyle**|`kab`| |**Kachin**|`kac`| |**Kamba (Kenya)**|`kam`| |**Kannada**|`kn`| |**Kashmiri**|`ks`| |**Kazakh**|`kk`| |**Kikuyu**|`ki`| |**Kimbundu**|`kmb`| |**Kinyarwanda**|`rw`| |**Kirghiz**|`ky`| |**Kongo**|`kg`| |**Korean**|`ko`| |**Kurdish**|`ku`| |**Lao**|`lo`| |**Latgalian**|`ltg`| |**Latin**|`la`| |**Latvian**|`lv`| |**Ligurian**|`lij`| |**Limburgan**|`li`| |**Lingala**|`ln`| |**Lithuanian**|`lt`| |**Lombard**|`lmo`| |**Luba-Katanga**|`lu`| |**Luo (Kenya and Tanzania)**|`luo`| |**Lushai**|`lus`| |**Luxembourgish**|`lb`| |**Macedonian**|`mk`| |**Magahi**|`mag`| |**Maithili**|`mai`| |**Malagasy**|`mg`| |**Malay (macrolanguage)**|`ms`| |**Malayalam**|`ml`| |**Maltese**|`mt`| |**Manipuri**|`mni`| |**Maori**|`mi`| |**Marathi**|`mr`| |**Mesopotamian Arabic**|`acm`| |**Minangkabau**|`min`| |**Modern Greek (1453-)**|`el`| |**Mongolian**|`mn`| |**Moroccan Arabic**|`ary`| |**Mossi**|`mos`| |**Najdi Arabic**|`ars`| |**Nepali (macrolanguage)**|`ne`| |**Nigerian Fulfulde**|`fuv`| |**North Azerbaijani**|`azj`| |**North Levantine Arabic**|`apc`| |**Northern Kurdish**|`kmr`| |**Northern Uzbek**|`uzn`| |**Norwegian**|`no`| |**Norwegian Bokmål**|`nb`| |**Norwegian Nynorsk**|`nn`| |**Nuer**|`nus`| |**Nyanja**|`ny`| |**Occitan (post 1500)**|`oc`| |**Oriya (macrolanguage)**|`or`| |**Pangasinan**|`pag`| |**Panjabi**|`pa`| |**Papiamento**|`pap`| |**Pedi**|`nso`| |**Persian**|`fa`| |**Plateau Malagasy**|`plt`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Pushto**|`ps`| |**Romanian**|`ro`| |**Rundi**|`rn`| |**Russian**|`ru`| |**Samoan**|`sm`| |**Sango**|`sg`| |**Sanskrit**|`sa`| |**Santali**|`sat`| |**Sardinian**|`sc`| |**Scottish Gaelic**|`gd`| |**Serbian**|`sr`| |**Shan**|`shn`| |**Shona**|`sn`| |**Sicilian**|`scn`| |**Silesian**|`szl`| |**Sindhi**|`sd`| |**Sinhala**|`si`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**South Azerbaijani**|`azb`| |**South Levantine Arabic**|`ajp`| |**Southern Pashto**|`pbt`| |**Southern Sotho**|`st`| |**Southwestern Dinka**|`dik`| |**Spanish**|`es`| |**Standard Latvian**|`lvs`| |**Standard Malay**|`zsm`| |**Sundanese**|`su`| |**Swahili (macrolanguage)**|`sw`| |**Swati**|`ss`| |**Swedish**|`sv`| |**Ta'izzi-Adeni Arabic**|`acq`| |**Tagalog**|`tl`| |**Tajik**|`tg`| |**Tamashek**|`tmh`| |**Tamil**|`ta`| |**Tatar**|`tt`| |**Telugu**|`te`| |**Thai**|`th`| |**Tibetan**|`bo`| |**Tigrinya**|`ti`| |**Tok Pisin**|`tpi`| |**Tosk Albanian**|`als`| |**Tsonga**|`ts`| |**Tswana**|`tn`| |**Tumbuka**|`tum`| |**Tunisian Arabic**|`aeb`| |**Turkish**|`tr`| |**Turkmen**|`tk`| |**Twi**|`tw`| |**Uighur**|`ug`| |**Ukrainian**|`uk`| |**Umbundu**|`umb`| |**Urdu**|`ur`| |**Uzbek**|`uz`| |**Venetian**|`vec`| |**Vietnamese**|`vi`| |**Waray (Philippines)**|`war`| |**Welsh**|`cy`| |**West Central Oromo**|`gaz`| |**Western Frisian**|`fy`| |**Wolof**|`wo`| |**Xhosa**|`xh`| |**Yiddish**|`yi`| |**Yoruba**|`yo`| |**Yue Chinese**|`yue`| |**Zulu**|`zu`| |**jp**|`jp`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Arabic (world)**|`ar-001`| |**Chinese (China)**|`zh-CN`| |**Chinese (Simplified)**|`zh-hans`| |**Chinese (Taiwan)**|`zh-TW`| |**Chinese (Traditional)**|`zh-Hant`| |**Chinese (Traditional)**|`zh-hant`| |**English (United Kingdom)**|`en-gb`| |**Persian (Afghanistan)**|`fa-AF`| |**Portuguese (Brazil)**|`pt-br`| |**Portuguese (Portugal)**|`pt-pt`|  </details>

        :param textspell_check_spell_check_request: (required)
        :type textspell_check_spell_check_request: TextspellCheckSpellCheckRequest
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
        """  # noqa: E501

        _param = self._text_text_spell_check_create_serialize(
            textspell_check_spell_check_request=textspell_check_spell_check_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "TextspellCheckResponseModel",
            "400": "BadRequest",
            "500": "Error",
            "403": "Error",
            "404": "NotFoundResponse",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _text_text_spell_check_create_serialize(
        self,
        textspell_check_spell_check_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

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
        if textspell_check_spell_check_request is not None:
            _body_params = textspell_check_spell_check_request

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = ["FeatureApiAuth"]

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/text/spell_check",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )
