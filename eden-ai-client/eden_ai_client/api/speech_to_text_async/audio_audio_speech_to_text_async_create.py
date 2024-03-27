from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.launch_async_job_response import LaunchAsyncJobResponse
from ...models.speech_to_text_async_request import SpeechToTextAsyncRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        SpeechToTextAsyncRequest,
        SpeechToTextAsyncRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/audio/speech_to_text_async",
    }

    if isinstance(body, SpeechToTextAsyncRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"
    if isinstance(body, SpeechToTextAsyncRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[LaunchAsyncJobResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LaunchAsyncJobResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[LaunchAsyncJobResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        SpeechToTextAsyncRequest,
        SpeechToTextAsyncRequest,
    ],
) -> Response[LaunchAsyncJobResponse]:
    """Speech to Text Launch Job

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**amazon**|-|`boto3 (v1.15.18)`|0.024 (per 60 seconde)|15 seconde
    |**google**|-|`v1p1beta1`|0.024 (per 60 seconde)|1 seconde
    |**ibm**|-|`v1`|0.02 (per 60 seconde)|1 seconde
    |**microsoft**|-|`v1.0`|0.0168 (per 60 seconde)|1 seconde
    |**revai**|-|`v1`|0.02 (per 60 seconde)|15 seconde
    |**symbl**|-|`v1`|0.027 (per 60 seconde)|60 seconde
    |**voci**|-|`v1`|0.0162 (per 60 seconde)|1 seconde
    |**neuralspace**|-|`v1`|0.024 (per 60 seconde)|60 seconde
    |**assembly**|-|`v2`|0.011 (per 60 seconde)|1 seconde
    |**deepgram**|**enhanced**|`v1`|0.0189 (per 60 seconde)|1 seconde
    |**deepgram**|-|`v1`|0.0189 (per 60 seconde)|1 seconde
    |**deepgram**|**base**|`v1`|0.0169 (per 60 seconde)|1 seconde
    |**openai**|-|`boto3 (v1.15.18)`|0.006 (per 60 seconde)|1 seconde
    |**speechmatics**|**enhanced**|`v2`|0.022 (per 60 seconde)|1 seconde
    |**speechmatics**|**standard**|`v2`|0.017 (per 60 seconde)|1 seconde
    |**speechmatics**|-|`v2`|0.022 (per 60 seconde)|1 seconde
    |**gladia**|-|`v1`|0.0102 (per 60 seconde)|1 seconde


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Armenian**|`hy`|
    |**Azerbaijani**|`az`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bengali**|`bn`|
    |**Bosnian**|`bs`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Central Khmer**|`km`|
    |**Chinese**|`zh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hebrew**|`he`|
    |**Hebrew**|`iw`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Indonesian**|`id`|
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kannada**|`kn`|
    |**Kazakh**|`kk`|
    |**Korean**|`ko`|
    |**Lao**|`lo`|
    |**Latvian**|`lv`|
    |**Lingala**|`ln`|
    |**Lithuanian**|`lt`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Mandarin Chinese**|`cmn`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Occitan (post 1500)**|`oc`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Romanian**|`mo`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Serbian**|`sr`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**Spanish**|`es`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tamil**|`ta`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Turkish**|`tr`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Welsh**|`cy`|
    |**Wu Chinese**|`wuu`|
    |**Yiddish**|`yi`|
    |**Yoruba**|`yo`|
    |**Yue Chinese**|`yue`|
    |**Zulu**|`zu`|
    |**at**|`at`|
    |**jp**|`jp`|
    |**mymr**|`mymr`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Afrikaans (South Africa)**|`af-ZA`|
    |**Albanian (Albania)**|`sq-AL`|
    |**Amharic (Ethiopia)**|`am-ET`|
    |**Arabic (Algeria)**|`ar-DZ`|
    |**Arabic (Bahrain)**|`ar-BH`|
    |**Arabic (Egypt)**|`ar-EG`|
    |**Arabic (Iraq)**|`ar-IQ`|
    |**Arabic (Israel)**|`ar-IL`|
    |**Arabic (Jordan)**|`ar-JO`|
    |**Arabic (Kuwait)**|`ar-KW`|
    |**Arabic (Lebanon)**|`ar-LB`|
    |**Arabic (Libya)**|`ar-LY`|
    |**Arabic (Mauritania)**|`ar-MR`|
    |**Arabic (Montserrat)**|`ar-MS`|
    |**Arabic (Morocco)**|`ar-MA`|
    |**Arabic (Oman)**|`ar-OM`|
    |**Arabic (Palestinian Territories)**|`ar-PS`|
    |**Arabic (Qatar)**|`ar-QA`|
    |**Arabic (Saudi Arabia)**|`ar-SA`|
    |**Arabic (Syria)**|`ar-SY`|
    |**Arabic (Tunisia)**|`ar-TN`|
    |**Arabic (United Arab Emirates)**|`ar-AE`|
    |**Arabic (Yemen)**|`ar-YE`|
    |**Armenian (Armenia)**|`hy-AM`|
    |**Azerbaijani (Azerbaijan)**|`az-AZ`|
    |**Bangla (Bangladesh)**|`bn-BD`|
    |**Bangla (India)**|`bn-IN`|
    |**Basque (Spain)**|`eu-ES`|
    |**Bosnian (Bosnia & Herzegovina)**|`bs-BA`|
    |**Bulgarian (Bulgaria)**|`bg-BG`|
    |**Burmese (Myanmar (Burma))**|`my-MM`|
    |**Cantonese (China)**|`yue-CN`|
    |**Cantonese (Traditional, Hong Kong SAR China)**|`yue-Hant-HK`|
    |**Catalan (Spain)**|`ca-ES`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (Hong Kong SAR China)**|`zh-HK`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Croatian (Croatia)**|`hr-HR`|
    |**Czech (Czechia)**|`cs-CZ`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Belgium)**|`nl-BE`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (Australia)**|`en-AU`|
    |**English (Canada)**|`en-CA`|
    |**English (Ghana)**|`en-GH`|
    |**English (Hong Kong SAR China)**|`en-HK`|
    |**English (India)**|`en-IN`|
    |**English (Ireland)**|`en-IE`|
    |**English (Kenya)**|`en-KE`|
    |**English (New Zealand)**|`en-NZ`|
    |**English (Nigeria)**|`en-NG`|
    |**English (Pakistan)**|`en-PK`|
    |**English (Philippines)**|`en-PH`|
    |**English (Singapore)**|`en-SG`|
    |**English (South Africa)**|`en-ZA`|
    |**English (Tanzania)**|`en-TZ`|
    |**English (United Kingdom)**|`en-GB`|
    |**English (United Kingdom)**|`en-UK`|
    |**English (United States)**|`en-US`|
    |**Estonian (Estonia)**|`et-EE`|
    |**Filipino (Philippines)**|`fil-PH`|
    |**Finnish (Finland)**|`fi-FI`|
    |**French (Belgium)**|`fr-BE`|
    |**French (Canada)**|`fr-CA`|
    |**French (France)**|`fr-FR`|
    |**French (Switzerland)**|`fr-CH`|
    |**Galician (Spain)**|`gl-ES`|
    |**Georgian (Georgia)**|`ka-GE`|
    |**German (Austria)**|`de-AT`|
    |**German (Germany)**|`de-DE`|
    |**German (Switzerland)**|`de-CH`|
    |**Greek (Greece)**|`el-GR`|
    |**Gujarati (India)**|`gu-IN`|
    |**Hebrew (Israel)**|`he-IL`|
    |**Hebrew (Israel)**|`iw-IL`|
    |**Hindi (India)**|`hi-IN`|
    |**Hindi (Latin)**|`hi-Latn`|
    |**Hungarian (Hungary)**|`hu-HU`|
    |**Icelandic (Iceland)**|`is-IS`|
    |**Indonesian (Indonesia)**|`id-ID`|
    |**Irish (Ireland)**|`ga-IE`|
    |**Italian (Italy)**|`it-IT`|
    |**Italian (Switzerland)**|`it-CH`|
    |**Japanese (Japan)**|`ja-JP`|
    |**Javanese (Indonesia)**|`jv-ID`|
    |**Kannada (India)**|`kn-IN`|
    |**Kazakh (Kazakhstan)**|`kk-KZ`|
    |**Khmer (Cambodia)**|`km-KH`|
    |**Korean (South Korea)**|`ko-KR`|
    |**Lao (Laos)**|`lo-LA`|
    |**Latvian (Latvia)**|`lv-LV`|
    |**Lithuanian (Lithuania)**|`lt-LT`|
    |**Macedonian (North Macedonia)**|`mk-MK`|
    |**Malay (Malaysia)**|`ms-MY`|
    |**Malayalam (India)**|`ml-IN`|
    |**Maltese (Malta)**|`mt-MT`|
    |**Marathi (India)**|`mr-IN`|
    |**Mongolian (Mongolia)**|`mn-MN`|
    |**Nepali (Nepal)**|`ne-NP`|
    |**Norwegian (Norway)**|`no-NO`|
    |**Norwegian Bokmål (Norway)**|`nb-NO`|
    |**Pashto (Afghanistan)**|`ps-AF`|
    |**Persian (Iran)**|`fa-IR`|
    |**Polish (Poland)**|`pl-PL`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Punjabi (India)**|`pa-Guru-IN`|
    |**Romanian (Romania)**|`ro-RO`|
    |**Russian (Russia)**|`ru-RU`|
    |**Serbian (Serbia)**|`sr-RS`|
    |**Sinhala (Sri Lanka)**|`si-LK`|
    |**Slovak (Slovakia)**|`sk-SK`|
    |**Slovenian (Slovenia)**|`sl-SI`|
    |**Somali (Somalia)**|`so-SO`|
    |**Spanish (Argentina)**|`es-AR`|
    |**Spanish (Bolivia)**|`es-BO`|
    |**Spanish (Chile)**|`es-CL`|
    |**Spanish (Colombia)**|`es-CO`|
    |**Spanish (Costa Rica)**|`es-CR`|
    |**Spanish (Cuba)**|`es-CU`|
    |**Spanish (Dominican Republic)**|`es-DO`|
    |**Spanish (Ecuador)**|`es-EC`|
    |**Spanish (El Salvador)**|`es-SV`|
    |**Spanish (Equatorial Guinea)**|`es-GQ`|
    |**Spanish (Guatemala)**|`es-GT`|
    |**Spanish (Honduras)**|`es-HN`|
    |**Spanish (Laos)**|`es-LA`|
    |**Spanish (Latin America)**|`es-419`|
    |**Spanish (Mexico)**|`es-MX`|
    |**Spanish (Nicaragua)**|`es-NI`|
    |**Spanish (Panama)**|`es-PA`|
    |**Spanish (Paraguay)**|`es-PY`|
    |**Spanish (Peru)**|`es-PE`|
    |**Spanish (Puerto Rico)**|`es-PR`|
    |**Spanish (Spain)**|`es-ES`|
    |**Spanish (United States)**|`es-US`|
    |**Spanish (Uruguay)**|`es-UY`|
    |**Spanish (Venezuela)**|`es-VE`|
    |**Sundanese (Indonesia)**|`su-ID`|
    |**Swahili (Kenya)**|`sw-KE`|
    |**Swahili (Tanzania)**|`sw-TZ`|
    |**Swedish (Sweden)**|`sv-SE`|
    |**Tamil (India)**|`ta-IN`|
    |**Tamil (Malaysia)**|`ta-MY`|
    |**Tamil (Singapore)**|`ta-SG`|
    |**Tamil (Sri Lanka)**|`ta-LK`|
    |**Telugu (India)**|`te-IN`|
    |**Thai (Thailand)**|`th-TH`|
    |**Turkish (Turkey)**|`tr-TR`|
    |**Ukrainian (Ukraine)**|`uk-UA`|
    |**Urdu (India)**|`ur-IN`|
    |**Urdu (Pakistan)**|`ur-PK`|
    |**Uzbek (Uzbekistan)**|`uz-UZ`|
    |**Vietnamese (Vietnam)**|`vi-VN`|
    |**Welsh (United Kingdom)**|`cy-GB`|
    |**Wu Chinese (China)**|`wuu-CN`|
    |**Zulu (South Africa)**|`zu-ZA`|

    </details><details><summary>Supported Models</summary><details><summary>deepgram</summary>





    |Name|Value|
    |----|-----|
    |**deepgram**|`base`|
    ||`enhanced`|

    </details><details><summary>speechmatics</summary>





    |Name|Value|
    |----|-----|
    |**speechmatics**|`enhanced`|
    ||`standard`|

    </details>

    </details>

    Args:
        body (SpeechToTextAsyncRequest):
        body (SpeechToTextAsyncRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LaunchAsyncJobResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        SpeechToTextAsyncRequest,
        SpeechToTextAsyncRequest,
    ],
) -> Optional[LaunchAsyncJobResponse]:
    """Speech to Text Launch Job

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**amazon**|-|`boto3 (v1.15.18)`|0.024 (per 60 seconde)|15 seconde
    |**google**|-|`v1p1beta1`|0.024 (per 60 seconde)|1 seconde
    |**ibm**|-|`v1`|0.02 (per 60 seconde)|1 seconde
    |**microsoft**|-|`v1.0`|0.0168 (per 60 seconde)|1 seconde
    |**revai**|-|`v1`|0.02 (per 60 seconde)|15 seconde
    |**symbl**|-|`v1`|0.027 (per 60 seconde)|60 seconde
    |**voci**|-|`v1`|0.0162 (per 60 seconde)|1 seconde
    |**neuralspace**|-|`v1`|0.024 (per 60 seconde)|60 seconde
    |**assembly**|-|`v2`|0.011 (per 60 seconde)|1 seconde
    |**deepgram**|**enhanced**|`v1`|0.0189 (per 60 seconde)|1 seconde
    |**deepgram**|-|`v1`|0.0189 (per 60 seconde)|1 seconde
    |**deepgram**|**base**|`v1`|0.0169 (per 60 seconde)|1 seconde
    |**openai**|-|`boto3 (v1.15.18)`|0.006 (per 60 seconde)|1 seconde
    |**speechmatics**|**enhanced**|`v2`|0.022 (per 60 seconde)|1 seconde
    |**speechmatics**|**standard**|`v2`|0.017 (per 60 seconde)|1 seconde
    |**speechmatics**|-|`v2`|0.022 (per 60 seconde)|1 seconde
    |**gladia**|-|`v1`|0.0102 (per 60 seconde)|1 seconde


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Armenian**|`hy`|
    |**Azerbaijani**|`az`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bengali**|`bn`|
    |**Bosnian**|`bs`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Central Khmer**|`km`|
    |**Chinese**|`zh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hebrew**|`he`|
    |**Hebrew**|`iw`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Indonesian**|`id`|
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kannada**|`kn`|
    |**Kazakh**|`kk`|
    |**Korean**|`ko`|
    |**Lao**|`lo`|
    |**Latvian**|`lv`|
    |**Lingala**|`ln`|
    |**Lithuanian**|`lt`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Mandarin Chinese**|`cmn`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Occitan (post 1500)**|`oc`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Romanian**|`mo`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Serbian**|`sr`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**Spanish**|`es`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tamil**|`ta`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Turkish**|`tr`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Welsh**|`cy`|
    |**Wu Chinese**|`wuu`|
    |**Yiddish**|`yi`|
    |**Yoruba**|`yo`|
    |**Yue Chinese**|`yue`|
    |**Zulu**|`zu`|
    |**at**|`at`|
    |**jp**|`jp`|
    |**mymr**|`mymr`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Afrikaans (South Africa)**|`af-ZA`|
    |**Albanian (Albania)**|`sq-AL`|
    |**Amharic (Ethiopia)**|`am-ET`|
    |**Arabic (Algeria)**|`ar-DZ`|
    |**Arabic (Bahrain)**|`ar-BH`|
    |**Arabic (Egypt)**|`ar-EG`|
    |**Arabic (Iraq)**|`ar-IQ`|
    |**Arabic (Israel)**|`ar-IL`|
    |**Arabic (Jordan)**|`ar-JO`|
    |**Arabic (Kuwait)**|`ar-KW`|
    |**Arabic (Lebanon)**|`ar-LB`|
    |**Arabic (Libya)**|`ar-LY`|
    |**Arabic (Mauritania)**|`ar-MR`|
    |**Arabic (Montserrat)**|`ar-MS`|
    |**Arabic (Morocco)**|`ar-MA`|
    |**Arabic (Oman)**|`ar-OM`|
    |**Arabic (Palestinian Territories)**|`ar-PS`|
    |**Arabic (Qatar)**|`ar-QA`|
    |**Arabic (Saudi Arabia)**|`ar-SA`|
    |**Arabic (Syria)**|`ar-SY`|
    |**Arabic (Tunisia)**|`ar-TN`|
    |**Arabic (United Arab Emirates)**|`ar-AE`|
    |**Arabic (Yemen)**|`ar-YE`|
    |**Armenian (Armenia)**|`hy-AM`|
    |**Azerbaijani (Azerbaijan)**|`az-AZ`|
    |**Bangla (Bangladesh)**|`bn-BD`|
    |**Bangla (India)**|`bn-IN`|
    |**Basque (Spain)**|`eu-ES`|
    |**Bosnian (Bosnia & Herzegovina)**|`bs-BA`|
    |**Bulgarian (Bulgaria)**|`bg-BG`|
    |**Burmese (Myanmar (Burma))**|`my-MM`|
    |**Cantonese (China)**|`yue-CN`|
    |**Cantonese (Traditional, Hong Kong SAR China)**|`yue-Hant-HK`|
    |**Catalan (Spain)**|`ca-ES`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (Hong Kong SAR China)**|`zh-HK`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Croatian (Croatia)**|`hr-HR`|
    |**Czech (Czechia)**|`cs-CZ`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Belgium)**|`nl-BE`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (Australia)**|`en-AU`|
    |**English (Canada)**|`en-CA`|
    |**English (Ghana)**|`en-GH`|
    |**English (Hong Kong SAR China)**|`en-HK`|
    |**English (India)**|`en-IN`|
    |**English (Ireland)**|`en-IE`|
    |**English (Kenya)**|`en-KE`|
    |**English (New Zealand)**|`en-NZ`|
    |**English (Nigeria)**|`en-NG`|
    |**English (Pakistan)**|`en-PK`|
    |**English (Philippines)**|`en-PH`|
    |**English (Singapore)**|`en-SG`|
    |**English (South Africa)**|`en-ZA`|
    |**English (Tanzania)**|`en-TZ`|
    |**English (United Kingdom)**|`en-GB`|
    |**English (United Kingdom)**|`en-UK`|
    |**English (United States)**|`en-US`|
    |**Estonian (Estonia)**|`et-EE`|
    |**Filipino (Philippines)**|`fil-PH`|
    |**Finnish (Finland)**|`fi-FI`|
    |**French (Belgium)**|`fr-BE`|
    |**French (Canada)**|`fr-CA`|
    |**French (France)**|`fr-FR`|
    |**French (Switzerland)**|`fr-CH`|
    |**Galician (Spain)**|`gl-ES`|
    |**Georgian (Georgia)**|`ka-GE`|
    |**German (Austria)**|`de-AT`|
    |**German (Germany)**|`de-DE`|
    |**German (Switzerland)**|`de-CH`|
    |**Greek (Greece)**|`el-GR`|
    |**Gujarati (India)**|`gu-IN`|
    |**Hebrew (Israel)**|`he-IL`|
    |**Hebrew (Israel)**|`iw-IL`|
    |**Hindi (India)**|`hi-IN`|
    |**Hindi (Latin)**|`hi-Latn`|
    |**Hungarian (Hungary)**|`hu-HU`|
    |**Icelandic (Iceland)**|`is-IS`|
    |**Indonesian (Indonesia)**|`id-ID`|
    |**Irish (Ireland)**|`ga-IE`|
    |**Italian (Italy)**|`it-IT`|
    |**Italian (Switzerland)**|`it-CH`|
    |**Japanese (Japan)**|`ja-JP`|
    |**Javanese (Indonesia)**|`jv-ID`|
    |**Kannada (India)**|`kn-IN`|
    |**Kazakh (Kazakhstan)**|`kk-KZ`|
    |**Khmer (Cambodia)**|`km-KH`|
    |**Korean (South Korea)**|`ko-KR`|
    |**Lao (Laos)**|`lo-LA`|
    |**Latvian (Latvia)**|`lv-LV`|
    |**Lithuanian (Lithuania)**|`lt-LT`|
    |**Macedonian (North Macedonia)**|`mk-MK`|
    |**Malay (Malaysia)**|`ms-MY`|
    |**Malayalam (India)**|`ml-IN`|
    |**Maltese (Malta)**|`mt-MT`|
    |**Marathi (India)**|`mr-IN`|
    |**Mongolian (Mongolia)**|`mn-MN`|
    |**Nepali (Nepal)**|`ne-NP`|
    |**Norwegian (Norway)**|`no-NO`|
    |**Norwegian Bokmål (Norway)**|`nb-NO`|
    |**Pashto (Afghanistan)**|`ps-AF`|
    |**Persian (Iran)**|`fa-IR`|
    |**Polish (Poland)**|`pl-PL`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Punjabi (India)**|`pa-Guru-IN`|
    |**Romanian (Romania)**|`ro-RO`|
    |**Russian (Russia)**|`ru-RU`|
    |**Serbian (Serbia)**|`sr-RS`|
    |**Sinhala (Sri Lanka)**|`si-LK`|
    |**Slovak (Slovakia)**|`sk-SK`|
    |**Slovenian (Slovenia)**|`sl-SI`|
    |**Somali (Somalia)**|`so-SO`|
    |**Spanish (Argentina)**|`es-AR`|
    |**Spanish (Bolivia)**|`es-BO`|
    |**Spanish (Chile)**|`es-CL`|
    |**Spanish (Colombia)**|`es-CO`|
    |**Spanish (Costa Rica)**|`es-CR`|
    |**Spanish (Cuba)**|`es-CU`|
    |**Spanish (Dominican Republic)**|`es-DO`|
    |**Spanish (Ecuador)**|`es-EC`|
    |**Spanish (El Salvador)**|`es-SV`|
    |**Spanish (Equatorial Guinea)**|`es-GQ`|
    |**Spanish (Guatemala)**|`es-GT`|
    |**Spanish (Honduras)**|`es-HN`|
    |**Spanish (Laos)**|`es-LA`|
    |**Spanish (Latin America)**|`es-419`|
    |**Spanish (Mexico)**|`es-MX`|
    |**Spanish (Nicaragua)**|`es-NI`|
    |**Spanish (Panama)**|`es-PA`|
    |**Spanish (Paraguay)**|`es-PY`|
    |**Spanish (Peru)**|`es-PE`|
    |**Spanish (Puerto Rico)**|`es-PR`|
    |**Spanish (Spain)**|`es-ES`|
    |**Spanish (United States)**|`es-US`|
    |**Spanish (Uruguay)**|`es-UY`|
    |**Spanish (Venezuela)**|`es-VE`|
    |**Sundanese (Indonesia)**|`su-ID`|
    |**Swahili (Kenya)**|`sw-KE`|
    |**Swahili (Tanzania)**|`sw-TZ`|
    |**Swedish (Sweden)**|`sv-SE`|
    |**Tamil (India)**|`ta-IN`|
    |**Tamil (Malaysia)**|`ta-MY`|
    |**Tamil (Singapore)**|`ta-SG`|
    |**Tamil (Sri Lanka)**|`ta-LK`|
    |**Telugu (India)**|`te-IN`|
    |**Thai (Thailand)**|`th-TH`|
    |**Turkish (Turkey)**|`tr-TR`|
    |**Ukrainian (Ukraine)**|`uk-UA`|
    |**Urdu (India)**|`ur-IN`|
    |**Urdu (Pakistan)**|`ur-PK`|
    |**Uzbek (Uzbekistan)**|`uz-UZ`|
    |**Vietnamese (Vietnam)**|`vi-VN`|
    |**Welsh (United Kingdom)**|`cy-GB`|
    |**Wu Chinese (China)**|`wuu-CN`|
    |**Zulu (South Africa)**|`zu-ZA`|

    </details><details><summary>Supported Models</summary><details><summary>deepgram</summary>





    |Name|Value|
    |----|-----|
    |**deepgram**|`base`|
    ||`enhanced`|

    </details><details><summary>speechmatics</summary>





    |Name|Value|
    |----|-----|
    |**speechmatics**|`enhanced`|
    ||`standard`|

    </details>

    </details>

    Args:
        body (SpeechToTextAsyncRequest):
        body (SpeechToTextAsyncRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LaunchAsyncJobResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        SpeechToTextAsyncRequest,
        SpeechToTextAsyncRequest,
    ],
) -> Response[LaunchAsyncJobResponse]:
    """Speech to Text Launch Job

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**amazon**|-|`boto3 (v1.15.18)`|0.024 (per 60 seconde)|15 seconde
    |**google**|-|`v1p1beta1`|0.024 (per 60 seconde)|1 seconde
    |**ibm**|-|`v1`|0.02 (per 60 seconde)|1 seconde
    |**microsoft**|-|`v1.0`|0.0168 (per 60 seconde)|1 seconde
    |**revai**|-|`v1`|0.02 (per 60 seconde)|15 seconde
    |**symbl**|-|`v1`|0.027 (per 60 seconde)|60 seconde
    |**voci**|-|`v1`|0.0162 (per 60 seconde)|1 seconde
    |**neuralspace**|-|`v1`|0.024 (per 60 seconde)|60 seconde
    |**assembly**|-|`v2`|0.011 (per 60 seconde)|1 seconde
    |**deepgram**|**enhanced**|`v1`|0.0189 (per 60 seconde)|1 seconde
    |**deepgram**|-|`v1`|0.0189 (per 60 seconde)|1 seconde
    |**deepgram**|**base**|`v1`|0.0169 (per 60 seconde)|1 seconde
    |**openai**|-|`boto3 (v1.15.18)`|0.006 (per 60 seconde)|1 seconde
    |**speechmatics**|**enhanced**|`v2`|0.022 (per 60 seconde)|1 seconde
    |**speechmatics**|**standard**|`v2`|0.017 (per 60 seconde)|1 seconde
    |**speechmatics**|-|`v2`|0.022 (per 60 seconde)|1 seconde
    |**gladia**|-|`v1`|0.0102 (per 60 seconde)|1 seconde


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Armenian**|`hy`|
    |**Azerbaijani**|`az`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bengali**|`bn`|
    |**Bosnian**|`bs`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Central Khmer**|`km`|
    |**Chinese**|`zh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hebrew**|`he`|
    |**Hebrew**|`iw`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Indonesian**|`id`|
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kannada**|`kn`|
    |**Kazakh**|`kk`|
    |**Korean**|`ko`|
    |**Lao**|`lo`|
    |**Latvian**|`lv`|
    |**Lingala**|`ln`|
    |**Lithuanian**|`lt`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Mandarin Chinese**|`cmn`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Occitan (post 1500)**|`oc`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Romanian**|`mo`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Serbian**|`sr`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**Spanish**|`es`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tamil**|`ta`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Turkish**|`tr`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Welsh**|`cy`|
    |**Wu Chinese**|`wuu`|
    |**Yiddish**|`yi`|
    |**Yoruba**|`yo`|
    |**Yue Chinese**|`yue`|
    |**Zulu**|`zu`|
    |**at**|`at`|
    |**jp**|`jp`|
    |**mymr**|`mymr`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Afrikaans (South Africa)**|`af-ZA`|
    |**Albanian (Albania)**|`sq-AL`|
    |**Amharic (Ethiopia)**|`am-ET`|
    |**Arabic (Algeria)**|`ar-DZ`|
    |**Arabic (Bahrain)**|`ar-BH`|
    |**Arabic (Egypt)**|`ar-EG`|
    |**Arabic (Iraq)**|`ar-IQ`|
    |**Arabic (Israel)**|`ar-IL`|
    |**Arabic (Jordan)**|`ar-JO`|
    |**Arabic (Kuwait)**|`ar-KW`|
    |**Arabic (Lebanon)**|`ar-LB`|
    |**Arabic (Libya)**|`ar-LY`|
    |**Arabic (Mauritania)**|`ar-MR`|
    |**Arabic (Montserrat)**|`ar-MS`|
    |**Arabic (Morocco)**|`ar-MA`|
    |**Arabic (Oman)**|`ar-OM`|
    |**Arabic (Palestinian Territories)**|`ar-PS`|
    |**Arabic (Qatar)**|`ar-QA`|
    |**Arabic (Saudi Arabia)**|`ar-SA`|
    |**Arabic (Syria)**|`ar-SY`|
    |**Arabic (Tunisia)**|`ar-TN`|
    |**Arabic (United Arab Emirates)**|`ar-AE`|
    |**Arabic (Yemen)**|`ar-YE`|
    |**Armenian (Armenia)**|`hy-AM`|
    |**Azerbaijani (Azerbaijan)**|`az-AZ`|
    |**Bangla (Bangladesh)**|`bn-BD`|
    |**Bangla (India)**|`bn-IN`|
    |**Basque (Spain)**|`eu-ES`|
    |**Bosnian (Bosnia & Herzegovina)**|`bs-BA`|
    |**Bulgarian (Bulgaria)**|`bg-BG`|
    |**Burmese (Myanmar (Burma))**|`my-MM`|
    |**Cantonese (China)**|`yue-CN`|
    |**Cantonese (Traditional, Hong Kong SAR China)**|`yue-Hant-HK`|
    |**Catalan (Spain)**|`ca-ES`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (Hong Kong SAR China)**|`zh-HK`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Croatian (Croatia)**|`hr-HR`|
    |**Czech (Czechia)**|`cs-CZ`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Belgium)**|`nl-BE`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (Australia)**|`en-AU`|
    |**English (Canada)**|`en-CA`|
    |**English (Ghana)**|`en-GH`|
    |**English (Hong Kong SAR China)**|`en-HK`|
    |**English (India)**|`en-IN`|
    |**English (Ireland)**|`en-IE`|
    |**English (Kenya)**|`en-KE`|
    |**English (New Zealand)**|`en-NZ`|
    |**English (Nigeria)**|`en-NG`|
    |**English (Pakistan)**|`en-PK`|
    |**English (Philippines)**|`en-PH`|
    |**English (Singapore)**|`en-SG`|
    |**English (South Africa)**|`en-ZA`|
    |**English (Tanzania)**|`en-TZ`|
    |**English (United Kingdom)**|`en-GB`|
    |**English (United Kingdom)**|`en-UK`|
    |**English (United States)**|`en-US`|
    |**Estonian (Estonia)**|`et-EE`|
    |**Filipino (Philippines)**|`fil-PH`|
    |**Finnish (Finland)**|`fi-FI`|
    |**French (Belgium)**|`fr-BE`|
    |**French (Canada)**|`fr-CA`|
    |**French (France)**|`fr-FR`|
    |**French (Switzerland)**|`fr-CH`|
    |**Galician (Spain)**|`gl-ES`|
    |**Georgian (Georgia)**|`ka-GE`|
    |**German (Austria)**|`de-AT`|
    |**German (Germany)**|`de-DE`|
    |**German (Switzerland)**|`de-CH`|
    |**Greek (Greece)**|`el-GR`|
    |**Gujarati (India)**|`gu-IN`|
    |**Hebrew (Israel)**|`he-IL`|
    |**Hebrew (Israel)**|`iw-IL`|
    |**Hindi (India)**|`hi-IN`|
    |**Hindi (Latin)**|`hi-Latn`|
    |**Hungarian (Hungary)**|`hu-HU`|
    |**Icelandic (Iceland)**|`is-IS`|
    |**Indonesian (Indonesia)**|`id-ID`|
    |**Irish (Ireland)**|`ga-IE`|
    |**Italian (Italy)**|`it-IT`|
    |**Italian (Switzerland)**|`it-CH`|
    |**Japanese (Japan)**|`ja-JP`|
    |**Javanese (Indonesia)**|`jv-ID`|
    |**Kannada (India)**|`kn-IN`|
    |**Kazakh (Kazakhstan)**|`kk-KZ`|
    |**Khmer (Cambodia)**|`km-KH`|
    |**Korean (South Korea)**|`ko-KR`|
    |**Lao (Laos)**|`lo-LA`|
    |**Latvian (Latvia)**|`lv-LV`|
    |**Lithuanian (Lithuania)**|`lt-LT`|
    |**Macedonian (North Macedonia)**|`mk-MK`|
    |**Malay (Malaysia)**|`ms-MY`|
    |**Malayalam (India)**|`ml-IN`|
    |**Maltese (Malta)**|`mt-MT`|
    |**Marathi (India)**|`mr-IN`|
    |**Mongolian (Mongolia)**|`mn-MN`|
    |**Nepali (Nepal)**|`ne-NP`|
    |**Norwegian (Norway)**|`no-NO`|
    |**Norwegian Bokmål (Norway)**|`nb-NO`|
    |**Pashto (Afghanistan)**|`ps-AF`|
    |**Persian (Iran)**|`fa-IR`|
    |**Polish (Poland)**|`pl-PL`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Punjabi (India)**|`pa-Guru-IN`|
    |**Romanian (Romania)**|`ro-RO`|
    |**Russian (Russia)**|`ru-RU`|
    |**Serbian (Serbia)**|`sr-RS`|
    |**Sinhala (Sri Lanka)**|`si-LK`|
    |**Slovak (Slovakia)**|`sk-SK`|
    |**Slovenian (Slovenia)**|`sl-SI`|
    |**Somali (Somalia)**|`so-SO`|
    |**Spanish (Argentina)**|`es-AR`|
    |**Spanish (Bolivia)**|`es-BO`|
    |**Spanish (Chile)**|`es-CL`|
    |**Spanish (Colombia)**|`es-CO`|
    |**Spanish (Costa Rica)**|`es-CR`|
    |**Spanish (Cuba)**|`es-CU`|
    |**Spanish (Dominican Republic)**|`es-DO`|
    |**Spanish (Ecuador)**|`es-EC`|
    |**Spanish (El Salvador)**|`es-SV`|
    |**Spanish (Equatorial Guinea)**|`es-GQ`|
    |**Spanish (Guatemala)**|`es-GT`|
    |**Spanish (Honduras)**|`es-HN`|
    |**Spanish (Laos)**|`es-LA`|
    |**Spanish (Latin America)**|`es-419`|
    |**Spanish (Mexico)**|`es-MX`|
    |**Spanish (Nicaragua)**|`es-NI`|
    |**Spanish (Panama)**|`es-PA`|
    |**Spanish (Paraguay)**|`es-PY`|
    |**Spanish (Peru)**|`es-PE`|
    |**Spanish (Puerto Rico)**|`es-PR`|
    |**Spanish (Spain)**|`es-ES`|
    |**Spanish (United States)**|`es-US`|
    |**Spanish (Uruguay)**|`es-UY`|
    |**Spanish (Venezuela)**|`es-VE`|
    |**Sundanese (Indonesia)**|`su-ID`|
    |**Swahili (Kenya)**|`sw-KE`|
    |**Swahili (Tanzania)**|`sw-TZ`|
    |**Swedish (Sweden)**|`sv-SE`|
    |**Tamil (India)**|`ta-IN`|
    |**Tamil (Malaysia)**|`ta-MY`|
    |**Tamil (Singapore)**|`ta-SG`|
    |**Tamil (Sri Lanka)**|`ta-LK`|
    |**Telugu (India)**|`te-IN`|
    |**Thai (Thailand)**|`th-TH`|
    |**Turkish (Turkey)**|`tr-TR`|
    |**Ukrainian (Ukraine)**|`uk-UA`|
    |**Urdu (India)**|`ur-IN`|
    |**Urdu (Pakistan)**|`ur-PK`|
    |**Uzbek (Uzbekistan)**|`uz-UZ`|
    |**Vietnamese (Vietnam)**|`vi-VN`|
    |**Welsh (United Kingdom)**|`cy-GB`|
    |**Wu Chinese (China)**|`wuu-CN`|
    |**Zulu (South Africa)**|`zu-ZA`|

    </details><details><summary>Supported Models</summary><details><summary>deepgram</summary>





    |Name|Value|
    |----|-----|
    |**deepgram**|`base`|
    ||`enhanced`|

    </details><details><summary>speechmatics</summary>





    |Name|Value|
    |----|-----|
    |**speechmatics**|`enhanced`|
    ||`standard`|

    </details>

    </details>

    Args:
        body (SpeechToTextAsyncRequest):
        body (SpeechToTextAsyncRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LaunchAsyncJobResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        SpeechToTextAsyncRequest,
        SpeechToTextAsyncRequest,
    ],
) -> Optional[LaunchAsyncJobResponse]:
    """Speech to Text Launch Job

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**amazon**|-|`boto3 (v1.15.18)`|0.024 (per 60 seconde)|15 seconde
    |**google**|-|`v1p1beta1`|0.024 (per 60 seconde)|1 seconde
    |**ibm**|-|`v1`|0.02 (per 60 seconde)|1 seconde
    |**microsoft**|-|`v1.0`|0.0168 (per 60 seconde)|1 seconde
    |**revai**|-|`v1`|0.02 (per 60 seconde)|15 seconde
    |**symbl**|-|`v1`|0.027 (per 60 seconde)|60 seconde
    |**voci**|-|`v1`|0.0162 (per 60 seconde)|1 seconde
    |**neuralspace**|-|`v1`|0.024 (per 60 seconde)|60 seconde
    |**assembly**|-|`v2`|0.011 (per 60 seconde)|1 seconde
    |**deepgram**|**enhanced**|`v1`|0.0189 (per 60 seconde)|1 seconde
    |**deepgram**|-|`v1`|0.0189 (per 60 seconde)|1 seconde
    |**deepgram**|**base**|`v1`|0.0169 (per 60 seconde)|1 seconde
    |**openai**|-|`boto3 (v1.15.18)`|0.006 (per 60 seconde)|1 seconde
    |**speechmatics**|**enhanced**|`v2`|0.022 (per 60 seconde)|1 seconde
    |**speechmatics**|**standard**|`v2`|0.017 (per 60 seconde)|1 seconde
    |**speechmatics**|-|`v2`|0.022 (per 60 seconde)|1 seconde
    |**gladia**|-|`v1`|0.0102 (per 60 seconde)|1 seconde


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Armenian**|`hy`|
    |**Azerbaijani**|`az`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bengali**|`bn`|
    |**Bosnian**|`bs`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Central Khmer**|`km`|
    |**Chinese**|`zh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hebrew**|`he`|
    |**Hebrew**|`iw`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Indonesian**|`id`|
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kannada**|`kn`|
    |**Kazakh**|`kk`|
    |**Korean**|`ko`|
    |**Lao**|`lo`|
    |**Latvian**|`lv`|
    |**Lingala**|`ln`|
    |**Lithuanian**|`lt`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Mandarin Chinese**|`cmn`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Occitan (post 1500)**|`oc`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Romanian**|`mo`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Serbian**|`sr`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**Spanish**|`es`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tamil**|`ta`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Turkish**|`tr`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Welsh**|`cy`|
    |**Wu Chinese**|`wuu`|
    |**Yiddish**|`yi`|
    |**Yoruba**|`yo`|
    |**Yue Chinese**|`yue`|
    |**Zulu**|`zu`|
    |**at**|`at`|
    |**jp**|`jp`|
    |**mymr**|`mymr`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Afrikaans (South Africa)**|`af-ZA`|
    |**Albanian (Albania)**|`sq-AL`|
    |**Amharic (Ethiopia)**|`am-ET`|
    |**Arabic (Algeria)**|`ar-DZ`|
    |**Arabic (Bahrain)**|`ar-BH`|
    |**Arabic (Egypt)**|`ar-EG`|
    |**Arabic (Iraq)**|`ar-IQ`|
    |**Arabic (Israel)**|`ar-IL`|
    |**Arabic (Jordan)**|`ar-JO`|
    |**Arabic (Kuwait)**|`ar-KW`|
    |**Arabic (Lebanon)**|`ar-LB`|
    |**Arabic (Libya)**|`ar-LY`|
    |**Arabic (Mauritania)**|`ar-MR`|
    |**Arabic (Montserrat)**|`ar-MS`|
    |**Arabic (Morocco)**|`ar-MA`|
    |**Arabic (Oman)**|`ar-OM`|
    |**Arabic (Palestinian Territories)**|`ar-PS`|
    |**Arabic (Qatar)**|`ar-QA`|
    |**Arabic (Saudi Arabia)**|`ar-SA`|
    |**Arabic (Syria)**|`ar-SY`|
    |**Arabic (Tunisia)**|`ar-TN`|
    |**Arabic (United Arab Emirates)**|`ar-AE`|
    |**Arabic (Yemen)**|`ar-YE`|
    |**Armenian (Armenia)**|`hy-AM`|
    |**Azerbaijani (Azerbaijan)**|`az-AZ`|
    |**Bangla (Bangladesh)**|`bn-BD`|
    |**Bangla (India)**|`bn-IN`|
    |**Basque (Spain)**|`eu-ES`|
    |**Bosnian (Bosnia & Herzegovina)**|`bs-BA`|
    |**Bulgarian (Bulgaria)**|`bg-BG`|
    |**Burmese (Myanmar (Burma))**|`my-MM`|
    |**Cantonese (China)**|`yue-CN`|
    |**Cantonese (Traditional, Hong Kong SAR China)**|`yue-Hant-HK`|
    |**Catalan (Spain)**|`ca-ES`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (Hong Kong SAR China)**|`zh-HK`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Croatian (Croatia)**|`hr-HR`|
    |**Czech (Czechia)**|`cs-CZ`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Belgium)**|`nl-BE`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (Australia)**|`en-AU`|
    |**English (Canada)**|`en-CA`|
    |**English (Ghana)**|`en-GH`|
    |**English (Hong Kong SAR China)**|`en-HK`|
    |**English (India)**|`en-IN`|
    |**English (Ireland)**|`en-IE`|
    |**English (Kenya)**|`en-KE`|
    |**English (New Zealand)**|`en-NZ`|
    |**English (Nigeria)**|`en-NG`|
    |**English (Pakistan)**|`en-PK`|
    |**English (Philippines)**|`en-PH`|
    |**English (Singapore)**|`en-SG`|
    |**English (South Africa)**|`en-ZA`|
    |**English (Tanzania)**|`en-TZ`|
    |**English (United Kingdom)**|`en-GB`|
    |**English (United Kingdom)**|`en-UK`|
    |**English (United States)**|`en-US`|
    |**Estonian (Estonia)**|`et-EE`|
    |**Filipino (Philippines)**|`fil-PH`|
    |**Finnish (Finland)**|`fi-FI`|
    |**French (Belgium)**|`fr-BE`|
    |**French (Canada)**|`fr-CA`|
    |**French (France)**|`fr-FR`|
    |**French (Switzerland)**|`fr-CH`|
    |**Galician (Spain)**|`gl-ES`|
    |**Georgian (Georgia)**|`ka-GE`|
    |**German (Austria)**|`de-AT`|
    |**German (Germany)**|`de-DE`|
    |**German (Switzerland)**|`de-CH`|
    |**Greek (Greece)**|`el-GR`|
    |**Gujarati (India)**|`gu-IN`|
    |**Hebrew (Israel)**|`he-IL`|
    |**Hebrew (Israel)**|`iw-IL`|
    |**Hindi (India)**|`hi-IN`|
    |**Hindi (Latin)**|`hi-Latn`|
    |**Hungarian (Hungary)**|`hu-HU`|
    |**Icelandic (Iceland)**|`is-IS`|
    |**Indonesian (Indonesia)**|`id-ID`|
    |**Irish (Ireland)**|`ga-IE`|
    |**Italian (Italy)**|`it-IT`|
    |**Italian (Switzerland)**|`it-CH`|
    |**Japanese (Japan)**|`ja-JP`|
    |**Javanese (Indonesia)**|`jv-ID`|
    |**Kannada (India)**|`kn-IN`|
    |**Kazakh (Kazakhstan)**|`kk-KZ`|
    |**Khmer (Cambodia)**|`km-KH`|
    |**Korean (South Korea)**|`ko-KR`|
    |**Lao (Laos)**|`lo-LA`|
    |**Latvian (Latvia)**|`lv-LV`|
    |**Lithuanian (Lithuania)**|`lt-LT`|
    |**Macedonian (North Macedonia)**|`mk-MK`|
    |**Malay (Malaysia)**|`ms-MY`|
    |**Malayalam (India)**|`ml-IN`|
    |**Maltese (Malta)**|`mt-MT`|
    |**Marathi (India)**|`mr-IN`|
    |**Mongolian (Mongolia)**|`mn-MN`|
    |**Nepali (Nepal)**|`ne-NP`|
    |**Norwegian (Norway)**|`no-NO`|
    |**Norwegian Bokmål (Norway)**|`nb-NO`|
    |**Pashto (Afghanistan)**|`ps-AF`|
    |**Persian (Iran)**|`fa-IR`|
    |**Polish (Poland)**|`pl-PL`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Punjabi (India)**|`pa-Guru-IN`|
    |**Romanian (Romania)**|`ro-RO`|
    |**Russian (Russia)**|`ru-RU`|
    |**Serbian (Serbia)**|`sr-RS`|
    |**Sinhala (Sri Lanka)**|`si-LK`|
    |**Slovak (Slovakia)**|`sk-SK`|
    |**Slovenian (Slovenia)**|`sl-SI`|
    |**Somali (Somalia)**|`so-SO`|
    |**Spanish (Argentina)**|`es-AR`|
    |**Spanish (Bolivia)**|`es-BO`|
    |**Spanish (Chile)**|`es-CL`|
    |**Spanish (Colombia)**|`es-CO`|
    |**Spanish (Costa Rica)**|`es-CR`|
    |**Spanish (Cuba)**|`es-CU`|
    |**Spanish (Dominican Republic)**|`es-DO`|
    |**Spanish (Ecuador)**|`es-EC`|
    |**Spanish (El Salvador)**|`es-SV`|
    |**Spanish (Equatorial Guinea)**|`es-GQ`|
    |**Spanish (Guatemala)**|`es-GT`|
    |**Spanish (Honduras)**|`es-HN`|
    |**Spanish (Laos)**|`es-LA`|
    |**Spanish (Latin America)**|`es-419`|
    |**Spanish (Mexico)**|`es-MX`|
    |**Spanish (Nicaragua)**|`es-NI`|
    |**Spanish (Panama)**|`es-PA`|
    |**Spanish (Paraguay)**|`es-PY`|
    |**Spanish (Peru)**|`es-PE`|
    |**Spanish (Puerto Rico)**|`es-PR`|
    |**Spanish (Spain)**|`es-ES`|
    |**Spanish (United States)**|`es-US`|
    |**Spanish (Uruguay)**|`es-UY`|
    |**Spanish (Venezuela)**|`es-VE`|
    |**Sundanese (Indonesia)**|`su-ID`|
    |**Swahili (Kenya)**|`sw-KE`|
    |**Swahili (Tanzania)**|`sw-TZ`|
    |**Swedish (Sweden)**|`sv-SE`|
    |**Tamil (India)**|`ta-IN`|
    |**Tamil (Malaysia)**|`ta-MY`|
    |**Tamil (Singapore)**|`ta-SG`|
    |**Tamil (Sri Lanka)**|`ta-LK`|
    |**Telugu (India)**|`te-IN`|
    |**Thai (Thailand)**|`th-TH`|
    |**Turkish (Turkey)**|`tr-TR`|
    |**Ukrainian (Ukraine)**|`uk-UA`|
    |**Urdu (India)**|`ur-IN`|
    |**Urdu (Pakistan)**|`ur-PK`|
    |**Uzbek (Uzbekistan)**|`uz-UZ`|
    |**Vietnamese (Vietnam)**|`vi-VN`|
    |**Welsh (United Kingdom)**|`cy-GB`|
    |**Wu Chinese (China)**|`wuu-CN`|
    |**Zulu (South Africa)**|`zu-ZA`|

    </details><details><summary>Supported Models</summary><details><summary>deepgram</summary>





    |Name|Value|
    |----|-----|
    |**deepgram**|`base`|
    ||`enhanced`|

    </details><details><summary>speechmatics</summary>





    |Name|Value|
    |----|-----|
    |**speechmatics**|`enhanced`|
    ||`standard`|

    </details>

    </details>

    Args:
        body (SpeechToTextAsyncRequest):
        body (SpeechToTextAsyncRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LaunchAsyncJobResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
