from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audiotext_to_speech_text_to_speech_request import AudiotextToSpeechTextToSpeechRequest
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.not_found_response import NotFoundResponse
from ...types import Response


def _get_kwargs(
    *,
    body: AudiotextToSpeechTextToSpeechRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/audio/text_to_speech",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = BadRequest.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = NotFoundResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AudiotextToSpeechTextToSpeechRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Text to Speech

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**amazon**|-|`boto3 (v1.15.18)`|4.0 (per 1000000 char)|1 char
    |**amazon**|**Neural**|`boto3 (v1.15.18)`|16.0 (per 1000000 char)|1 char
    |**google**|-|`v1`|4.0 (per 1000000 char)|1 char
    |**google**|**Standard**|`v1`|4.0 (per 1000000 char)|1 char
    |**google**|**Neural**|`v1`|16.0 (per 1000000 char)|1 char
    |**google**|**Wavenet**|`v1`|16.0 (per 1000000 char)|1 char
    |**google**|**Studio**|`v1`|0.16 (per 1000 char)|1 char
    |**ibm**|-|`v1`|20.0 (per 1000000 char)|1000 char
    |**microsoft**|-|`v1.0`|16.0 (per 1000000 char)|1 char
    |**lovoai**|-|`v1`|160.0 (per 1000000 char)|1000 char
    |**elevenlabs**|-|`v1`|0.3 (per 1000 char)|1 char
    |**openai**|-|`v1.0`|0.015 (per 1000 char)|1 char


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
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bengali**|`bn`|
    |**Bosnian**|`bs`|
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
    |**Estonian**|`et`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Indonesian**|`id`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kannada**|`kn`|
    |**Kazakh**|`kk`|
    |**Korean**|`ko`|
    |**Lao**|`lo`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Macedonian**|`mk`|
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
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Serbian**|`sr`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**Spanish**|`es`|
    |**Standard Arabic**|`arb`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tamil**|`ta`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Turkish**|`tr`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Welsh**|`cy`|
    |**Wu Chinese**|`wuu`|
    |**Xhosa**|`xh`|
    |**Yue Chinese**|`yue`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans (South Africa)**|`af-ZA`|
    |**Albanian (Albania)**|`sq-AL`|
    |**Amharic (Ethiopia)**|`am-ET`|
    |**Arabic (Algeria)**|`ar-DZ`|
    |**Arabic (Bahrain)**|`ar-BH`|
    |**Arabic (Egypt)**|`ar-EG`|
    |**Arabic (Iraq)**|`ar-IQ`|
    |**Arabic (Jordan)**|`ar-JO`|
    |**Arabic (Kuwait)**|`ar-KW`|
    |**Arabic (Lebanon)**|`ar-LB`|
    |**Arabic (Libya)**|`ar-LY`|
    |**Arabic (Morocco)**|`ar-MA`|
    |**Arabic (Oman)**|`ar-OM`|
    |**Arabic (Pseudo-Accents)**|`ar-XA`|
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
    |**Cantonese (Hong Kong SAR China)**|`yue-HK`|
    |**Catalan (Spain)**|`ca-ES`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (China)**|`zh-CN-henan`|
    |**Chinese (China)**|`zh-CN-shandong`|
    |**Chinese (China)**|`zh-CN-sichuan`|
    |**Chinese (Hong Kong SAR China)**|`zh-HK`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Croatian (Croatia)**|`hr-HR`|
    |**Czech (Czechia)**|`cs-CZ`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Belgium)**|`nl-BE`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (Australia)**|`en-AU`|
    |**English (Canada)**|`en-CA`|
    |**English (Curaçao)**|`en-AN`|
    |**English (Hong Kong SAR China)**|`en-HK`|
    |**English (India)**|`en-IN`|
    |**English (Ireland)**|`en-IE`|
    |**English (Kenya)**|`en-KE`|
    |**English (New Zealand)**|`en-NZ`|
    |**English (Nigeria)**|`en-NG`|
    |**English (Philippines)**|`en-PH`|
    |**English (Singapore)**|`en-SG`|
    |**English (South Africa)**|`en-ZA`|
    |**English (Tanzania)**|`en-TZ`|
    |**English (United Kingdom)**|`en-GB`|
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
    |**Hindi (India)**|`hi-IN`|
    |**Hungarian (Hungary)**|`hu-HU`|
    |**Icelandic (Iceland)**|`is-IS`|
    |**Indonesian (Indonesia)**|`id-ID`|
    |**Irish (Ireland)**|`ga-IE`|
    |**Italian (Italy)**|`it-IT`|
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
    |**Mandarin Chinese (China)**|`cmn-CN`|
    |**Mandarin Chinese (Taiwan)**|`cmn-TW`|
    |**Marathi (India)**|`mr-IN`|
    |**Mongolian (Mongolia)**|`mn-MN`|
    |**Nepali (Nepal)**|`ne-NP`|
    |**Norwegian Bokmål (Norway)**|`nb-NO`|
    |**Pashto (Afghanistan)**|`ps-AF`|
    |**Persian (Iran)**|`fa-IR`|
    |**Polish (Poland)**|`pl-PL`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Punjabi (India)**|`pa-IN`|
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
    |**Uzbek (United Kingdom)**|`uz-UK`|
    |**Uzbek (Uzbekistan)**|`uz-UZ`|
    |**Vietnamese (Vietnam)**|`vi-VN`|
    |**Welsh (United Kingdom)**|`cy-GB`|
    |**Wu Chinese (China)**|`wuu-CN`|
    |**Xhosa (South Africa)**|`xh-ZA`|
    |**Zulu (South Africa)**|`zu-ZA`|

    </details><details><summary>Supported Models</summary><details><summary>amazon</summary>





    |Name|Value|
    |----|-----|
    |**amazon**|`ar-AE_Hala_Neural`|
    ||`arb_Zeina_Standard`|
    ||`ca-ES_Arlet_Neural`|
    ||`cmn-CN_Zhiyu_Neural`|
    ||`cmn-CN_Zhiyu_Standard`|
    ||`cy-GB_Gwyneth_Standard`|
    ||`da-DK_Mads_Standard`|
    ||`da-DK_Naja_Standard`|
    ||`de-AT_Hannah_Neural`|
    ||`de-DE_Daniel_Neural`|
    ||`de-DE_Hans_Standard`|
    ||`de-DE_Marlene_Standard`|
    ||`de-DE_Vicki_Neural`|
    ||`de-DE_Vicki_Standard`|
    ||`en-AU_Nicole_Neural`|
    ||`en-AU_Olivia_Standard`|
    ||`en-AU_Russell_Neural`|
    ||`en-GB_Amy_Neural`|
    ||`en-GB_Amy_Standard`|
    ||`en-GB_Arthur_Neural`|
    ||`en-GB_Brian_Neural`|
    ||`en-GB_Brian_Standard`|
    ||`en-GB_Emma_Neural`|
    ||`en-GB_Emma_Standard`|
    ||`en-IN_Aditi_Standard`|
    ||`en-IN_Kajal_Neural`|
    ||`en-IN_Raveena_Standard`|
    ||`en-NZ_Aria_Neural`|
    ||`en-US_Ivy_Neural`|
    ||`en-US_Ivy_Standard`|
    ||`en-US_Joanna_Neural`|
    ||`en-US_Joanna_Standard`|
    ||`en-US_Joey_Neural`|
    ||`en-US_Joey_Standard`|
    ||`en-US_Justin_Neural`|
    ||`en-US_Justin_Standard`|
    ||`en-US_Kendra_Neural`|
    ||`en-US_Kendra_Standard`|
    ||`en-US_Kevin_Neural`|
    ||`en-US_Kimberly_Neural`|
    ||`en-US_Kimberly_Standard`|
    ||`en-US_Matthew_Neural`|
    ||`en-US_Matthew_Standard`|
    ||`en-US_Ruth_Neural`|
    ||`en-US_Salli_Neural`|
    ||`en-US_Salli_Standard`|
    ||`en-US_Stephen_Neural`|
    ||`en-ZA_Ayanda_Neural`|
    ||`es-ES_Conchita_Standard`|
    ||`es-ES_Enrique_Standard`|
    ||`es-ES_Lucia_Neural`|
    ||`es-ES_Lucia_Standard`|
    ||`es-ES_Sergio_Neural`|
    ||`es-MX_Andres_Neural`|
    ||`es-MX_Mia_Neural`|
    ||`es-MX_Mia_Standard`|
    ||`es-US_Lupe_Neural`|
    ||`es-US_Lupe_Standard`|
    ||`es-US_Miguel_Standard`|
    ||`es-US_Pedro_Neural`|
    ||`es-US_Penelope_Standard`|
    ||`fi-FI_Suvi_Neural`|
    ||`fr-CA_Chantal_Standard`|
    ||`fr-CA_Gabrielle_Neural`|
    ||`fr-CA_Liam_Neural`|
    ||`fr-FR_Celine_Standard`|
    ||`fr-FR_Lea_Neural`|
    ||`fr-FR_Lea_Standard`|
    ||`fr-FR_Mathieu_Standard`|
    ||`fr-FR_Remi_Neural`|
    ||`hi-IN_Aditi_Standard`|
    ||`hi-IN_Kajal_Neural`|
    ||`is-IS_Dora_Standard`|
    ||`is-IS_Karl_Neural`|
    ||`is-IS_Karl_Standard`|
    ||`it-IT_Adriano_Neural`|
    ||`it-IT_Bianca_Neural`|
    ||`it-IT_Bianca_Standard`|
    ||`it-IT_Carla_Standard`|
    ||`it-IT_Giorgio_Standard`|
    ||`ja-JP_Kazuha_Neural`|
    ||`ja-JP_Mizuki_Standard`|
    ||`ja-JP_Takumi_Neural`|
    ||`ja-JP_Takumi_Standard`|
    ||`ja-JP_Tomoko_Neural`|
    ||`ko-KR_Seoyeon_Neural`|
    ||`ko-KR_Seoyeon_Standard`|
    ||`nb-NO_Liv_Standard`|
    ||`nl-NL_Laura_Neural`|
    ||`nl-NL_Lotte_Standard`|
    ||`nl-NL_Ruben_Standard`|
    ||`pl-PL_Ewa_Standard`|
    ||`pl-PL_Jacek_Standard`|
    ||`pl-PL_Jan_Standard`|
    ||`pl-PL_Maja_Standard`|
    ||`pl-PL_Ola_Neural`|
    ||`pt-BR_Camila_Neural`|
    ||`pt-BR_Camila_Standard`|
    ||`pt-BR_Ricardo_Standard`|
    ||`pt-BR_Thiago_Neural`|
    ||`pt-BR_Vitoria_Neural`|
    ||`pt-BR_Vitoria_Standard`|
    ||`pt-PT_Cristiano_Standard`|
    ||`pt-PT_Ines_Neural`|
    ||`pt-PT_Ines_Standard`|
    ||`ro-RO_Carmen_Standard`|
    ||`ru-RU_Maxim_Standard`|
    ||`ru-RU_Tatyana_Standard`|
    ||`sv-SE_Astrid_Standard`|
    ||`sv-SE_Elin_Neural`|
    ||`tr-TR_Filiz_Standard`|
    ||`yue-CN_Hiujin_Neural`|

    </details><details><summary>google</summary>





    |Name|Value|
    |----|-----|
    |**google**|`af-ZA-Standard-A`|
    ||`ar-XA-Standard-A`|
    ||`ar-XA-Standard-B`|
    ||`ar-XA-Standard-C`|
    ||`ar-XA-Standard-D`|
    ||`ar-XA-Wavenet-A`|
    ||`ar-XA-Wavenet-B`|
    ||`ar-XA-Wavenet-C`|
    ||`ar-XA-Wavenet-D`|
    ||`bg-BG-Standard-A`|
    ||`bn-IN-Standard-A`|
    ||`bn-IN-Standard-B`|
    ||`bn-IN-Wavenet-A`|
    ||`bn-IN-Wavenet-B`|
    ||`ca-ES-Standard-A`|
    ||`cmn-CN-Standard-A`|
    ||`cmn-CN-Standard-B`|
    ||`cmn-CN-Standard-C`|
    ||`cmn-CN-Standard-D`|
    ||`cmn-CN-Wavenet-A`|
    ||`cmn-CN-Wavenet-B`|
    ||`cmn-CN-Wavenet-C`|
    ||`cmn-CN-Wavenet-D`|
    ||`cmn-TW-Standard-A`|
    ||`cmn-TW-Standard-B`|
    ||`cmn-TW-Standard-C`|
    ||`cmn-TW-Wavenet-A`|
    ||`cmn-TW-Wavenet-B`|
    ||`cmn-TW-Wavenet-C`|
    ||`cs-CZ-Standard-A`|
    ||`cs-CZ-Wavenet-A`|
    ||`da-DK-Standard-A`|
    ||`da-DK-Standard-C`|
    ||`da-DK-Standard-D`|
    ||`da-DK-Standard-E`|
    ||`da-DK-Wavenet-A`|
    ||`da-DK-Wavenet-C`|
    ||`da-DK-Wavenet-D`|
    ||`da-DK-Wavenet-E`|
    ||`de-DE-Neural2-B`|
    ||`de-DE-Neural2-C`|
    ||`de-DE-Neural2-D`|
    ||`de-DE-Neural2-F`|
    ||`de-DE-Standard-A`|
    ||`de-DE-Standard-B`|
    ||`de-DE-Standard-C`|
    ||`de-DE-Standard-D`|
    ||`de-DE-Standard-E`|
    ||`de-DE-Standard-F`|
    ||`de-DE-Wavenet-A`|
    ||`de-DE-Wavenet-B`|
    ||`de-DE-Wavenet-C`|
    ||`de-DE-Wavenet-D`|
    ||`de-DE-Wavenet-E`|
    ||`de-DE-Wavenet-F`|
    ||`el-GR-Standard-A`|
    ||`el-GR-Wavenet-A`|
    ||`en-AU-Neural2-A`|
    ||`en-AU-Neural2-B`|
    ||`en-AU-Neural2-C`|
    ||`en-AU-Neural2-D`|
    ||`en-AU-News-E`|
    ||`en-AU-News-F`|
    ||`en-AU-News-G`|
    ||`en-AU-Standard-A`|
    ||`en-AU-Standard-B`|
    ||`en-AU-Standard-C`|
    ||`en-AU-Standard-D`|
    ||`en-AU-Wavenet-A`|
    ||`en-AU-Wavenet-B`|
    ||`en-AU-Wavenet-C`|
    ||`en-AU-Wavenet-D`|
    ||`en-GB-Neural2-A`|
    ||`en-GB-Neural2-B`|
    ||`en-GB-Neural2-C`|
    ||`en-GB-Neural2-D`|
    ||`en-GB-Neural2-F`|
    ||`en-GB-News-G`|
    ||`en-GB-News-H`|
    ||`en-GB-News-I`|
    ||`en-GB-News-J`|
    ||`en-GB-News-K`|
    ||`en-GB-News-L`|
    ||`en-GB-News-M`|
    ||`en-GB-Standard-A`|
    ||`en-GB-Standard-B`|
    ||`en-GB-Standard-C`|
    ||`en-GB-Standard-D`|
    ||`en-GB-Standard-F`|
    ||`en-GB-Wavenet-A`|
    ||`en-GB-Wavenet-B`|
    ||`en-GB-Wavenet-C`|
    ||`en-GB-Wavenet-D`|
    ||`en-GB-Wavenet-F`|
    ||`en-IN-Standard-A`|
    ||`en-IN-Standard-B`|
    ||`en-IN-Standard-C`|
    ||`en-IN-Standard-D`|
    ||`en-IN-Wavenet-A`|
    ||`en-IN-Wavenet-B`|
    ||`en-IN-Wavenet-C`|
    ||`en-IN-Wavenet-D`|
    ||`en-US-Neural2-A`|
    ||`en-US-Neural2-C`|
    ||`en-US-Neural2-D`|
    ||`en-US-Neural2-E`|
    ||`en-US-Neural2-F`|
    ||`en-US-Neural2-G`|
    ||`en-US-Neural2-H`|
    ||`en-US-Neural2-I`|
    ||`en-US-Neural2-J`|
    ||`en-US-News-K`|
    ||`en-US-News-L`|
    ||`en-US-News-M`|
    ||`en-US-News-N`|
    ||`en-US-Standard-A`|
    ||`en-US-Standard-B`|
    ||`en-US-Standard-C`|
    ||`en-US-Standard-D`|
    ||`en-US-Standard-E`|
    ||`en-US-Standard-F`|
    ||`en-US-Standard-G`|
    ||`en-US-Standard-H`|
    ||`en-US-Standard-I`|
    ||`en-US-Standard-J`|
    ||`en-US-Studio-M`|
    ||`en-US-Studio-O`|
    ||`en-US-Wavenet-A`|
    ||`en-US-Wavenet-B`|
    ||`en-US-Wavenet-C`|
    ||`en-US-Wavenet-D`|
    ||`en-US-Wavenet-E`|
    ||`en-US-Wavenet-F`|
    ||`en-US-Wavenet-G`|
    ||`en-US-Wavenet-H`|
    ||`en-US-Wavenet-I`|
    ||`en-US-Wavenet-J`|
    ||`es-ES-Neural2-A`|
    ||`es-ES-Neural2-B`|
    ||`es-ES-Neural2-C`|
    ||`es-ES-Neural2-D`|
    ||`es-ES-Neural2-E`|
    ||`es-ES-Neural2-F`|
    ||`es-ES-Standard-A`|
    ||`es-ES-Standard-B`|
    ||`es-ES-Standard-C`|
    ||`es-ES-Standard-D`|
    ||`es-ES-Wavenet-B`|
    ||`es-ES-Wavenet-C`|
    ||`es-ES-Wavenet-D`|
    ||`es-US-Neural2-A`|
    ||`es-US-Neural2-B`|
    ||`es-US-Neural2-C`|
    ||`es-US-News-D`|
    ||`es-US-News-E`|
    ||`es-US-News-F`|
    ||`es-US-News-G`|
    ||`es-US-Standard-A`|
    ||`es-US-Standard-B`|
    ||`es-US-Standard-C`|
    ||`es-US-Studio-B`|
    ||`es-US-Wavenet-A`|
    ||`es-US-Wavenet-B`|
    ||`es-US-Wavenet-C`|
    ||`eu-ES-Standard-A`|
    ||`fi-FI-Standard-A`|
    ||`fi-FI-Wavenet-A`|
    ||`fil-PH-Standard-A`|
    ||`fil-PH-Standard-B`|
    ||`fil-PH-Standard-C`|
    ||`fil-PH-Standard-D`|
    ||`fil-PH-Wavenet-A`|
    ||`fil-PH-Wavenet-B`|
    ||`fil-PH-Wavenet-C`|
    ||`fil-PH-Wavenet-D`|
    ||`fr-CA-Neural2-A`|
    ||`fr-CA-Neural2-B`|
    ||`fr-CA-Neural2-C`|
    ||`fr-CA-Neural2-D`|
    ||`fr-CA-Standard-A`|
    ||`fr-CA-Standard-B`|
    ||`fr-CA-Standard-C`|
    ||`fr-CA-Standard-D`|
    ||`fr-CA-Wavenet-A`|
    ||`fr-CA-Wavenet-B`|
    ||`fr-CA-Wavenet-C`|
    ||`fr-CA-Wavenet-D`|
    ||`fr-FR-Neural2-A`|
    ||`fr-FR-Neural2-B`|
    ||`fr-FR-Neural2-C`|
    ||`fr-FR-Neural2-D`|
    ||`fr-FR-Neural2-E`|
    ||`fr-FR-Standard-A`|
    ||`fr-FR-Standard-B`|
    ||`fr-FR-Standard-C`|
    ||`fr-FR-Standard-D`|
    ||`fr-FR-Standard-E`|
    ||`fr-FR-Wavenet-A`|
    ||`fr-FR-Wavenet-B`|
    ||`fr-FR-Wavenet-C`|
    ||`fr-FR-Wavenet-D`|
    ||`fr-FR-Wavenet-E`|
    ||`gl-ES-Standard-A`|
    ||`gu-IN-Standard-A`|
    ||`gu-IN-Standard-B`|
    ||`gu-IN-Wavenet-A`|
    ||`gu-IN-Wavenet-B`|
    ||`he-IL-Standard-A`|
    ||`he-IL-Standard-B`|
    ||`he-IL-Standard-C`|
    ||`he-IL-Standard-D`|
    ||`he-IL-Wavenet-A`|
    ||`he-IL-Wavenet-B`|
    ||`he-IL-Wavenet-C`|
    ||`he-IL-Wavenet-D`|
    ||`hi-IN-Neural2-A`|
    ||`hi-IN-Neural2-B`|
    ||`hi-IN-Neural2-C`|
    ||`hi-IN-Neural2-D`|
    ||`hi-IN-Standard-A`|
    ||`hi-IN-Standard-B`|
    ||`hi-IN-Standard-C`|
    ||`hi-IN-Standard-D`|
    ||`hi-IN-Wavenet-A`|
    ||`hi-IN-Wavenet-B`|
    ||`hi-IN-Wavenet-C`|
    ||`hi-IN-Wavenet-D`|
    ||`hu-HU-Standard-A`|
    ||`hu-HU-Wavenet-A`|
    ||`id-ID-Standard-A`|
    ||`id-ID-Standard-B`|
    ||`id-ID-Standard-C`|
    ||`id-ID-Standard-D`|
    ||`id-ID-Wavenet-A`|
    ||`id-ID-Wavenet-B`|
    ||`id-ID-Wavenet-C`|
    ||`id-ID-Wavenet-D`|
    ||`is-IS-Standard-A`|
    ||`it-IT-Neural2-A`|
    ||`it-IT-Neural2-C`|
    ||`it-IT-Standard-A`|
    ||`it-IT-Standard-B`|
    ||`it-IT-Standard-C`|
    ||`it-IT-Standard-D`|
    ||`it-IT-Wavenet-A`|
    ||`it-IT-Wavenet-B`|
    ||`it-IT-Wavenet-C`|
    ||`it-IT-Wavenet-D`|
    ||`ja-JP-Neural2-B`|
    ||`ja-JP-Neural2-C`|
    ||`ja-JP-Neural2-D`|
    ||`ja-JP-Standard-A`|
    ||`ja-JP-Standard-B`|
    ||`ja-JP-Standard-C`|
    ||`ja-JP-Standard-D`|
    ||`ja-JP-Wavenet-A`|
    ||`ja-JP-Wavenet-B`|
    ||`ja-JP-Wavenet-C`|
    ||`ja-JP-Wavenet-D`|
    ||`kn-IN-Standard-A`|
    ||`kn-IN-Standard-B`|
    ||`kn-IN-Wavenet-A`|
    ||`kn-IN-Wavenet-B`|
    ||`ko-KR-Neural2-A`|
    ||`ko-KR-Neural2-B`|
    ||`ko-KR-Neural2-C`|
    ||`ko-KR-Standard-A`|
    ||`ko-KR-Standard-B`|
    ||`ko-KR-Standard-C`|
    ||`ko-KR-Standard-D`|
    ||`ko-KR-Wavenet-A`|
    ||`ko-KR-Wavenet-B`|
    ||`ko-KR-Wavenet-C`|
    ||`ko-KR-Wavenet-D`|
    ||`lt-LT-Standard-A`|
    ||`lv-LV-Standard-A`|
    ||`ml-IN-Standard-A`|
    ||`ml-IN-Standard-B`|
    ||`ml-IN-Wavenet-A`|
    ||`ml-IN-Wavenet-B`|
    ||`ml-IN-Wavenet-C`|
    ||`ml-IN-Wavenet-D`|
    ||`mr-IN-Standard-A`|
    ||`mr-IN-Standard-B`|
    ||`mr-IN-Standard-C`|
    ||`mr-IN-Wavenet-A`|
    ||`mr-IN-Wavenet-B`|
    ||`mr-IN-Wavenet-C`|
    ||`ms-MY-Standard-A`|
    ||`ms-MY-Standard-B`|
    ||`ms-MY-Standard-C`|
    ||`ms-MY-Standard-D`|
    ||`ms-MY-Wavenet-A`|
    ||`ms-MY-Wavenet-B`|
    ||`ms-MY-Wavenet-C`|
    ||`ms-MY-Wavenet-D`|
    ||`nb-NO-Standard-A`|
    ||`nb-NO-Standard-B`|
    ||`nb-NO-Standard-C`|
    ||`nb-NO-Standard-D`|
    ||`nb-NO-Standard-E`|
    ||`nb-NO-Wavenet-A`|
    ||`nb-NO-Wavenet-B`|
    ||`nb-NO-Wavenet-C`|
    ||`nb-NO-Wavenet-D`|
    ||`nb-NO-Wavenet-E`|
    ||`nl-BE-Standard-A`|
    ||`nl-BE-Standard-B`|
    ||`nl-BE-Wavenet-A`|
    ||`nl-BE-Wavenet-B`|
    ||`nl-NL-Standard-A`|
    ||`nl-NL-Standard-B`|
    ||`nl-NL-Standard-C`|
    ||`nl-NL-Standard-D`|
    ||`nl-NL-Standard-E`|
    ||`nl-NL-Wavenet-A`|
    ||`nl-NL-Wavenet-B`|
    ||`nl-NL-Wavenet-C`|
    ||`nl-NL-Wavenet-D`|
    ||`nl-NL-Wavenet-E`|
    ||`pa-IN-Standard-A`|
    ||`pa-IN-Standard-B`|
    ||`pa-IN-Standard-C`|
    ||`pa-IN-Standard-D`|
    ||`pa-IN-Wavenet-A`|
    ||`pa-IN-Wavenet-B`|
    ||`pa-IN-Wavenet-C`|
    ||`pa-IN-Wavenet-D`|
    ||`pl-PL-Standard-A`|
    ||`pl-PL-Standard-B`|
    ||`pl-PL-Standard-C`|
    ||`pl-PL-Standard-D`|
    ||`pl-PL-Standard-E`|
    ||`pl-PL-Wavenet-A`|
    ||`pl-PL-Wavenet-B`|
    ||`pl-PL-Wavenet-C`|
    ||`pl-PL-Wavenet-D`|
    ||`pl-PL-Wavenet-E`|
    ||`pt-BR-Neural2-A`|
    ||`pt-BR-Neural2-B`|
    ||`pt-BR-Neural2-C`|
    ||`pt-BR-Standard-A`|
    ||`pt-BR-Standard-B`|
    ||`pt-BR-Standard-C`|
    ||`pt-BR-Wavenet-A`|
    ||`pt-BR-Wavenet-B`|
    ||`pt-BR-Wavenet-C`|
    ||`pt-PT-Standard-A`|
    ||`pt-PT-Standard-B`|
    ||`pt-PT-Standard-C`|
    ||`pt-PT-Standard-D`|
    ||`pt-PT-Wavenet-A`|
    ||`pt-PT-Wavenet-B`|
    ||`pt-PT-Wavenet-C`|
    ||`pt-PT-Wavenet-D`|
    ||`ro-RO-Standard-A`|
    ||`ro-RO-Wavenet-A`|
    ||`ru-RU-Standard-A`|
    ||`ru-RU-Standard-B`|
    ||`ru-RU-Standard-C`|
    ||`ru-RU-Standard-D`|
    ||`ru-RU-Standard-E`|
    ||`ru-RU-Wavenet-A`|
    ||`ru-RU-Wavenet-B`|
    ||`ru-RU-Wavenet-C`|
    ||`ru-RU-Wavenet-D`|
    ||`ru-RU-Wavenet-E`|
    ||`sk-SK-Standard-A`|
    ||`sk-SK-Wavenet-A`|
    ||`sr-RS-Standard-A`|
    ||`sv-SE-Standard-A`|
    ||`sv-SE-Standard-B`|
    ||`sv-SE-Standard-C`|
    ||`sv-SE-Standard-D`|
    ||`sv-SE-Standard-E`|
    ||`sv-SE-Wavenet-A`|
    ||`sv-SE-Wavenet-B`|
    ||`sv-SE-Wavenet-C`|
    ||`sv-SE-Wavenet-D`|
    ||`sv-SE-Wavenet-E`|
    ||`ta-IN-Standard-A`|
    ||`ta-IN-Standard-B`|
    ||`ta-IN-Standard-C`|
    ||`ta-IN-Standard-D`|
    ||`ta-IN-Wavenet-A`|
    ||`ta-IN-Wavenet-B`|
    ||`ta-IN-Wavenet-C`|
    ||`ta-IN-Wavenet-D`|
    ||`te-IN-Standard-A`|
    ||`te-IN-Standard-B`|
    ||`th-TH-Standard-A`|
    ||`tr-TR-Standard-A`|
    ||`tr-TR-Standard-B`|
    ||`tr-TR-Standard-C`|
    ||`tr-TR-Standard-D`|
    ||`tr-TR-Standard-E`|
    ||`tr-TR-Wavenet-A`|
    ||`tr-TR-Wavenet-B`|
    ||`tr-TR-Wavenet-C`|
    ||`tr-TR-Wavenet-D`|
    ||`tr-TR-Wavenet-E`|
    ||`uk-UA-Standard-A`|
    ||`uk-UA-Wavenet-A`|
    ||`vi-VN-Standard-A`|
    ||`vi-VN-Standard-B`|
    ||`vi-VN-Standard-C`|
    ||`vi-VN-Standard-D`|
    ||`vi-VN-Wavenet-A`|
    ||`vi-VN-Wavenet-B`|
    ||`vi-VN-Wavenet-C`|
    ||`vi-VN-Wavenet-D`|
    ||`yue-HK-Standard-A`|
    ||`yue-HK-Standard-B`|
    ||`yue-HK-Standard-C`|
    ||`yue-HK-Standard-D`|

    </details><details><summary>ibm</summary>





    |Name|Value|
    |----|-----|
    |**ibm**|`de-DE_BirgitV3Voice`|
    ||`de-DE_DieterV3Voice`|
    ||`de-DE_ErikaV3Voice`|
    ||`en-AU_HeidiExpressive`|
    ||`en-AU_JackExpressive`|
    ||`en-GB_CharlotteV3Voice`|
    ||`en-GB_JamesV3Voice`|
    ||`en-GB_KateV3Voice`|
    ||`en-US_AllisonExpressive`|
    ||`en-US_AllisonV3Voice`|
    ||`en-US_EmilyV3Voice`|
    ||`en-US_EmmaExpressive`|
    ||`en-US_HenryV3Voice`|
    ||`en-US_KevinV3Voice`|
    ||`en-US_LisaExpressive`|
    ||`en-US_LisaV3Voice`|
    ||`en-US_MichaelExpressive`|
    ||`en-US_MichaelV3Voice`|
    ||`en-US_OliviaV3Voice`|
    ||`es-ES_EnriqueV3Voice`|
    ||`es-ES_LauraV3Voice`|
    ||`es-LA_SofiaV3Voice`|
    ||`es-US_SofiaV3Voice`|
    ||`fr-CA_LouiseV3Voice`|
    ||`fr-FR_NicolasV3Voice`|
    ||`fr-FR_ReneeV3Voice`|
    ||`it-IT_FrancescaV3Voice`|
    ||`ja-JP_EmiV3Voice`|
    ||`ko-KR_JinV3Voice`|
    ||`nl-NL_MerelV3Voice`|
    ||`pt-BR_IsabelaV3Voice`|

    </details><details><summary>microsoft</summary>





    |Name|Value|
    |----|-----|
    |**microsoft**|`af-ZA-AdriNeural`|
    ||`af-ZA-WillemNeural`|
    ||`am-ET-AmehaNeural`|
    ||`am-ET-MekdesNeural`|
    ||`ar-AE-FatimaNeural`|
    ||`ar-AE-HamdanNeural`|
    ||`ar-BH-AliNeural`|
    ||`ar-BH-LailaNeural`|
    ||`ar-DZ-AminaNeural`|
    ||`ar-DZ-IsmaelNeural`|
    ||`ar-EG-SalmaNeural`|
    ||`ar-EG-ShakirNeural`|
    ||`ar-IQ-BasselNeural`|
    ||`ar-IQ-RanaNeural`|
    ||`ar-JO-SanaNeural`|
    ||`ar-JO-TaimNeural`|
    ||`ar-KW-FahedNeural`|
    ||`ar-KW-NouraNeural`|
    ||`ar-LB-LaylaNeural`|
    ||`ar-LB-RamiNeural`|
    ||`ar-LY-ImanNeural`|
    ||`ar-LY-OmarNeural`|
    ||`ar-MA-JamalNeural`|
    ||`ar-MA-MounaNeural`|
    ||`ar-OM-AbdullahNeural`|
    ||`ar-OM-AyshaNeural`|
    ||`ar-QA-AmalNeural`|
    ||`ar-QA-MoazNeural`|
    ||`ar-SA-HamedNeural`|
    ||`ar-SA-ZariyahNeural`|
    ||`ar-SY-AmanyNeural`|
    ||`ar-SY-LaithNeural`|
    ||`ar-TN-HediNeural`|
    ||`ar-TN-ReemNeural`|
    ||`ar-YE-MaryamNeural`|
    ||`ar-YE-SalehNeural`|
    ||`az-AZ-BabekNeural`|
    ||`az-AZ-BanuNeural`|
    ||`bg-BG-BorislavNeural`|
    ||`bg-BG-KalinaNeural`|
    ||`bn-BD-NabanitaNeural`|
    ||`bn-BD-PradeepNeural`|
    ||`bn-IN-BashkarNeural`|
    ||`bn-IN-TanishaaNeural`|
    ||`bs-BA-GoranNeural`|
    ||`bs-BA-VesnaNeural`|
    ||`ca-ES-AlbaNeural`|
    ||`ca-ES-EnricNeural`|
    ||`ca-ES-JoanaNeural`|
    ||`cs-CZ-AntoninNeural`|
    ||`cs-CZ-VlastaNeural`|
    ||`cy-GB-AledNeural`|
    ||`cy-GB-NiaNeural`|
    ||`da-DK-ChristelNeural`|
    ||`da-DK-JeppeNeural`|
    ||`de-AT-IngridNeural`|
    ||`de-AT-JonasNeural`|
    ||`de-CH-JanNeural`|
    ||`de-CH-LeniNeural`|
    ||`de-DE-AmalaNeural`|
    ||`de-DE-BerndNeural`|
    ||`de-DE-ChristophNeural`|
    ||`de-DE-ConradNeural`|
    ||`de-DE-ElkeNeural`|
    ||`de-DE-GiselaNeural`|
    ||`de-DE-KasperNeural`|
    ||`de-DE-KatjaNeural`|
    ||`de-DE-KillianNeural`|
    ||`de-DE-KlarissaNeural`|
    ||`de-DE-KlausNeural`|
    ||`de-DE-LouisaNeural`|
    ||`de-DE-MajaNeural`|
    ||`de-DE-RalfNeural`|
    ||`de-DE-TanjaNeural`|
    ||`el-GR-AthinaNeural`|
    ||`el-GR-NestorasNeural`|
    ||`en-AU-AnnetteNeural`|
    ||`en-AU-CarlyNeural`|
    ||`en-AU-DarrenNeural`|
    ||`en-AU-DuncanNeural`|
    ||`en-AU-ElsieNeural`|
    ||`en-AU-FreyaNeural`|
    ||`en-AU-JoanneNeural`|
    ||`en-AU-KenNeural`|
    ||`en-AU-KimNeural`|
    ||`en-AU-NatashaNeural`|
    ||`en-AU-NeilNeural`|
    ||`en-AU-TimNeural`|
    ||`en-AU-TinaNeural`|
    ||`en-AU-WilliamNeural`|
    ||`en-CA-ClaraNeural`|
    ||`en-CA-LiamNeural`|
    ||`en-GB-AbbiNeural`|
    ||`en-GB-AlfieNeural`|
    ||`en-GB-BellaNeural`|
    ||`en-GB-ElliotNeural`|
    ||`en-GB-EthanNeural`|
    ||`en-GB-HollieNeural`|
    ||`en-GB-LibbyNeural`|
    ||`en-GB-MaisieNeural`|
    ||`en-GB-NoahNeural`|
    ||`en-GB-OliverNeural`|
    ||`en-GB-OliviaNeural`|
    ||`en-GB-RyanNeural`|
    ||`en-GB-SoniaNeural`|
    ||`en-GB-ThomasNeural`|
    ||`en-HK-SamNeural`|
    ||`en-HK-YanNeural`|
    ||`en-IE-ConnorNeural`|
    ||`en-IE-EmilyNeural`|
    ||`en-IN-NeerjaNeural`|
    ||`en-IN-PrabhatNeural`|
    ||`en-KE-AsiliaNeural`|
    ||`en-KE-ChilembaNeural`|
    ||`en-NG-AbeoNeural`|
    ||`en-NG-EzinneNeural`|
    ||`en-NZ-MitchellNeural`|
    ||`en-NZ-MollyNeural`|
    ||`en-PH-JamesNeural`|
    ||`en-PH-RosaNeural`|
    ||`en-SG-LunaNeural`|
    ||`en-SG-WayneNeural`|
    ||`en-TZ-ElimuNeural`|
    ||`en-TZ-ImaniNeural`|
    ||`en-US-AIGenerate1Neural`|
    ||`en-US-AIGenerate2Neural`|
    ||`en-US-AmberNeural`|
    ||`en-US-AnaNeural`|
    ||`en-US-AriaNeural`|
    ||`en-US-AshleyNeural`|
    ||`en-US-BrandonNeural`|
    ||`en-US-ChristopherNeural`|
    ||`en-US-CoraNeural`|
    ||`en-US-DavisNeural`|
    ||`en-US-ElizabethNeural`|
    ||`en-US-EricNeural`|
    ||`en-US-GuyNeural`|
    ||`en-US-JacobNeural`|
    ||`en-US-JaneNeural`|
    ||`en-US-JasonNeural`|
    ||`en-US-JennyMultilingualNeural`|
    ||`en-US-JennyNeural`|
    ||`en-US-MichelleNeural`|
    ||`en-US-MonicaNeural`|
    ||`en-US-NancyNeural`|
    ||`en-US-RogerNeural`|
    ||`en-US-SaraNeural`|
    ||`en-US-SteffanNeural`|
    ||`en-US-TonyNeural`|
    ||`en-ZA-LeahNeural`|
    ||`en-ZA-LukeNeural`|
    ||`es-AR-ElenaNeural`|
    ||`es-AR-TomasNeural`|
    ||`es-BO-MarceloNeural`|
    ||`es-BO-SofiaNeural`|
    ||`es-CL-CatalinaNeural`|
    ||`es-CL-LorenzoNeural`|
    ||`es-CO-GonzaloNeural`|
    ||`es-CO-SalomeNeural`|
    ||`es-CR-JuanNeural`|
    ||`es-CR-MariaNeural`|
    ||`es-CU-BelkysNeural`|
    ||`es-CU-ManuelNeural`|
    ||`es-DO-EmilioNeural`|
    ||`es-DO-RamonaNeural`|
    ||`es-EC-AndreaNeural`|
    ||`es-EC-LuisNeural`|
    ||`es-ES-AbrilNeural`|
    ||`es-ES-AlvaroNeural`|
    ||`es-ES-ArnauNeural`|
    ||`es-ES-DarioNeural`|
    ||`es-ES-EliasNeural`|
    ||`es-ES-ElviraNeural`|
    ||`es-ES-EstrellaNeural`|
    ||`es-ES-IreneNeural`|
    ||`es-ES-LaiaNeural`|
    ||`es-ES-LiaNeural`|
    ||`es-ES-NilNeural`|
    ||`es-ES-SaulNeural`|
    ||`es-ES-TeoNeural`|
    ||`es-ES-TrianaNeural`|
    ||`es-ES-VeraNeural`|
    ||`es-GQ-JavierNeural`|
    ||`es-GQ-TeresaNeural`|
    ||`es-GT-AndresNeural`|
    ||`es-GT-MartaNeural`|
    ||`es-HN-CarlosNeural`|
    ||`es-HN-KarlaNeural`|
    ||`es-MX-BeatrizNeural`|
    ||`es-MX-CandelaNeural`|
    ||`es-MX-CarlotaNeural`|
    ||`es-MX-CecilioNeural`|
    ||`es-MX-DaliaNeural`|
    ||`es-MX-GerardoNeural`|
    ||`es-MX-JorgeNeural`|
    ||`es-MX-LarissaNeural`|
    ||`es-MX-LibertoNeural`|
    ||`es-MX-LucianoNeural`|
    ||`es-MX-MarinaNeural`|
    ||`es-MX-NuriaNeural`|
    ||`es-MX-PelayoNeural`|
    ||`es-MX-RenataNeural`|
    ||`es-MX-YagoNeural`|
    ||`es-NI-FedericoNeural`|
    ||`es-NI-YolandaNeural`|
    ||`es-PA-MargaritaNeural`|
    ||`es-PA-RobertoNeural`|
    ||`es-PE-AlexNeural`|
    ||`es-PE-CamilaNeural`|
    ||`es-PR-KarinaNeural`|
    ||`es-PR-VictorNeural`|
    ||`es-PY-MarioNeural`|
    ||`es-PY-TaniaNeural`|
    ||`es-SV-LorenaNeural`|
    ||`es-SV-RodrigoNeural`|
    ||`es-US-AlonsoNeural`|
    ||`es-US-PalomaNeural`|
    ||`es-UY-MateoNeural`|
    ||`es-UY-ValentinaNeural`|
    ||`es-VE-PaolaNeural`|
    ||`es-VE-SebastianNeural`|
    ||`et-EE-AnuNeural`|
    ||`et-EE-KertNeural`|
    ||`eu-ES-AinhoaNeural`|
    ||`eu-ES-AnderNeural`|
    ||`fa-IR-DilaraNeural`|
    ||`fa-IR-FaridNeural`|
    ||`fi-FI-HarriNeural`|
    ||`fi-FI-NooraNeural`|
    ||`fi-FI-SelmaNeural`|
    ||`fil-PH-AngeloNeural`|
    ||`fil-PH-BlessicaNeural`|
    ||`fr-BE-CharlineNeural`|
    ||`fr-BE-GerardNeural`|
    ||`fr-CA-AntoineNeural`|
    ||`fr-CA-JeanNeural`|
    ||`fr-CA-SylvieNeural`|
    ||`fr-CH-ArianeNeural`|
    ||`fr-CH-FabriceNeural`|
    ||`fr-FR-AlainNeural`|
    ||`fr-FR-BrigitteNeural`|
    ||`fr-FR-CelesteNeural`|
    ||`fr-FR-ClaudeNeural`|
    ||`fr-FR-CoralieNeural`|
    ||`fr-FR-DeniseNeural`|
    ||`fr-FR-EloiseNeural`|
    ||`fr-FR-HenriNeural`|
    ||`fr-FR-JacquelineNeural`|
    ||`fr-FR-JeromeNeural`|
    ||`fr-FR-JosephineNeural`|
    ||`fr-FR-MauriceNeural`|
    ||`fr-FR-YvesNeural`|
    ||`fr-FR-YvetteNeural`|
    ||`ga-IE-ColmNeural`|
    ||`ga-IE-OrlaNeural`|
    ||`gl-ES-RoiNeural`|
    ||`gl-ES-SabelaNeural`|
    ||`gu-IN-DhwaniNeural`|
    ||`gu-IN-NiranjanNeural`|
    ||`he-IL-AvriNeural`|
    ||`he-IL-HilaNeural`|
    ||`hi-IN-MadhurNeural`|
    ||`hi-IN-SwaraNeural`|
    ||`hr-HR-GabrijelaNeural`|
    ||`hr-HR-SreckoNeural`|
    ||`hu-HU-NoemiNeural`|
    ||`hu-HU-TamasNeural`|
    ||`hy-AM-AnahitNeural`|
    ||`hy-AM-HaykNeural`|
    ||`id-ID-ArdiNeural`|
    ||`id-ID-GadisNeural`|
    ||`is-IS-GudrunNeural`|
    ||`is-IS-GunnarNeural`|
    ||`it-IT-BenignoNeural`|
    ||`it-IT-CalimeroNeural`|
    ||`it-IT-CataldoNeural`|
    ||`it-IT-DiegoNeural`|
    ||`it-IT-ElsaNeural`|
    ||`it-IT-FabiolaNeural`|
    ||`it-IT-FiammaNeural`|
    ||`it-IT-GianniNeural`|
    ||`it-IT-ImeldaNeural`|
    ||`it-IT-IrmaNeural`|
    ||`it-IT-IsabellaNeural`|
    ||`it-IT-LisandroNeural`|
    ||`it-IT-PalmiraNeural`|
    ||`it-IT-PierinaNeural`|
    ||`it-IT-RinaldoNeural`|
    ||`ja-JP-AoiNeural`|
    ||`ja-JP-DaichiNeural`|
    ||`ja-JP-KeitaNeural`|
    ||`ja-JP-MayuNeural`|
    ||`ja-JP-NanamiNeural`|
    ||`ja-JP-NaokiNeural`|
    ||`ja-JP-ShioriNeural`|
    ||`jv-ID-DimasNeural`|
    ||`jv-ID-SitiNeural`|
    ||`ka-GE-EkaNeural`|
    ||`ka-GE-GiorgiNeural`|
    ||`kk-KZ-AigulNeural`|
    ||`kk-KZ-DauletNeural`|
    ||`km-KH-PisethNeural`|
    ||`km-KH-SreymomNeural`|
    ||`kn-IN-GaganNeural`|
    ||`kn-IN-SapnaNeural`|
    ||`ko-KR-BongJinNeural`|
    ||`ko-KR-GookMinNeural`|
    ||`ko-KR-InJoonNeural`|
    ||`ko-KR-JiMinNeural`|
    ||`ko-KR-SeoHyeonNeural`|
    ||`ko-KR-SoonBokNeural`|
    ||`ko-KR-SunHiNeural`|
    ||`ko-KR-YuJinNeural`|
    ||`lo-LA-ChanthavongNeural`|
    ||`lo-LA-KeomanyNeural`|
    ||`lt-LT-LeonasNeural`|
    ||`lt-LT-OnaNeural`|
    ||`lv-LV-EveritaNeural`|
    ||`lv-LV-NilsNeural`|
    ||`mk-MK-AleksandarNeural`|
    ||`mk-MK-MarijaNeural`|
    ||`ml-IN-MidhunNeural`|
    ||`ml-IN-SobhanaNeural`|
    ||`mn-MN-BataaNeural`|
    ||`mn-MN-YesuiNeural`|
    ||`mr-IN-AarohiNeural`|
    ||`mr-IN-ManoharNeural`|
    ||`ms-MY-OsmanNeural`|
    ||`ms-MY-YasminNeural`|
    ||`mt-MT-GraceNeural`|
    ||`mt-MT-JosephNeural`|
    ||`my-MM-NilarNeural`|
    ||`my-MM-ThihaNeural`|
    ||`nb-NO-FinnNeural`|
    ||`nb-NO-IselinNeural`|
    ||`nb-NO-PernilleNeural`|
    ||`ne-NP-HemkalaNeural`|
    ||`ne-NP-SagarNeural`|
    ||`nl-BE-ArnaudNeural`|
    ||`nl-BE-DenaNeural`|
    ||`nl-NL-ColetteNeural`|
    ||`nl-NL-FennaNeural`|
    ||`nl-NL-MaartenNeural`|
    ||`pl-PL-AgnieszkaNeural`|
    ||`pl-PL-MarekNeural`|
    ||`pl-PL-ZofiaNeural`|
    ||`ps-AF-GulNawazNeural`|
    ||`ps-AF-LatifaNeural`|
    ||`pt-BR-AntonioNeural`|
    ||`pt-BR-BrendaNeural`|
    ||`pt-BR-DonatoNeural`|
    ||`pt-BR-ElzaNeural`|
    ||`pt-BR-FabioNeural`|
    ||`pt-BR-FranciscaNeural`|
    ||`pt-BR-GiovannaNeural`|
    ||`pt-BR-HumbertoNeural`|
    ||`pt-BR-JulioNeural`|
    ||`pt-BR-LeilaNeural`|
    ||`pt-BR-LeticiaNeural`|
    ||`pt-BR-ManuelaNeural`|
    ||`pt-BR-NicolauNeural`|
    ||`pt-BR-ValerioNeural`|
    ||`pt-BR-YaraNeural`|
    ||`pt-PT-DuarteNeural`|
    ||`pt-PT-FernandaNeural`|
    ||`pt-PT-RaquelNeural`|
    ||`ro-RO-AlinaNeural`|
    ||`ro-RO-EmilNeural`|
    ||`ru-RU-DariyaNeural`|
    ||`ru-RU-DmitryNeural`|
    ||`ru-RU-SvetlanaNeural`|
    ||`si-LK-SameeraNeural`|
    ||`si-LK-ThiliniNeural`|
    ||`sk-SK-LukasNeural`|
    ||`sk-SK-ViktoriaNeural`|
    ||`sl-SI-PetraNeural`|
    ||`sl-SI-RokNeural`|
    ||`so-SO-MuuseNeural`|
    ||`so-SO-UbaxNeural`|
    ||`sq-AL-AnilaNeural`|
    ||`sq-AL-IlirNeural`|
    ||`sr-RS-NicholasNeural`|
    ||`sr-RS-SophieNeural`|
    ||`su-ID-JajangNeural`|
    ||`su-ID-TutiNeural`|
    ||`sv-SE-HilleviNeural`|
    ||`sv-SE-MattiasNeural`|
    ||`sv-SE-SofieNeural`|
    ||`sw-KE-RafikiNeural`|
    ||`sw-KE-ZuriNeural`|
    ||`sw-TZ-DaudiNeural`|
    ||`sw-TZ-RehemaNeural`|
    ||`ta-IN-PallaviNeural`|
    ||`ta-IN-ValluvarNeural`|
    ||`ta-LK-KumarNeural`|
    ||`ta-LK-SaranyaNeural`|
    ||`ta-MY-KaniNeural`|
    ||`ta-MY-SuryaNeural`|
    ||`ta-SG-AnbuNeural`|
    ||`ta-SG-VenbaNeural`|
    ||`te-IN-MohanNeural`|
    ||`te-IN-ShrutiNeural`|
    ||`th-TH-AcharaNeural`|
    ||`th-TH-NiwatNeural`|
    ||`th-TH-PremwadeeNeural`|
    ||`tr-TR-AhmetNeural`|
    ||`tr-TR-EmelNeural`|
    ||`uk-UA-OstapNeural`|
    ||`uk-UA-PolinaNeural`|
    ||`ur-IN-GulNeural`|
    ||`ur-IN-SalmanNeural`|
    ||`ur-PK-AsadNeural`|
    ||`ur-PK-UzmaNeural`|
    ||`uz-UZ-MadinaNeural`|
    ||`uz-UZ-SardorNeural`|
    ||`vi-VN-HoaiMyNeural`|
    ||`vi-VN-NamMinhNeural`|
    ||`wuu-CN-XiaotongNeural`|
    ||`wuu-CN-YunzheNeural`|
    ||`yue-CN-XiaoMinNeural`|
    ||`yue-CN-YunSongNeural`|
    ||`zh-CN-XiaochenNeural`|
    ||`zh-CN-XiaohanNeural`|
    ||`zh-CN-XiaomengNeural`|
    ||`zh-CN-XiaomoNeural`|
    ||`zh-CN-XiaoqiuNeural`|
    ||`zh-CN-XiaoruiNeural`|
    ||`zh-CN-XiaoshuangNeural`|
    ||`zh-CN-XiaoxiaoNeural`|
    ||`zh-CN-XiaoxuanNeural`|
    ||`zh-CN-XiaoyanNeural`|
    ||`zh-CN-XiaoyiNeural`|
    ||`zh-CN-XiaoyouNeural`|
    ||`zh-CN-XiaozhenNeural`|
    ||`zh-CN-YunfengNeural`|
    ||`zh-CN-YunhaoNeural`|
    ||`zh-CN-YunjianNeural`|
    ||`zh-CN-YunxiNeural`|
    ||`zh-CN-YunxiaNeural`|
    ||`zh-CN-YunyangNeural`|
    ||`zh-CN-YunyeNeural`|
    ||`zh-CN-YunzeNeural`|
    ||`zh-CN-henan-YundengNeural`|
    ||`zh-CN-liaoning-XiaobeiNeural`|
    ||`zh-CN-shaanxi-XiaoniNeural`|
    ||`zh-CN-shandong-YunxiangNeural`|
    ||`zh-CN-sichuan-YunxiNeural`|
    ||`zh-HK-HiuGaaiNeural`|
    ||`zh-HK-HiuMaanNeural`|
    ||`zh-HK-WanLungNeural`|
    ||`zh-TW-HsiaoChenNeural`|
    ||`zh-TW-HsiaoYuNeural`|
    ||`zh-TW-YunJheNeural`|
    ||`zu-ZA-ThandoNeural`|
    ||`zu-ZA-ThembaNeural`|

    </details><details><summary>lovoai</summary>





    |Name|Value|
    |----|-----|
    |**lovoai**|`af-ZA_Albertus Ruan`|
    ||`af-ZA_Danelle Wessel`|
    ||`am-ET_Abai Berhe`|
    ||`am-ET_Cherenet Tesfaye`|
    ||`ar-AE_Mansour Ahmed`|
    ||`ar-AE_Maryam Khan`|
    ||`ar-BH_Fatima Kumar`|
    ||`ar-BH_Omar Hassan`|
    ||`ar-DZ_Samia Touati`|
    ||`ar-DZ_Zuthimalin Brahimi`|
    ||`ar-EG_Ahmed Gamal`|
    ||`ar-EG_Reem Salah`|
    ||`ar-IQ_Aveen Majid`|
    ||`ar-IQ_Ismail Hashem`|
    ||`ar-JO_Fatima Jaber`|
    ||`ar-JO_Yousef Saleh`|
    ||`ar-KW_Areej Nair`|
    ||`ar-KW_Khaled Al Azmi`|
    ||`ar-LB_Abdel El Din`|
    ||`ar-LB_Eessa Kadifa`|
    ||`ar-LY_Abir Salem`|
    ||`ar-LY_Ahsan Omar`|
    ||`ar-MA_Hamid Bennani`|
    ||`ar-MA_Salma Naciri`|
    ||`ar-OM_Jabbar Singh`|
    ||`ar-OM_Zahra Sultan`|
    ||`ar-QA_Faizur Kumar`|
    ||`ar-QA_Noora Hussain`|
    ||`ar-SA_Majidah Khan`|
    ||`ar-SA_Omar Aziz`|
    ||`ar-SY_Oraida El-Assad`|
    ||`ar-SY_Rabah Ibrahim`|
    ||`ar-TN_Donia Cherif`|
    ||`ar-TN_Karim Dridi`|
    ||`ar-YE_Mansour Kasim`|
    ||`ar-YE_Mehdi Bawazeer`|
    ||`az-AZ_Ugur Quliyeva`|
    ||`az_AZ_Zeynab Cafarova`|
    ||`bg-BG_Damyan Ivanov`|
    ||`bg-BG_Fidanka Georgiev`|
    ||`bn-BD_Pranshu Akter`|
    ||`bn-BD_Vaagdevi Khatun`|
    ||`bn-IN_Gazi Mondal`|
    ||`bn-IN_Wali Ghosh`|
    ||`bs-BA_Esma Dodik`|
    ||`bs-BA_Ismet Rakic`|
    ||`ca-ES_Amada Fernando`|
    ||`ca-ES_Carmen Santiago`|
    ||`ca-ES_Miguel Torres`|
    ||`cs-CZ_Jana Rosicky`|
    ||`cs-CZ_Tomas Malecek`|
    ||`cy-GB_Branwen Jones`|
    ||`cy-GB_Elen Hughes`|
    ||`da-DK_Bjarne Jensen`|
    ||`da-DK_Helge Nielsen`|
    ||`de-AT_Lena Gruber`|
    ||`de-AT_Wilhelm Wagner`|
    ||`de-CH_Adolfus Meier`|
    ||`de-CH_Lara Keller`|
    ||`de-DE_Ada Weber`|
    ||`de-DE_Anna Schmidt`|
    ||`de-DE_Emma Muller`|
    ||`de-DE_Gerda Becker`|
    ||`de-DE_Hans Schulz`|
    ||`de-DE_Heidi Schneider`|
    ||`de-DE_Johanna Meyer`|
    ||`de-DE_Joshua Bauer`|
    ||`de-DE_Julian Koch`|
    ||`de-DE_Karl Hummels`|
    ||`de-DE_Maria Fischer`|
    ||`de-DE_Oliver Richter`|
    ||`de-DE_Otto Schaefer`|
    ||`de-DE_Petra Hoffman`|
    ||`de-DE_Walter Kimmich`|
    ||`el-GR_Petros Andino`|
    ||`el-GR_Thalia Klisiaris`|
    ||`en-AU_Amelia Taylor`|
    ||`en-AU_Charlotte Brown`|
    ||`en-AU_Darrell Robinson`|
    ||`en-AU_George Thompson`|
    ||`en-AU_Georgie Smith`|
    ||`en-AU_Isla Johnson`|
    ||`en-AU_Jake Nguyen`|
    ||`en-AU_Keegan Walker`|
    ||`en-AU_Kelly Opie`|
    ||`en-AU_Kevin Turner`|
    ||`en-AU_Mia White`|
    ||`en-AU_Nancy Jones`|
    ||`en-AU_Ryan Murphy`|
    ||`en-AU_Willow Martin`|
    ||`en-CA_Emily Salo`|
    ||`en-CA_Eric Fidyk`|
    ||`en-GB_Abigail Fraser`|
    ||`en-GB_Annie Smith`|
    ||`en-GB_Gertrude Baker`|
    ||`en-GB_Ian Kensington`|
    ||`en-GB_Kane Tooney`|
    ||`en-GB_Kelsey Michaels`|
    ||`en-GB_Kerrington Pacey`|
    ||`en-GB_Lizzy Wright`|
    ||`en-GB_Marcus O'Donell`|
    ||`en-GB_Nathaniel Jacobs`|
    ||`en-GB_Samuel Lee-Richards`|
    ||`en-GB_T.S. Cooper`|
    ||`en-GB_Theresa King`|
    ||`en-GB_William Tripp`|
    ||`en-HK_Heather Yiu`|
    ||`en-HK_Kevin Lau`|
    ||`en-IE_Aoife Byrne`|
    ||`en-IE_Bill Parkin`|
    ||`en-IN_Isha Singh`|
    ||`en-IN_Prabhdeep Patel`|
    ||`en-KE_Almasi Otieno`|
    ||`en-KE_Chitundu Mwangi`|
    ||`en-NG_Blessing Musa`|
    ||`en-NG_Kehinde Sade`|
    ||`en-NZ_Benson Duncan`|
    ||`en-NZ_Destiny Mitchell`|
    ||`en-PH_Angel dela Cruz`|
    ||`en-PH_Francis Reynaldo`|
    ||`en-SG_Chris Tan`|
    ||`en-SG_Rachel Ng`|
    ||`en-TZ_Busara Charles`|
    ||`en-TZ_Darweshi Juma`|
    ||`en-US_Alysha Imani`|
    ||`en-US_Betty Parker`|
    ||`en-US_Catherine Zania`|
    ||`en-US_Christopher Navarrez`|
    ||`en-US_Clara Ho`|
    ||`en-US_Eric Gonzalez`|
    ||`en-US_Heather Everett`|
    ||`en-US_Jamal Starke`|
    ||`en-US_Jasonna Johnson`|
    ||`en-US_Kaylee Montana`|
    ||`en-US_Ken hunter`|
    ||`en-US_Kim Howard`|
    ||`en-US_Kyle Moreno`|
    ||`en-US_Leroy Alshak`|
    ||`en-US_Micah Washington`|
    ||`en-US_Molly Richardson`|
    ||`en-US_Peter Lee`|
    ||`en-US_Phil Gough`|
    ||`en-US_Phoebe Nicholson`|
    ||`en-US_Samantha Hawthorne`|
    ||`en-US_Sean Orson`|
    ||`en-US_Serena Yang`|
    ||`en-US_Shannon Mechare`|
    ||`en-US_Thelma Browne`|
    ||`en-US_Tim Hardway`|
    ||`en-ZA_Cody Fergudson`|
    ||`en-ZA_Elna VanDijk`|
    ||`es-AR_Hyacinthe Castro`|
    ||`es-AR_Lautaro Gomez`|
    ||`es-BO_Elena Lopez`|
    ||`es-BO_Juan Perez`|
    ||`es-CL_Francisca Batistuta`|
    ||`es-CL_Gabriel Rodriguez`|
    ||`es-CO_Lorenzo Vazquez`|
    ||`es-CO_Sofia Garcia`|
    ||`es-CR_Guadalupe Suarez`|
    ||`es-CR_Sebastian Ramos`|
    ||`es-CU_Isabel Molina`|
    ||`es-CU_Luis Ortega`|
    ||`es-DO_Gabriela Serrano`|
    ||`es-DO_Raul Dominguez`|
    ||`es-EC_Angelina Romero`|
    ||`es-EC_Christian Diaz`|
    ||`es-EN_Carmen Martinela`|
    ||`es-ES_Andres Marin`|
    ||`es-ES_Emiliano Delgado`|
    ||`es-ES_Esmeralda Molina`|
    ||`es-ES_Hector Gavi`|
    ||`es-ES_Leo Gil`|
    ||`es-ES_Liliana Sanz`|
    ||`es-ES_Maria Ruiz`|
    ||`es-ES_Martin Enrique`|
    ||`es-ES_Miranda Navarro`|
    ||`es-ES_Pablo Iniesta`|
    ||`es-ES_Silvia Alvarez`|
    ||`es-ES_Teresa Iglesias`|
    ||`es-ES_Valentina Blanco`|
    ||`es-GQ_Elena Rubio`|
    ||`es-GQ_Teo Jimenez`|
    ||`es-GT_Ceciah Mendoza`|
    ||`es-GT_Paolo Ortiz`|
    ||`es-HN_Juana Flores`|
    ||`es-HN_Roberto Gutierrez`|
    ||`es-MX_Agata Albiol`|
    ||`es-MX_Darion Nunez`|
    ||`es-MX_Elias Lorenzo`|
    ||`es-MX_Elvira de Paul`|
    ||`es-MX_Enzo Paqueta`|
    ||`es-MX_Ezequiel Pacheco`|
    ||`es-MX_Iago Domingo`|
    ||`es-MX_Irene Vasquez`|
    ||`es-MX_Julieta Aguilar`|
    ||`es-MX_Lia Medina`|
    ||`es-MX_Nil Alvarez`|
    ||`es-MX_Pedro Rojas`|
    ||`es-MX_Rosa Valdoza`|
    ||`es-MX_Valencia Alba`|
    ||`es-MX_Veronica Mairal`|
    ||`es-NI_Abril Santacruz`|
    ||`es-NI_Lorenzo Llorente`|
    ||`es-PA_Liberto Marcos`|
    ||`es-PA_Yolanda Ezequiel`|
    ||`es-PE_Margarita de Fuentes`|
    ||`es-PE_Rey Sancho`|
    ||`es-PR_Alex de Santos`|
    ||`es-PR_Carlota Almiron`|
    ||`es-PY_Karina Diego`|
    ||`es-PY_Victor Mariela`|
    ||`es-SV_Jacinta Vela`|
    ||`es-SV_Marina Llorente`|
    ||`es-US_Jodrigo Alonso`|
    ||`es-US_Laia Paloma`|
    ||`es-US_Sergio Morata`|
    ||`es-UY_Lia Valentina`|
    ||`es-UY_Luis Ramon`|
    ||`es-VE_Manuel Rojos`|
    ||`es-VE_Sofia Vargas`|
    ||`et-EE_Barba Sepp`|
    ||`et-EE_Eduk Tamm`|
    ||`eu-ES_Markel Zubiri`|
    ||`eu-ES_Nahia Texpare`|
    ||`fa-IR_Bizhan Gilgamesh`|
    ||`fa-IR_Yasmina Hakimi`|
    ||`fi-FI_Anneli Niemnien`|
    ||`fi-FI_Kristiina Koskinen`|
    ||`fi-FI_Tapanni Korhonen`|
    ||`fil-PH_Amihan Reyes`|
    ||`fil-PH_Dennis de Saul`|
    ||`fr-BE_Louis Maes`|
    ||`fr-BE_Noah Peeters`|
    ||`fr-CA_Cherise DuPont`|
    ||`fr-CA_Olivier Varane`|
    ||`fr-CA_Raphael Jacques`|
    ||`fr-CH_Luca Dalot`|
    ||`fr-CH_Sylvie Gallace`|
    ||`fr-FR_Alain Hamel`|
    ||`fr-FR_Albertine Dubois`|
    ||`fr-FR_Antoine Petit`|
    ||`fr-FR_Brigitte Richard`|
    ||`fr-FR_Celeste Lefevre`|
    ||`fr-FR_Celine Bundchen`|
    ||`fr-FR_Damian Trezeguet`|
    ||`fr-FR_Diogo Pavard`|
    ||`fr-FR_Francoise LaFont`|
    ||`fr-FR_Gisele Guerin`|
    ||`fr-FR_Hugo Duval`|
    ||`fr-FR_Jacqueline Simon`|
    ||`fr-FR_Lois Allaire`|
    ||`fr-FR_Theo Bernard`|
    ||`ga-IE_Anja O'Brien`|
    ||`ga-IE_Liam Murphy`|
    ||`gl-ES_Clara Campos`|
    ||`gl-ES_Nicolas Montoya`|
    ||`gu-IN_Arzoo Chowdhury`|
    ||`gu-IN_Pramukh Barot`|
    ||`he-IL_Avi Goldmann`|
    ||`he-IL_Yael Haddad`|
    ||`hi-IN_Ashwin Nikhil`|
    ||`hi-IN_Uma Aravind`|
    ||`hr-HR_Krasna Perisic`|
    ||`hr-HR_Luka Horvat`|
    ||`hu-HU_Endre Szabo`|
    ||`hu-HU_Zoe Nagy`|
    ||`hy-AM_Arpi Hovhannisyan`|
    ||`hy-AM_Gor Grigoryan`|
    ||`id-ID_Bagaskoro Ulunjandi`|
    ||`id-ID_Diah Sukatendel`|
    ||`is-IS_Fridrika Sigurdsson`|
    ||`is-IS_Olafur Jonsdottir`|
    ||`it-IT_Alessandro Ferrari`|
    ||`it-IT_Alessia Ricci`|
    ||`it-IT_Allegra Greco`|
    ||`it-IT_Angelo Bianchi`|
    ||`it-IT_Antonio Colombo`|
    ||`it-IT_Eva De Luca`|
    ||`it-IT_Filomena Mancini`|
    ||`it-IT_Francesco Rossi`|
    ||`it-IT_Gaia Marino`|
    ||`it-IT_Gemma Conti`|
    ||`it-IT_Gianluigi Russo`|
    ||`it-IT_Greta Bruno`|
    ||`it-IT_Marco Romano`|
    ||`it-IT_Paul Esposito`|
    ||`it-IT_Serafina Gallo`|
    ||`ja-JP_Ayaka Musashi`|
    ||`ja-JP_Hiromi Tanaka`|
    ||`ja-JP_Hiroshi Maeda`|
    ||`ja-JP_Ichiro Sayaka`|
    ||`ja-JP_Naomi Sora`|
    ||`ja-JP_Sartoshi Juno`|
    ||`ja-JP_Sayuri Watanabe`|
    ||`jv-ID_Anom Zees`|
    ||`jv-ID_Bratawati Pulukadang`|
    ||`ka-GE_Ava Lomidze`|
    ||`ka-GE_Elijah Maisuradze`|
    ||`kk-KZ_Nurislam Omarov`|
    ||`kk-KZ_Rayana Kenes`|
    ||`km-KH_Chanthou Sok`|
    ||`km-KH_Kaliyanei Chea`|
    ||`kn-IN_Aadesh Madar`|
    ||`kn-IN_Rhyah Nayka`|
    ||`ko-KR_Eunjin Bae`|
    ||`ko-KR_Heechul Kim`|
    ||`ko-KR_Isu Choi`|
    ||`ko-KR_Jisoo Han`|
    ||`ko-KR_Meesun Kang`|
    ||`ko-KR_Minjoon Lee`|
    ||`ko-KR_Seung Hee Hwang`|
    ||`ko-KR_Yoosung Park`|
    ||`lo-LA_Lawan Vang`|
    ||`lo-LA_Sengphet Inthavong`|
    ||`lt-LT_Nojus Antanas`|
    ||`lt-LT_Ruta Bagdonas`|
    ||`lv-LV_Mozus Berzina`|
    ||`lv-LV_Santa Ozola`|
    ||`mk-MK_Berislav Stojanovski`|
    ||`mk-MK_Smaragda Jovanovska`|
    ||`ml-IN_Abha Nair`|
    ||`ml-IN_Akhil Kumar`|
    ||`mn-MN_Altan Batbayar`|
    ||`mn-MN_Enkhjargal Ganbold`|
    ||`mr-IN_Mihir Chitre`|
    ||`mr-IN_Vedvika Deo`|
    ||`ms-MY_Nur Tengku`|
    ||`ms-MY_Zikri Wan`|
    ||`mt-MT_Lola Farrugia`|
    ||`mt-MT_Milo Borg`|
    ||`my-MM_Dedan Khin`|
    ||`my-MM_Eindra Aung`|
    ||`nb-NO_Henrik Larsen`|
    ||`nb-NO_Vilde Hansen`|
    ||`nb_NO_Malin Pedersen`|
    ||`ne-NP_Batsal Khadka`|
    ||`ne-NP_Druhi Mahat`|
    ||`nl-BE_Arthur Mertens`|
    ||`nl-BE_Martine Claes`|
    ||`nl-NL_Adriana De Vries`|
    ||`nl-NL_Helena De Jong`|
    ||`nl-NL_Jan Visser`|
    ||`pl-PL_Ewa Grabowski`|
    ||`pl-PL_Piotr Duda`|
    ||`pl-PL_Zuzanna Kackz`|
    ||`ps-AF_Abdul-Alim Sayyid`|
    ||`ps-AF_Zahra Qurban`|
    ||`pt-BR_Adriana Rocha`|
    ||`pt-BR_Ana Bahiense`|
    ||`pt-BR_Anabella Teixeira`|
    ||`pt-BR_Antonia Macedo`|
    ||`pt-BR_Antonio Barros`|
    ||`pt-BR_Fernanda Pedreira`|
    ||`pt-BR_Francisco Guimaraes`|
    ||`pt-BR_Joao Azevedo`|
    ||`pt-BR_Jose Almeida`|
    ||`pt-BR_Juliana Costa`|
    ||`pt-BR_Marcia Ribeiro`|
    ||`pt-BR_Maria Cardoso`|
    ||`pt-BR_Paulo Correia`|
    ||`pt-BR_Pedro Magalhaes`|
    ||`pt-BR_Roberto Braga`|
    ||`pt-PT_Benedita Motta`|
    ||`pt-PT_Renato Matos`|
    ||`pt-PT_Rita Oliveira`|
    ||`ro-RO_Cristian Ionescu`|
    ||`ro-RO_Mirabela Gheata`|
    ||`ru-RU_Galina Ivanov`|
    ||`ru-RU_Nadezhda Smirnoff`|
    ||`ru-RU_Pyotr Semenov`|
    ||`si-LK_Kasun Perera`|
    ||`si-LK_Saanvi de Silva`|
    ||`sk-SK_Havel Varga`|
    ||`sk-SK_Olga Kovac`|
    ||`sl-SI_Neza Mlakar`|
    ||`sl-SI_Nik Krajnc`|
    ||`so-SO_Axado Ibrahim`|
    ||`so-SO_Taifa Mohamed`|
    ||`sq-AL_Bora Marku`|
    ||`sq-AL_Dren Kedare`|
    ||`sr-RS_Lara Markovic`|
    ||`sr-RS_Vlado Popovic`|
    ||`su-ID_Aarifa Bol`|
    ||`su-ID_Mustafa Deng`|
    ||`sv-SE_Agnes Lidstrom`|
    ||`sv-SE_Nicklas Forsberg`|
    ||`sv-SE_Wilma Sundin`|
    ||`sw-KE_Akeyo Njoroge`|
    ||`sw-KE_Chege Odhiambo`|
    ||`sw-TZ_Binti Ramadhani`|
    ||`sw-TZ_Darweshi Ally`|
    ||`ta-IN_Ashwin Kumar`|
    ||`ta-IN_Nila Suresh`|
    ||`ta-LK_Adya Pillai`|
    ||`ta-LK_Prahan Aachari`|
    ||`ta-MY_Aahna Konar`|
    ||`ta-MY_Kethan Nadar`|
    ||`ta-SG_Abilasha Naicker`|
    ||`ta-SG_Nemi Udayar`|
    ||`te-IN_Aarkash Reddy`|
    ||`te-IN_Tanvi Sharma`|
    ||`th-TH_Buppha Prasit`|
    ||`th-TH_Kanchana Sangthong`|
    ||`th-TH_Somchai Thongkham`|
    ||`tr-TR_Emre Ozdemir`|
    ||`tr-TR_Nehir Celik`|
    ||`uk-UA_Artem Shevchenko`|
    ||`uk-UA_Daryna Kovalenko`|
    ||`ur-IN_Farah Abbasi`|
    ||`ur-IN_Sharyar Alvi`|
    ||`ur-PK_Hamza Farooqi`|
    ||`ur-PK_Sana Dhanial`|
    ||`uz-UK_Javlonbek Yusupov`|
    ||`uz-UZ_Rustam Karimova`|
    ||`vi-VN_Huu Duong`|
    ||`vi-VN_Vi Ly`|
    ||`wuu-CN_Muchen Li`|
    ||`wuu-CN_Ruoxi Wang`|
    ||`yue-CN_Ah-lam Lei`|
    ||`yue-CN_Xiaoxiao Wong`|
    ||`zh-CN-henan_Genji Zhou`|
    ||`zh-CN-liaoning_Chu Zhang`|
    ||`zh-CN-shaanxi_Chunhua Lin`|
    ||`zh-CN-shandong_Jiayi Wu`|
    ||`zh-CN-sichuan_Juan Yang`|
    ||`zh-CN_An Liu`|
    ||`zh-CN_Bai Yang`|
    ||`zh-CN_Bao Huang`|
    ||`zh-CN_Chao Zhou`|
    ||`zh-CN_Chen Chen Huo`|
    ||`zh-CN_Cheng Sun`|
    ||`zh-CN_Chichi Wu`|
    ||`zh-CN_Chin Ma`|
    ||`zh-CN_Chun Hu`|
    ||`zh-CN_Cong Zhang`|
    ||`zh-CN_Da Xia Li`|
    ||`zh-CN_Daiyu Zhu`|
    ||`zh-CN_Diu Wang`|
    ||`zh-CN_Huan Luo`|
    ||`zh-CN_Huifen Chen`|
    ||`zh-CN_Huiqing Wang`|
    ||`zh-CN_Meng Li`|
    ||`zh-CN_Xuan Xu`|
    ||`zh-CN_Yifu Wu`|
    ||`zh-CN_Yihan Chen`|
    ||`zh-CN_Yinuo Zhang`|
    ||`zh-HK_Kun Lo`|
    ||`zh-HK_Lanying Lei`|
    ||`zh-HK_Lee Lam`|
    ||`zh-TW_Mingxia Luo`|
    ||`zh-TW_Mingzhu Gao`|
    ||`zh-TW_Susu Song`|
    ||`zu-ZA_Bonginkosi Masina`|
    ||`zu-ZA_Ulwazi Mangede`|

    </details><details><summary>elevenlabs</summary>





    |Name|Value|
    |----|-----|
    |**elevenlabs**|`de-DE_Multilingual_Callum`|
    ||`de-DE_Multilingual_Charlie`|
    ||`de-DE_Multilingual_Charlotte`|
    ||`de-DE_Multilingual_Clyde`|
    ||`de-DE_Multilingual_Daniel`|
    ||`de-DE_Multilingual_Dave`|
    ||`de-DE_Multilingual_Dorothy`|
    ||`de-DE_Multilingual_Emily`|
    ||`de-DE_Multilingual_Ethan`|
    ||`de-DE_Multilingual_Fin`|
    ||`de-DE_Multilingual_Freya`|
    ||`de-DE_Multilingual_Gigi`|
    ||`de-DE_Multilingual_Giovanni`|
    ||`de-DE_Multilingual_Grace`|
    ||`de-DE_Multilingual_Harry`|
    ||`de-DE_Multilingual_James`|
    ||`de-DE_Multilingual_Jeremy`|
    ||`de-DE_Multilingual_Jessie`|
    ||`de-DE_Multilingual_Joseph`|
    ||`de-DE_Multilingual_Liam`|
    ||`de-DE_Multilingual_Matilda`|
    ||`de-DE_Multilingual_Matthew`|
    ||`de-DE_Multilingual_Michael`|
    ||`de-DE_Multilingual_Mimi`|
    ||`de-DE_Multilingual_Nicole`|
    ||`de-DE_Multilingual_Patrick`|
    ||`de-DE_Multilingual_Ryan`|
    ||`de-DE_Multilingual_Serena`|
    ||`de-DE_Multilingual_Thomas`|
    ||`en-AU_Monolingual_Charlie`|
    ||`en-AU_Monolingual_James`|
    ||`en-GB_Monolingual_Daniel`|
    ||`en-GB_Monolingual_Dave`|
    ||`en-GB_Monolingual_Dorothy`|
    ||`en-GB_Monolingual_Joseph`|
    ||`en-GB_Monolingual_Matthew`|
    ||`en-IE_Monolingual_Fin`|
    ||`en-IT_Monolingual_Giovanni`|
    ||`en-SWE_Monolingual_Charlotte`|
    ||`en-SWE_Monolingual_Mimi`|
    ||`en-US_Monolingual_Adam`|
    ||`en-US_Monolingual_Antoni`|
    ||`en-US_Monolingual_Arnold`|
    ||`en-US_Monolingual_Bella`|
    ||`en-US_Monolingual_Callum`|
    ||`en-US_Monolingual_Clyde`|
    ||`en-US_Monolingual_Domi`|
    ||`en-US_Monolingual_Elli`|
    ||`en-US_Monolingual_Emily`|
    ||`en-US_Monolingual_Ethan`|
    ||`en-US_Monolingual_Freya`|
    ||`en-US_Monolingual_Gigi`|
    ||`en-US_Monolingual_Glinda`|
    ||`en-US_Monolingual_Grace`|
    ||`en-US_Monolingual_Harry`|
    ||`en-US_Monolingual_Jeremy`|
    ||`en-US_Monolingual_Jessie`|
    ||`en-US_Monolingual_Josh`|
    ||`en-US_Monolingual_Liam`|
    ||`en-US_Monolingual_Matilda`|
    ||`en-US_Monolingual_Michael`|
    ||`en-US_Monolingual_Nicole`|
    ||`en-US_Monolingual_Patrick`|
    ||`en-US_Monolingual_Rachel`|
    ||`en-US_Monolingual_Ryan`|
    ||`en-US_Monolingual_Sam`|
    ||`en-US_Monolingual_Sarah`|
    ||`en-US_Monolingual_Serena`|
    ||`en-US_Monolingual_Thomas`|
    ||`es-ES_Multilingual_Callum`|
    ||`es-ES_Multilingual_Charlie`|
    ||`es-ES_Multilingual_Charlotte`|
    ||`es-ES_Multilingual_Clyde`|
    ||`es-ES_Multilingual_Daniel`|
    ||`es-ES_Multilingual_Dave`|
    ||`es-ES_Multilingual_Dorothy`|
    ||`es-ES_Multilingual_Emily`|
    ||`es-ES_Multilingual_Ethan`|
    ||`es-ES_Multilingual_Fin`|
    ||`es-ES_Multilingual_Freya`|
    ||`es-ES_Multilingual_Gigi`|
    ||`es-ES_Multilingual_Giovanni`|
    ||`es-ES_Multilingual_Grace`|
    ||`es-ES_Multilingual_James`|
    ||`es-ES_Multilingual_Jeremy`|
    ||`es-ES_Multilingual_Jessie`|
    ||`es-ES_Multilingual_Joseph`|
    ||`es-ES_Multilingual_Liam`|
    ||`es-ES_Multilingual_Matilda`|
    ||`es-ES_Multilingual_Matthew`|
    ||`es-ES_Multilingual_Michael`|
    ||`es-ES_Multilingual_Mimi`|
    ||`es-ES_Multilingual_Nicole`|
    ||`es-ES_Multilingual_Patrick`|
    ||`es-ES_Multilingual_Ryan`|
    ||`es-ES_Multilingual_Serena`|
    ||`es-ES_Multilingual_Thomas`|
    ||`es-US_Multilingual_Harry`|
    ||`fr-FR_Multilingual_Callum`|
    ||`fr-FR_Multilingual_Charlie`|
    ||`fr-FR_Multilingual_Charlotte`|
    ||`fr-FR_Multilingual_Clyde`|
    ||`fr-FR_Multilingual_Daniel`|
    ||`fr-FR_Multilingual_Dave`|
    ||`fr-FR_Multilingual_Dorothy`|
    ||`fr-FR_Multilingual_Emily`|
    ||`fr-FR_Multilingual_Ethan`|
    ||`fr-FR_Multilingual_Fin`|
    ||`fr-FR_Multilingual_Freya`|
    ||`fr-FR_Multilingual_Gigi`|
    ||`fr-FR_Multilingual_Giovanni`|
    ||`fr-FR_Multilingual_Grace`|
    ||`fr-FR_Multilingual_Harry`|
    ||`fr-FR_Multilingual_James`|
    ||`fr-FR_Multilingual_Jeremy`|
    ||`fr-FR_Multilingual_Jessie`|
    ||`fr-FR_Multilingual_Joseph`|
    ||`fr-FR_Multilingual_Liam`|
    ||`fr-FR_Multilingual_Matilda`|
    ||`fr-FR_Multilingual_Matthew`|
    ||`fr-FR_Multilingual_Michael`|
    ||`fr-FR_Multilingual_Mimi`|
    ||`fr-FR_Multilingual_Nicole`|
    ||`fr-FR_Multilingual_Patrick`|
    ||`fr-FR_Multilingual_Ryan`|
    ||`fr-FR_Multilingual_Serena`|
    ||`fr-FR_Multilingual_Thomas`|
    ||`hi-IN_Multilingual_Callum`|
    ||`hi-IN_Multilingual_Charlie`|
    ||`hi-IN_Multilingual_Charlotte`|
    ||`hi-IN_Multilingual_Clyde`|
    ||`hi-IN_Multilingual_Daniel`|
    ||`hi-IN_Multilingual_Dave`|
    ||`hi-IN_Multilingual_Dorothy`|
    ||`hi-IN_Multilingual_Emily`|
    ||`hi-IN_Multilingual_Ethan`|
    ||`hi-IN_Multilingual_Fin`|
    ||`hi-IN_Multilingual_Freya`|
    ||`hi-IN_Multilingual_Gigi`|
    ||`hi-IN_Multilingual_Giovanni`|
    ||`hi-IN_Multilingual_Grace`|
    ||`hi-IN_Multilingual_Harry`|
    ||`hi-IN_Multilingual_James`|
    ||`hi-IN_Multilingual_Jeremy`|
    ||`hi-IN_Multilingual_Jessie`|
    ||`hi-IN_Multilingual_Joseph`|
    ||`hi-IN_Multilingual_Liam`|
    ||`hi-IN_Multilingual_Matilda`|
    ||`hi-IN_Multilingual_Matthew`|
    ||`hi-IN_Multilingual_Michael`|
    ||`hi-IN_Multilingual_Mimi`|
    ||`hi-IN_Multilingual_Nicole`|
    ||`hi-IN_Multilingual_Patrick`|
    ||`hi-IN_Multilingual_Ryan`|
    ||`hi-IN_Multilingual_Serena`|
    ||`hi-IN_Multilingual_Thomas`|
    ||`it-IT_Multilingual_Callum`|
    ||`it-IT_Multilingual_Charlie`|
    ||`it-IT_Multilingual_Charlotte`|
    ||`it-IT_Multilingual_Clyde`|
    ||`it-IT_Multilingual_Daniel`|
    ||`it-IT_Multilingual_Dave`|
    ||`it-IT_Multilingual_Dorothy`|
    ||`it-IT_Multilingual_Emily`|
    ||`it-IT_Multilingual_Ethan`|
    ||`it-IT_Multilingual_Fin`|
    ||`it-IT_Multilingual_Freya`|
    ||`it-IT_Multilingual_Gigi`|
    ||`it-IT_Multilingual_Giovanni`|
    ||`it-IT_Multilingual_Grace`|
    ||`it-IT_Multilingual_Harry`|
    ||`it-IT_Multilingual_James`|
    ||`it-IT_Multilingual_Jeremy`|
    ||`it-IT_Multilingual_Jessie`|
    ||`it-IT_Multilingual_Joseph`|
    ||`it-IT_Multilingual_Liam`|
    ||`it-IT_Multilingual_Matilda`|
    ||`it-IT_Multilingual_Matthew`|
    ||`it-IT_Multilingual_Michael`|
    ||`it-IT_Multilingual_Mimi`|
    ||`it-IT_Multilingual_Nicole`|
    ||`it-IT_Multilingual_Patrick`|
    ||`it-IT_Multilingual_Ryan`|
    ||`it-IT_Multilingual_Serena`|
    ||`it-IT_Multilingual_Thomas`|
    ||`pl-PL_Multilingual_Callum`|
    ||`pl-PL_Multilingual_Charlie`|
    ||`pl-PL_Multilingual_Charlotte`|
    ||`pl-PL_Multilingual_Clyde`|
    ||`pl-PL_Multilingual_Daniel`|
    ||`pl-PL_Multilingual_Dave`|
    ||`pl-PL_Multilingual_Dorothy`|
    ||`pl-PL_Multilingual_Emily`|
    ||`pl-PL_Multilingual_Ethan`|
    ||`pl-PL_Multilingual_Fin`|
    ||`pl-PL_Multilingual_Freya`|
    ||`pl-PL_Multilingual_Gigi`|
    ||`pl-PL_Multilingual_Giovanni`|
    ||`pl-PL_Multilingual_Grace`|
    ||`pl-PL_Multilingual_Harry`|
    ||`pl-PL_Multilingual_James`|
    ||`pl-PL_Multilingual_Jeremy`|
    ||`pl-PL_Multilingual_Jessie`|
    ||`pl-PL_Multilingual_Joseph`|
    ||`pl-PL_Multilingual_Liam`|
    ||`pl-PL_Multilingual_Matilda`|
    ||`pl-PL_Multilingual_Matthew`|
    ||`pl-PL_Multilingual_Michael`|
    ||`pl-PL_Multilingual_Mimi`|
    ||`pl-PL_Multilingual_Nicole`|
    ||`pl-PL_Multilingual_Patrick`|
    ||`pl-PL_Multilingual_Ryan`|
    ||`pl-PL_Multilingual_Serena`|
    ||`pl-PL_Multilingual_Thomas`|
    ||`pt-PT_Multilingual_Callum`|
    ||`pt-PT_Multilingual_Charlie`|
    ||`pt-PT_Multilingual_Charlotte`|
    ||`pt-PT_Multilingual_Clyde`|
    ||`pt-PT_Multilingual_Daniel`|
    ||`pt-PT_Multilingual_Dave`|
    ||`pt-PT_Multilingual_Dorothy`|
    ||`pt-PT_Multilingual_Emily`|
    ||`pt-PT_Multilingual_Ethan`|
    ||`pt-PT_Multilingual_Fin`|
    ||`pt-PT_Multilingual_Freya`|
    ||`pt-PT_Multilingual_Gigi`|
    ||`pt-PT_Multilingual_Giovanni`|
    ||`pt-PT_Multilingual_Grace`|
    ||`pt-PT_Multilingual_Harry`|
    ||`pt-PT_Multilingual_James`|
    ||`pt-PT_Multilingual_Jeremy`|
    ||`pt-PT_Multilingual_Jessie`|
    ||`pt-PT_Multilingual_Joseph`|
    ||`pt-PT_Multilingual_Liam`|
    ||`pt-PT_Multilingual_Matilda`|
    ||`pt-PT_Multilingual_Matthew`|
    ||`pt-PT_Multilingual_Michael`|
    ||`pt-PT_Multilingual_Mimi`|
    ||`pt-PT_Multilingual_Nicole`|
    ||`pt-PT_Multilingual_Patrick`|
    ||`pt-PT_Multilingual_Ryan`|
    ||`pt-PT_Multilingual_Serena`|
    ||`pt-PT_Multilingual_Thomas`|

    </details><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`af_alloy`|
    ||`af_echo`|
    ||`af_fable`|
    ||`af_nova`|
    ||`af_onyx`|
    ||`af_shimmer`|
    ||`ar_alloy`|
    ||`ar_echo`|
    ||`ar_fable`|
    ||`ar_nova`|
    ||`ar_onyx`|
    ||`ar_shimmer`|
    ||`az_alloy`|
    ||`az_echo`|
    ||`az_fable`|
    ||`az_nova`|
    ||`az_onyx`|
    ||`az_shimmer`|
    ||`be_alloy`|
    ||`be_echo`|
    ||`be_fable`|
    ||`be_nova`|
    ||`be_onyx`|
    ||`be_shimmer`|
    ||`bg_alloy`|
    ||`bg_echo`|
    ||`bg_fable`|
    ||`bg_nova`|
    ||`bg_onyx`|
    ||`bg_shimmer`|
    ||`bs_alloy`|
    ||`bs_echo`|
    ||`bs_fable`|
    ||`bs_nova`|
    ||`bs_onyx`|
    ||`bs_shimmer`|
    ||`ca_alloy`|
    ||`ca_echo`|
    ||`ca_fable`|
    ||`ca_nova`|
    ||`ca_onyx`|
    ||`ca_shimmer`|
    ||`cs_alloy`|
    ||`cs_echo`|
    ||`cs_fable`|
    ||`cs_nova`|
    ||`cs_onyx`|
    ||`cs_shimmer`|
    ||`cy_alloy`|
    ||`cy_echo`|
    ||`cy_fable`|
    ||`cy_nova`|
    ||`cy_onyx`|
    ||`cy_shimmer`|
    ||`da_alloy`|
    ||`da_echo`|
    ||`da_fable`|
    ||`da_nova`|
    ||`da_onyx`|
    ||`da_shimmer`|
    ||`de_alloy`|
    ||`de_echo`|
    ||`de_fable`|
    ||`de_nova`|
    ||`de_onyx`|
    ||`de_shimmer`|
    ||`el_alloy`|
    ||`el_echo`|
    ||`el_fable`|
    ||`el_nova`|
    ||`el_onyx`|
    ||`el_shimmer`|
    ||`en_alloy`|
    ||`en_echo`|
    ||`en_fable`|
    ||`en_nova`|
    ||`en_onyx`|
    ||`en_shimmer`|
    ||`es_alloy`|
    ||`es_echo`|
    ||`es_fable`|
    ||`es_nova`|
    ||`es_onyx`|
    ||`es_shimmer`|
    ||`et_alloy`|
    ||`et_echo`|
    ||`et_fable`|
    ||`et_nova`|
    ||`et_onyx`|
    ||`et_shimmer`|
    ||`fa_alloy`|
    ||`fa_echo`|
    ||`fa_fable`|
    ||`fa_nova`|
    ||`fa_onyx`|
    ||`fa_shimmer`|
    ||`fi_alloy`|
    ||`fi_echo`|
    ||`fi_fable`|
    ||`fi_nova`|
    ||`fi_onyx`|
    ||`fi_shimmer`|
    ||`fr_alloy`|
    ||`fr_echo`|
    ||`fr_fable`|
    ||`fr_nova`|
    ||`fr_onyx`|
    ||`fr_shimmer`|
    ||`gl_alloy`|
    ||`gl_echo`|
    ||`gl_fable`|
    ||`gl_nova`|
    ||`gl_onyx`|
    ||`gl_shimmer`|
    ||`he_alloy`|
    ||`he_echo`|
    ||`he_fable`|
    ||`he_nova`|
    ||`he_onyx`|
    ||`he_shimmer`|
    ||`hi_alloy`|
    ||`hi_echo`|
    ||`hi_fable`|
    ||`hi_nova`|
    ||`hi_onyx`|
    ||`hi_shimmer`|
    ||`hr_alloy`|
    ||`hr_echo`|
    ||`hr_fable`|
    ||`hr_nova`|
    ||`hr_onyx`|
    ||`hr_shimmer`|
    ||`hu_alloy`|
    ||`hu_echo`|
    ||`hu_fable`|
    ||`hu_nova`|
    ||`hu_onyx`|
    ||`hu_shimmer`|
    ||`hy_alloy`|
    ||`hy_echo`|
    ||`hy_fable`|
    ||`hy_nova`|
    ||`hy_onyx`|
    ||`hy_shimmer`|
    ||`id_alloy`|
    ||`id_echo`|
    ||`id_fable`|
    ||`id_nova`|
    ||`id_onyx`|
    ||`id_shimmer`|
    ||`is_alloy`|
    ||`is_echo`|
    ||`is_fable`|
    ||`is_nova`|
    ||`is_onyx`|
    ||`is_shimmer`|
    ||`it_alloy`|
    ||`it_echo`|
    ||`it_fable`|
    ||`it_nova`|
    ||`it_onyx`|
    ||`it_shimmer`|
    ||`ja_alloy`|
    ||`ja_echo`|
    ||`ja_fable`|
    ||`ja_nova`|
    ||`ja_onyx`|
    ||`ja_shimmer`|
    ||`kk_alloy`|
    ||`kk_echo`|
    ||`kk_fable`|
    ||`kk_nova`|
    ||`kk_onyx`|
    ||`kk_shimmer`|
    ||`kn_alloy`|
    ||`kn_echo`|
    ||`kn_fable`|
    ||`kn_nova`|
    ||`kn_onyx`|
    ||`kn_shimmer`|
    ||`ko_alloy`|
    ||`ko_echo`|
    ||`ko_fable`|
    ||`ko_nova`|
    ||`ko_onyx`|
    ||`ko_shimmer`|
    ||`lt_alloy`|
    ||`lt_echo`|
    ||`lt_fable`|
    ||`lt_nova`|
    ||`lt_onyx`|
    ||`lt_shimmer`|
    ||`lv_alloy`|
    ||`lv_echo`|
    ||`lv_fable`|
    ||`lv_nova`|
    ||`lv_onyx`|
    ||`lv_shimmer`|
    ||`mi_alloy`|
    ||`mi_echo`|
    ||`mi_fable`|
    ||`mi_nova`|
    ||`mi_onyx`|
    ||`mi_shimmer`|
    ||`mk_alloy`|
    ||`mk_echo`|
    ||`mk_fable`|
    ||`mk_nova`|
    ||`mk_onyx`|
    ||`mk_shimmer`|
    ||`mr_alloy`|
    ||`mr_echo`|
    ||`mr_fable`|
    ||`mr_nova`|
    ||`mr_onyx`|
    ||`mr_shimmer`|
    ||`ms_alloy`|
    ||`ms_echo`|
    ||`ms_fable`|
    ||`ms_nova`|
    ||`ms_onyx`|
    ||`ms_shimmer`|
    ||`ne_alloy`|
    ||`ne_echo`|
    ||`ne_fable`|
    ||`ne_nova`|
    ||`ne_onyx`|
    ||`ne_shimmer`|
    ||`nl_alloy`|
    ||`nl_echo`|
    ||`nl_fable`|
    ||`nl_nova`|
    ||`nl_onyx`|
    ||`nl_shimmer`|
    ||`no_alloy`|
    ||`no_echo`|
    ||`no_fable`|
    ||`no_nova`|
    ||`no_onyx`|
    ||`no_shimmer`|
    ||`pl_alloy`|
    ||`pl_echo`|
    ||`pl_fable`|
    ||`pl_nova`|
    ||`pl_onyx`|
    ||`pl_shimmer`|
    ||`pt_alloy`|
    ||`pt_echo`|
    ||`pt_fable`|
    ||`pt_nova`|
    ||`pt_onyx`|
    ||`pt_shimmer`|
    ||`ro_alloy`|
    ||`ro_echo`|
    ||`ro_fable`|
    ||`ro_nova`|
    ||`ro_onyx`|
    ||`ro_shimmer`|
    ||`ru_alloy`|
    ||`ru_echo`|
    ||`ru_fable`|
    ||`ru_nova`|
    ||`ru_onyx`|
    ||`ru_shimmer`|
    ||`sk_alloy`|
    ||`sk_echo`|
    ||`sk_fable`|
    ||`sk_nova`|
    ||`sk_onyx`|
    ||`sk_shimmer`|
    ||`sl_alloy`|
    ||`sl_echo`|
    ||`sl_fable`|
    ||`sl_nova`|
    ||`sl_onyx`|
    ||`sl_shimmer`|
    ||`sr_alloy`|
    ||`sr_echo`|
    ||`sr_fable`|
    ||`sr_nova`|
    ||`sr_onyx`|
    ||`sr_shimmer`|
    ||`sv_alloy`|
    ||`sv_echo`|
    ||`sv_fable`|
    ||`sv_nova`|
    ||`sv_onyx`|
    ||`sv_shimmer`|
    ||`sw_alloy`|
    ||`sw_echo`|
    ||`sw_fable`|
    ||`sw_nova`|
    ||`sw_onyx`|
    ||`sw_shimmer`|
    ||`ta_alloy`|
    ||`ta_echo`|
    ||`ta_fable`|
    ||`ta_nova`|
    ||`ta_onyx`|
    ||`ta_shimmer`|
    ||`th_alloy`|
    ||`th_echo`|
    ||`th_fable`|
    ||`th_nova`|
    ||`th_onyx`|
    ||`th_shimmer`|
    ||`tl_alloy`|
    ||`tl_echo`|
    ||`tl_fable`|
    ||`tl_nova`|
    ||`tl_onyx`|
    ||`tl_shimmer`|
    ||`tr_alloy`|
    ||`tr_echo`|
    ||`tr_fable`|
    ||`tr_nova`|
    ||`tr_onyx`|
    ||`tr_shimmer`|
    ||`uk_alloy`|
    ||`uk_echo`|
    ||`uk_fable`|
    ||`uk_nova`|
    ||`uk_onyx`|
    ||`uk_shimmer`|
    ||`ur_alloy`|
    ||`ur_echo`|
    ||`ur_fable`|
    ||`ur_nova`|
    ||`ur_onyx`|
    ||`ur_shimmer`|
    ||`vi_alloy`|
    ||`vi_echo`|
    ||`vi_fable`|
    ||`vi_nova`|
    ||`vi_onyx`|
    ||`vi_shimmer`|
    ||`zh_alloy`|
    ||`zh_echo`|
    ||`zh_fable`|
    ||`zh_nova`|
    ||`zh_onyx`|
    ||`zh_shimmer`|

    </details>

    </details>

    Args:
        body (AudiotextToSpeechTextToSpeechRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse]]
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
    body: AudiotextToSpeechTextToSpeechRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Text to Speech

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**amazon**|-|`boto3 (v1.15.18)`|4.0 (per 1000000 char)|1 char
    |**amazon**|**Neural**|`boto3 (v1.15.18)`|16.0 (per 1000000 char)|1 char
    |**google**|-|`v1`|4.0 (per 1000000 char)|1 char
    |**google**|**Standard**|`v1`|4.0 (per 1000000 char)|1 char
    |**google**|**Neural**|`v1`|16.0 (per 1000000 char)|1 char
    |**google**|**Wavenet**|`v1`|16.0 (per 1000000 char)|1 char
    |**google**|**Studio**|`v1`|0.16 (per 1000 char)|1 char
    |**ibm**|-|`v1`|20.0 (per 1000000 char)|1000 char
    |**microsoft**|-|`v1.0`|16.0 (per 1000000 char)|1 char
    |**lovoai**|-|`v1`|160.0 (per 1000000 char)|1000 char
    |**elevenlabs**|-|`v1`|0.3 (per 1000 char)|1 char
    |**openai**|-|`v1.0`|0.015 (per 1000 char)|1 char


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
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bengali**|`bn`|
    |**Bosnian**|`bs`|
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
    |**Estonian**|`et`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Indonesian**|`id`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kannada**|`kn`|
    |**Kazakh**|`kk`|
    |**Korean**|`ko`|
    |**Lao**|`lo`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Macedonian**|`mk`|
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
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Serbian**|`sr`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**Spanish**|`es`|
    |**Standard Arabic**|`arb`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tamil**|`ta`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Turkish**|`tr`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Welsh**|`cy`|
    |**Wu Chinese**|`wuu`|
    |**Xhosa**|`xh`|
    |**Yue Chinese**|`yue`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans (South Africa)**|`af-ZA`|
    |**Albanian (Albania)**|`sq-AL`|
    |**Amharic (Ethiopia)**|`am-ET`|
    |**Arabic (Algeria)**|`ar-DZ`|
    |**Arabic (Bahrain)**|`ar-BH`|
    |**Arabic (Egypt)**|`ar-EG`|
    |**Arabic (Iraq)**|`ar-IQ`|
    |**Arabic (Jordan)**|`ar-JO`|
    |**Arabic (Kuwait)**|`ar-KW`|
    |**Arabic (Lebanon)**|`ar-LB`|
    |**Arabic (Libya)**|`ar-LY`|
    |**Arabic (Morocco)**|`ar-MA`|
    |**Arabic (Oman)**|`ar-OM`|
    |**Arabic (Pseudo-Accents)**|`ar-XA`|
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
    |**Cantonese (Hong Kong SAR China)**|`yue-HK`|
    |**Catalan (Spain)**|`ca-ES`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (China)**|`zh-CN-henan`|
    |**Chinese (China)**|`zh-CN-shandong`|
    |**Chinese (China)**|`zh-CN-sichuan`|
    |**Chinese (Hong Kong SAR China)**|`zh-HK`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Croatian (Croatia)**|`hr-HR`|
    |**Czech (Czechia)**|`cs-CZ`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Belgium)**|`nl-BE`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (Australia)**|`en-AU`|
    |**English (Canada)**|`en-CA`|
    |**English (Curaçao)**|`en-AN`|
    |**English (Hong Kong SAR China)**|`en-HK`|
    |**English (India)**|`en-IN`|
    |**English (Ireland)**|`en-IE`|
    |**English (Kenya)**|`en-KE`|
    |**English (New Zealand)**|`en-NZ`|
    |**English (Nigeria)**|`en-NG`|
    |**English (Philippines)**|`en-PH`|
    |**English (Singapore)**|`en-SG`|
    |**English (South Africa)**|`en-ZA`|
    |**English (Tanzania)**|`en-TZ`|
    |**English (United Kingdom)**|`en-GB`|
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
    |**Hindi (India)**|`hi-IN`|
    |**Hungarian (Hungary)**|`hu-HU`|
    |**Icelandic (Iceland)**|`is-IS`|
    |**Indonesian (Indonesia)**|`id-ID`|
    |**Irish (Ireland)**|`ga-IE`|
    |**Italian (Italy)**|`it-IT`|
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
    |**Mandarin Chinese (China)**|`cmn-CN`|
    |**Mandarin Chinese (Taiwan)**|`cmn-TW`|
    |**Marathi (India)**|`mr-IN`|
    |**Mongolian (Mongolia)**|`mn-MN`|
    |**Nepali (Nepal)**|`ne-NP`|
    |**Norwegian Bokmål (Norway)**|`nb-NO`|
    |**Pashto (Afghanistan)**|`ps-AF`|
    |**Persian (Iran)**|`fa-IR`|
    |**Polish (Poland)**|`pl-PL`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Punjabi (India)**|`pa-IN`|
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
    |**Uzbek (United Kingdom)**|`uz-UK`|
    |**Uzbek (Uzbekistan)**|`uz-UZ`|
    |**Vietnamese (Vietnam)**|`vi-VN`|
    |**Welsh (United Kingdom)**|`cy-GB`|
    |**Wu Chinese (China)**|`wuu-CN`|
    |**Xhosa (South Africa)**|`xh-ZA`|
    |**Zulu (South Africa)**|`zu-ZA`|

    </details><details><summary>Supported Models</summary><details><summary>amazon</summary>





    |Name|Value|
    |----|-----|
    |**amazon**|`ar-AE_Hala_Neural`|
    ||`arb_Zeina_Standard`|
    ||`ca-ES_Arlet_Neural`|
    ||`cmn-CN_Zhiyu_Neural`|
    ||`cmn-CN_Zhiyu_Standard`|
    ||`cy-GB_Gwyneth_Standard`|
    ||`da-DK_Mads_Standard`|
    ||`da-DK_Naja_Standard`|
    ||`de-AT_Hannah_Neural`|
    ||`de-DE_Daniel_Neural`|
    ||`de-DE_Hans_Standard`|
    ||`de-DE_Marlene_Standard`|
    ||`de-DE_Vicki_Neural`|
    ||`de-DE_Vicki_Standard`|
    ||`en-AU_Nicole_Neural`|
    ||`en-AU_Olivia_Standard`|
    ||`en-AU_Russell_Neural`|
    ||`en-GB_Amy_Neural`|
    ||`en-GB_Amy_Standard`|
    ||`en-GB_Arthur_Neural`|
    ||`en-GB_Brian_Neural`|
    ||`en-GB_Brian_Standard`|
    ||`en-GB_Emma_Neural`|
    ||`en-GB_Emma_Standard`|
    ||`en-IN_Aditi_Standard`|
    ||`en-IN_Kajal_Neural`|
    ||`en-IN_Raveena_Standard`|
    ||`en-NZ_Aria_Neural`|
    ||`en-US_Ivy_Neural`|
    ||`en-US_Ivy_Standard`|
    ||`en-US_Joanna_Neural`|
    ||`en-US_Joanna_Standard`|
    ||`en-US_Joey_Neural`|
    ||`en-US_Joey_Standard`|
    ||`en-US_Justin_Neural`|
    ||`en-US_Justin_Standard`|
    ||`en-US_Kendra_Neural`|
    ||`en-US_Kendra_Standard`|
    ||`en-US_Kevin_Neural`|
    ||`en-US_Kimberly_Neural`|
    ||`en-US_Kimberly_Standard`|
    ||`en-US_Matthew_Neural`|
    ||`en-US_Matthew_Standard`|
    ||`en-US_Ruth_Neural`|
    ||`en-US_Salli_Neural`|
    ||`en-US_Salli_Standard`|
    ||`en-US_Stephen_Neural`|
    ||`en-ZA_Ayanda_Neural`|
    ||`es-ES_Conchita_Standard`|
    ||`es-ES_Enrique_Standard`|
    ||`es-ES_Lucia_Neural`|
    ||`es-ES_Lucia_Standard`|
    ||`es-ES_Sergio_Neural`|
    ||`es-MX_Andres_Neural`|
    ||`es-MX_Mia_Neural`|
    ||`es-MX_Mia_Standard`|
    ||`es-US_Lupe_Neural`|
    ||`es-US_Lupe_Standard`|
    ||`es-US_Miguel_Standard`|
    ||`es-US_Pedro_Neural`|
    ||`es-US_Penelope_Standard`|
    ||`fi-FI_Suvi_Neural`|
    ||`fr-CA_Chantal_Standard`|
    ||`fr-CA_Gabrielle_Neural`|
    ||`fr-CA_Liam_Neural`|
    ||`fr-FR_Celine_Standard`|
    ||`fr-FR_Lea_Neural`|
    ||`fr-FR_Lea_Standard`|
    ||`fr-FR_Mathieu_Standard`|
    ||`fr-FR_Remi_Neural`|
    ||`hi-IN_Aditi_Standard`|
    ||`hi-IN_Kajal_Neural`|
    ||`is-IS_Dora_Standard`|
    ||`is-IS_Karl_Neural`|
    ||`is-IS_Karl_Standard`|
    ||`it-IT_Adriano_Neural`|
    ||`it-IT_Bianca_Neural`|
    ||`it-IT_Bianca_Standard`|
    ||`it-IT_Carla_Standard`|
    ||`it-IT_Giorgio_Standard`|
    ||`ja-JP_Kazuha_Neural`|
    ||`ja-JP_Mizuki_Standard`|
    ||`ja-JP_Takumi_Neural`|
    ||`ja-JP_Takumi_Standard`|
    ||`ja-JP_Tomoko_Neural`|
    ||`ko-KR_Seoyeon_Neural`|
    ||`ko-KR_Seoyeon_Standard`|
    ||`nb-NO_Liv_Standard`|
    ||`nl-NL_Laura_Neural`|
    ||`nl-NL_Lotte_Standard`|
    ||`nl-NL_Ruben_Standard`|
    ||`pl-PL_Ewa_Standard`|
    ||`pl-PL_Jacek_Standard`|
    ||`pl-PL_Jan_Standard`|
    ||`pl-PL_Maja_Standard`|
    ||`pl-PL_Ola_Neural`|
    ||`pt-BR_Camila_Neural`|
    ||`pt-BR_Camila_Standard`|
    ||`pt-BR_Ricardo_Standard`|
    ||`pt-BR_Thiago_Neural`|
    ||`pt-BR_Vitoria_Neural`|
    ||`pt-BR_Vitoria_Standard`|
    ||`pt-PT_Cristiano_Standard`|
    ||`pt-PT_Ines_Neural`|
    ||`pt-PT_Ines_Standard`|
    ||`ro-RO_Carmen_Standard`|
    ||`ru-RU_Maxim_Standard`|
    ||`ru-RU_Tatyana_Standard`|
    ||`sv-SE_Astrid_Standard`|
    ||`sv-SE_Elin_Neural`|
    ||`tr-TR_Filiz_Standard`|
    ||`yue-CN_Hiujin_Neural`|

    </details><details><summary>google</summary>





    |Name|Value|
    |----|-----|
    |**google**|`af-ZA-Standard-A`|
    ||`ar-XA-Standard-A`|
    ||`ar-XA-Standard-B`|
    ||`ar-XA-Standard-C`|
    ||`ar-XA-Standard-D`|
    ||`ar-XA-Wavenet-A`|
    ||`ar-XA-Wavenet-B`|
    ||`ar-XA-Wavenet-C`|
    ||`ar-XA-Wavenet-D`|
    ||`bg-BG-Standard-A`|
    ||`bn-IN-Standard-A`|
    ||`bn-IN-Standard-B`|
    ||`bn-IN-Wavenet-A`|
    ||`bn-IN-Wavenet-B`|
    ||`ca-ES-Standard-A`|
    ||`cmn-CN-Standard-A`|
    ||`cmn-CN-Standard-B`|
    ||`cmn-CN-Standard-C`|
    ||`cmn-CN-Standard-D`|
    ||`cmn-CN-Wavenet-A`|
    ||`cmn-CN-Wavenet-B`|
    ||`cmn-CN-Wavenet-C`|
    ||`cmn-CN-Wavenet-D`|
    ||`cmn-TW-Standard-A`|
    ||`cmn-TW-Standard-B`|
    ||`cmn-TW-Standard-C`|
    ||`cmn-TW-Wavenet-A`|
    ||`cmn-TW-Wavenet-B`|
    ||`cmn-TW-Wavenet-C`|
    ||`cs-CZ-Standard-A`|
    ||`cs-CZ-Wavenet-A`|
    ||`da-DK-Standard-A`|
    ||`da-DK-Standard-C`|
    ||`da-DK-Standard-D`|
    ||`da-DK-Standard-E`|
    ||`da-DK-Wavenet-A`|
    ||`da-DK-Wavenet-C`|
    ||`da-DK-Wavenet-D`|
    ||`da-DK-Wavenet-E`|
    ||`de-DE-Neural2-B`|
    ||`de-DE-Neural2-C`|
    ||`de-DE-Neural2-D`|
    ||`de-DE-Neural2-F`|
    ||`de-DE-Standard-A`|
    ||`de-DE-Standard-B`|
    ||`de-DE-Standard-C`|
    ||`de-DE-Standard-D`|
    ||`de-DE-Standard-E`|
    ||`de-DE-Standard-F`|
    ||`de-DE-Wavenet-A`|
    ||`de-DE-Wavenet-B`|
    ||`de-DE-Wavenet-C`|
    ||`de-DE-Wavenet-D`|
    ||`de-DE-Wavenet-E`|
    ||`de-DE-Wavenet-F`|
    ||`el-GR-Standard-A`|
    ||`el-GR-Wavenet-A`|
    ||`en-AU-Neural2-A`|
    ||`en-AU-Neural2-B`|
    ||`en-AU-Neural2-C`|
    ||`en-AU-Neural2-D`|
    ||`en-AU-News-E`|
    ||`en-AU-News-F`|
    ||`en-AU-News-G`|
    ||`en-AU-Standard-A`|
    ||`en-AU-Standard-B`|
    ||`en-AU-Standard-C`|
    ||`en-AU-Standard-D`|
    ||`en-AU-Wavenet-A`|
    ||`en-AU-Wavenet-B`|
    ||`en-AU-Wavenet-C`|
    ||`en-AU-Wavenet-D`|
    ||`en-GB-Neural2-A`|
    ||`en-GB-Neural2-B`|
    ||`en-GB-Neural2-C`|
    ||`en-GB-Neural2-D`|
    ||`en-GB-Neural2-F`|
    ||`en-GB-News-G`|
    ||`en-GB-News-H`|
    ||`en-GB-News-I`|
    ||`en-GB-News-J`|
    ||`en-GB-News-K`|
    ||`en-GB-News-L`|
    ||`en-GB-News-M`|
    ||`en-GB-Standard-A`|
    ||`en-GB-Standard-B`|
    ||`en-GB-Standard-C`|
    ||`en-GB-Standard-D`|
    ||`en-GB-Standard-F`|
    ||`en-GB-Wavenet-A`|
    ||`en-GB-Wavenet-B`|
    ||`en-GB-Wavenet-C`|
    ||`en-GB-Wavenet-D`|
    ||`en-GB-Wavenet-F`|
    ||`en-IN-Standard-A`|
    ||`en-IN-Standard-B`|
    ||`en-IN-Standard-C`|
    ||`en-IN-Standard-D`|
    ||`en-IN-Wavenet-A`|
    ||`en-IN-Wavenet-B`|
    ||`en-IN-Wavenet-C`|
    ||`en-IN-Wavenet-D`|
    ||`en-US-Neural2-A`|
    ||`en-US-Neural2-C`|
    ||`en-US-Neural2-D`|
    ||`en-US-Neural2-E`|
    ||`en-US-Neural2-F`|
    ||`en-US-Neural2-G`|
    ||`en-US-Neural2-H`|
    ||`en-US-Neural2-I`|
    ||`en-US-Neural2-J`|
    ||`en-US-News-K`|
    ||`en-US-News-L`|
    ||`en-US-News-M`|
    ||`en-US-News-N`|
    ||`en-US-Standard-A`|
    ||`en-US-Standard-B`|
    ||`en-US-Standard-C`|
    ||`en-US-Standard-D`|
    ||`en-US-Standard-E`|
    ||`en-US-Standard-F`|
    ||`en-US-Standard-G`|
    ||`en-US-Standard-H`|
    ||`en-US-Standard-I`|
    ||`en-US-Standard-J`|
    ||`en-US-Studio-M`|
    ||`en-US-Studio-O`|
    ||`en-US-Wavenet-A`|
    ||`en-US-Wavenet-B`|
    ||`en-US-Wavenet-C`|
    ||`en-US-Wavenet-D`|
    ||`en-US-Wavenet-E`|
    ||`en-US-Wavenet-F`|
    ||`en-US-Wavenet-G`|
    ||`en-US-Wavenet-H`|
    ||`en-US-Wavenet-I`|
    ||`en-US-Wavenet-J`|
    ||`es-ES-Neural2-A`|
    ||`es-ES-Neural2-B`|
    ||`es-ES-Neural2-C`|
    ||`es-ES-Neural2-D`|
    ||`es-ES-Neural2-E`|
    ||`es-ES-Neural2-F`|
    ||`es-ES-Standard-A`|
    ||`es-ES-Standard-B`|
    ||`es-ES-Standard-C`|
    ||`es-ES-Standard-D`|
    ||`es-ES-Wavenet-B`|
    ||`es-ES-Wavenet-C`|
    ||`es-ES-Wavenet-D`|
    ||`es-US-Neural2-A`|
    ||`es-US-Neural2-B`|
    ||`es-US-Neural2-C`|
    ||`es-US-News-D`|
    ||`es-US-News-E`|
    ||`es-US-News-F`|
    ||`es-US-News-G`|
    ||`es-US-Standard-A`|
    ||`es-US-Standard-B`|
    ||`es-US-Standard-C`|
    ||`es-US-Studio-B`|
    ||`es-US-Wavenet-A`|
    ||`es-US-Wavenet-B`|
    ||`es-US-Wavenet-C`|
    ||`eu-ES-Standard-A`|
    ||`fi-FI-Standard-A`|
    ||`fi-FI-Wavenet-A`|
    ||`fil-PH-Standard-A`|
    ||`fil-PH-Standard-B`|
    ||`fil-PH-Standard-C`|
    ||`fil-PH-Standard-D`|
    ||`fil-PH-Wavenet-A`|
    ||`fil-PH-Wavenet-B`|
    ||`fil-PH-Wavenet-C`|
    ||`fil-PH-Wavenet-D`|
    ||`fr-CA-Neural2-A`|
    ||`fr-CA-Neural2-B`|
    ||`fr-CA-Neural2-C`|
    ||`fr-CA-Neural2-D`|
    ||`fr-CA-Standard-A`|
    ||`fr-CA-Standard-B`|
    ||`fr-CA-Standard-C`|
    ||`fr-CA-Standard-D`|
    ||`fr-CA-Wavenet-A`|
    ||`fr-CA-Wavenet-B`|
    ||`fr-CA-Wavenet-C`|
    ||`fr-CA-Wavenet-D`|
    ||`fr-FR-Neural2-A`|
    ||`fr-FR-Neural2-B`|
    ||`fr-FR-Neural2-C`|
    ||`fr-FR-Neural2-D`|
    ||`fr-FR-Neural2-E`|
    ||`fr-FR-Standard-A`|
    ||`fr-FR-Standard-B`|
    ||`fr-FR-Standard-C`|
    ||`fr-FR-Standard-D`|
    ||`fr-FR-Standard-E`|
    ||`fr-FR-Wavenet-A`|
    ||`fr-FR-Wavenet-B`|
    ||`fr-FR-Wavenet-C`|
    ||`fr-FR-Wavenet-D`|
    ||`fr-FR-Wavenet-E`|
    ||`gl-ES-Standard-A`|
    ||`gu-IN-Standard-A`|
    ||`gu-IN-Standard-B`|
    ||`gu-IN-Wavenet-A`|
    ||`gu-IN-Wavenet-B`|
    ||`he-IL-Standard-A`|
    ||`he-IL-Standard-B`|
    ||`he-IL-Standard-C`|
    ||`he-IL-Standard-D`|
    ||`he-IL-Wavenet-A`|
    ||`he-IL-Wavenet-B`|
    ||`he-IL-Wavenet-C`|
    ||`he-IL-Wavenet-D`|
    ||`hi-IN-Neural2-A`|
    ||`hi-IN-Neural2-B`|
    ||`hi-IN-Neural2-C`|
    ||`hi-IN-Neural2-D`|
    ||`hi-IN-Standard-A`|
    ||`hi-IN-Standard-B`|
    ||`hi-IN-Standard-C`|
    ||`hi-IN-Standard-D`|
    ||`hi-IN-Wavenet-A`|
    ||`hi-IN-Wavenet-B`|
    ||`hi-IN-Wavenet-C`|
    ||`hi-IN-Wavenet-D`|
    ||`hu-HU-Standard-A`|
    ||`hu-HU-Wavenet-A`|
    ||`id-ID-Standard-A`|
    ||`id-ID-Standard-B`|
    ||`id-ID-Standard-C`|
    ||`id-ID-Standard-D`|
    ||`id-ID-Wavenet-A`|
    ||`id-ID-Wavenet-B`|
    ||`id-ID-Wavenet-C`|
    ||`id-ID-Wavenet-D`|
    ||`is-IS-Standard-A`|
    ||`it-IT-Neural2-A`|
    ||`it-IT-Neural2-C`|
    ||`it-IT-Standard-A`|
    ||`it-IT-Standard-B`|
    ||`it-IT-Standard-C`|
    ||`it-IT-Standard-D`|
    ||`it-IT-Wavenet-A`|
    ||`it-IT-Wavenet-B`|
    ||`it-IT-Wavenet-C`|
    ||`it-IT-Wavenet-D`|
    ||`ja-JP-Neural2-B`|
    ||`ja-JP-Neural2-C`|
    ||`ja-JP-Neural2-D`|
    ||`ja-JP-Standard-A`|
    ||`ja-JP-Standard-B`|
    ||`ja-JP-Standard-C`|
    ||`ja-JP-Standard-D`|
    ||`ja-JP-Wavenet-A`|
    ||`ja-JP-Wavenet-B`|
    ||`ja-JP-Wavenet-C`|
    ||`ja-JP-Wavenet-D`|
    ||`kn-IN-Standard-A`|
    ||`kn-IN-Standard-B`|
    ||`kn-IN-Wavenet-A`|
    ||`kn-IN-Wavenet-B`|
    ||`ko-KR-Neural2-A`|
    ||`ko-KR-Neural2-B`|
    ||`ko-KR-Neural2-C`|
    ||`ko-KR-Standard-A`|
    ||`ko-KR-Standard-B`|
    ||`ko-KR-Standard-C`|
    ||`ko-KR-Standard-D`|
    ||`ko-KR-Wavenet-A`|
    ||`ko-KR-Wavenet-B`|
    ||`ko-KR-Wavenet-C`|
    ||`ko-KR-Wavenet-D`|
    ||`lt-LT-Standard-A`|
    ||`lv-LV-Standard-A`|
    ||`ml-IN-Standard-A`|
    ||`ml-IN-Standard-B`|
    ||`ml-IN-Wavenet-A`|
    ||`ml-IN-Wavenet-B`|
    ||`ml-IN-Wavenet-C`|
    ||`ml-IN-Wavenet-D`|
    ||`mr-IN-Standard-A`|
    ||`mr-IN-Standard-B`|
    ||`mr-IN-Standard-C`|
    ||`mr-IN-Wavenet-A`|
    ||`mr-IN-Wavenet-B`|
    ||`mr-IN-Wavenet-C`|
    ||`ms-MY-Standard-A`|
    ||`ms-MY-Standard-B`|
    ||`ms-MY-Standard-C`|
    ||`ms-MY-Standard-D`|
    ||`ms-MY-Wavenet-A`|
    ||`ms-MY-Wavenet-B`|
    ||`ms-MY-Wavenet-C`|
    ||`ms-MY-Wavenet-D`|
    ||`nb-NO-Standard-A`|
    ||`nb-NO-Standard-B`|
    ||`nb-NO-Standard-C`|
    ||`nb-NO-Standard-D`|
    ||`nb-NO-Standard-E`|
    ||`nb-NO-Wavenet-A`|
    ||`nb-NO-Wavenet-B`|
    ||`nb-NO-Wavenet-C`|
    ||`nb-NO-Wavenet-D`|
    ||`nb-NO-Wavenet-E`|
    ||`nl-BE-Standard-A`|
    ||`nl-BE-Standard-B`|
    ||`nl-BE-Wavenet-A`|
    ||`nl-BE-Wavenet-B`|
    ||`nl-NL-Standard-A`|
    ||`nl-NL-Standard-B`|
    ||`nl-NL-Standard-C`|
    ||`nl-NL-Standard-D`|
    ||`nl-NL-Standard-E`|
    ||`nl-NL-Wavenet-A`|
    ||`nl-NL-Wavenet-B`|
    ||`nl-NL-Wavenet-C`|
    ||`nl-NL-Wavenet-D`|
    ||`nl-NL-Wavenet-E`|
    ||`pa-IN-Standard-A`|
    ||`pa-IN-Standard-B`|
    ||`pa-IN-Standard-C`|
    ||`pa-IN-Standard-D`|
    ||`pa-IN-Wavenet-A`|
    ||`pa-IN-Wavenet-B`|
    ||`pa-IN-Wavenet-C`|
    ||`pa-IN-Wavenet-D`|
    ||`pl-PL-Standard-A`|
    ||`pl-PL-Standard-B`|
    ||`pl-PL-Standard-C`|
    ||`pl-PL-Standard-D`|
    ||`pl-PL-Standard-E`|
    ||`pl-PL-Wavenet-A`|
    ||`pl-PL-Wavenet-B`|
    ||`pl-PL-Wavenet-C`|
    ||`pl-PL-Wavenet-D`|
    ||`pl-PL-Wavenet-E`|
    ||`pt-BR-Neural2-A`|
    ||`pt-BR-Neural2-B`|
    ||`pt-BR-Neural2-C`|
    ||`pt-BR-Standard-A`|
    ||`pt-BR-Standard-B`|
    ||`pt-BR-Standard-C`|
    ||`pt-BR-Wavenet-A`|
    ||`pt-BR-Wavenet-B`|
    ||`pt-BR-Wavenet-C`|
    ||`pt-PT-Standard-A`|
    ||`pt-PT-Standard-B`|
    ||`pt-PT-Standard-C`|
    ||`pt-PT-Standard-D`|
    ||`pt-PT-Wavenet-A`|
    ||`pt-PT-Wavenet-B`|
    ||`pt-PT-Wavenet-C`|
    ||`pt-PT-Wavenet-D`|
    ||`ro-RO-Standard-A`|
    ||`ro-RO-Wavenet-A`|
    ||`ru-RU-Standard-A`|
    ||`ru-RU-Standard-B`|
    ||`ru-RU-Standard-C`|
    ||`ru-RU-Standard-D`|
    ||`ru-RU-Standard-E`|
    ||`ru-RU-Wavenet-A`|
    ||`ru-RU-Wavenet-B`|
    ||`ru-RU-Wavenet-C`|
    ||`ru-RU-Wavenet-D`|
    ||`ru-RU-Wavenet-E`|
    ||`sk-SK-Standard-A`|
    ||`sk-SK-Wavenet-A`|
    ||`sr-RS-Standard-A`|
    ||`sv-SE-Standard-A`|
    ||`sv-SE-Standard-B`|
    ||`sv-SE-Standard-C`|
    ||`sv-SE-Standard-D`|
    ||`sv-SE-Standard-E`|
    ||`sv-SE-Wavenet-A`|
    ||`sv-SE-Wavenet-B`|
    ||`sv-SE-Wavenet-C`|
    ||`sv-SE-Wavenet-D`|
    ||`sv-SE-Wavenet-E`|
    ||`ta-IN-Standard-A`|
    ||`ta-IN-Standard-B`|
    ||`ta-IN-Standard-C`|
    ||`ta-IN-Standard-D`|
    ||`ta-IN-Wavenet-A`|
    ||`ta-IN-Wavenet-B`|
    ||`ta-IN-Wavenet-C`|
    ||`ta-IN-Wavenet-D`|
    ||`te-IN-Standard-A`|
    ||`te-IN-Standard-B`|
    ||`th-TH-Standard-A`|
    ||`tr-TR-Standard-A`|
    ||`tr-TR-Standard-B`|
    ||`tr-TR-Standard-C`|
    ||`tr-TR-Standard-D`|
    ||`tr-TR-Standard-E`|
    ||`tr-TR-Wavenet-A`|
    ||`tr-TR-Wavenet-B`|
    ||`tr-TR-Wavenet-C`|
    ||`tr-TR-Wavenet-D`|
    ||`tr-TR-Wavenet-E`|
    ||`uk-UA-Standard-A`|
    ||`uk-UA-Wavenet-A`|
    ||`vi-VN-Standard-A`|
    ||`vi-VN-Standard-B`|
    ||`vi-VN-Standard-C`|
    ||`vi-VN-Standard-D`|
    ||`vi-VN-Wavenet-A`|
    ||`vi-VN-Wavenet-B`|
    ||`vi-VN-Wavenet-C`|
    ||`vi-VN-Wavenet-D`|
    ||`yue-HK-Standard-A`|
    ||`yue-HK-Standard-B`|
    ||`yue-HK-Standard-C`|
    ||`yue-HK-Standard-D`|

    </details><details><summary>ibm</summary>





    |Name|Value|
    |----|-----|
    |**ibm**|`de-DE_BirgitV3Voice`|
    ||`de-DE_DieterV3Voice`|
    ||`de-DE_ErikaV3Voice`|
    ||`en-AU_HeidiExpressive`|
    ||`en-AU_JackExpressive`|
    ||`en-GB_CharlotteV3Voice`|
    ||`en-GB_JamesV3Voice`|
    ||`en-GB_KateV3Voice`|
    ||`en-US_AllisonExpressive`|
    ||`en-US_AllisonV3Voice`|
    ||`en-US_EmilyV3Voice`|
    ||`en-US_EmmaExpressive`|
    ||`en-US_HenryV3Voice`|
    ||`en-US_KevinV3Voice`|
    ||`en-US_LisaExpressive`|
    ||`en-US_LisaV3Voice`|
    ||`en-US_MichaelExpressive`|
    ||`en-US_MichaelV3Voice`|
    ||`en-US_OliviaV3Voice`|
    ||`es-ES_EnriqueV3Voice`|
    ||`es-ES_LauraV3Voice`|
    ||`es-LA_SofiaV3Voice`|
    ||`es-US_SofiaV3Voice`|
    ||`fr-CA_LouiseV3Voice`|
    ||`fr-FR_NicolasV3Voice`|
    ||`fr-FR_ReneeV3Voice`|
    ||`it-IT_FrancescaV3Voice`|
    ||`ja-JP_EmiV3Voice`|
    ||`ko-KR_JinV3Voice`|
    ||`nl-NL_MerelV3Voice`|
    ||`pt-BR_IsabelaV3Voice`|

    </details><details><summary>microsoft</summary>





    |Name|Value|
    |----|-----|
    |**microsoft**|`af-ZA-AdriNeural`|
    ||`af-ZA-WillemNeural`|
    ||`am-ET-AmehaNeural`|
    ||`am-ET-MekdesNeural`|
    ||`ar-AE-FatimaNeural`|
    ||`ar-AE-HamdanNeural`|
    ||`ar-BH-AliNeural`|
    ||`ar-BH-LailaNeural`|
    ||`ar-DZ-AminaNeural`|
    ||`ar-DZ-IsmaelNeural`|
    ||`ar-EG-SalmaNeural`|
    ||`ar-EG-ShakirNeural`|
    ||`ar-IQ-BasselNeural`|
    ||`ar-IQ-RanaNeural`|
    ||`ar-JO-SanaNeural`|
    ||`ar-JO-TaimNeural`|
    ||`ar-KW-FahedNeural`|
    ||`ar-KW-NouraNeural`|
    ||`ar-LB-LaylaNeural`|
    ||`ar-LB-RamiNeural`|
    ||`ar-LY-ImanNeural`|
    ||`ar-LY-OmarNeural`|
    ||`ar-MA-JamalNeural`|
    ||`ar-MA-MounaNeural`|
    ||`ar-OM-AbdullahNeural`|
    ||`ar-OM-AyshaNeural`|
    ||`ar-QA-AmalNeural`|
    ||`ar-QA-MoazNeural`|
    ||`ar-SA-HamedNeural`|
    ||`ar-SA-ZariyahNeural`|
    ||`ar-SY-AmanyNeural`|
    ||`ar-SY-LaithNeural`|
    ||`ar-TN-HediNeural`|
    ||`ar-TN-ReemNeural`|
    ||`ar-YE-MaryamNeural`|
    ||`ar-YE-SalehNeural`|
    ||`az-AZ-BabekNeural`|
    ||`az-AZ-BanuNeural`|
    ||`bg-BG-BorislavNeural`|
    ||`bg-BG-KalinaNeural`|
    ||`bn-BD-NabanitaNeural`|
    ||`bn-BD-PradeepNeural`|
    ||`bn-IN-BashkarNeural`|
    ||`bn-IN-TanishaaNeural`|
    ||`bs-BA-GoranNeural`|
    ||`bs-BA-VesnaNeural`|
    ||`ca-ES-AlbaNeural`|
    ||`ca-ES-EnricNeural`|
    ||`ca-ES-JoanaNeural`|
    ||`cs-CZ-AntoninNeural`|
    ||`cs-CZ-VlastaNeural`|
    ||`cy-GB-AledNeural`|
    ||`cy-GB-NiaNeural`|
    ||`da-DK-ChristelNeural`|
    ||`da-DK-JeppeNeural`|
    ||`de-AT-IngridNeural`|
    ||`de-AT-JonasNeural`|
    ||`de-CH-JanNeural`|
    ||`de-CH-LeniNeural`|
    ||`de-DE-AmalaNeural`|
    ||`de-DE-BerndNeural`|
    ||`de-DE-ChristophNeural`|
    ||`de-DE-ConradNeural`|
    ||`de-DE-ElkeNeural`|
    ||`de-DE-GiselaNeural`|
    ||`de-DE-KasperNeural`|
    ||`de-DE-KatjaNeural`|
    ||`de-DE-KillianNeural`|
    ||`de-DE-KlarissaNeural`|
    ||`de-DE-KlausNeural`|
    ||`de-DE-LouisaNeural`|
    ||`de-DE-MajaNeural`|
    ||`de-DE-RalfNeural`|
    ||`de-DE-TanjaNeural`|
    ||`el-GR-AthinaNeural`|
    ||`el-GR-NestorasNeural`|
    ||`en-AU-AnnetteNeural`|
    ||`en-AU-CarlyNeural`|
    ||`en-AU-DarrenNeural`|
    ||`en-AU-DuncanNeural`|
    ||`en-AU-ElsieNeural`|
    ||`en-AU-FreyaNeural`|
    ||`en-AU-JoanneNeural`|
    ||`en-AU-KenNeural`|
    ||`en-AU-KimNeural`|
    ||`en-AU-NatashaNeural`|
    ||`en-AU-NeilNeural`|
    ||`en-AU-TimNeural`|
    ||`en-AU-TinaNeural`|
    ||`en-AU-WilliamNeural`|
    ||`en-CA-ClaraNeural`|
    ||`en-CA-LiamNeural`|
    ||`en-GB-AbbiNeural`|
    ||`en-GB-AlfieNeural`|
    ||`en-GB-BellaNeural`|
    ||`en-GB-ElliotNeural`|
    ||`en-GB-EthanNeural`|
    ||`en-GB-HollieNeural`|
    ||`en-GB-LibbyNeural`|
    ||`en-GB-MaisieNeural`|
    ||`en-GB-NoahNeural`|
    ||`en-GB-OliverNeural`|
    ||`en-GB-OliviaNeural`|
    ||`en-GB-RyanNeural`|
    ||`en-GB-SoniaNeural`|
    ||`en-GB-ThomasNeural`|
    ||`en-HK-SamNeural`|
    ||`en-HK-YanNeural`|
    ||`en-IE-ConnorNeural`|
    ||`en-IE-EmilyNeural`|
    ||`en-IN-NeerjaNeural`|
    ||`en-IN-PrabhatNeural`|
    ||`en-KE-AsiliaNeural`|
    ||`en-KE-ChilembaNeural`|
    ||`en-NG-AbeoNeural`|
    ||`en-NG-EzinneNeural`|
    ||`en-NZ-MitchellNeural`|
    ||`en-NZ-MollyNeural`|
    ||`en-PH-JamesNeural`|
    ||`en-PH-RosaNeural`|
    ||`en-SG-LunaNeural`|
    ||`en-SG-WayneNeural`|
    ||`en-TZ-ElimuNeural`|
    ||`en-TZ-ImaniNeural`|
    ||`en-US-AIGenerate1Neural`|
    ||`en-US-AIGenerate2Neural`|
    ||`en-US-AmberNeural`|
    ||`en-US-AnaNeural`|
    ||`en-US-AriaNeural`|
    ||`en-US-AshleyNeural`|
    ||`en-US-BrandonNeural`|
    ||`en-US-ChristopherNeural`|
    ||`en-US-CoraNeural`|
    ||`en-US-DavisNeural`|
    ||`en-US-ElizabethNeural`|
    ||`en-US-EricNeural`|
    ||`en-US-GuyNeural`|
    ||`en-US-JacobNeural`|
    ||`en-US-JaneNeural`|
    ||`en-US-JasonNeural`|
    ||`en-US-JennyMultilingualNeural`|
    ||`en-US-JennyNeural`|
    ||`en-US-MichelleNeural`|
    ||`en-US-MonicaNeural`|
    ||`en-US-NancyNeural`|
    ||`en-US-RogerNeural`|
    ||`en-US-SaraNeural`|
    ||`en-US-SteffanNeural`|
    ||`en-US-TonyNeural`|
    ||`en-ZA-LeahNeural`|
    ||`en-ZA-LukeNeural`|
    ||`es-AR-ElenaNeural`|
    ||`es-AR-TomasNeural`|
    ||`es-BO-MarceloNeural`|
    ||`es-BO-SofiaNeural`|
    ||`es-CL-CatalinaNeural`|
    ||`es-CL-LorenzoNeural`|
    ||`es-CO-GonzaloNeural`|
    ||`es-CO-SalomeNeural`|
    ||`es-CR-JuanNeural`|
    ||`es-CR-MariaNeural`|
    ||`es-CU-BelkysNeural`|
    ||`es-CU-ManuelNeural`|
    ||`es-DO-EmilioNeural`|
    ||`es-DO-RamonaNeural`|
    ||`es-EC-AndreaNeural`|
    ||`es-EC-LuisNeural`|
    ||`es-ES-AbrilNeural`|
    ||`es-ES-AlvaroNeural`|
    ||`es-ES-ArnauNeural`|
    ||`es-ES-DarioNeural`|
    ||`es-ES-EliasNeural`|
    ||`es-ES-ElviraNeural`|
    ||`es-ES-EstrellaNeural`|
    ||`es-ES-IreneNeural`|
    ||`es-ES-LaiaNeural`|
    ||`es-ES-LiaNeural`|
    ||`es-ES-NilNeural`|
    ||`es-ES-SaulNeural`|
    ||`es-ES-TeoNeural`|
    ||`es-ES-TrianaNeural`|
    ||`es-ES-VeraNeural`|
    ||`es-GQ-JavierNeural`|
    ||`es-GQ-TeresaNeural`|
    ||`es-GT-AndresNeural`|
    ||`es-GT-MartaNeural`|
    ||`es-HN-CarlosNeural`|
    ||`es-HN-KarlaNeural`|
    ||`es-MX-BeatrizNeural`|
    ||`es-MX-CandelaNeural`|
    ||`es-MX-CarlotaNeural`|
    ||`es-MX-CecilioNeural`|
    ||`es-MX-DaliaNeural`|
    ||`es-MX-GerardoNeural`|
    ||`es-MX-JorgeNeural`|
    ||`es-MX-LarissaNeural`|
    ||`es-MX-LibertoNeural`|
    ||`es-MX-LucianoNeural`|
    ||`es-MX-MarinaNeural`|
    ||`es-MX-NuriaNeural`|
    ||`es-MX-PelayoNeural`|
    ||`es-MX-RenataNeural`|
    ||`es-MX-YagoNeural`|
    ||`es-NI-FedericoNeural`|
    ||`es-NI-YolandaNeural`|
    ||`es-PA-MargaritaNeural`|
    ||`es-PA-RobertoNeural`|
    ||`es-PE-AlexNeural`|
    ||`es-PE-CamilaNeural`|
    ||`es-PR-KarinaNeural`|
    ||`es-PR-VictorNeural`|
    ||`es-PY-MarioNeural`|
    ||`es-PY-TaniaNeural`|
    ||`es-SV-LorenaNeural`|
    ||`es-SV-RodrigoNeural`|
    ||`es-US-AlonsoNeural`|
    ||`es-US-PalomaNeural`|
    ||`es-UY-MateoNeural`|
    ||`es-UY-ValentinaNeural`|
    ||`es-VE-PaolaNeural`|
    ||`es-VE-SebastianNeural`|
    ||`et-EE-AnuNeural`|
    ||`et-EE-KertNeural`|
    ||`eu-ES-AinhoaNeural`|
    ||`eu-ES-AnderNeural`|
    ||`fa-IR-DilaraNeural`|
    ||`fa-IR-FaridNeural`|
    ||`fi-FI-HarriNeural`|
    ||`fi-FI-NooraNeural`|
    ||`fi-FI-SelmaNeural`|
    ||`fil-PH-AngeloNeural`|
    ||`fil-PH-BlessicaNeural`|
    ||`fr-BE-CharlineNeural`|
    ||`fr-BE-GerardNeural`|
    ||`fr-CA-AntoineNeural`|
    ||`fr-CA-JeanNeural`|
    ||`fr-CA-SylvieNeural`|
    ||`fr-CH-ArianeNeural`|
    ||`fr-CH-FabriceNeural`|
    ||`fr-FR-AlainNeural`|
    ||`fr-FR-BrigitteNeural`|
    ||`fr-FR-CelesteNeural`|
    ||`fr-FR-ClaudeNeural`|
    ||`fr-FR-CoralieNeural`|
    ||`fr-FR-DeniseNeural`|
    ||`fr-FR-EloiseNeural`|
    ||`fr-FR-HenriNeural`|
    ||`fr-FR-JacquelineNeural`|
    ||`fr-FR-JeromeNeural`|
    ||`fr-FR-JosephineNeural`|
    ||`fr-FR-MauriceNeural`|
    ||`fr-FR-YvesNeural`|
    ||`fr-FR-YvetteNeural`|
    ||`ga-IE-ColmNeural`|
    ||`ga-IE-OrlaNeural`|
    ||`gl-ES-RoiNeural`|
    ||`gl-ES-SabelaNeural`|
    ||`gu-IN-DhwaniNeural`|
    ||`gu-IN-NiranjanNeural`|
    ||`he-IL-AvriNeural`|
    ||`he-IL-HilaNeural`|
    ||`hi-IN-MadhurNeural`|
    ||`hi-IN-SwaraNeural`|
    ||`hr-HR-GabrijelaNeural`|
    ||`hr-HR-SreckoNeural`|
    ||`hu-HU-NoemiNeural`|
    ||`hu-HU-TamasNeural`|
    ||`hy-AM-AnahitNeural`|
    ||`hy-AM-HaykNeural`|
    ||`id-ID-ArdiNeural`|
    ||`id-ID-GadisNeural`|
    ||`is-IS-GudrunNeural`|
    ||`is-IS-GunnarNeural`|
    ||`it-IT-BenignoNeural`|
    ||`it-IT-CalimeroNeural`|
    ||`it-IT-CataldoNeural`|
    ||`it-IT-DiegoNeural`|
    ||`it-IT-ElsaNeural`|
    ||`it-IT-FabiolaNeural`|
    ||`it-IT-FiammaNeural`|
    ||`it-IT-GianniNeural`|
    ||`it-IT-ImeldaNeural`|
    ||`it-IT-IrmaNeural`|
    ||`it-IT-IsabellaNeural`|
    ||`it-IT-LisandroNeural`|
    ||`it-IT-PalmiraNeural`|
    ||`it-IT-PierinaNeural`|
    ||`it-IT-RinaldoNeural`|
    ||`ja-JP-AoiNeural`|
    ||`ja-JP-DaichiNeural`|
    ||`ja-JP-KeitaNeural`|
    ||`ja-JP-MayuNeural`|
    ||`ja-JP-NanamiNeural`|
    ||`ja-JP-NaokiNeural`|
    ||`ja-JP-ShioriNeural`|
    ||`jv-ID-DimasNeural`|
    ||`jv-ID-SitiNeural`|
    ||`ka-GE-EkaNeural`|
    ||`ka-GE-GiorgiNeural`|
    ||`kk-KZ-AigulNeural`|
    ||`kk-KZ-DauletNeural`|
    ||`km-KH-PisethNeural`|
    ||`km-KH-SreymomNeural`|
    ||`kn-IN-GaganNeural`|
    ||`kn-IN-SapnaNeural`|
    ||`ko-KR-BongJinNeural`|
    ||`ko-KR-GookMinNeural`|
    ||`ko-KR-InJoonNeural`|
    ||`ko-KR-JiMinNeural`|
    ||`ko-KR-SeoHyeonNeural`|
    ||`ko-KR-SoonBokNeural`|
    ||`ko-KR-SunHiNeural`|
    ||`ko-KR-YuJinNeural`|
    ||`lo-LA-ChanthavongNeural`|
    ||`lo-LA-KeomanyNeural`|
    ||`lt-LT-LeonasNeural`|
    ||`lt-LT-OnaNeural`|
    ||`lv-LV-EveritaNeural`|
    ||`lv-LV-NilsNeural`|
    ||`mk-MK-AleksandarNeural`|
    ||`mk-MK-MarijaNeural`|
    ||`ml-IN-MidhunNeural`|
    ||`ml-IN-SobhanaNeural`|
    ||`mn-MN-BataaNeural`|
    ||`mn-MN-YesuiNeural`|
    ||`mr-IN-AarohiNeural`|
    ||`mr-IN-ManoharNeural`|
    ||`ms-MY-OsmanNeural`|
    ||`ms-MY-YasminNeural`|
    ||`mt-MT-GraceNeural`|
    ||`mt-MT-JosephNeural`|
    ||`my-MM-NilarNeural`|
    ||`my-MM-ThihaNeural`|
    ||`nb-NO-FinnNeural`|
    ||`nb-NO-IselinNeural`|
    ||`nb-NO-PernilleNeural`|
    ||`ne-NP-HemkalaNeural`|
    ||`ne-NP-SagarNeural`|
    ||`nl-BE-ArnaudNeural`|
    ||`nl-BE-DenaNeural`|
    ||`nl-NL-ColetteNeural`|
    ||`nl-NL-FennaNeural`|
    ||`nl-NL-MaartenNeural`|
    ||`pl-PL-AgnieszkaNeural`|
    ||`pl-PL-MarekNeural`|
    ||`pl-PL-ZofiaNeural`|
    ||`ps-AF-GulNawazNeural`|
    ||`ps-AF-LatifaNeural`|
    ||`pt-BR-AntonioNeural`|
    ||`pt-BR-BrendaNeural`|
    ||`pt-BR-DonatoNeural`|
    ||`pt-BR-ElzaNeural`|
    ||`pt-BR-FabioNeural`|
    ||`pt-BR-FranciscaNeural`|
    ||`pt-BR-GiovannaNeural`|
    ||`pt-BR-HumbertoNeural`|
    ||`pt-BR-JulioNeural`|
    ||`pt-BR-LeilaNeural`|
    ||`pt-BR-LeticiaNeural`|
    ||`pt-BR-ManuelaNeural`|
    ||`pt-BR-NicolauNeural`|
    ||`pt-BR-ValerioNeural`|
    ||`pt-BR-YaraNeural`|
    ||`pt-PT-DuarteNeural`|
    ||`pt-PT-FernandaNeural`|
    ||`pt-PT-RaquelNeural`|
    ||`ro-RO-AlinaNeural`|
    ||`ro-RO-EmilNeural`|
    ||`ru-RU-DariyaNeural`|
    ||`ru-RU-DmitryNeural`|
    ||`ru-RU-SvetlanaNeural`|
    ||`si-LK-SameeraNeural`|
    ||`si-LK-ThiliniNeural`|
    ||`sk-SK-LukasNeural`|
    ||`sk-SK-ViktoriaNeural`|
    ||`sl-SI-PetraNeural`|
    ||`sl-SI-RokNeural`|
    ||`so-SO-MuuseNeural`|
    ||`so-SO-UbaxNeural`|
    ||`sq-AL-AnilaNeural`|
    ||`sq-AL-IlirNeural`|
    ||`sr-RS-NicholasNeural`|
    ||`sr-RS-SophieNeural`|
    ||`su-ID-JajangNeural`|
    ||`su-ID-TutiNeural`|
    ||`sv-SE-HilleviNeural`|
    ||`sv-SE-MattiasNeural`|
    ||`sv-SE-SofieNeural`|
    ||`sw-KE-RafikiNeural`|
    ||`sw-KE-ZuriNeural`|
    ||`sw-TZ-DaudiNeural`|
    ||`sw-TZ-RehemaNeural`|
    ||`ta-IN-PallaviNeural`|
    ||`ta-IN-ValluvarNeural`|
    ||`ta-LK-KumarNeural`|
    ||`ta-LK-SaranyaNeural`|
    ||`ta-MY-KaniNeural`|
    ||`ta-MY-SuryaNeural`|
    ||`ta-SG-AnbuNeural`|
    ||`ta-SG-VenbaNeural`|
    ||`te-IN-MohanNeural`|
    ||`te-IN-ShrutiNeural`|
    ||`th-TH-AcharaNeural`|
    ||`th-TH-NiwatNeural`|
    ||`th-TH-PremwadeeNeural`|
    ||`tr-TR-AhmetNeural`|
    ||`tr-TR-EmelNeural`|
    ||`uk-UA-OstapNeural`|
    ||`uk-UA-PolinaNeural`|
    ||`ur-IN-GulNeural`|
    ||`ur-IN-SalmanNeural`|
    ||`ur-PK-AsadNeural`|
    ||`ur-PK-UzmaNeural`|
    ||`uz-UZ-MadinaNeural`|
    ||`uz-UZ-SardorNeural`|
    ||`vi-VN-HoaiMyNeural`|
    ||`vi-VN-NamMinhNeural`|
    ||`wuu-CN-XiaotongNeural`|
    ||`wuu-CN-YunzheNeural`|
    ||`yue-CN-XiaoMinNeural`|
    ||`yue-CN-YunSongNeural`|
    ||`zh-CN-XiaochenNeural`|
    ||`zh-CN-XiaohanNeural`|
    ||`zh-CN-XiaomengNeural`|
    ||`zh-CN-XiaomoNeural`|
    ||`zh-CN-XiaoqiuNeural`|
    ||`zh-CN-XiaoruiNeural`|
    ||`zh-CN-XiaoshuangNeural`|
    ||`zh-CN-XiaoxiaoNeural`|
    ||`zh-CN-XiaoxuanNeural`|
    ||`zh-CN-XiaoyanNeural`|
    ||`zh-CN-XiaoyiNeural`|
    ||`zh-CN-XiaoyouNeural`|
    ||`zh-CN-XiaozhenNeural`|
    ||`zh-CN-YunfengNeural`|
    ||`zh-CN-YunhaoNeural`|
    ||`zh-CN-YunjianNeural`|
    ||`zh-CN-YunxiNeural`|
    ||`zh-CN-YunxiaNeural`|
    ||`zh-CN-YunyangNeural`|
    ||`zh-CN-YunyeNeural`|
    ||`zh-CN-YunzeNeural`|
    ||`zh-CN-henan-YundengNeural`|
    ||`zh-CN-liaoning-XiaobeiNeural`|
    ||`zh-CN-shaanxi-XiaoniNeural`|
    ||`zh-CN-shandong-YunxiangNeural`|
    ||`zh-CN-sichuan-YunxiNeural`|
    ||`zh-HK-HiuGaaiNeural`|
    ||`zh-HK-HiuMaanNeural`|
    ||`zh-HK-WanLungNeural`|
    ||`zh-TW-HsiaoChenNeural`|
    ||`zh-TW-HsiaoYuNeural`|
    ||`zh-TW-YunJheNeural`|
    ||`zu-ZA-ThandoNeural`|
    ||`zu-ZA-ThembaNeural`|

    </details><details><summary>lovoai</summary>





    |Name|Value|
    |----|-----|
    |**lovoai**|`af-ZA_Albertus Ruan`|
    ||`af-ZA_Danelle Wessel`|
    ||`am-ET_Abai Berhe`|
    ||`am-ET_Cherenet Tesfaye`|
    ||`ar-AE_Mansour Ahmed`|
    ||`ar-AE_Maryam Khan`|
    ||`ar-BH_Fatima Kumar`|
    ||`ar-BH_Omar Hassan`|
    ||`ar-DZ_Samia Touati`|
    ||`ar-DZ_Zuthimalin Brahimi`|
    ||`ar-EG_Ahmed Gamal`|
    ||`ar-EG_Reem Salah`|
    ||`ar-IQ_Aveen Majid`|
    ||`ar-IQ_Ismail Hashem`|
    ||`ar-JO_Fatima Jaber`|
    ||`ar-JO_Yousef Saleh`|
    ||`ar-KW_Areej Nair`|
    ||`ar-KW_Khaled Al Azmi`|
    ||`ar-LB_Abdel El Din`|
    ||`ar-LB_Eessa Kadifa`|
    ||`ar-LY_Abir Salem`|
    ||`ar-LY_Ahsan Omar`|
    ||`ar-MA_Hamid Bennani`|
    ||`ar-MA_Salma Naciri`|
    ||`ar-OM_Jabbar Singh`|
    ||`ar-OM_Zahra Sultan`|
    ||`ar-QA_Faizur Kumar`|
    ||`ar-QA_Noora Hussain`|
    ||`ar-SA_Majidah Khan`|
    ||`ar-SA_Omar Aziz`|
    ||`ar-SY_Oraida El-Assad`|
    ||`ar-SY_Rabah Ibrahim`|
    ||`ar-TN_Donia Cherif`|
    ||`ar-TN_Karim Dridi`|
    ||`ar-YE_Mansour Kasim`|
    ||`ar-YE_Mehdi Bawazeer`|
    ||`az-AZ_Ugur Quliyeva`|
    ||`az_AZ_Zeynab Cafarova`|
    ||`bg-BG_Damyan Ivanov`|
    ||`bg-BG_Fidanka Georgiev`|
    ||`bn-BD_Pranshu Akter`|
    ||`bn-BD_Vaagdevi Khatun`|
    ||`bn-IN_Gazi Mondal`|
    ||`bn-IN_Wali Ghosh`|
    ||`bs-BA_Esma Dodik`|
    ||`bs-BA_Ismet Rakic`|
    ||`ca-ES_Amada Fernando`|
    ||`ca-ES_Carmen Santiago`|
    ||`ca-ES_Miguel Torres`|
    ||`cs-CZ_Jana Rosicky`|
    ||`cs-CZ_Tomas Malecek`|
    ||`cy-GB_Branwen Jones`|
    ||`cy-GB_Elen Hughes`|
    ||`da-DK_Bjarne Jensen`|
    ||`da-DK_Helge Nielsen`|
    ||`de-AT_Lena Gruber`|
    ||`de-AT_Wilhelm Wagner`|
    ||`de-CH_Adolfus Meier`|
    ||`de-CH_Lara Keller`|
    ||`de-DE_Ada Weber`|
    ||`de-DE_Anna Schmidt`|
    ||`de-DE_Emma Muller`|
    ||`de-DE_Gerda Becker`|
    ||`de-DE_Hans Schulz`|
    ||`de-DE_Heidi Schneider`|
    ||`de-DE_Johanna Meyer`|
    ||`de-DE_Joshua Bauer`|
    ||`de-DE_Julian Koch`|
    ||`de-DE_Karl Hummels`|
    ||`de-DE_Maria Fischer`|
    ||`de-DE_Oliver Richter`|
    ||`de-DE_Otto Schaefer`|
    ||`de-DE_Petra Hoffman`|
    ||`de-DE_Walter Kimmich`|
    ||`el-GR_Petros Andino`|
    ||`el-GR_Thalia Klisiaris`|
    ||`en-AU_Amelia Taylor`|
    ||`en-AU_Charlotte Brown`|
    ||`en-AU_Darrell Robinson`|
    ||`en-AU_George Thompson`|
    ||`en-AU_Georgie Smith`|
    ||`en-AU_Isla Johnson`|
    ||`en-AU_Jake Nguyen`|
    ||`en-AU_Keegan Walker`|
    ||`en-AU_Kelly Opie`|
    ||`en-AU_Kevin Turner`|
    ||`en-AU_Mia White`|
    ||`en-AU_Nancy Jones`|
    ||`en-AU_Ryan Murphy`|
    ||`en-AU_Willow Martin`|
    ||`en-CA_Emily Salo`|
    ||`en-CA_Eric Fidyk`|
    ||`en-GB_Abigail Fraser`|
    ||`en-GB_Annie Smith`|
    ||`en-GB_Gertrude Baker`|
    ||`en-GB_Ian Kensington`|
    ||`en-GB_Kane Tooney`|
    ||`en-GB_Kelsey Michaels`|
    ||`en-GB_Kerrington Pacey`|
    ||`en-GB_Lizzy Wright`|
    ||`en-GB_Marcus O'Donell`|
    ||`en-GB_Nathaniel Jacobs`|
    ||`en-GB_Samuel Lee-Richards`|
    ||`en-GB_T.S. Cooper`|
    ||`en-GB_Theresa King`|
    ||`en-GB_William Tripp`|
    ||`en-HK_Heather Yiu`|
    ||`en-HK_Kevin Lau`|
    ||`en-IE_Aoife Byrne`|
    ||`en-IE_Bill Parkin`|
    ||`en-IN_Isha Singh`|
    ||`en-IN_Prabhdeep Patel`|
    ||`en-KE_Almasi Otieno`|
    ||`en-KE_Chitundu Mwangi`|
    ||`en-NG_Blessing Musa`|
    ||`en-NG_Kehinde Sade`|
    ||`en-NZ_Benson Duncan`|
    ||`en-NZ_Destiny Mitchell`|
    ||`en-PH_Angel dela Cruz`|
    ||`en-PH_Francis Reynaldo`|
    ||`en-SG_Chris Tan`|
    ||`en-SG_Rachel Ng`|
    ||`en-TZ_Busara Charles`|
    ||`en-TZ_Darweshi Juma`|
    ||`en-US_Alysha Imani`|
    ||`en-US_Betty Parker`|
    ||`en-US_Catherine Zania`|
    ||`en-US_Christopher Navarrez`|
    ||`en-US_Clara Ho`|
    ||`en-US_Eric Gonzalez`|
    ||`en-US_Heather Everett`|
    ||`en-US_Jamal Starke`|
    ||`en-US_Jasonna Johnson`|
    ||`en-US_Kaylee Montana`|
    ||`en-US_Ken hunter`|
    ||`en-US_Kim Howard`|
    ||`en-US_Kyle Moreno`|
    ||`en-US_Leroy Alshak`|
    ||`en-US_Micah Washington`|
    ||`en-US_Molly Richardson`|
    ||`en-US_Peter Lee`|
    ||`en-US_Phil Gough`|
    ||`en-US_Phoebe Nicholson`|
    ||`en-US_Samantha Hawthorne`|
    ||`en-US_Sean Orson`|
    ||`en-US_Serena Yang`|
    ||`en-US_Shannon Mechare`|
    ||`en-US_Thelma Browne`|
    ||`en-US_Tim Hardway`|
    ||`en-ZA_Cody Fergudson`|
    ||`en-ZA_Elna VanDijk`|
    ||`es-AR_Hyacinthe Castro`|
    ||`es-AR_Lautaro Gomez`|
    ||`es-BO_Elena Lopez`|
    ||`es-BO_Juan Perez`|
    ||`es-CL_Francisca Batistuta`|
    ||`es-CL_Gabriel Rodriguez`|
    ||`es-CO_Lorenzo Vazquez`|
    ||`es-CO_Sofia Garcia`|
    ||`es-CR_Guadalupe Suarez`|
    ||`es-CR_Sebastian Ramos`|
    ||`es-CU_Isabel Molina`|
    ||`es-CU_Luis Ortega`|
    ||`es-DO_Gabriela Serrano`|
    ||`es-DO_Raul Dominguez`|
    ||`es-EC_Angelina Romero`|
    ||`es-EC_Christian Diaz`|
    ||`es-EN_Carmen Martinela`|
    ||`es-ES_Andres Marin`|
    ||`es-ES_Emiliano Delgado`|
    ||`es-ES_Esmeralda Molina`|
    ||`es-ES_Hector Gavi`|
    ||`es-ES_Leo Gil`|
    ||`es-ES_Liliana Sanz`|
    ||`es-ES_Maria Ruiz`|
    ||`es-ES_Martin Enrique`|
    ||`es-ES_Miranda Navarro`|
    ||`es-ES_Pablo Iniesta`|
    ||`es-ES_Silvia Alvarez`|
    ||`es-ES_Teresa Iglesias`|
    ||`es-ES_Valentina Blanco`|
    ||`es-GQ_Elena Rubio`|
    ||`es-GQ_Teo Jimenez`|
    ||`es-GT_Ceciah Mendoza`|
    ||`es-GT_Paolo Ortiz`|
    ||`es-HN_Juana Flores`|
    ||`es-HN_Roberto Gutierrez`|
    ||`es-MX_Agata Albiol`|
    ||`es-MX_Darion Nunez`|
    ||`es-MX_Elias Lorenzo`|
    ||`es-MX_Elvira de Paul`|
    ||`es-MX_Enzo Paqueta`|
    ||`es-MX_Ezequiel Pacheco`|
    ||`es-MX_Iago Domingo`|
    ||`es-MX_Irene Vasquez`|
    ||`es-MX_Julieta Aguilar`|
    ||`es-MX_Lia Medina`|
    ||`es-MX_Nil Alvarez`|
    ||`es-MX_Pedro Rojas`|
    ||`es-MX_Rosa Valdoza`|
    ||`es-MX_Valencia Alba`|
    ||`es-MX_Veronica Mairal`|
    ||`es-NI_Abril Santacruz`|
    ||`es-NI_Lorenzo Llorente`|
    ||`es-PA_Liberto Marcos`|
    ||`es-PA_Yolanda Ezequiel`|
    ||`es-PE_Margarita de Fuentes`|
    ||`es-PE_Rey Sancho`|
    ||`es-PR_Alex de Santos`|
    ||`es-PR_Carlota Almiron`|
    ||`es-PY_Karina Diego`|
    ||`es-PY_Victor Mariela`|
    ||`es-SV_Jacinta Vela`|
    ||`es-SV_Marina Llorente`|
    ||`es-US_Jodrigo Alonso`|
    ||`es-US_Laia Paloma`|
    ||`es-US_Sergio Morata`|
    ||`es-UY_Lia Valentina`|
    ||`es-UY_Luis Ramon`|
    ||`es-VE_Manuel Rojos`|
    ||`es-VE_Sofia Vargas`|
    ||`et-EE_Barba Sepp`|
    ||`et-EE_Eduk Tamm`|
    ||`eu-ES_Markel Zubiri`|
    ||`eu-ES_Nahia Texpare`|
    ||`fa-IR_Bizhan Gilgamesh`|
    ||`fa-IR_Yasmina Hakimi`|
    ||`fi-FI_Anneli Niemnien`|
    ||`fi-FI_Kristiina Koskinen`|
    ||`fi-FI_Tapanni Korhonen`|
    ||`fil-PH_Amihan Reyes`|
    ||`fil-PH_Dennis de Saul`|
    ||`fr-BE_Louis Maes`|
    ||`fr-BE_Noah Peeters`|
    ||`fr-CA_Cherise DuPont`|
    ||`fr-CA_Olivier Varane`|
    ||`fr-CA_Raphael Jacques`|
    ||`fr-CH_Luca Dalot`|
    ||`fr-CH_Sylvie Gallace`|
    ||`fr-FR_Alain Hamel`|
    ||`fr-FR_Albertine Dubois`|
    ||`fr-FR_Antoine Petit`|
    ||`fr-FR_Brigitte Richard`|
    ||`fr-FR_Celeste Lefevre`|
    ||`fr-FR_Celine Bundchen`|
    ||`fr-FR_Damian Trezeguet`|
    ||`fr-FR_Diogo Pavard`|
    ||`fr-FR_Francoise LaFont`|
    ||`fr-FR_Gisele Guerin`|
    ||`fr-FR_Hugo Duval`|
    ||`fr-FR_Jacqueline Simon`|
    ||`fr-FR_Lois Allaire`|
    ||`fr-FR_Theo Bernard`|
    ||`ga-IE_Anja O'Brien`|
    ||`ga-IE_Liam Murphy`|
    ||`gl-ES_Clara Campos`|
    ||`gl-ES_Nicolas Montoya`|
    ||`gu-IN_Arzoo Chowdhury`|
    ||`gu-IN_Pramukh Barot`|
    ||`he-IL_Avi Goldmann`|
    ||`he-IL_Yael Haddad`|
    ||`hi-IN_Ashwin Nikhil`|
    ||`hi-IN_Uma Aravind`|
    ||`hr-HR_Krasna Perisic`|
    ||`hr-HR_Luka Horvat`|
    ||`hu-HU_Endre Szabo`|
    ||`hu-HU_Zoe Nagy`|
    ||`hy-AM_Arpi Hovhannisyan`|
    ||`hy-AM_Gor Grigoryan`|
    ||`id-ID_Bagaskoro Ulunjandi`|
    ||`id-ID_Diah Sukatendel`|
    ||`is-IS_Fridrika Sigurdsson`|
    ||`is-IS_Olafur Jonsdottir`|
    ||`it-IT_Alessandro Ferrari`|
    ||`it-IT_Alessia Ricci`|
    ||`it-IT_Allegra Greco`|
    ||`it-IT_Angelo Bianchi`|
    ||`it-IT_Antonio Colombo`|
    ||`it-IT_Eva De Luca`|
    ||`it-IT_Filomena Mancini`|
    ||`it-IT_Francesco Rossi`|
    ||`it-IT_Gaia Marino`|
    ||`it-IT_Gemma Conti`|
    ||`it-IT_Gianluigi Russo`|
    ||`it-IT_Greta Bruno`|
    ||`it-IT_Marco Romano`|
    ||`it-IT_Paul Esposito`|
    ||`it-IT_Serafina Gallo`|
    ||`ja-JP_Ayaka Musashi`|
    ||`ja-JP_Hiromi Tanaka`|
    ||`ja-JP_Hiroshi Maeda`|
    ||`ja-JP_Ichiro Sayaka`|
    ||`ja-JP_Naomi Sora`|
    ||`ja-JP_Sartoshi Juno`|
    ||`ja-JP_Sayuri Watanabe`|
    ||`jv-ID_Anom Zees`|
    ||`jv-ID_Bratawati Pulukadang`|
    ||`ka-GE_Ava Lomidze`|
    ||`ka-GE_Elijah Maisuradze`|
    ||`kk-KZ_Nurislam Omarov`|
    ||`kk-KZ_Rayana Kenes`|
    ||`km-KH_Chanthou Sok`|
    ||`km-KH_Kaliyanei Chea`|
    ||`kn-IN_Aadesh Madar`|
    ||`kn-IN_Rhyah Nayka`|
    ||`ko-KR_Eunjin Bae`|
    ||`ko-KR_Heechul Kim`|
    ||`ko-KR_Isu Choi`|
    ||`ko-KR_Jisoo Han`|
    ||`ko-KR_Meesun Kang`|
    ||`ko-KR_Minjoon Lee`|
    ||`ko-KR_Seung Hee Hwang`|
    ||`ko-KR_Yoosung Park`|
    ||`lo-LA_Lawan Vang`|
    ||`lo-LA_Sengphet Inthavong`|
    ||`lt-LT_Nojus Antanas`|
    ||`lt-LT_Ruta Bagdonas`|
    ||`lv-LV_Mozus Berzina`|
    ||`lv-LV_Santa Ozola`|
    ||`mk-MK_Berislav Stojanovski`|
    ||`mk-MK_Smaragda Jovanovska`|
    ||`ml-IN_Abha Nair`|
    ||`ml-IN_Akhil Kumar`|
    ||`mn-MN_Altan Batbayar`|
    ||`mn-MN_Enkhjargal Ganbold`|
    ||`mr-IN_Mihir Chitre`|
    ||`mr-IN_Vedvika Deo`|
    ||`ms-MY_Nur Tengku`|
    ||`ms-MY_Zikri Wan`|
    ||`mt-MT_Lola Farrugia`|
    ||`mt-MT_Milo Borg`|
    ||`my-MM_Dedan Khin`|
    ||`my-MM_Eindra Aung`|
    ||`nb-NO_Henrik Larsen`|
    ||`nb-NO_Vilde Hansen`|
    ||`nb_NO_Malin Pedersen`|
    ||`ne-NP_Batsal Khadka`|
    ||`ne-NP_Druhi Mahat`|
    ||`nl-BE_Arthur Mertens`|
    ||`nl-BE_Martine Claes`|
    ||`nl-NL_Adriana De Vries`|
    ||`nl-NL_Helena De Jong`|
    ||`nl-NL_Jan Visser`|
    ||`pl-PL_Ewa Grabowski`|
    ||`pl-PL_Piotr Duda`|
    ||`pl-PL_Zuzanna Kackz`|
    ||`ps-AF_Abdul-Alim Sayyid`|
    ||`ps-AF_Zahra Qurban`|
    ||`pt-BR_Adriana Rocha`|
    ||`pt-BR_Ana Bahiense`|
    ||`pt-BR_Anabella Teixeira`|
    ||`pt-BR_Antonia Macedo`|
    ||`pt-BR_Antonio Barros`|
    ||`pt-BR_Fernanda Pedreira`|
    ||`pt-BR_Francisco Guimaraes`|
    ||`pt-BR_Joao Azevedo`|
    ||`pt-BR_Jose Almeida`|
    ||`pt-BR_Juliana Costa`|
    ||`pt-BR_Marcia Ribeiro`|
    ||`pt-BR_Maria Cardoso`|
    ||`pt-BR_Paulo Correia`|
    ||`pt-BR_Pedro Magalhaes`|
    ||`pt-BR_Roberto Braga`|
    ||`pt-PT_Benedita Motta`|
    ||`pt-PT_Renato Matos`|
    ||`pt-PT_Rita Oliveira`|
    ||`ro-RO_Cristian Ionescu`|
    ||`ro-RO_Mirabela Gheata`|
    ||`ru-RU_Galina Ivanov`|
    ||`ru-RU_Nadezhda Smirnoff`|
    ||`ru-RU_Pyotr Semenov`|
    ||`si-LK_Kasun Perera`|
    ||`si-LK_Saanvi de Silva`|
    ||`sk-SK_Havel Varga`|
    ||`sk-SK_Olga Kovac`|
    ||`sl-SI_Neza Mlakar`|
    ||`sl-SI_Nik Krajnc`|
    ||`so-SO_Axado Ibrahim`|
    ||`so-SO_Taifa Mohamed`|
    ||`sq-AL_Bora Marku`|
    ||`sq-AL_Dren Kedare`|
    ||`sr-RS_Lara Markovic`|
    ||`sr-RS_Vlado Popovic`|
    ||`su-ID_Aarifa Bol`|
    ||`su-ID_Mustafa Deng`|
    ||`sv-SE_Agnes Lidstrom`|
    ||`sv-SE_Nicklas Forsberg`|
    ||`sv-SE_Wilma Sundin`|
    ||`sw-KE_Akeyo Njoroge`|
    ||`sw-KE_Chege Odhiambo`|
    ||`sw-TZ_Binti Ramadhani`|
    ||`sw-TZ_Darweshi Ally`|
    ||`ta-IN_Ashwin Kumar`|
    ||`ta-IN_Nila Suresh`|
    ||`ta-LK_Adya Pillai`|
    ||`ta-LK_Prahan Aachari`|
    ||`ta-MY_Aahna Konar`|
    ||`ta-MY_Kethan Nadar`|
    ||`ta-SG_Abilasha Naicker`|
    ||`ta-SG_Nemi Udayar`|
    ||`te-IN_Aarkash Reddy`|
    ||`te-IN_Tanvi Sharma`|
    ||`th-TH_Buppha Prasit`|
    ||`th-TH_Kanchana Sangthong`|
    ||`th-TH_Somchai Thongkham`|
    ||`tr-TR_Emre Ozdemir`|
    ||`tr-TR_Nehir Celik`|
    ||`uk-UA_Artem Shevchenko`|
    ||`uk-UA_Daryna Kovalenko`|
    ||`ur-IN_Farah Abbasi`|
    ||`ur-IN_Sharyar Alvi`|
    ||`ur-PK_Hamza Farooqi`|
    ||`ur-PK_Sana Dhanial`|
    ||`uz-UK_Javlonbek Yusupov`|
    ||`uz-UZ_Rustam Karimova`|
    ||`vi-VN_Huu Duong`|
    ||`vi-VN_Vi Ly`|
    ||`wuu-CN_Muchen Li`|
    ||`wuu-CN_Ruoxi Wang`|
    ||`yue-CN_Ah-lam Lei`|
    ||`yue-CN_Xiaoxiao Wong`|
    ||`zh-CN-henan_Genji Zhou`|
    ||`zh-CN-liaoning_Chu Zhang`|
    ||`zh-CN-shaanxi_Chunhua Lin`|
    ||`zh-CN-shandong_Jiayi Wu`|
    ||`zh-CN-sichuan_Juan Yang`|
    ||`zh-CN_An Liu`|
    ||`zh-CN_Bai Yang`|
    ||`zh-CN_Bao Huang`|
    ||`zh-CN_Chao Zhou`|
    ||`zh-CN_Chen Chen Huo`|
    ||`zh-CN_Cheng Sun`|
    ||`zh-CN_Chichi Wu`|
    ||`zh-CN_Chin Ma`|
    ||`zh-CN_Chun Hu`|
    ||`zh-CN_Cong Zhang`|
    ||`zh-CN_Da Xia Li`|
    ||`zh-CN_Daiyu Zhu`|
    ||`zh-CN_Diu Wang`|
    ||`zh-CN_Huan Luo`|
    ||`zh-CN_Huifen Chen`|
    ||`zh-CN_Huiqing Wang`|
    ||`zh-CN_Meng Li`|
    ||`zh-CN_Xuan Xu`|
    ||`zh-CN_Yifu Wu`|
    ||`zh-CN_Yihan Chen`|
    ||`zh-CN_Yinuo Zhang`|
    ||`zh-HK_Kun Lo`|
    ||`zh-HK_Lanying Lei`|
    ||`zh-HK_Lee Lam`|
    ||`zh-TW_Mingxia Luo`|
    ||`zh-TW_Mingzhu Gao`|
    ||`zh-TW_Susu Song`|
    ||`zu-ZA_Bonginkosi Masina`|
    ||`zu-ZA_Ulwazi Mangede`|

    </details><details><summary>elevenlabs</summary>





    |Name|Value|
    |----|-----|
    |**elevenlabs**|`de-DE_Multilingual_Callum`|
    ||`de-DE_Multilingual_Charlie`|
    ||`de-DE_Multilingual_Charlotte`|
    ||`de-DE_Multilingual_Clyde`|
    ||`de-DE_Multilingual_Daniel`|
    ||`de-DE_Multilingual_Dave`|
    ||`de-DE_Multilingual_Dorothy`|
    ||`de-DE_Multilingual_Emily`|
    ||`de-DE_Multilingual_Ethan`|
    ||`de-DE_Multilingual_Fin`|
    ||`de-DE_Multilingual_Freya`|
    ||`de-DE_Multilingual_Gigi`|
    ||`de-DE_Multilingual_Giovanni`|
    ||`de-DE_Multilingual_Grace`|
    ||`de-DE_Multilingual_Harry`|
    ||`de-DE_Multilingual_James`|
    ||`de-DE_Multilingual_Jeremy`|
    ||`de-DE_Multilingual_Jessie`|
    ||`de-DE_Multilingual_Joseph`|
    ||`de-DE_Multilingual_Liam`|
    ||`de-DE_Multilingual_Matilda`|
    ||`de-DE_Multilingual_Matthew`|
    ||`de-DE_Multilingual_Michael`|
    ||`de-DE_Multilingual_Mimi`|
    ||`de-DE_Multilingual_Nicole`|
    ||`de-DE_Multilingual_Patrick`|
    ||`de-DE_Multilingual_Ryan`|
    ||`de-DE_Multilingual_Serena`|
    ||`de-DE_Multilingual_Thomas`|
    ||`en-AU_Monolingual_Charlie`|
    ||`en-AU_Monolingual_James`|
    ||`en-GB_Monolingual_Daniel`|
    ||`en-GB_Monolingual_Dave`|
    ||`en-GB_Monolingual_Dorothy`|
    ||`en-GB_Monolingual_Joseph`|
    ||`en-GB_Monolingual_Matthew`|
    ||`en-IE_Monolingual_Fin`|
    ||`en-IT_Monolingual_Giovanni`|
    ||`en-SWE_Monolingual_Charlotte`|
    ||`en-SWE_Monolingual_Mimi`|
    ||`en-US_Monolingual_Adam`|
    ||`en-US_Monolingual_Antoni`|
    ||`en-US_Monolingual_Arnold`|
    ||`en-US_Monolingual_Bella`|
    ||`en-US_Monolingual_Callum`|
    ||`en-US_Monolingual_Clyde`|
    ||`en-US_Monolingual_Domi`|
    ||`en-US_Monolingual_Elli`|
    ||`en-US_Monolingual_Emily`|
    ||`en-US_Monolingual_Ethan`|
    ||`en-US_Monolingual_Freya`|
    ||`en-US_Monolingual_Gigi`|
    ||`en-US_Monolingual_Glinda`|
    ||`en-US_Monolingual_Grace`|
    ||`en-US_Monolingual_Harry`|
    ||`en-US_Monolingual_Jeremy`|
    ||`en-US_Monolingual_Jessie`|
    ||`en-US_Monolingual_Josh`|
    ||`en-US_Monolingual_Liam`|
    ||`en-US_Monolingual_Matilda`|
    ||`en-US_Monolingual_Michael`|
    ||`en-US_Monolingual_Nicole`|
    ||`en-US_Monolingual_Patrick`|
    ||`en-US_Monolingual_Rachel`|
    ||`en-US_Monolingual_Ryan`|
    ||`en-US_Monolingual_Sam`|
    ||`en-US_Monolingual_Sarah`|
    ||`en-US_Monolingual_Serena`|
    ||`en-US_Monolingual_Thomas`|
    ||`es-ES_Multilingual_Callum`|
    ||`es-ES_Multilingual_Charlie`|
    ||`es-ES_Multilingual_Charlotte`|
    ||`es-ES_Multilingual_Clyde`|
    ||`es-ES_Multilingual_Daniel`|
    ||`es-ES_Multilingual_Dave`|
    ||`es-ES_Multilingual_Dorothy`|
    ||`es-ES_Multilingual_Emily`|
    ||`es-ES_Multilingual_Ethan`|
    ||`es-ES_Multilingual_Fin`|
    ||`es-ES_Multilingual_Freya`|
    ||`es-ES_Multilingual_Gigi`|
    ||`es-ES_Multilingual_Giovanni`|
    ||`es-ES_Multilingual_Grace`|
    ||`es-ES_Multilingual_James`|
    ||`es-ES_Multilingual_Jeremy`|
    ||`es-ES_Multilingual_Jessie`|
    ||`es-ES_Multilingual_Joseph`|
    ||`es-ES_Multilingual_Liam`|
    ||`es-ES_Multilingual_Matilda`|
    ||`es-ES_Multilingual_Matthew`|
    ||`es-ES_Multilingual_Michael`|
    ||`es-ES_Multilingual_Mimi`|
    ||`es-ES_Multilingual_Nicole`|
    ||`es-ES_Multilingual_Patrick`|
    ||`es-ES_Multilingual_Ryan`|
    ||`es-ES_Multilingual_Serena`|
    ||`es-ES_Multilingual_Thomas`|
    ||`es-US_Multilingual_Harry`|
    ||`fr-FR_Multilingual_Callum`|
    ||`fr-FR_Multilingual_Charlie`|
    ||`fr-FR_Multilingual_Charlotte`|
    ||`fr-FR_Multilingual_Clyde`|
    ||`fr-FR_Multilingual_Daniel`|
    ||`fr-FR_Multilingual_Dave`|
    ||`fr-FR_Multilingual_Dorothy`|
    ||`fr-FR_Multilingual_Emily`|
    ||`fr-FR_Multilingual_Ethan`|
    ||`fr-FR_Multilingual_Fin`|
    ||`fr-FR_Multilingual_Freya`|
    ||`fr-FR_Multilingual_Gigi`|
    ||`fr-FR_Multilingual_Giovanni`|
    ||`fr-FR_Multilingual_Grace`|
    ||`fr-FR_Multilingual_Harry`|
    ||`fr-FR_Multilingual_James`|
    ||`fr-FR_Multilingual_Jeremy`|
    ||`fr-FR_Multilingual_Jessie`|
    ||`fr-FR_Multilingual_Joseph`|
    ||`fr-FR_Multilingual_Liam`|
    ||`fr-FR_Multilingual_Matilda`|
    ||`fr-FR_Multilingual_Matthew`|
    ||`fr-FR_Multilingual_Michael`|
    ||`fr-FR_Multilingual_Mimi`|
    ||`fr-FR_Multilingual_Nicole`|
    ||`fr-FR_Multilingual_Patrick`|
    ||`fr-FR_Multilingual_Ryan`|
    ||`fr-FR_Multilingual_Serena`|
    ||`fr-FR_Multilingual_Thomas`|
    ||`hi-IN_Multilingual_Callum`|
    ||`hi-IN_Multilingual_Charlie`|
    ||`hi-IN_Multilingual_Charlotte`|
    ||`hi-IN_Multilingual_Clyde`|
    ||`hi-IN_Multilingual_Daniel`|
    ||`hi-IN_Multilingual_Dave`|
    ||`hi-IN_Multilingual_Dorothy`|
    ||`hi-IN_Multilingual_Emily`|
    ||`hi-IN_Multilingual_Ethan`|
    ||`hi-IN_Multilingual_Fin`|
    ||`hi-IN_Multilingual_Freya`|
    ||`hi-IN_Multilingual_Gigi`|
    ||`hi-IN_Multilingual_Giovanni`|
    ||`hi-IN_Multilingual_Grace`|
    ||`hi-IN_Multilingual_Harry`|
    ||`hi-IN_Multilingual_James`|
    ||`hi-IN_Multilingual_Jeremy`|
    ||`hi-IN_Multilingual_Jessie`|
    ||`hi-IN_Multilingual_Joseph`|
    ||`hi-IN_Multilingual_Liam`|
    ||`hi-IN_Multilingual_Matilda`|
    ||`hi-IN_Multilingual_Matthew`|
    ||`hi-IN_Multilingual_Michael`|
    ||`hi-IN_Multilingual_Mimi`|
    ||`hi-IN_Multilingual_Nicole`|
    ||`hi-IN_Multilingual_Patrick`|
    ||`hi-IN_Multilingual_Ryan`|
    ||`hi-IN_Multilingual_Serena`|
    ||`hi-IN_Multilingual_Thomas`|
    ||`it-IT_Multilingual_Callum`|
    ||`it-IT_Multilingual_Charlie`|
    ||`it-IT_Multilingual_Charlotte`|
    ||`it-IT_Multilingual_Clyde`|
    ||`it-IT_Multilingual_Daniel`|
    ||`it-IT_Multilingual_Dave`|
    ||`it-IT_Multilingual_Dorothy`|
    ||`it-IT_Multilingual_Emily`|
    ||`it-IT_Multilingual_Ethan`|
    ||`it-IT_Multilingual_Fin`|
    ||`it-IT_Multilingual_Freya`|
    ||`it-IT_Multilingual_Gigi`|
    ||`it-IT_Multilingual_Giovanni`|
    ||`it-IT_Multilingual_Grace`|
    ||`it-IT_Multilingual_Harry`|
    ||`it-IT_Multilingual_James`|
    ||`it-IT_Multilingual_Jeremy`|
    ||`it-IT_Multilingual_Jessie`|
    ||`it-IT_Multilingual_Joseph`|
    ||`it-IT_Multilingual_Liam`|
    ||`it-IT_Multilingual_Matilda`|
    ||`it-IT_Multilingual_Matthew`|
    ||`it-IT_Multilingual_Michael`|
    ||`it-IT_Multilingual_Mimi`|
    ||`it-IT_Multilingual_Nicole`|
    ||`it-IT_Multilingual_Patrick`|
    ||`it-IT_Multilingual_Ryan`|
    ||`it-IT_Multilingual_Serena`|
    ||`it-IT_Multilingual_Thomas`|
    ||`pl-PL_Multilingual_Callum`|
    ||`pl-PL_Multilingual_Charlie`|
    ||`pl-PL_Multilingual_Charlotte`|
    ||`pl-PL_Multilingual_Clyde`|
    ||`pl-PL_Multilingual_Daniel`|
    ||`pl-PL_Multilingual_Dave`|
    ||`pl-PL_Multilingual_Dorothy`|
    ||`pl-PL_Multilingual_Emily`|
    ||`pl-PL_Multilingual_Ethan`|
    ||`pl-PL_Multilingual_Fin`|
    ||`pl-PL_Multilingual_Freya`|
    ||`pl-PL_Multilingual_Gigi`|
    ||`pl-PL_Multilingual_Giovanni`|
    ||`pl-PL_Multilingual_Grace`|
    ||`pl-PL_Multilingual_Harry`|
    ||`pl-PL_Multilingual_James`|
    ||`pl-PL_Multilingual_Jeremy`|
    ||`pl-PL_Multilingual_Jessie`|
    ||`pl-PL_Multilingual_Joseph`|
    ||`pl-PL_Multilingual_Liam`|
    ||`pl-PL_Multilingual_Matilda`|
    ||`pl-PL_Multilingual_Matthew`|
    ||`pl-PL_Multilingual_Michael`|
    ||`pl-PL_Multilingual_Mimi`|
    ||`pl-PL_Multilingual_Nicole`|
    ||`pl-PL_Multilingual_Patrick`|
    ||`pl-PL_Multilingual_Ryan`|
    ||`pl-PL_Multilingual_Serena`|
    ||`pl-PL_Multilingual_Thomas`|
    ||`pt-PT_Multilingual_Callum`|
    ||`pt-PT_Multilingual_Charlie`|
    ||`pt-PT_Multilingual_Charlotte`|
    ||`pt-PT_Multilingual_Clyde`|
    ||`pt-PT_Multilingual_Daniel`|
    ||`pt-PT_Multilingual_Dave`|
    ||`pt-PT_Multilingual_Dorothy`|
    ||`pt-PT_Multilingual_Emily`|
    ||`pt-PT_Multilingual_Ethan`|
    ||`pt-PT_Multilingual_Fin`|
    ||`pt-PT_Multilingual_Freya`|
    ||`pt-PT_Multilingual_Gigi`|
    ||`pt-PT_Multilingual_Giovanni`|
    ||`pt-PT_Multilingual_Grace`|
    ||`pt-PT_Multilingual_Harry`|
    ||`pt-PT_Multilingual_James`|
    ||`pt-PT_Multilingual_Jeremy`|
    ||`pt-PT_Multilingual_Jessie`|
    ||`pt-PT_Multilingual_Joseph`|
    ||`pt-PT_Multilingual_Liam`|
    ||`pt-PT_Multilingual_Matilda`|
    ||`pt-PT_Multilingual_Matthew`|
    ||`pt-PT_Multilingual_Michael`|
    ||`pt-PT_Multilingual_Mimi`|
    ||`pt-PT_Multilingual_Nicole`|
    ||`pt-PT_Multilingual_Patrick`|
    ||`pt-PT_Multilingual_Ryan`|
    ||`pt-PT_Multilingual_Serena`|
    ||`pt-PT_Multilingual_Thomas`|

    </details><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`af_alloy`|
    ||`af_echo`|
    ||`af_fable`|
    ||`af_nova`|
    ||`af_onyx`|
    ||`af_shimmer`|
    ||`ar_alloy`|
    ||`ar_echo`|
    ||`ar_fable`|
    ||`ar_nova`|
    ||`ar_onyx`|
    ||`ar_shimmer`|
    ||`az_alloy`|
    ||`az_echo`|
    ||`az_fable`|
    ||`az_nova`|
    ||`az_onyx`|
    ||`az_shimmer`|
    ||`be_alloy`|
    ||`be_echo`|
    ||`be_fable`|
    ||`be_nova`|
    ||`be_onyx`|
    ||`be_shimmer`|
    ||`bg_alloy`|
    ||`bg_echo`|
    ||`bg_fable`|
    ||`bg_nova`|
    ||`bg_onyx`|
    ||`bg_shimmer`|
    ||`bs_alloy`|
    ||`bs_echo`|
    ||`bs_fable`|
    ||`bs_nova`|
    ||`bs_onyx`|
    ||`bs_shimmer`|
    ||`ca_alloy`|
    ||`ca_echo`|
    ||`ca_fable`|
    ||`ca_nova`|
    ||`ca_onyx`|
    ||`ca_shimmer`|
    ||`cs_alloy`|
    ||`cs_echo`|
    ||`cs_fable`|
    ||`cs_nova`|
    ||`cs_onyx`|
    ||`cs_shimmer`|
    ||`cy_alloy`|
    ||`cy_echo`|
    ||`cy_fable`|
    ||`cy_nova`|
    ||`cy_onyx`|
    ||`cy_shimmer`|
    ||`da_alloy`|
    ||`da_echo`|
    ||`da_fable`|
    ||`da_nova`|
    ||`da_onyx`|
    ||`da_shimmer`|
    ||`de_alloy`|
    ||`de_echo`|
    ||`de_fable`|
    ||`de_nova`|
    ||`de_onyx`|
    ||`de_shimmer`|
    ||`el_alloy`|
    ||`el_echo`|
    ||`el_fable`|
    ||`el_nova`|
    ||`el_onyx`|
    ||`el_shimmer`|
    ||`en_alloy`|
    ||`en_echo`|
    ||`en_fable`|
    ||`en_nova`|
    ||`en_onyx`|
    ||`en_shimmer`|
    ||`es_alloy`|
    ||`es_echo`|
    ||`es_fable`|
    ||`es_nova`|
    ||`es_onyx`|
    ||`es_shimmer`|
    ||`et_alloy`|
    ||`et_echo`|
    ||`et_fable`|
    ||`et_nova`|
    ||`et_onyx`|
    ||`et_shimmer`|
    ||`fa_alloy`|
    ||`fa_echo`|
    ||`fa_fable`|
    ||`fa_nova`|
    ||`fa_onyx`|
    ||`fa_shimmer`|
    ||`fi_alloy`|
    ||`fi_echo`|
    ||`fi_fable`|
    ||`fi_nova`|
    ||`fi_onyx`|
    ||`fi_shimmer`|
    ||`fr_alloy`|
    ||`fr_echo`|
    ||`fr_fable`|
    ||`fr_nova`|
    ||`fr_onyx`|
    ||`fr_shimmer`|
    ||`gl_alloy`|
    ||`gl_echo`|
    ||`gl_fable`|
    ||`gl_nova`|
    ||`gl_onyx`|
    ||`gl_shimmer`|
    ||`he_alloy`|
    ||`he_echo`|
    ||`he_fable`|
    ||`he_nova`|
    ||`he_onyx`|
    ||`he_shimmer`|
    ||`hi_alloy`|
    ||`hi_echo`|
    ||`hi_fable`|
    ||`hi_nova`|
    ||`hi_onyx`|
    ||`hi_shimmer`|
    ||`hr_alloy`|
    ||`hr_echo`|
    ||`hr_fable`|
    ||`hr_nova`|
    ||`hr_onyx`|
    ||`hr_shimmer`|
    ||`hu_alloy`|
    ||`hu_echo`|
    ||`hu_fable`|
    ||`hu_nova`|
    ||`hu_onyx`|
    ||`hu_shimmer`|
    ||`hy_alloy`|
    ||`hy_echo`|
    ||`hy_fable`|
    ||`hy_nova`|
    ||`hy_onyx`|
    ||`hy_shimmer`|
    ||`id_alloy`|
    ||`id_echo`|
    ||`id_fable`|
    ||`id_nova`|
    ||`id_onyx`|
    ||`id_shimmer`|
    ||`is_alloy`|
    ||`is_echo`|
    ||`is_fable`|
    ||`is_nova`|
    ||`is_onyx`|
    ||`is_shimmer`|
    ||`it_alloy`|
    ||`it_echo`|
    ||`it_fable`|
    ||`it_nova`|
    ||`it_onyx`|
    ||`it_shimmer`|
    ||`ja_alloy`|
    ||`ja_echo`|
    ||`ja_fable`|
    ||`ja_nova`|
    ||`ja_onyx`|
    ||`ja_shimmer`|
    ||`kk_alloy`|
    ||`kk_echo`|
    ||`kk_fable`|
    ||`kk_nova`|
    ||`kk_onyx`|
    ||`kk_shimmer`|
    ||`kn_alloy`|
    ||`kn_echo`|
    ||`kn_fable`|
    ||`kn_nova`|
    ||`kn_onyx`|
    ||`kn_shimmer`|
    ||`ko_alloy`|
    ||`ko_echo`|
    ||`ko_fable`|
    ||`ko_nova`|
    ||`ko_onyx`|
    ||`ko_shimmer`|
    ||`lt_alloy`|
    ||`lt_echo`|
    ||`lt_fable`|
    ||`lt_nova`|
    ||`lt_onyx`|
    ||`lt_shimmer`|
    ||`lv_alloy`|
    ||`lv_echo`|
    ||`lv_fable`|
    ||`lv_nova`|
    ||`lv_onyx`|
    ||`lv_shimmer`|
    ||`mi_alloy`|
    ||`mi_echo`|
    ||`mi_fable`|
    ||`mi_nova`|
    ||`mi_onyx`|
    ||`mi_shimmer`|
    ||`mk_alloy`|
    ||`mk_echo`|
    ||`mk_fable`|
    ||`mk_nova`|
    ||`mk_onyx`|
    ||`mk_shimmer`|
    ||`mr_alloy`|
    ||`mr_echo`|
    ||`mr_fable`|
    ||`mr_nova`|
    ||`mr_onyx`|
    ||`mr_shimmer`|
    ||`ms_alloy`|
    ||`ms_echo`|
    ||`ms_fable`|
    ||`ms_nova`|
    ||`ms_onyx`|
    ||`ms_shimmer`|
    ||`ne_alloy`|
    ||`ne_echo`|
    ||`ne_fable`|
    ||`ne_nova`|
    ||`ne_onyx`|
    ||`ne_shimmer`|
    ||`nl_alloy`|
    ||`nl_echo`|
    ||`nl_fable`|
    ||`nl_nova`|
    ||`nl_onyx`|
    ||`nl_shimmer`|
    ||`no_alloy`|
    ||`no_echo`|
    ||`no_fable`|
    ||`no_nova`|
    ||`no_onyx`|
    ||`no_shimmer`|
    ||`pl_alloy`|
    ||`pl_echo`|
    ||`pl_fable`|
    ||`pl_nova`|
    ||`pl_onyx`|
    ||`pl_shimmer`|
    ||`pt_alloy`|
    ||`pt_echo`|
    ||`pt_fable`|
    ||`pt_nova`|
    ||`pt_onyx`|
    ||`pt_shimmer`|
    ||`ro_alloy`|
    ||`ro_echo`|
    ||`ro_fable`|
    ||`ro_nova`|
    ||`ro_onyx`|
    ||`ro_shimmer`|
    ||`ru_alloy`|
    ||`ru_echo`|
    ||`ru_fable`|
    ||`ru_nova`|
    ||`ru_onyx`|
    ||`ru_shimmer`|
    ||`sk_alloy`|
    ||`sk_echo`|
    ||`sk_fable`|
    ||`sk_nova`|
    ||`sk_onyx`|
    ||`sk_shimmer`|
    ||`sl_alloy`|
    ||`sl_echo`|
    ||`sl_fable`|
    ||`sl_nova`|
    ||`sl_onyx`|
    ||`sl_shimmer`|
    ||`sr_alloy`|
    ||`sr_echo`|
    ||`sr_fable`|
    ||`sr_nova`|
    ||`sr_onyx`|
    ||`sr_shimmer`|
    ||`sv_alloy`|
    ||`sv_echo`|
    ||`sv_fable`|
    ||`sv_nova`|
    ||`sv_onyx`|
    ||`sv_shimmer`|
    ||`sw_alloy`|
    ||`sw_echo`|
    ||`sw_fable`|
    ||`sw_nova`|
    ||`sw_onyx`|
    ||`sw_shimmer`|
    ||`ta_alloy`|
    ||`ta_echo`|
    ||`ta_fable`|
    ||`ta_nova`|
    ||`ta_onyx`|
    ||`ta_shimmer`|
    ||`th_alloy`|
    ||`th_echo`|
    ||`th_fable`|
    ||`th_nova`|
    ||`th_onyx`|
    ||`th_shimmer`|
    ||`tl_alloy`|
    ||`tl_echo`|
    ||`tl_fable`|
    ||`tl_nova`|
    ||`tl_onyx`|
    ||`tl_shimmer`|
    ||`tr_alloy`|
    ||`tr_echo`|
    ||`tr_fable`|
    ||`tr_nova`|
    ||`tr_onyx`|
    ||`tr_shimmer`|
    ||`uk_alloy`|
    ||`uk_echo`|
    ||`uk_fable`|
    ||`uk_nova`|
    ||`uk_onyx`|
    ||`uk_shimmer`|
    ||`ur_alloy`|
    ||`ur_echo`|
    ||`ur_fable`|
    ||`ur_nova`|
    ||`ur_onyx`|
    ||`ur_shimmer`|
    ||`vi_alloy`|
    ||`vi_echo`|
    ||`vi_fable`|
    ||`vi_nova`|
    ||`vi_onyx`|
    ||`vi_shimmer`|
    ||`zh_alloy`|
    ||`zh_echo`|
    ||`zh_fable`|
    ||`zh_nova`|
    ||`zh_onyx`|
    ||`zh_shimmer`|

    </details>

    </details>

    Args:
        body (AudiotextToSpeechTextToSpeechRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, NotFoundResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AudiotextToSpeechTextToSpeechRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Text to Speech

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**amazon**|-|`boto3 (v1.15.18)`|4.0 (per 1000000 char)|1 char
    |**amazon**|**Neural**|`boto3 (v1.15.18)`|16.0 (per 1000000 char)|1 char
    |**google**|-|`v1`|4.0 (per 1000000 char)|1 char
    |**google**|**Standard**|`v1`|4.0 (per 1000000 char)|1 char
    |**google**|**Neural**|`v1`|16.0 (per 1000000 char)|1 char
    |**google**|**Wavenet**|`v1`|16.0 (per 1000000 char)|1 char
    |**google**|**Studio**|`v1`|0.16 (per 1000 char)|1 char
    |**ibm**|-|`v1`|20.0 (per 1000000 char)|1000 char
    |**microsoft**|-|`v1.0`|16.0 (per 1000000 char)|1 char
    |**lovoai**|-|`v1`|160.0 (per 1000000 char)|1000 char
    |**elevenlabs**|-|`v1`|0.3 (per 1000 char)|1 char
    |**openai**|-|`v1.0`|0.015 (per 1000 char)|1 char


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
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bengali**|`bn`|
    |**Bosnian**|`bs`|
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
    |**Estonian**|`et`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Indonesian**|`id`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kannada**|`kn`|
    |**Kazakh**|`kk`|
    |**Korean**|`ko`|
    |**Lao**|`lo`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Macedonian**|`mk`|
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
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Serbian**|`sr`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**Spanish**|`es`|
    |**Standard Arabic**|`arb`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tamil**|`ta`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Turkish**|`tr`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Welsh**|`cy`|
    |**Wu Chinese**|`wuu`|
    |**Xhosa**|`xh`|
    |**Yue Chinese**|`yue`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans (South Africa)**|`af-ZA`|
    |**Albanian (Albania)**|`sq-AL`|
    |**Amharic (Ethiopia)**|`am-ET`|
    |**Arabic (Algeria)**|`ar-DZ`|
    |**Arabic (Bahrain)**|`ar-BH`|
    |**Arabic (Egypt)**|`ar-EG`|
    |**Arabic (Iraq)**|`ar-IQ`|
    |**Arabic (Jordan)**|`ar-JO`|
    |**Arabic (Kuwait)**|`ar-KW`|
    |**Arabic (Lebanon)**|`ar-LB`|
    |**Arabic (Libya)**|`ar-LY`|
    |**Arabic (Morocco)**|`ar-MA`|
    |**Arabic (Oman)**|`ar-OM`|
    |**Arabic (Pseudo-Accents)**|`ar-XA`|
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
    |**Cantonese (Hong Kong SAR China)**|`yue-HK`|
    |**Catalan (Spain)**|`ca-ES`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (China)**|`zh-CN-henan`|
    |**Chinese (China)**|`zh-CN-shandong`|
    |**Chinese (China)**|`zh-CN-sichuan`|
    |**Chinese (Hong Kong SAR China)**|`zh-HK`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Croatian (Croatia)**|`hr-HR`|
    |**Czech (Czechia)**|`cs-CZ`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Belgium)**|`nl-BE`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (Australia)**|`en-AU`|
    |**English (Canada)**|`en-CA`|
    |**English (Curaçao)**|`en-AN`|
    |**English (Hong Kong SAR China)**|`en-HK`|
    |**English (India)**|`en-IN`|
    |**English (Ireland)**|`en-IE`|
    |**English (Kenya)**|`en-KE`|
    |**English (New Zealand)**|`en-NZ`|
    |**English (Nigeria)**|`en-NG`|
    |**English (Philippines)**|`en-PH`|
    |**English (Singapore)**|`en-SG`|
    |**English (South Africa)**|`en-ZA`|
    |**English (Tanzania)**|`en-TZ`|
    |**English (United Kingdom)**|`en-GB`|
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
    |**Hindi (India)**|`hi-IN`|
    |**Hungarian (Hungary)**|`hu-HU`|
    |**Icelandic (Iceland)**|`is-IS`|
    |**Indonesian (Indonesia)**|`id-ID`|
    |**Irish (Ireland)**|`ga-IE`|
    |**Italian (Italy)**|`it-IT`|
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
    |**Mandarin Chinese (China)**|`cmn-CN`|
    |**Mandarin Chinese (Taiwan)**|`cmn-TW`|
    |**Marathi (India)**|`mr-IN`|
    |**Mongolian (Mongolia)**|`mn-MN`|
    |**Nepali (Nepal)**|`ne-NP`|
    |**Norwegian Bokmål (Norway)**|`nb-NO`|
    |**Pashto (Afghanistan)**|`ps-AF`|
    |**Persian (Iran)**|`fa-IR`|
    |**Polish (Poland)**|`pl-PL`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Punjabi (India)**|`pa-IN`|
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
    |**Uzbek (United Kingdom)**|`uz-UK`|
    |**Uzbek (Uzbekistan)**|`uz-UZ`|
    |**Vietnamese (Vietnam)**|`vi-VN`|
    |**Welsh (United Kingdom)**|`cy-GB`|
    |**Wu Chinese (China)**|`wuu-CN`|
    |**Xhosa (South Africa)**|`xh-ZA`|
    |**Zulu (South Africa)**|`zu-ZA`|

    </details><details><summary>Supported Models</summary><details><summary>amazon</summary>





    |Name|Value|
    |----|-----|
    |**amazon**|`ar-AE_Hala_Neural`|
    ||`arb_Zeina_Standard`|
    ||`ca-ES_Arlet_Neural`|
    ||`cmn-CN_Zhiyu_Neural`|
    ||`cmn-CN_Zhiyu_Standard`|
    ||`cy-GB_Gwyneth_Standard`|
    ||`da-DK_Mads_Standard`|
    ||`da-DK_Naja_Standard`|
    ||`de-AT_Hannah_Neural`|
    ||`de-DE_Daniel_Neural`|
    ||`de-DE_Hans_Standard`|
    ||`de-DE_Marlene_Standard`|
    ||`de-DE_Vicki_Neural`|
    ||`de-DE_Vicki_Standard`|
    ||`en-AU_Nicole_Neural`|
    ||`en-AU_Olivia_Standard`|
    ||`en-AU_Russell_Neural`|
    ||`en-GB_Amy_Neural`|
    ||`en-GB_Amy_Standard`|
    ||`en-GB_Arthur_Neural`|
    ||`en-GB_Brian_Neural`|
    ||`en-GB_Brian_Standard`|
    ||`en-GB_Emma_Neural`|
    ||`en-GB_Emma_Standard`|
    ||`en-IN_Aditi_Standard`|
    ||`en-IN_Kajal_Neural`|
    ||`en-IN_Raveena_Standard`|
    ||`en-NZ_Aria_Neural`|
    ||`en-US_Ivy_Neural`|
    ||`en-US_Ivy_Standard`|
    ||`en-US_Joanna_Neural`|
    ||`en-US_Joanna_Standard`|
    ||`en-US_Joey_Neural`|
    ||`en-US_Joey_Standard`|
    ||`en-US_Justin_Neural`|
    ||`en-US_Justin_Standard`|
    ||`en-US_Kendra_Neural`|
    ||`en-US_Kendra_Standard`|
    ||`en-US_Kevin_Neural`|
    ||`en-US_Kimberly_Neural`|
    ||`en-US_Kimberly_Standard`|
    ||`en-US_Matthew_Neural`|
    ||`en-US_Matthew_Standard`|
    ||`en-US_Ruth_Neural`|
    ||`en-US_Salli_Neural`|
    ||`en-US_Salli_Standard`|
    ||`en-US_Stephen_Neural`|
    ||`en-ZA_Ayanda_Neural`|
    ||`es-ES_Conchita_Standard`|
    ||`es-ES_Enrique_Standard`|
    ||`es-ES_Lucia_Neural`|
    ||`es-ES_Lucia_Standard`|
    ||`es-ES_Sergio_Neural`|
    ||`es-MX_Andres_Neural`|
    ||`es-MX_Mia_Neural`|
    ||`es-MX_Mia_Standard`|
    ||`es-US_Lupe_Neural`|
    ||`es-US_Lupe_Standard`|
    ||`es-US_Miguel_Standard`|
    ||`es-US_Pedro_Neural`|
    ||`es-US_Penelope_Standard`|
    ||`fi-FI_Suvi_Neural`|
    ||`fr-CA_Chantal_Standard`|
    ||`fr-CA_Gabrielle_Neural`|
    ||`fr-CA_Liam_Neural`|
    ||`fr-FR_Celine_Standard`|
    ||`fr-FR_Lea_Neural`|
    ||`fr-FR_Lea_Standard`|
    ||`fr-FR_Mathieu_Standard`|
    ||`fr-FR_Remi_Neural`|
    ||`hi-IN_Aditi_Standard`|
    ||`hi-IN_Kajal_Neural`|
    ||`is-IS_Dora_Standard`|
    ||`is-IS_Karl_Neural`|
    ||`is-IS_Karl_Standard`|
    ||`it-IT_Adriano_Neural`|
    ||`it-IT_Bianca_Neural`|
    ||`it-IT_Bianca_Standard`|
    ||`it-IT_Carla_Standard`|
    ||`it-IT_Giorgio_Standard`|
    ||`ja-JP_Kazuha_Neural`|
    ||`ja-JP_Mizuki_Standard`|
    ||`ja-JP_Takumi_Neural`|
    ||`ja-JP_Takumi_Standard`|
    ||`ja-JP_Tomoko_Neural`|
    ||`ko-KR_Seoyeon_Neural`|
    ||`ko-KR_Seoyeon_Standard`|
    ||`nb-NO_Liv_Standard`|
    ||`nl-NL_Laura_Neural`|
    ||`nl-NL_Lotte_Standard`|
    ||`nl-NL_Ruben_Standard`|
    ||`pl-PL_Ewa_Standard`|
    ||`pl-PL_Jacek_Standard`|
    ||`pl-PL_Jan_Standard`|
    ||`pl-PL_Maja_Standard`|
    ||`pl-PL_Ola_Neural`|
    ||`pt-BR_Camila_Neural`|
    ||`pt-BR_Camila_Standard`|
    ||`pt-BR_Ricardo_Standard`|
    ||`pt-BR_Thiago_Neural`|
    ||`pt-BR_Vitoria_Neural`|
    ||`pt-BR_Vitoria_Standard`|
    ||`pt-PT_Cristiano_Standard`|
    ||`pt-PT_Ines_Neural`|
    ||`pt-PT_Ines_Standard`|
    ||`ro-RO_Carmen_Standard`|
    ||`ru-RU_Maxim_Standard`|
    ||`ru-RU_Tatyana_Standard`|
    ||`sv-SE_Astrid_Standard`|
    ||`sv-SE_Elin_Neural`|
    ||`tr-TR_Filiz_Standard`|
    ||`yue-CN_Hiujin_Neural`|

    </details><details><summary>google</summary>





    |Name|Value|
    |----|-----|
    |**google**|`af-ZA-Standard-A`|
    ||`ar-XA-Standard-A`|
    ||`ar-XA-Standard-B`|
    ||`ar-XA-Standard-C`|
    ||`ar-XA-Standard-D`|
    ||`ar-XA-Wavenet-A`|
    ||`ar-XA-Wavenet-B`|
    ||`ar-XA-Wavenet-C`|
    ||`ar-XA-Wavenet-D`|
    ||`bg-BG-Standard-A`|
    ||`bn-IN-Standard-A`|
    ||`bn-IN-Standard-B`|
    ||`bn-IN-Wavenet-A`|
    ||`bn-IN-Wavenet-B`|
    ||`ca-ES-Standard-A`|
    ||`cmn-CN-Standard-A`|
    ||`cmn-CN-Standard-B`|
    ||`cmn-CN-Standard-C`|
    ||`cmn-CN-Standard-D`|
    ||`cmn-CN-Wavenet-A`|
    ||`cmn-CN-Wavenet-B`|
    ||`cmn-CN-Wavenet-C`|
    ||`cmn-CN-Wavenet-D`|
    ||`cmn-TW-Standard-A`|
    ||`cmn-TW-Standard-B`|
    ||`cmn-TW-Standard-C`|
    ||`cmn-TW-Wavenet-A`|
    ||`cmn-TW-Wavenet-B`|
    ||`cmn-TW-Wavenet-C`|
    ||`cs-CZ-Standard-A`|
    ||`cs-CZ-Wavenet-A`|
    ||`da-DK-Standard-A`|
    ||`da-DK-Standard-C`|
    ||`da-DK-Standard-D`|
    ||`da-DK-Standard-E`|
    ||`da-DK-Wavenet-A`|
    ||`da-DK-Wavenet-C`|
    ||`da-DK-Wavenet-D`|
    ||`da-DK-Wavenet-E`|
    ||`de-DE-Neural2-B`|
    ||`de-DE-Neural2-C`|
    ||`de-DE-Neural2-D`|
    ||`de-DE-Neural2-F`|
    ||`de-DE-Standard-A`|
    ||`de-DE-Standard-B`|
    ||`de-DE-Standard-C`|
    ||`de-DE-Standard-D`|
    ||`de-DE-Standard-E`|
    ||`de-DE-Standard-F`|
    ||`de-DE-Wavenet-A`|
    ||`de-DE-Wavenet-B`|
    ||`de-DE-Wavenet-C`|
    ||`de-DE-Wavenet-D`|
    ||`de-DE-Wavenet-E`|
    ||`de-DE-Wavenet-F`|
    ||`el-GR-Standard-A`|
    ||`el-GR-Wavenet-A`|
    ||`en-AU-Neural2-A`|
    ||`en-AU-Neural2-B`|
    ||`en-AU-Neural2-C`|
    ||`en-AU-Neural2-D`|
    ||`en-AU-News-E`|
    ||`en-AU-News-F`|
    ||`en-AU-News-G`|
    ||`en-AU-Standard-A`|
    ||`en-AU-Standard-B`|
    ||`en-AU-Standard-C`|
    ||`en-AU-Standard-D`|
    ||`en-AU-Wavenet-A`|
    ||`en-AU-Wavenet-B`|
    ||`en-AU-Wavenet-C`|
    ||`en-AU-Wavenet-D`|
    ||`en-GB-Neural2-A`|
    ||`en-GB-Neural2-B`|
    ||`en-GB-Neural2-C`|
    ||`en-GB-Neural2-D`|
    ||`en-GB-Neural2-F`|
    ||`en-GB-News-G`|
    ||`en-GB-News-H`|
    ||`en-GB-News-I`|
    ||`en-GB-News-J`|
    ||`en-GB-News-K`|
    ||`en-GB-News-L`|
    ||`en-GB-News-M`|
    ||`en-GB-Standard-A`|
    ||`en-GB-Standard-B`|
    ||`en-GB-Standard-C`|
    ||`en-GB-Standard-D`|
    ||`en-GB-Standard-F`|
    ||`en-GB-Wavenet-A`|
    ||`en-GB-Wavenet-B`|
    ||`en-GB-Wavenet-C`|
    ||`en-GB-Wavenet-D`|
    ||`en-GB-Wavenet-F`|
    ||`en-IN-Standard-A`|
    ||`en-IN-Standard-B`|
    ||`en-IN-Standard-C`|
    ||`en-IN-Standard-D`|
    ||`en-IN-Wavenet-A`|
    ||`en-IN-Wavenet-B`|
    ||`en-IN-Wavenet-C`|
    ||`en-IN-Wavenet-D`|
    ||`en-US-Neural2-A`|
    ||`en-US-Neural2-C`|
    ||`en-US-Neural2-D`|
    ||`en-US-Neural2-E`|
    ||`en-US-Neural2-F`|
    ||`en-US-Neural2-G`|
    ||`en-US-Neural2-H`|
    ||`en-US-Neural2-I`|
    ||`en-US-Neural2-J`|
    ||`en-US-News-K`|
    ||`en-US-News-L`|
    ||`en-US-News-M`|
    ||`en-US-News-N`|
    ||`en-US-Standard-A`|
    ||`en-US-Standard-B`|
    ||`en-US-Standard-C`|
    ||`en-US-Standard-D`|
    ||`en-US-Standard-E`|
    ||`en-US-Standard-F`|
    ||`en-US-Standard-G`|
    ||`en-US-Standard-H`|
    ||`en-US-Standard-I`|
    ||`en-US-Standard-J`|
    ||`en-US-Studio-M`|
    ||`en-US-Studio-O`|
    ||`en-US-Wavenet-A`|
    ||`en-US-Wavenet-B`|
    ||`en-US-Wavenet-C`|
    ||`en-US-Wavenet-D`|
    ||`en-US-Wavenet-E`|
    ||`en-US-Wavenet-F`|
    ||`en-US-Wavenet-G`|
    ||`en-US-Wavenet-H`|
    ||`en-US-Wavenet-I`|
    ||`en-US-Wavenet-J`|
    ||`es-ES-Neural2-A`|
    ||`es-ES-Neural2-B`|
    ||`es-ES-Neural2-C`|
    ||`es-ES-Neural2-D`|
    ||`es-ES-Neural2-E`|
    ||`es-ES-Neural2-F`|
    ||`es-ES-Standard-A`|
    ||`es-ES-Standard-B`|
    ||`es-ES-Standard-C`|
    ||`es-ES-Standard-D`|
    ||`es-ES-Wavenet-B`|
    ||`es-ES-Wavenet-C`|
    ||`es-ES-Wavenet-D`|
    ||`es-US-Neural2-A`|
    ||`es-US-Neural2-B`|
    ||`es-US-Neural2-C`|
    ||`es-US-News-D`|
    ||`es-US-News-E`|
    ||`es-US-News-F`|
    ||`es-US-News-G`|
    ||`es-US-Standard-A`|
    ||`es-US-Standard-B`|
    ||`es-US-Standard-C`|
    ||`es-US-Studio-B`|
    ||`es-US-Wavenet-A`|
    ||`es-US-Wavenet-B`|
    ||`es-US-Wavenet-C`|
    ||`eu-ES-Standard-A`|
    ||`fi-FI-Standard-A`|
    ||`fi-FI-Wavenet-A`|
    ||`fil-PH-Standard-A`|
    ||`fil-PH-Standard-B`|
    ||`fil-PH-Standard-C`|
    ||`fil-PH-Standard-D`|
    ||`fil-PH-Wavenet-A`|
    ||`fil-PH-Wavenet-B`|
    ||`fil-PH-Wavenet-C`|
    ||`fil-PH-Wavenet-D`|
    ||`fr-CA-Neural2-A`|
    ||`fr-CA-Neural2-B`|
    ||`fr-CA-Neural2-C`|
    ||`fr-CA-Neural2-D`|
    ||`fr-CA-Standard-A`|
    ||`fr-CA-Standard-B`|
    ||`fr-CA-Standard-C`|
    ||`fr-CA-Standard-D`|
    ||`fr-CA-Wavenet-A`|
    ||`fr-CA-Wavenet-B`|
    ||`fr-CA-Wavenet-C`|
    ||`fr-CA-Wavenet-D`|
    ||`fr-FR-Neural2-A`|
    ||`fr-FR-Neural2-B`|
    ||`fr-FR-Neural2-C`|
    ||`fr-FR-Neural2-D`|
    ||`fr-FR-Neural2-E`|
    ||`fr-FR-Standard-A`|
    ||`fr-FR-Standard-B`|
    ||`fr-FR-Standard-C`|
    ||`fr-FR-Standard-D`|
    ||`fr-FR-Standard-E`|
    ||`fr-FR-Wavenet-A`|
    ||`fr-FR-Wavenet-B`|
    ||`fr-FR-Wavenet-C`|
    ||`fr-FR-Wavenet-D`|
    ||`fr-FR-Wavenet-E`|
    ||`gl-ES-Standard-A`|
    ||`gu-IN-Standard-A`|
    ||`gu-IN-Standard-B`|
    ||`gu-IN-Wavenet-A`|
    ||`gu-IN-Wavenet-B`|
    ||`he-IL-Standard-A`|
    ||`he-IL-Standard-B`|
    ||`he-IL-Standard-C`|
    ||`he-IL-Standard-D`|
    ||`he-IL-Wavenet-A`|
    ||`he-IL-Wavenet-B`|
    ||`he-IL-Wavenet-C`|
    ||`he-IL-Wavenet-D`|
    ||`hi-IN-Neural2-A`|
    ||`hi-IN-Neural2-B`|
    ||`hi-IN-Neural2-C`|
    ||`hi-IN-Neural2-D`|
    ||`hi-IN-Standard-A`|
    ||`hi-IN-Standard-B`|
    ||`hi-IN-Standard-C`|
    ||`hi-IN-Standard-D`|
    ||`hi-IN-Wavenet-A`|
    ||`hi-IN-Wavenet-B`|
    ||`hi-IN-Wavenet-C`|
    ||`hi-IN-Wavenet-D`|
    ||`hu-HU-Standard-A`|
    ||`hu-HU-Wavenet-A`|
    ||`id-ID-Standard-A`|
    ||`id-ID-Standard-B`|
    ||`id-ID-Standard-C`|
    ||`id-ID-Standard-D`|
    ||`id-ID-Wavenet-A`|
    ||`id-ID-Wavenet-B`|
    ||`id-ID-Wavenet-C`|
    ||`id-ID-Wavenet-D`|
    ||`is-IS-Standard-A`|
    ||`it-IT-Neural2-A`|
    ||`it-IT-Neural2-C`|
    ||`it-IT-Standard-A`|
    ||`it-IT-Standard-B`|
    ||`it-IT-Standard-C`|
    ||`it-IT-Standard-D`|
    ||`it-IT-Wavenet-A`|
    ||`it-IT-Wavenet-B`|
    ||`it-IT-Wavenet-C`|
    ||`it-IT-Wavenet-D`|
    ||`ja-JP-Neural2-B`|
    ||`ja-JP-Neural2-C`|
    ||`ja-JP-Neural2-D`|
    ||`ja-JP-Standard-A`|
    ||`ja-JP-Standard-B`|
    ||`ja-JP-Standard-C`|
    ||`ja-JP-Standard-D`|
    ||`ja-JP-Wavenet-A`|
    ||`ja-JP-Wavenet-B`|
    ||`ja-JP-Wavenet-C`|
    ||`ja-JP-Wavenet-D`|
    ||`kn-IN-Standard-A`|
    ||`kn-IN-Standard-B`|
    ||`kn-IN-Wavenet-A`|
    ||`kn-IN-Wavenet-B`|
    ||`ko-KR-Neural2-A`|
    ||`ko-KR-Neural2-B`|
    ||`ko-KR-Neural2-C`|
    ||`ko-KR-Standard-A`|
    ||`ko-KR-Standard-B`|
    ||`ko-KR-Standard-C`|
    ||`ko-KR-Standard-D`|
    ||`ko-KR-Wavenet-A`|
    ||`ko-KR-Wavenet-B`|
    ||`ko-KR-Wavenet-C`|
    ||`ko-KR-Wavenet-D`|
    ||`lt-LT-Standard-A`|
    ||`lv-LV-Standard-A`|
    ||`ml-IN-Standard-A`|
    ||`ml-IN-Standard-B`|
    ||`ml-IN-Wavenet-A`|
    ||`ml-IN-Wavenet-B`|
    ||`ml-IN-Wavenet-C`|
    ||`ml-IN-Wavenet-D`|
    ||`mr-IN-Standard-A`|
    ||`mr-IN-Standard-B`|
    ||`mr-IN-Standard-C`|
    ||`mr-IN-Wavenet-A`|
    ||`mr-IN-Wavenet-B`|
    ||`mr-IN-Wavenet-C`|
    ||`ms-MY-Standard-A`|
    ||`ms-MY-Standard-B`|
    ||`ms-MY-Standard-C`|
    ||`ms-MY-Standard-D`|
    ||`ms-MY-Wavenet-A`|
    ||`ms-MY-Wavenet-B`|
    ||`ms-MY-Wavenet-C`|
    ||`ms-MY-Wavenet-D`|
    ||`nb-NO-Standard-A`|
    ||`nb-NO-Standard-B`|
    ||`nb-NO-Standard-C`|
    ||`nb-NO-Standard-D`|
    ||`nb-NO-Standard-E`|
    ||`nb-NO-Wavenet-A`|
    ||`nb-NO-Wavenet-B`|
    ||`nb-NO-Wavenet-C`|
    ||`nb-NO-Wavenet-D`|
    ||`nb-NO-Wavenet-E`|
    ||`nl-BE-Standard-A`|
    ||`nl-BE-Standard-B`|
    ||`nl-BE-Wavenet-A`|
    ||`nl-BE-Wavenet-B`|
    ||`nl-NL-Standard-A`|
    ||`nl-NL-Standard-B`|
    ||`nl-NL-Standard-C`|
    ||`nl-NL-Standard-D`|
    ||`nl-NL-Standard-E`|
    ||`nl-NL-Wavenet-A`|
    ||`nl-NL-Wavenet-B`|
    ||`nl-NL-Wavenet-C`|
    ||`nl-NL-Wavenet-D`|
    ||`nl-NL-Wavenet-E`|
    ||`pa-IN-Standard-A`|
    ||`pa-IN-Standard-B`|
    ||`pa-IN-Standard-C`|
    ||`pa-IN-Standard-D`|
    ||`pa-IN-Wavenet-A`|
    ||`pa-IN-Wavenet-B`|
    ||`pa-IN-Wavenet-C`|
    ||`pa-IN-Wavenet-D`|
    ||`pl-PL-Standard-A`|
    ||`pl-PL-Standard-B`|
    ||`pl-PL-Standard-C`|
    ||`pl-PL-Standard-D`|
    ||`pl-PL-Standard-E`|
    ||`pl-PL-Wavenet-A`|
    ||`pl-PL-Wavenet-B`|
    ||`pl-PL-Wavenet-C`|
    ||`pl-PL-Wavenet-D`|
    ||`pl-PL-Wavenet-E`|
    ||`pt-BR-Neural2-A`|
    ||`pt-BR-Neural2-B`|
    ||`pt-BR-Neural2-C`|
    ||`pt-BR-Standard-A`|
    ||`pt-BR-Standard-B`|
    ||`pt-BR-Standard-C`|
    ||`pt-BR-Wavenet-A`|
    ||`pt-BR-Wavenet-B`|
    ||`pt-BR-Wavenet-C`|
    ||`pt-PT-Standard-A`|
    ||`pt-PT-Standard-B`|
    ||`pt-PT-Standard-C`|
    ||`pt-PT-Standard-D`|
    ||`pt-PT-Wavenet-A`|
    ||`pt-PT-Wavenet-B`|
    ||`pt-PT-Wavenet-C`|
    ||`pt-PT-Wavenet-D`|
    ||`ro-RO-Standard-A`|
    ||`ro-RO-Wavenet-A`|
    ||`ru-RU-Standard-A`|
    ||`ru-RU-Standard-B`|
    ||`ru-RU-Standard-C`|
    ||`ru-RU-Standard-D`|
    ||`ru-RU-Standard-E`|
    ||`ru-RU-Wavenet-A`|
    ||`ru-RU-Wavenet-B`|
    ||`ru-RU-Wavenet-C`|
    ||`ru-RU-Wavenet-D`|
    ||`ru-RU-Wavenet-E`|
    ||`sk-SK-Standard-A`|
    ||`sk-SK-Wavenet-A`|
    ||`sr-RS-Standard-A`|
    ||`sv-SE-Standard-A`|
    ||`sv-SE-Standard-B`|
    ||`sv-SE-Standard-C`|
    ||`sv-SE-Standard-D`|
    ||`sv-SE-Standard-E`|
    ||`sv-SE-Wavenet-A`|
    ||`sv-SE-Wavenet-B`|
    ||`sv-SE-Wavenet-C`|
    ||`sv-SE-Wavenet-D`|
    ||`sv-SE-Wavenet-E`|
    ||`ta-IN-Standard-A`|
    ||`ta-IN-Standard-B`|
    ||`ta-IN-Standard-C`|
    ||`ta-IN-Standard-D`|
    ||`ta-IN-Wavenet-A`|
    ||`ta-IN-Wavenet-B`|
    ||`ta-IN-Wavenet-C`|
    ||`ta-IN-Wavenet-D`|
    ||`te-IN-Standard-A`|
    ||`te-IN-Standard-B`|
    ||`th-TH-Standard-A`|
    ||`tr-TR-Standard-A`|
    ||`tr-TR-Standard-B`|
    ||`tr-TR-Standard-C`|
    ||`tr-TR-Standard-D`|
    ||`tr-TR-Standard-E`|
    ||`tr-TR-Wavenet-A`|
    ||`tr-TR-Wavenet-B`|
    ||`tr-TR-Wavenet-C`|
    ||`tr-TR-Wavenet-D`|
    ||`tr-TR-Wavenet-E`|
    ||`uk-UA-Standard-A`|
    ||`uk-UA-Wavenet-A`|
    ||`vi-VN-Standard-A`|
    ||`vi-VN-Standard-B`|
    ||`vi-VN-Standard-C`|
    ||`vi-VN-Standard-D`|
    ||`vi-VN-Wavenet-A`|
    ||`vi-VN-Wavenet-B`|
    ||`vi-VN-Wavenet-C`|
    ||`vi-VN-Wavenet-D`|
    ||`yue-HK-Standard-A`|
    ||`yue-HK-Standard-B`|
    ||`yue-HK-Standard-C`|
    ||`yue-HK-Standard-D`|

    </details><details><summary>ibm</summary>





    |Name|Value|
    |----|-----|
    |**ibm**|`de-DE_BirgitV3Voice`|
    ||`de-DE_DieterV3Voice`|
    ||`de-DE_ErikaV3Voice`|
    ||`en-AU_HeidiExpressive`|
    ||`en-AU_JackExpressive`|
    ||`en-GB_CharlotteV3Voice`|
    ||`en-GB_JamesV3Voice`|
    ||`en-GB_KateV3Voice`|
    ||`en-US_AllisonExpressive`|
    ||`en-US_AllisonV3Voice`|
    ||`en-US_EmilyV3Voice`|
    ||`en-US_EmmaExpressive`|
    ||`en-US_HenryV3Voice`|
    ||`en-US_KevinV3Voice`|
    ||`en-US_LisaExpressive`|
    ||`en-US_LisaV3Voice`|
    ||`en-US_MichaelExpressive`|
    ||`en-US_MichaelV3Voice`|
    ||`en-US_OliviaV3Voice`|
    ||`es-ES_EnriqueV3Voice`|
    ||`es-ES_LauraV3Voice`|
    ||`es-LA_SofiaV3Voice`|
    ||`es-US_SofiaV3Voice`|
    ||`fr-CA_LouiseV3Voice`|
    ||`fr-FR_NicolasV3Voice`|
    ||`fr-FR_ReneeV3Voice`|
    ||`it-IT_FrancescaV3Voice`|
    ||`ja-JP_EmiV3Voice`|
    ||`ko-KR_JinV3Voice`|
    ||`nl-NL_MerelV3Voice`|
    ||`pt-BR_IsabelaV3Voice`|

    </details><details><summary>microsoft</summary>





    |Name|Value|
    |----|-----|
    |**microsoft**|`af-ZA-AdriNeural`|
    ||`af-ZA-WillemNeural`|
    ||`am-ET-AmehaNeural`|
    ||`am-ET-MekdesNeural`|
    ||`ar-AE-FatimaNeural`|
    ||`ar-AE-HamdanNeural`|
    ||`ar-BH-AliNeural`|
    ||`ar-BH-LailaNeural`|
    ||`ar-DZ-AminaNeural`|
    ||`ar-DZ-IsmaelNeural`|
    ||`ar-EG-SalmaNeural`|
    ||`ar-EG-ShakirNeural`|
    ||`ar-IQ-BasselNeural`|
    ||`ar-IQ-RanaNeural`|
    ||`ar-JO-SanaNeural`|
    ||`ar-JO-TaimNeural`|
    ||`ar-KW-FahedNeural`|
    ||`ar-KW-NouraNeural`|
    ||`ar-LB-LaylaNeural`|
    ||`ar-LB-RamiNeural`|
    ||`ar-LY-ImanNeural`|
    ||`ar-LY-OmarNeural`|
    ||`ar-MA-JamalNeural`|
    ||`ar-MA-MounaNeural`|
    ||`ar-OM-AbdullahNeural`|
    ||`ar-OM-AyshaNeural`|
    ||`ar-QA-AmalNeural`|
    ||`ar-QA-MoazNeural`|
    ||`ar-SA-HamedNeural`|
    ||`ar-SA-ZariyahNeural`|
    ||`ar-SY-AmanyNeural`|
    ||`ar-SY-LaithNeural`|
    ||`ar-TN-HediNeural`|
    ||`ar-TN-ReemNeural`|
    ||`ar-YE-MaryamNeural`|
    ||`ar-YE-SalehNeural`|
    ||`az-AZ-BabekNeural`|
    ||`az-AZ-BanuNeural`|
    ||`bg-BG-BorislavNeural`|
    ||`bg-BG-KalinaNeural`|
    ||`bn-BD-NabanitaNeural`|
    ||`bn-BD-PradeepNeural`|
    ||`bn-IN-BashkarNeural`|
    ||`bn-IN-TanishaaNeural`|
    ||`bs-BA-GoranNeural`|
    ||`bs-BA-VesnaNeural`|
    ||`ca-ES-AlbaNeural`|
    ||`ca-ES-EnricNeural`|
    ||`ca-ES-JoanaNeural`|
    ||`cs-CZ-AntoninNeural`|
    ||`cs-CZ-VlastaNeural`|
    ||`cy-GB-AledNeural`|
    ||`cy-GB-NiaNeural`|
    ||`da-DK-ChristelNeural`|
    ||`da-DK-JeppeNeural`|
    ||`de-AT-IngridNeural`|
    ||`de-AT-JonasNeural`|
    ||`de-CH-JanNeural`|
    ||`de-CH-LeniNeural`|
    ||`de-DE-AmalaNeural`|
    ||`de-DE-BerndNeural`|
    ||`de-DE-ChristophNeural`|
    ||`de-DE-ConradNeural`|
    ||`de-DE-ElkeNeural`|
    ||`de-DE-GiselaNeural`|
    ||`de-DE-KasperNeural`|
    ||`de-DE-KatjaNeural`|
    ||`de-DE-KillianNeural`|
    ||`de-DE-KlarissaNeural`|
    ||`de-DE-KlausNeural`|
    ||`de-DE-LouisaNeural`|
    ||`de-DE-MajaNeural`|
    ||`de-DE-RalfNeural`|
    ||`de-DE-TanjaNeural`|
    ||`el-GR-AthinaNeural`|
    ||`el-GR-NestorasNeural`|
    ||`en-AU-AnnetteNeural`|
    ||`en-AU-CarlyNeural`|
    ||`en-AU-DarrenNeural`|
    ||`en-AU-DuncanNeural`|
    ||`en-AU-ElsieNeural`|
    ||`en-AU-FreyaNeural`|
    ||`en-AU-JoanneNeural`|
    ||`en-AU-KenNeural`|
    ||`en-AU-KimNeural`|
    ||`en-AU-NatashaNeural`|
    ||`en-AU-NeilNeural`|
    ||`en-AU-TimNeural`|
    ||`en-AU-TinaNeural`|
    ||`en-AU-WilliamNeural`|
    ||`en-CA-ClaraNeural`|
    ||`en-CA-LiamNeural`|
    ||`en-GB-AbbiNeural`|
    ||`en-GB-AlfieNeural`|
    ||`en-GB-BellaNeural`|
    ||`en-GB-ElliotNeural`|
    ||`en-GB-EthanNeural`|
    ||`en-GB-HollieNeural`|
    ||`en-GB-LibbyNeural`|
    ||`en-GB-MaisieNeural`|
    ||`en-GB-NoahNeural`|
    ||`en-GB-OliverNeural`|
    ||`en-GB-OliviaNeural`|
    ||`en-GB-RyanNeural`|
    ||`en-GB-SoniaNeural`|
    ||`en-GB-ThomasNeural`|
    ||`en-HK-SamNeural`|
    ||`en-HK-YanNeural`|
    ||`en-IE-ConnorNeural`|
    ||`en-IE-EmilyNeural`|
    ||`en-IN-NeerjaNeural`|
    ||`en-IN-PrabhatNeural`|
    ||`en-KE-AsiliaNeural`|
    ||`en-KE-ChilembaNeural`|
    ||`en-NG-AbeoNeural`|
    ||`en-NG-EzinneNeural`|
    ||`en-NZ-MitchellNeural`|
    ||`en-NZ-MollyNeural`|
    ||`en-PH-JamesNeural`|
    ||`en-PH-RosaNeural`|
    ||`en-SG-LunaNeural`|
    ||`en-SG-WayneNeural`|
    ||`en-TZ-ElimuNeural`|
    ||`en-TZ-ImaniNeural`|
    ||`en-US-AIGenerate1Neural`|
    ||`en-US-AIGenerate2Neural`|
    ||`en-US-AmberNeural`|
    ||`en-US-AnaNeural`|
    ||`en-US-AriaNeural`|
    ||`en-US-AshleyNeural`|
    ||`en-US-BrandonNeural`|
    ||`en-US-ChristopherNeural`|
    ||`en-US-CoraNeural`|
    ||`en-US-DavisNeural`|
    ||`en-US-ElizabethNeural`|
    ||`en-US-EricNeural`|
    ||`en-US-GuyNeural`|
    ||`en-US-JacobNeural`|
    ||`en-US-JaneNeural`|
    ||`en-US-JasonNeural`|
    ||`en-US-JennyMultilingualNeural`|
    ||`en-US-JennyNeural`|
    ||`en-US-MichelleNeural`|
    ||`en-US-MonicaNeural`|
    ||`en-US-NancyNeural`|
    ||`en-US-RogerNeural`|
    ||`en-US-SaraNeural`|
    ||`en-US-SteffanNeural`|
    ||`en-US-TonyNeural`|
    ||`en-ZA-LeahNeural`|
    ||`en-ZA-LukeNeural`|
    ||`es-AR-ElenaNeural`|
    ||`es-AR-TomasNeural`|
    ||`es-BO-MarceloNeural`|
    ||`es-BO-SofiaNeural`|
    ||`es-CL-CatalinaNeural`|
    ||`es-CL-LorenzoNeural`|
    ||`es-CO-GonzaloNeural`|
    ||`es-CO-SalomeNeural`|
    ||`es-CR-JuanNeural`|
    ||`es-CR-MariaNeural`|
    ||`es-CU-BelkysNeural`|
    ||`es-CU-ManuelNeural`|
    ||`es-DO-EmilioNeural`|
    ||`es-DO-RamonaNeural`|
    ||`es-EC-AndreaNeural`|
    ||`es-EC-LuisNeural`|
    ||`es-ES-AbrilNeural`|
    ||`es-ES-AlvaroNeural`|
    ||`es-ES-ArnauNeural`|
    ||`es-ES-DarioNeural`|
    ||`es-ES-EliasNeural`|
    ||`es-ES-ElviraNeural`|
    ||`es-ES-EstrellaNeural`|
    ||`es-ES-IreneNeural`|
    ||`es-ES-LaiaNeural`|
    ||`es-ES-LiaNeural`|
    ||`es-ES-NilNeural`|
    ||`es-ES-SaulNeural`|
    ||`es-ES-TeoNeural`|
    ||`es-ES-TrianaNeural`|
    ||`es-ES-VeraNeural`|
    ||`es-GQ-JavierNeural`|
    ||`es-GQ-TeresaNeural`|
    ||`es-GT-AndresNeural`|
    ||`es-GT-MartaNeural`|
    ||`es-HN-CarlosNeural`|
    ||`es-HN-KarlaNeural`|
    ||`es-MX-BeatrizNeural`|
    ||`es-MX-CandelaNeural`|
    ||`es-MX-CarlotaNeural`|
    ||`es-MX-CecilioNeural`|
    ||`es-MX-DaliaNeural`|
    ||`es-MX-GerardoNeural`|
    ||`es-MX-JorgeNeural`|
    ||`es-MX-LarissaNeural`|
    ||`es-MX-LibertoNeural`|
    ||`es-MX-LucianoNeural`|
    ||`es-MX-MarinaNeural`|
    ||`es-MX-NuriaNeural`|
    ||`es-MX-PelayoNeural`|
    ||`es-MX-RenataNeural`|
    ||`es-MX-YagoNeural`|
    ||`es-NI-FedericoNeural`|
    ||`es-NI-YolandaNeural`|
    ||`es-PA-MargaritaNeural`|
    ||`es-PA-RobertoNeural`|
    ||`es-PE-AlexNeural`|
    ||`es-PE-CamilaNeural`|
    ||`es-PR-KarinaNeural`|
    ||`es-PR-VictorNeural`|
    ||`es-PY-MarioNeural`|
    ||`es-PY-TaniaNeural`|
    ||`es-SV-LorenaNeural`|
    ||`es-SV-RodrigoNeural`|
    ||`es-US-AlonsoNeural`|
    ||`es-US-PalomaNeural`|
    ||`es-UY-MateoNeural`|
    ||`es-UY-ValentinaNeural`|
    ||`es-VE-PaolaNeural`|
    ||`es-VE-SebastianNeural`|
    ||`et-EE-AnuNeural`|
    ||`et-EE-KertNeural`|
    ||`eu-ES-AinhoaNeural`|
    ||`eu-ES-AnderNeural`|
    ||`fa-IR-DilaraNeural`|
    ||`fa-IR-FaridNeural`|
    ||`fi-FI-HarriNeural`|
    ||`fi-FI-NooraNeural`|
    ||`fi-FI-SelmaNeural`|
    ||`fil-PH-AngeloNeural`|
    ||`fil-PH-BlessicaNeural`|
    ||`fr-BE-CharlineNeural`|
    ||`fr-BE-GerardNeural`|
    ||`fr-CA-AntoineNeural`|
    ||`fr-CA-JeanNeural`|
    ||`fr-CA-SylvieNeural`|
    ||`fr-CH-ArianeNeural`|
    ||`fr-CH-FabriceNeural`|
    ||`fr-FR-AlainNeural`|
    ||`fr-FR-BrigitteNeural`|
    ||`fr-FR-CelesteNeural`|
    ||`fr-FR-ClaudeNeural`|
    ||`fr-FR-CoralieNeural`|
    ||`fr-FR-DeniseNeural`|
    ||`fr-FR-EloiseNeural`|
    ||`fr-FR-HenriNeural`|
    ||`fr-FR-JacquelineNeural`|
    ||`fr-FR-JeromeNeural`|
    ||`fr-FR-JosephineNeural`|
    ||`fr-FR-MauriceNeural`|
    ||`fr-FR-YvesNeural`|
    ||`fr-FR-YvetteNeural`|
    ||`ga-IE-ColmNeural`|
    ||`ga-IE-OrlaNeural`|
    ||`gl-ES-RoiNeural`|
    ||`gl-ES-SabelaNeural`|
    ||`gu-IN-DhwaniNeural`|
    ||`gu-IN-NiranjanNeural`|
    ||`he-IL-AvriNeural`|
    ||`he-IL-HilaNeural`|
    ||`hi-IN-MadhurNeural`|
    ||`hi-IN-SwaraNeural`|
    ||`hr-HR-GabrijelaNeural`|
    ||`hr-HR-SreckoNeural`|
    ||`hu-HU-NoemiNeural`|
    ||`hu-HU-TamasNeural`|
    ||`hy-AM-AnahitNeural`|
    ||`hy-AM-HaykNeural`|
    ||`id-ID-ArdiNeural`|
    ||`id-ID-GadisNeural`|
    ||`is-IS-GudrunNeural`|
    ||`is-IS-GunnarNeural`|
    ||`it-IT-BenignoNeural`|
    ||`it-IT-CalimeroNeural`|
    ||`it-IT-CataldoNeural`|
    ||`it-IT-DiegoNeural`|
    ||`it-IT-ElsaNeural`|
    ||`it-IT-FabiolaNeural`|
    ||`it-IT-FiammaNeural`|
    ||`it-IT-GianniNeural`|
    ||`it-IT-ImeldaNeural`|
    ||`it-IT-IrmaNeural`|
    ||`it-IT-IsabellaNeural`|
    ||`it-IT-LisandroNeural`|
    ||`it-IT-PalmiraNeural`|
    ||`it-IT-PierinaNeural`|
    ||`it-IT-RinaldoNeural`|
    ||`ja-JP-AoiNeural`|
    ||`ja-JP-DaichiNeural`|
    ||`ja-JP-KeitaNeural`|
    ||`ja-JP-MayuNeural`|
    ||`ja-JP-NanamiNeural`|
    ||`ja-JP-NaokiNeural`|
    ||`ja-JP-ShioriNeural`|
    ||`jv-ID-DimasNeural`|
    ||`jv-ID-SitiNeural`|
    ||`ka-GE-EkaNeural`|
    ||`ka-GE-GiorgiNeural`|
    ||`kk-KZ-AigulNeural`|
    ||`kk-KZ-DauletNeural`|
    ||`km-KH-PisethNeural`|
    ||`km-KH-SreymomNeural`|
    ||`kn-IN-GaganNeural`|
    ||`kn-IN-SapnaNeural`|
    ||`ko-KR-BongJinNeural`|
    ||`ko-KR-GookMinNeural`|
    ||`ko-KR-InJoonNeural`|
    ||`ko-KR-JiMinNeural`|
    ||`ko-KR-SeoHyeonNeural`|
    ||`ko-KR-SoonBokNeural`|
    ||`ko-KR-SunHiNeural`|
    ||`ko-KR-YuJinNeural`|
    ||`lo-LA-ChanthavongNeural`|
    ||`lo-LA-KeomanyNeural`|
    ||`lt-LT-LeonasNeural`|
    ||`lt-LT-OnaNeural`|
    ||`lv-LV-EveritaNeural`|
    ||`lv-LV-NilsNeural`|
    ||`mk-MK-AleksandarNeural`|
    ||`mk-MK-MarijaNeural`|
    ||`ml-IN-MidhunNeural`|
    ||`ml-IN-SobhanaNeural`|
    ||`mn-MN-BataaNeural`|
    ||`mn-MN-YesuiNeural`|
    ||`mr-IN-AarohiNeural`|
    ||`mr-IN-ManoharNeural`|
    ||`ms-MY-OsmanNeural`|
    ||`ms-MY-YasminNeural`|
    ||`mt-MT-GraceNeural`|
    ||`mt-MT-JosephNeural`|
    ||`my-MM-NilarNeural`|
    ||`my-MM-ThihaNeural`|
    ||`nb-NO-FinnNeural`|
    ||`nb-NO-IselinNeural`|
    ||`nb-NO-PernilleNeural`|
    ||`ne-NP-HemkalaNeural`|
    ||`ne-NP-SagarNeural`|
    ||`nl-BE-ArnaudNeural`|
    ||`nl-BE-DenaNeural`|
    ||`nl-NL-ColetteNeural`|
    ||`nl-NL-FennaNeural`|
    ||`nl-NL-MaartenNeural`|
    ||`pl-PL-AgnieszkaNeural`|
    ||`pl-PL-MarekNeural`|
    ||`pl-PL-ZofiaNeural`|
    ||`ps-AF-GulNawazNeural`|
    ||`ps-AF-LatifaNeural`|
    ||`pt-BR-AntonioNeural`|
    ||`pt-BR-BrendaNeural`|
    ||`pt-BR-DonatoNeural`|
    ||`pt-BR-ElzaNeural`|
    ||`pt-BR-FabioNeural`|
    ||`pt-BR-FranciscaNeural`|
    ||`pt-BR-GiovannaNeural`|
    ||`pt-BR-HumbertoNeural`|
    ||`pt-BR-JulioNeural`|
    ||`pt-BR-LeilaNeural`|
    ||`pt-BR-LeticiaNeural`|
    ||`pt-BR-ManuelaNeural`|
    ||`pt-BR-NicolauNeural`|
    ||`pt-BR-ValerioNeural`|
    ||`pt-BR-YaraNeural`|
    ||`pt-PT-DuarteNeural`|
    ||`pt-PT-FernandaNeural`|
    ||`pt-PT-RaquelNeural`|
    ||`ro-RO-AlinaNeural`|
    ||`ro-RO-EmilNeural`|
    ||`ru-RU-DariyaNeural`|
    ||`ru-RU-DmitryNeural`|
    ||`ru-RU-SvetlanaNeural`|
    ||`si-LK-SameeraNeural`|
    ||`si-LK-ThiliniNeural`|
    ||`sk-SK-LukasNeural`|
    ||`sk-SK-ViktoriaNeural`|
    ||`sl-SI-PetraNeural`|
    ||`sl-SI-RokNeural`|
    ||`so-SO-MuuseNeural`|
    ||`so-SO-UbaxNeural`|
    ||`sq-AL-AnilaNeural`|
    ||`sq-AL-IlirNeural`|
    ||`sr-RS-NicholasNeural`|
    ||`sr-RS-SophieNeural`|
    ||`su-ID-JajangNeural`|
    ||`su-ID-TutiNeural`|
    ||`sv-SE-HilleviNeural`|
    ||`sv-SE-MattiasNeural`|
    ||`sv-SE-SofieNeural`|
    ||`sw-KE-RafikiNeural`|
    ||`sw-KE-ZuriNeural`|
    ||`sw-TZ-DaudiNeural`|
    ||`sw-TZ-RehemaNeural`|
    ||`ta-IN-PallaviNeural`|
    ||`ta-IN-ValluvarNeural`|
    ||`ta-LK-KumarNeural`|
    ||`ta-LK-SaranyaNeural`|
    ||`ta-MY-KaniNeural`|
    ||`ta-MY-SuryaNeural`|
    ||`ta-SG-AnbuNeural`|
    ||`ta-SG-VenbaNeural`|
    ||`te-IN-MohanNeural`|
    ||`te-IN-ShrutiNeural`|
    ||`th-TH-AcharaNeural`|
    ||`th-TH-NiwatNeural`|
    ||`th-TH-PremwadeeNeural`|
    ||`tr-TR-AhmetNeural`|
    ||`tr-TR-EmelNeural`|
    ||`uk-UA-OstapNeural`|
    ||`uk-UA-PolinaNeural`|
    ||`ur-IN-GulNeural`|
    ||`ur-IN-SalmanNeural`|
    ||`ur-PK-AsadNeural`|
    ||`ur-PK-UzmaNeural`|
    ||`uz-UZ-MadinaNeural`|
    ||`uz-UZ-SardorNeural`|
    ||`vi-VN-HoaiMyNeural`|
    ||`vi-VN-NamMinhNeural`|
    ||`wuu-CN-XiaotongNeural`|
    ||`wuu-CN-YunzheNeural`|
    ||`yue-CN-XiaoMinNeural`|
    ||`yue-CN-YunSongNeural`|
    ||`zh-CN-XiaochenNeural`|
    ||`zh-CN-XiaohanNeural`|
    ||`zh-CN-XiaomengNeural`|
    ||`zh-CN-XiaomoNeural`|
    ||`zh-CN-XiaoqiuNeural`|
    ||`zh-CN-XiaoruiNeural`|
    ||`zh-CN-XiaoshuangNeural`|
    ||`zh-CN-XiaoxiaoNeural`|
    ||`zh-CN-XiaoxuanNeural`|
    ||`zh-CN-XiaoyanNeural`|
    ||`zh-CN-XiaoyiNeural`|
    ||`zh-CN-XiaoyouNeural`|
    ||`zh-CN-XiaozhenNeural`|
    ||`zh-CN-YunfengNeural`|
    ||`zh-CN-YunhaoNeural`|
    ||`zh-CN-YunjianNeural`|
    ||`zh-CN-YunxiNeural`|
    ||`zh-CN-YunxiaNeural`|
    ||`zh-CN-YunyangNeural`|
    ||`zh-CN-YunyeNeural`|
    ||`zh-CN-YunzeNeural`|
    ||`zh-CN-henan-YundengNeural`|
    ||`zh-CN-liaoning-XiaobeiNeural`|
    ||`zh-CN-shaanxi-XiaoniNeural`|
    ||`zh-CN-shandong-YunxiangNeural`|
    ||`zh-CN-sichuan-YunxiNeural`|
    ||`zh-HK-HiuGaaiNeural`|
    ||`zh-HK-HiuMaanNeural`|
    ||`zh-HK-WanLungNeural`|
    ||`zh-TW-HsiaoChenNeural`|
    ||`zh-TW-HsiaoYuNeural`|
    ||`zh-TW-YunJheNeural`|
    ||`zu-ZA-ThandoNeural`|
    ||`zu-ZA-ThembaNeural`|

    </details><details><summary>lovoai</summary>





    |Name|Value|
    |----|-----|
    |**lovoai**|`af-ZA_Albertus Ruan`|
    ||`af-ZA_Danelle Wessel`|
    ||`am-ET_Abai Berhe`|
    ||`am-ET_Cherenet Tesfaye`|
    ||`ar-AE_Mansour Ahmed`|
    ||`ar-AE_Maryam Khan`|
    ||`ar-BH_Fatima Kumar`|
    ||`ar-BH_Omar Hassan`|
    ||`ar-DZ_Samia Touati`|
    ||`ar-DZ_Zuthimalin Brahimi`|
    ||`ar-EG_Ahmed Gamal`|
    ||`ar-EG_Reem Salah`|
    ||`ar-IQ_Aveen Majid`|
    ||`ar-IQ_Ismail Hashem`|
    ||`ar-JO_Fatima Jaber`|
    ||`ar-JO_Yousef Saleh`|
    ||`ar-KW_Areej Nair`|
    ||`ar-KW_Khaled Al Azmi`|
    ||`ar-LB_Abdel El Din`|
    ||`ar-LB_Eessa Kadifa`|
    ||`ar-LY_Abir Salem`|
    ||`ar-LY_Ahsan Omar`|
    ||`ar-MA_Hamid Bennani`|
    ||`ar-MA_Salma Naciri`|
    ||`ar-OM_Jabbar Singh`|
    ||`ar-OM_Zahra Sultan`|
    ||`ar-QA_Faizur Kumar`|
    ||`ar-QA_Noora Hussain`|
    ||`ar-SA_Majidah Khan`|
    ||`ar-SA_Omar Aziz`|
    ||`ar-SY_Oraida El-Assad`|
    ||`ar-SY_Rabah Ibrahim`|
    ||`ar-TN_Donia Cherif`|
    ||`ar-TN_Karim Dridi`|
    ||`ar-YE_Mansour Kasim`|
    ||`ar-YE_Mehdi Bawazeer`|
    ||`az-AZ_Ugur Quliyeva`|
    ||`az_AZ_Zeynab Cafarova`|
    ||`bg-BG_Damyan Ivanov`|
    ||`bg-BG_Fidanka Georgiev`|
    ||`bn-BD_Pranshu Akter`|
    ||`bn-BD_Vaagdevi Khatun`|
    ||`bn-IN_Gazi Mondal`|
    ||`bn-IN_Wali Ghosh`|
    ||`bs-BA_Esma Dodik`|
    ||`bs-BA_Ismet Rakic`|
    ||`ca-ES_Amada Fernando`|
    ||`ca-ES_Carmen Santiago`|
    ||`ca-ES_Miguel Torres`|
    ||`cs-CZ_Jana Rosicky`|
    ||`cs-CZ_Tomas Malecek`|
    ||`cy-GB_Branwen Jones`|
    ||`cy-GB_Elen Hughes`|
    ||`da-DK_Bjarne Jensen`|
    ||`da-DK_Helge Nielsen`|
    ||`de-AT_Lena Gruber`|
    ||`de-AT_Wilhelm Wagner`|
    ||`de-CH_Adolfus Meier`|
    ||`de-CH_Lara Keller`|
    ||`de-DE_Ada Weber`|
    ||`de-DE_Anna Schmidt`|
    ||`de-DE_Emma Muller`|
    ||`de-DE_Gerda Becker`|
    ||`de-DE_Hans Schulz`|
    ||`de-DE_Heidi Schneider`|
    ||`de-DE_Johanna Meyer`|
    ||`de-DE_Joshua Bauer`|
    ||`de-DE_Julian Koch`|
    ||`de-DE_Karl Hummels`|
    ||`de-DE_Maria Fischer`|
    ||`de-DE_Oliver Richter`|
    ||`de-DE_Otto Schaefer`|
    ||`de-DE_Petra Hoffman`|
    ||`de-DE_Walter Kimmich`|
    ||`el-GR_Petros Andino`|
    ||`el-GR_Thalia Klisiaris`|
    ||`en-AU_Amelia Taylor`|
    ||`en-AU_Charlotte Brown`|
    ||`en-AU_Darrell Robinson`|
    ||`en-AU_George Thompson`|
    ||`en-AU_Georgie Smith`|
    ||`en-AU_Isla Johnson`|
    ||`en-AU_Jake Nguyen`|
    ||`en-AU_Keegan Walker`|
    ||`en-AU_Kelly Opie`|
    ||`en-AU_Kevin Turner`|
    ||`en-AU_Mia White`|
    ||`en-AU_Nancy Jones`|
    ||`en-AU_Ryan Murphy`|
    ||`en-AU_Willow Martin`|
    ||`en-CA_Emily Salo`|
    ||`en-CA_Eric Fidyk`|
    ||`en-GB_Abigail Fraser`|
    ||`en-GB_Annie Smith`|
    ||`en-GB_Gertrude Baker`|
    ||`en-GB_Ian Kensington`|
    ||`en-GB_Kane Tooney`|
    ||`en-GB_Kelsey Michaels`|
    ||`en-GB_Kerrington Pacey`|
    ||`en-GB_Lizzy Wright`|
    ||`en-GB_Marcus O'Donell`|
    ||`en-GB_Nathaniel Jacobs`|
    ||`en-GB_Samuel Lee-Richards`|
    ||`en-GB_T.S. Cooper`|
    ||`en-GB_Theresa King`|
    ||`en-GB_William Tripp`|
    ||`en-HK_Heather Yiu`|
    ||`en-HK_Kevin Lau`|
    ||`en-IE_Aoife Byrne`|
    ||`en-IE_Bill Parkin`|
    ||`en-IN_Isha Singh`|
    ||`en-IN_Prabhdeep Patel`|
    ||`en-KE_Almasi Otieno`|
    ||`en-KE_Chitundu Mwangi`|
    ||`en-NG_Blessing Musa`|
    ||`en-NG_Kehinde Sade`|
    ||`en-NZ_Benson Duncan`|
    ||`en-NZ_Destiny Mitchell`|
    ||`en-PH_Angel dela Cruz`|
    ||`en-PH_Francis Reynaldo`|
    ||`en-SG_Chris Tan`|
    ||`en-SG_Rachel Ng`|
    ||`en-TZ_Busara Charles`|
    ||`en-TZ_Darweshi Juma`|
    ||`en-US_Alysha Imani`|
    ||`en-US_Betty Parker`|
    ||`en-US_Catherine Zania`|
    ||`en-US_Christopher Navarrez`|
    ||`en-US_Clara Ho`|
    ||`en-US_Eric Gonzalez`|
    ||`en-US_Heather Everett`|
    ||`en-US_Jamal Starke`|
    ||`en-US_Jasonna Johnson`|
    ||`en-US_Kaylee Montana`|
    ||`en-US_Ken hunter`|
    ||`en-US_Kim Howard`|
    ||`en-US_Kyle Moreno`|
    ||`en-US_Leroy Alshak`|
    ||`en-US_Micah Washington`|
    ||`en-US_Molly Richardson`|
    ||`en-US_Peter Lee`|
    ||`en-US_Phil Gough`|
    ||`en-US_Phoebe Nicholson`|
    ||`en-US_Samantha Hawthorne`|
    ||`en-US_Sean Orson`|
    ||`en-US_Serena Yang`|
    ||`en-US_Shannon Mechare`|
    ||`en-US_Thelma Browne`|
    ||`en-US_Tim Hardway`|
    ||`en-ZA_Cody Fergudson`|
    ||`en-ZA_Elna VanDijk`|
    ||`es-AR_Hyacinthe Castro`|
    ||`es-AR_Lautaro Gomez`|
    ||`es-BO_Elena Lopez`|
    ||`es-BO_Juan Perez`|
    ||`es-CL_Francisca Batistuta`|
    ||`es-CL_Gabriel Rodriguez`|
    ||`es-CO_Lorenzo Vazquez`|
    ||`es-CO_Sofia Garcia`|
    ||`es-CR_Guadalupe Suarez`|
    ||`es-CR_Sebastian Ramos`|
    ||`es-CU_Isabel Molina`|
    ||`es-CU_Luis Ortega`|
    ||`es-DO_Gabriela Serrano`|
    ||`es-DO_Raul Dominguez`|
    ||`es-EC_Angelina Romero`|
    ||`es-EC_Christian Diaz`|
    ||`es-EN_Carmen Martinela`|
    ||`es-ES_Andres Marin`|
    ||`es-ES_Emiliano Delgado`|
    ||`es-ES_Esmeralda Molina`|
    ||`es-ES_Hector Gavi`|
    ||`es-ES_Leo Gil`|
    ||`es-ES_Liliana Sanz`|
    ||`es-ES_Maria Ruiz`|
    ||`es-ES_Martin Enrique`|
    ||`es-ES_Miranda Navarro`|
    ||`es-ES_Pablo Iniesta`|
    ||`es-ES_Silvia Alvarez`|
    ||`es-ES_Teresa Iglesias`|
    ||`es-ES_Valentina Blanco`|
    ||`es-GQ_Elena Rubio`|
    ||`es-GQ_Teo Jimenez`|
    ||`es-GT_Ceciah Mendoza`|
    ||`es-GT_Paolo Ortiz`|
    ||`es-HN_Juana Flores`|
    ||`es-HN_Roberto Gutierrez`|
    ||`es-MX_Agata Albiol`|
    ||`es-MX_Darion Nunez`|
    ||`es-MX_Elias Lorenzo`|
    ||`es-MX_Elvira de Paul`|
    ||`es-MX_Enzo Paqueta`|
    ||`es-MX_Ezequiel Pacheco`|
    ||`es-MX_Iago Domingo`|
    ||`es-MX_Irene Vasquez`|
    ||`es-MX_Julieta Aguilar`|
    ||`es-MX_Lia Medina`|
    ||`es-MX_Nil Alvarez`|
    ||`es-MX_Pedro Rojas`|
    ||`es-MX_Rosa Valdoza`|
    ||`es-MX_Valencia Alba`|
    ||`es-MX_Veronica Mairal`|
    ||`es-NI_Abril Santacruz`|
    ||`es-NI_Lorenzo Llorente`|
    ||`es-PA_Liberto Marcos`|
    ||`es-PA_Yolanda Ezequiel`|
    ||`es-PE_Margarita de Fuentes`|
    ||`es-PE_Rey Sancho`|
    ||`es-PR_Alex de Santos`|
    ||`es-PR_Carlota Almiron`|
    ||`es-PY_Karina Diego`|
    ||`es-PY_Victor Mariela`|
    ||`es-SV_Jacinta Vela`|
    ||`es-SV_Marina Llorente`|
    ||`es-US_Jodrigo Alonso`|
    ||`es-US_Laia Paloma`|
    ||`es-US_Sergio Morata`|
    ||`es-UY_Lia Valentina`|
    ||`es-UY_Luis Ramon`|
    ||`es-VE_Manuel Rojos`|
    ||`es-VE_Sofia Vargas`|
    ||`et-EE_Barba Sepp`|
    ||`et-EE_Eduk Tamm`|
    ||`eu-ES_Markel Zubiri`|
    ||`eu-ES_Nahia Texpare`|
    ||`fa-IR_Bizhan Gilgamesh`|
    ||`fa-IR_Yasmina Hakimi`|
    ||`fi-FI_Anneli Niemnien`|
    ||`fi-FI_Kristiina Koskinen`|
    ||`fi-FI_Tapanni Korhonen`|
    ||`fil-PH_Amihan Reyes`|
    ||`fil-PH_Dennis de Saul`|
    ||`fr-BE_Louis Maes`|
    ||`fr-BE_Noah Peeters`|
    ||`fr-CA_Cherise DuPont`|
    ||`fr-CA_Olivier Varane`|
    ||`fr-CA_Raphael Jacques`|
    ||`fr-CH_Luca Dalot`|
    ||`fr-CH_Sylvie Gallace`|
    ||`fr-FR_Alain Hamel`|
    ||`fr-FR_Albertine Dubois`|
    ||`fr-FR_Antoine Petit`|
    ||`fr-FR_Brigitte Richard`|
    ||`fr-FR_Celeste Lefevre`|
    ||`fr-FR_Celine Bundchen`|
    ||`fr-FR_Damian Trezeguet`|
    ||`fr-FR_Diogo Pavard`|
    ||`fr-FR_Francoise LaFont`|
    ||`fr-FR_Gisele Guerin`|
    ||`fr-FR_Hugo Duval`|
    ||`fr-FR_Jacqueline Simon`|
    ||`fr-FR_Lois Allaire`|
    ||`fr-FR_Theo Bernard`|
    ||`ga-IE_Anja O'Brien`|
    ||`ga-IE_Liam Murphy`|
    ||`gl-ES_Clara Campos`|
    ||`gl-ES_Nicolas Montoya`|
    ||`gu-IN_Arzoo Chowdhury`|
    ||`gu-IN_Pramukh Barot`|
    ||`he-IL_Avi Goldmann`|
    ||`he-IL_Yael Haddad`|
    ||`hi-IN_Ashwin Nikhil`|
    ||`hi-IN_Uma Aravind`|
    ||`hr-HR_Krasna Perisic`|
    ||`hr-HR_Luka Horvat`|
    ||`hu-HU_Endre Szabo`|
    ||`hu-HU_Zoe Nagy`|
    ||`hy-AM_Arpi Hovhannisyan`|
    ||`hy-AM_Gor Grigoryan`|
    ||`id-ID_Bagaskoro Ulunjandi`|
    ||`id-ID_Diah Sukatendel`|
    ||`is-IS_Fridrika Sigurdsson`|
    ||`is-IS_Olafur Jonsdottir`|
    ||`it-IT_Alessandro Ferrari`|
    ||`it-IT_Alessia Ricci`|
    ||`it-IT_Allegra Greco`|
    ||`it-IT_Angelo Bianchi`|
    ||`it-IT_Antonio Colombo`|
    ||`it-IT_Eva De Luca`|
    ||`it-IT_Filomena Mancini`|
    ||`it-IT_Francesco Rossi`|
    ||`it-IT_Gaia Marino`|
    ||`it-IT_Gemma Conti`|
    ||`it-IT_Gianluigi Russo`|
    ||`it-IT_Greta Bruno`|
    ||`it-IT_Marco Romano`|
    ||`it-IT_Paul Esposito`|
    ||`it-IT_Serafina Gallo`|
    ||`ja-JP_Ayaka Musashi`|
    ||`ja-JP_Hiromi Tanaka`|
    ||`ja-JP_Hiroshi Maeda`|
    ||`ja-JP_Ichiro Sayaka`|
    ||`ja-JP_Naomi Sora`|
    ||`ja-JP_Sartoshi Juno`|
    ||`ja-JP_Sayuri Watanabe`|
    ||`jv-ID_Anom Zees`|
    ||`jv-ID_Bratawati Pulukadang`|
    ||`ka-GE_Ava Lomidze`|
    ||`ka-GE_Elijah Maisuradze`|
    ||`kk-KZ_Nurislam Omarov`|
    ||`kk-KZ_Rayana Kenes`|
    ||`km-KH_Chanthou Sok`|
    ||`km-KH_Kaliyanei Chea`|
    ||`kn-IN_Aadesh Madar`|
    ||`kn-IN_Rhyah Nayka`|
    ||`ko-KR_Eunjin Bae`|
    ||`ko-KR_Heechul Kim`|
    ||`ko-KR_Isu Choi`|
    ||`ko-KR_Jisoo Han`|
    ||`ko-KR_Meesun Kang`|
    ||`ko-KR_Minjoon Lee`|
    ||`ko-KR_Seung Hee Hwang`|
    ||`ko-KR_Yoosung Park`|
    ||`lo-LA_Lawan Vang`|
    ||`lo-LA_Sengphet Inthavong`|
    ||`lt-LT_Nojus Antanas`|
    ||`lt-LT_Ruta Bagdonas`|
    ||`lv-LV_Mozus Berzina`|
    ||`lv-LV_Santa Ozola`|
    ||`mk-MK_Berislav Stojanovski`|
    ||`mk-MK_Smaragda Jovanovska`|
    ||`ml-IN_Abha Nair`|
    ||`ml-IN_Akhil Kumar`|
    ||`mn-MN_Altan Batbayar`|
    ||`mn-MN_Enkhjargal Ganbold`|
    ||`mr-IN_Mihir Chitre`|
    ||`mr-IN_Vedvika Deo`|
    ||`ms-MY_Nur Tengku`|
    ||`ms-MY_Zikri Wan`|
    ||`mt-MT_Lola Farrugia`|
    ||`mt-MT_Milo Borg`|
    ||`my-MM_Dedan Khin`|
    ||`my-MM_Eindra Aung`|
    ||`nb-NO_Henrik Larsen`|
    ||`nb-NO_Vilde Hansen`|
    ||`nb_NO_Malin Pedersen`|
    ||`ne-NP_Batsal Khadka`|
    ||`ne-NP_Druhi Mahat`|
    ||`nl-BE_Arthur Mertens`|
    ||`nl-BE_Martine Claes`|
    ||`nl-NL_Adriana De Vries`|
    ||`nl-NL_Helena De Jong`|
    ||`nl-NL_Jan Visser`|
    ||`pl-PL_Ewa Grabowski`|
    ||`pl-PL_Piotr Duda`|
    ||`pl-PL_Zuzanna Kackz`|
    ||`ps-AF_Abdul-Alim Sayyid`|
    ||`ps-AF_Zahra Qurban`|
    ||`pt-BR_Adriana Rocha`|
    ||`pt-BR_Ana Bahiense`|
    ||`pt-BR_Anabella Teixeira`|
    ||`pt-BR_Antonia Macedo`|
    ||`pt-BR_Antonio Barros`|
    ||`pt-BR_Fernanda Pedreira`|
    ||`pt-BR_Francisco Guimaraes`|
    ||`pt-BR_Joao Azevedo`|
    ||`pt-BR_Jose Almeida`|
    ||`pt-BR_Juliana Costa`|
    ||`pt-BR_Marcia Ribeiro`|
    ||`pt-BR_Maria Cardoso`|
    ||`pt-BR_Paulo Correia`|
    ||`pt-BR_Pedro Magalhaes`|
    ||`pt-BR_Roberto Braga`|
    ||`pt-PT_Benedita Motta`|
    ||`pt-PT_Renato Matos`|
    ||`pt-PT_Rita Oliveira`|
    ||`ro-RO_Cristian Ionescu`|
    ||`ro-RO_Mirabela Gheata`|
    ||`ru-RU_Galina Ivanov`|
    ||`ru-RU_Nadezhda Smirnoff`|
    ||`ru-RU_Pyotr Semenov`|
    ||`si-LK_Kasun Perera`|
    ||`si-LK_Saanvi de Silva`|
    ||`sk-SK_Havel Varga`|
    ||`sk-SK_Olga Kovac`|
    ||`sl-SI_Neza Mlakar`|
    ||`sl-SI_Nik Krajnc`|
    ||`so-SO_Axado Ibrahim`|
    ||`so-SO_Taifa Mohamed`|
    ||`sq-AL_Bora Marku`|
    ||`sq-AL_Dren Kedare`|
    ||`sr-RS_Lara Markovic`|
    ||`sr-RS_Vlado Popovic`|
    ||`su-ID_Aarifa Bol`|
    ||`su-ID_Mustafa Deng`|
    ||`sv-SE_Agnes Lidstrom`|
    ||`sv-SE_Nicklas Forsberg`|
    ||`sv-SE_Wilma Sundin`|
    ||`sw-KE_Akeyo Njoroge`|
    ||`sw-KE_Chege Odhiambo`|
    ||`sw-TZ_Binti Ramadhani`|
    ||`sw-TZ_Darweshi Ally`|
    ||`ta-IN_Ashwin Kumar`|
    ||`ta-IN_Nila Suresh`|
    ||`ta-LK_Adya Pillai`|
    ||`ta-LK_Prahan Aachari`|
    ||`ta-MY_Aahna Konar`|
    ||`ta-MY_Kethan Nadar`|
    ||`ta-SG_Abilasha Naicker`|
    ||`ta-SG_Nemi Udayar`|
    ||`te-IN_Aarkash Reddy`|
    ||`te-IN_Tanvi Sharma`|
    ||`th-TH_Buppha Prasit`|
    ||`th-TH_Kanchana Sangthong`|
    ||`th-TH_Somchai Thongkham`|
    ||`tr-TR_Emre Ozdemir`|
    ||`tr-TR_Nehir Celik`|
    ||`uk-UA_Artem Shevchenko`|
    ||`uk-UA_Daryna Kovalenko`|
    ||`ur-IN_Farah Abbasi`|
    ||`ur-IN_Sharyar Alvi`|
    ||`ur-PK_Hamza Farooqi`|
    ||`ur-PK_Sana Dhanial`|
    ||`uz-UK_Javlonbek Yusupov`|
    ||`uz-UZ_Rustam Karimova`|
    ||`vi-VN_Huu Duong`|
    ||`vi-VN_Vi Ly`|
    ||`wuu-CN_Muchen Li`|
    ||`wuu-CN_Ruoxi Wang`|
    ||`yue-CN_Ah-lam Lei`|
    ||`yue-CN_Xiaoxiao Wong`|
    ||`zh-CN-henan_Genji Zhou`|
    ||`zh-CN-liaoning_Chu Zhang`|
    ||`zh-CN-shaanxi_Chunhua Lin`|
    ||`zh-CN-shandong_Jiayi Wu`|
    ||`zh-CN-sichuan_Juan Yang`|
    ||`zh-CN_An Liu`|
    ||`zh-CN_Bai Yang`|
    ||`zh-CN_Bao Huang`|
    ||`zh-CN_Chao Zhou`|
    ||`zh-CN_Chen Chen Huo`|
    ||`zh-CN_Cheng Sun`|
    ||`zh-CN_Chichi Wu`|
    ||`zh-CN_Chin Ma`|
    ||`zh-CN_Chun Hu`|
    ||`zh-CN_Cong Zhang`|
    ||`zh-CN_Da Xia Li`|
    ||`zh-CN_Daiyu Zhu`|
    ||`zh-CN_Diu Wang`|
    ||`zh-CN_Huan Luo`|
    ||`zh-CN_Huifen Chen`|
    ||`zh-CN_Huiqing Wang`|
    ||`zh-CN_Meng Li`|
    ||`zh-CN_Xuan Xu`|
    ||`zh-CN_Yifu Wu`|
    ||`zh-CN_Yihan Chen`|
    ||`zh-CN_Yinuo Zhang`|
    ||`zh-HK_Kun Lo`|
    ||`zh-HK_Lanying Lei`|
    ||`zh-HK_Lee Lam`|
    ||`zh-TW_Mingxia Luo`|
    ||`zh-TW_Mingzhu Gao`|
    ||`zh-TW_Susu Song`|
    ||`zu-ZA_Bonginkosi Masina`|
    ||`zu-ZA_Ulwazi Mangede`|

    </details><details><summary>elevenlabs</summary>





    |Name|Value|
    |----|-----|
    |**elevenlabs**|`de-DE_Multilingual_Callum`|
    ||`de-DE_Multilingual_Charlie`|
    ||`de-DE_Multilingual_Charlotte`|
    ||`de-DE_Multilingual_Clyde`|
    ||`de-DE_Multilingual_Daniel`|
    ||`de-DE_Multilingual_Dave`|
    ||`de-DE_Multilingual_Dorothy`|
    ||`de-DE_Multilingual_Emily`|
    ||`de-DE_Multilingual_Ethan`|
    ||`de-DE_Multilingual_Fin`|
    ||`de-DE_Multilingual_Freya`|
    ||`de-DE_Multilingual_Gigi`|
    ||`de-DE_Multilingual_Giovanni`|
    ||`de-DE_Multilingual_Grace`|
    ||`de-DE_Multilingual_Harry`|
    ||`de-DE_Multilingual_James`|
    ||`de-DE_Multilingual_Jeremy`|
    ||`de-DE_Multilingual_Jessie`|
    ||`de-DE_Multilingual_Joseph`|
    ||`de-DE_Multilingual_Liam`|
    ||`de-DE_Multilingual_Matilda`|
    ||`de-DE_Multilingual_Matthew`|
    ||`de-DE_Multilingual_Michael`|
    ||`de-DE_Multilingual_Mimi`|
    ||`de-DE_Multilingual_Nicole`|
    ||`de-DE_Multilingual_Patrick`|
    ||`de-DE_Multilingual_Ryan`|
    ||`de-DE_Multilingual_Serena`|
    ||`de-DE_Multilingual_Thomas`|
    ||`en-AU_Monolingual_Charlie`|
    ||`en-AU_Monolingual_James`|
    ||`en-GB_Monolingual_Daniel`|
    ||`en-GB_Monolingual_Dave`|
    ||`en-GB_Monolingual_Dorothy`|
    ||`en-GB_Monolingual_Joseph`|
    ||`en-GB_Monolingual_Matthew`|
    ||`en-IE_Monolingual_Fin`|
    ||`en-IT_Monolingual_Giovanni`|
    ||`en-SWE_Monolingual_Charlotte`|
    ||`en-SWE_Monolingual_Mimi`|
    ||`en-US_Monolingual_Adam`|
    ||`en-US_Monolingual_Antoni`|
    ||`en-US_Monolingual_Arnold`|
    ||`en-US_Monolingual_Bella`|
    ||`en-US_Monolingual_Callum`|
    ||`en-US_Monolingual_Clyde`|
    ||`en-US_Monolingual_Domi`|
    ||`en-US_Monolingual_Elli`|
    ||`en-US_Monolingual_Emily`|
    ||`en-US_Monolingual_Ethan`|
    ||`en-US_Monolingual_Freya`|
    ||`en-US_Monolingual_Gigi`|
    ||`en-US_Monolingual_Glinda`|
    ||`en-US_Monolingual_Grace`|
    ||`en-US_Monolingual_Harry`|
    ||`en-US_Monolingual_Jeremy`|
    ||`en-US_Monolingual_Jessie`|
    ||`en-US_Monolingual_Josh`|
    ||`en-US_Monolingual_Liam`|
    ||`en-US_Monolingual_Matilda`|
    ||`en-US_Monolingual_Michael`|
    ||`en-US_Monolingual_Nicole`|
    ||`en-US_Monolingual_Patrick`|
    ||`en-US_Monolingual_Rachel`|
    ||`en-US_Monolingual_Ryan`|
    ||`en-US_Monolingual_Sam`|
    ||`en-US_Monolingual_Sarah`|
    ||`en-US_Monolingual_Serena`|
    ||`en-US_Monolingual_Thomas`|
    ||`es-ES_Multilingual_Callum`|
    ||`es-ES_Multilingual_Charlie`|
    ||`es-ES_Multilingual_Charlotte`|
    ||`es-ES_Multilingual_Clyde`|
    ||`es-ES_Multilingual_Daniel`|
    ||`es-ES_Multilingual_Dave`|
    ||`es-ES_Multilingual_Dorothy`|
    ||`es-ES_Multilingual_Emily`|
    ||`es-ES_Multilingual_Ethan`|
    ||`es-ES_Multilingual_Fin`|
    ||`es-ES_Multilingual_Freya`|
    ||`es-ES_Multilingual_Gigi`|
    ||`es-ES_Multilingual_Giovanni`|
    ||`es-ES_Multilingual_Grace`|
    ||`es-ES_Multilingual_James`|
    ||`es-ES_Multilingual_Jeremy`|
    ||`es-ES_Multilingual_Jessie`|
    ||`es-ES_Multilingual_Joseph`|
    ||`es-ES_Multilingual_Liam`|
    ||`es-ES_Multilingual_Matilda`|
    ||`es-ES_Multilingual_Matthew`|
    ||`es-ES_Multilingual_Michael`|
    ||`es-ES_Multilingual_Mimi`|
    ||`es-ES_Multilingual_Nicole`|
    ||`es-ES_Multilingual_Patrick`|
    ||`es-ES_Multilingual_Ryan`|
    ||`es-ES_Multilingual_Serena`|
    ||`es-ES_Multilingual_Thomas`|
    ||`es-US_Multilingual_Harry`|
    ||`fr-FR_Multilingual_Callum`|
    ||`fr-FR_Multilingual_Charlie`|
    ||`fr-FR_Multilingual_Charlotte`|
    ||`fr-FR_Multilingual_Clyde`|
    ||`fr-FR_Multilingual_Daniel`|
    ||`fr-FR_Multilingual_Dave`|
    ||`fr-FR_Multilingual_Dorothy`|
    ||`fr-FR_Multilingual_Emily`|
    ||`fr-FR_Multilingual_Ethan`|
    ||`fr-FR_Multilingual_Fin`|
    ||`fr-FR_Multilingual_Freya`|
    ||`fr-FR_Multilingual_Gigi`|
    ||`fr-FR_Multilingual_Giovanni`|
    ||`fr-FR_Multilingual_Grace`|
    ||`fr-FR_Multilingual_Harry`|
    ||`fr-FR_Multilingual_James`|
    ||`fr-FR_Multilingual_Jeremy`|
    ||`fr-FR_Multilingual_Jessie`|
    ||`fr-FR_Multilingual_Joseph`|
    ||`fr-FR_Multilingual_Liam`|
    ||`fr-FR_Multilingual_Matilda`|
    ||`fr-FR_Multilingual_Matthew`|
    ||`fr-FR_Multilingual_Michael`|
    ||`fr-FR_Multilingual_Mimi`|
    ||`fr-FR_Multilingual_Nicole`|
    ||`fr-FR_Multilingual_Patrick`|
    ||`fr-FR_Multilingual_Ryan`|
    ||`fr-FR_Multilingual_Serena`|
    ||`fr-FR_Multilingual_Thomas`|
    ||`hi-IN_Multilingual_Callum`|
    ||`hi-IN_Multilingual_Charlie`|
    ||`hi-IN_Multilingual_Charlotte`|
    ||`hi-IN_Multilingual_Clyde`|
    ||`hi-IN_Multilingual_Daniel`|
    ||`hi-IN_Multilingual_Dave`|
    ||`hi-IN_Multilingual_Dorothy`|
    ||`hi-IN_Multilingual_Emily`|
    ||`hi-IN_Multilingual_Ethan`|
    ||`hi-IN_Multilingual_Fin`|
    ||`hi-IN_Multilingual_Freya`|
    ||`hi-IN_Multilingual_Gigi`|
    ||`hi-IN_Multilingual_Giovanni`|
    ||`hi-IN_Multilingual_Grace`|
    ||`hi-IN_Multilingual_Harry`|
    ||`hi-IN_Multilingual_James`|
    ||`hi-IN_Multilingual_Jeremy`|
    ||`hi-IN_Multilingual_Jessie`|
    ||`hi-IN_Multilingual_Joseph`|
    ||`hi-IN_Multilingual_Liam`|
    ||`hi-IN_Multilingual_Matilda`|
    ||`hi-IN_Multilingual_Matthew`|
    ||`hi-IN_Multilingual_Michael`|
    ||`hi-IN_Multilingual_Mimi`|
    ||`hi-IN_Multilingual_Nicole`|
    ||`hi-IN_Multilingual_Patrick`|
    ||`hi-IN_Multilingual_Ryan`|
    ||`hi-IN_Multilingual_Serena`|
    ||`hi-IN_Multilingual_Thomas`|
    ||`it-IT_Multilingual_Callum`|
    ||`it-IT_Multilingual_Charlie`|
    ||`it-IT_Multilingual_Charlotte`|
    ||`it-IT_Multilingual_Clyde`|
    ||`it-IT_Multilingual_Daniel`|
    ||`it-IT_Multilingual_Dave`|
    ||`it-IT_Multilingual_Dorothy`|
    ||`it-IT_Multilingual_Emily`|
    ||`it-IT_Multilingual_Ethan`|
    ||`it-IT_Multilingual_Fin`|
    ||`it-IT_Multilingual_Freya`|
    ||`it-IT_Multilingual_Gigi`|
    ||`it-IT_Multilingual_Giovanni`|
    ||`it-IT_Multilingual_Grace`|
    ||`it-IT_Multilingual_Harry`|
    ||`it-IT_Multilingual_James`|
    ||`it-IT_Multilingual_Jeremy`|
    ||`it-IT_Multilingual_Jessie`|
    ||`it-IT_Multilingual_Joseph`|
    ||`it-IT_Multilingual_Liam`|
    ||`it-IT_Multilingual_Matilda`|
    ||`it-IT_Multilingual_Matthew`|
    ||`it-IT_Multilingual_Michael`|
    ||`it-IT_Multilingual_Mimi`|
    ||`it-IT_Multilingual_Nicole`|
    ||`it-IT_Multilingual_Patrick`|
    ||`it-IT_Multilingual_Ryan`|
    ||`it-IT_Multilingual_Serena`|
    ||`it-IT_Multilingual_Thomas`|
    ||`pl-PL_Multilingual_Callum`|
    ||`pl-PL_Multilingual_Charlie`|
    ||`pl-PL_Multilingual_Charlotte`|
    ||`pl-PL_Multilingual_Clyde`|
    ||`pl-PL_Multilingual_Daniel`|
    ||`pl-PL_Multilingual_Dave`|
    ||`pl-PL_Multilingual_Dorothy`|
    ||`pl-PL_Multilingual_Emily`|
    ||`pl-PL_Multilingual_Ethan`|
    ||`pl-PL_Multilingual_Fin`|
    ||`pl-PL_Multilingual_Freya`|
    ||`pl-PL_Multilingual_Gigi`|
    ||`pl-PL_Multilingual_Giovanni`|
    ||`pl-PL_Multilingual_Grace`|
    ||`pl-PL_Multilingual_Harry`|
    ||`pl-PL_Multilingual_James`|
    ||`pl-PL_Multilingual_Jeremy`|
    ||`pl-PL_Multilingual_Jessie`|
    ||`pl-PL_Multilingual_Joseph`|
    ||`pl-PL_Multilingual_Liam`|
    ||`pl-PL_Multilingual_Matilda`|
    ||`pl-PL_Multilingual_Matthew`|
    ||`pl-PL_Multilingual_Michael`|
    ||`pl-PL_Multilingual_Mimi`|
    ||`pl-PL_Multilingual_Nicole`|
    ||`pl-PL_Multilingual_Patrick`|
    ||`pl-PL_Multilingual_Ryan`|
    ||`pl-PL_Multilingual_Serena`|
    ||`pl-PL_Multilingual_Thomas`|
    ||`pt-PT_Multilingual_Callum`|
    ||`pt-PT_Multilingual_Charlie`|
    ||`pt-PT_Multilingual_Charlotte`|
    ||`pt-PT_Multilingual_Clyde`|
    ||`pt-PT_Multilingual_Daniel`|
    ||`pt-PT_Multilingual_Dave`|
    ||`pt-PT_Multilingual_Dorothy`|
    ||`pt-PT_Multilingual_Emily`|
    ||`pt-PT_Multilingual_Ethan`|
    ||`pt-PT_Multilingual_Fin`|
    ||`pt-PT_Multilingual_Freya`|
    ||`pt-PT_Multilingual_Gigi`|
    ||`pt-PT_Multilingual_Giovanni`|
    ||`pt-PT_Multilingual_Grace`|
    ||`pt-PT_Multilingual_Harry`|
    ||`pt-PT_Multilingual_James`|
    ||`pt-PT_Multilingual_Jeremy`|
    ||`pt-PT_Multilingual_Jessie`|
    ||`pt-PT_Multilingual_Joseph`|
    ||`pt-PT_Multilingual_Liam`|
    ||`pt-PT_Multilingual_Matilda`|
    ||`pt-PT_Multilingual_Matthew`|
    ||`pt-PT_Multilingual_Michael`|
    ||`pt-PT_Multilingual_Mimi`|
    ||`pt-PT_Multilingual_Nicole`|
    ||`pt-PT_Multilingual_Patrick`|
    ||`pt-PT_Multilingual_Ryan`|
    ||`pt-PT_Multilingual_Serena`|
    ||`pt-PT_Multilingual_Thomas`|

    </details><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`af_alloy`|
    ||`af_echo`|
    ||`af_fable`|
    ||`af_nova`|
    ||`af_onyx`|
    ||`af_shimmer`|
    ||`ar_alloy`|
    ||`ar_echo`|
    ||`ar_fable`|
    ||`ar_nova`|
    ||`ar_onyx`|
    ||`ar_shimmer`|
    ||`az_alloy`|
    ||`az_echo`|
    ||`az_fable`|
    ||`az_nova`|
    ||`az_onyx`|
    ||`az_shimmer`|
    ||`be_alloy`|
    ||`be_echo`|
    ||`be_fable`|
    ||`be_nova`|
    ||`be_onyx`|
    ||`be_shimmer`|
    ||`bg_alloy`|
    ||`bg_echo`|
    ||`bg_fable`|
    ||`bg_nova`|
    ||`bg_onyx`|
    ||`bg_shimmer`|
    ||`bs_alloy`|
    ||`bs_echo`|
    ||`bs_fable`|
    ||`bs_nova`|
    ||`bs_onyx`|
    ||`bs_shimmer`|
    ||`ca_alloy`|
    ||`ca_echo`|
    ||`ca_fable`|
    ||`ca_nova`|
    ||`ca_onyx`|
    ||`ca_shimmer`|
    ||`cs_alloy`|
    ||`cs_echo`|
    ||`cs_fable`|
    ||`cs_nova`|
    ||`cs_onyx`|
    ||`cs_shimmer`|
    ||`cy_alloy`|
    ||`cy_echo`|
    ||`cy_fable`|
    ||`cy_nova`|
    ||`cy_onyx`|
    ||`cy_shimmer`|
    ||`da_alloy`|
    ||`da_echo`|
    ||`da_fable`|
    ||`da_nova`|
    ||`da_onyx`|
    ||`da_shimmer`|
    ||`de_alloy`|
    ||`de_echo`|
    ||`de_fable`|
    ||`de_nova`|
    ||`de_onyx`|
    ||`de_shimmer`|
    ||`el_alloy`|
    ||`el_echo`|
    ||`el_fable`|
    ||`el_nova`|
    ||`el_onyx`|
    ||`el_shimmer`|
    ||`en_alloy`|
    ||`en_echo`|
    ||`en_fable`|
    ||`en_nova`|
    ||`en_onyx`|
    ||`en_shimmer`|
    ||`es_alloy`|
    ||`es_echo`|
    ||`es_fable`|
    ||`es_nova`|
    ||`es_onyx`|
    ||`es_shimmer`|
    ||`et_alloy`|
    ||`et_echo`|
    ||`et_fable`|
    ||`et_nova`|
    ||`et_onyx`|
    ||`et_shimmer`|
    ||`fa_alloy`|
    ||`fa_echo`|
    ||`fa_fable`|
    ||`fa_nova`|
    ||`fa_onyx`|
    ||`fa_shimmer`|
    ||`fi_alloy`|
    ||`fi_echo`|
    ||`fi_fable`|
    ||`fi_nova`|
    ||`fi_onyx`|
    ||`fi_shimmer`|
    ||`fr_alloy`|
    ||`fr_echo`|
    ||`fr_fable`|
    ||`fr_nova`|
    ||`fr_onyx`|
    ||`fr_shimmer`|
    ||`gl_alloy`|
    ||`gl_echo`|
    ||`gl_fable`|
    ||`gl_nova`|
    ||`gl_onyx`|
    ||`gl_shimmer`|
    ||`he_alloy`|
    ||`he_echo`|
    ||`he_fable`|
    ||`he_nova`|
    ||`he_onyx`|
    ||`he_shimmer`|
    ||`hi_alloy`|
    ||`hi_echo`|
    ||`hi_fable`|
    ||`hi_nova`|
    ||`hi_onyx`|
    ||`hi_shimmer`|
    ||`hr_alloy`|
    ||`hr_echo`|
    ||`hr_fable`|
    ||`hr_nova`|
    ||`hr_onyx`|
    ||`hr_shimmer`|
    ||`hu_alloy`|
    ||`hu_echo`|
    ||`hu_fable`|
    ||`hu_nova`|
    ||`hu_onyx`|
    ||`hu_shimmer`|
    ||`hy_alloy`|
    ||`hy_echo`|
    ||`hy_fable`|
    ||`hy_nova`|
    ||`hy_onyx`|
    ||`hy_shimmer`|
    ||`id_alloy`|
    ||`id_echo`|
    ||`id_fable`|
    ||`id_nova`|
    ||`id_onyx`|
    ||`id_shimmer`|
    ||`is_alloy`|
    ||`is_echo`|
    ||`is_fable`|
    ||`is_nova`|
    ||`is_onyx`|
    ||`is_shimmer`|
    ||`it_alloy`|
    ||`it_echo`|
    ||`it_fable`|
    ||`it_nova`|
    ||`it_onyx`|
    ||`it_shimmer`|
    ||`ja_alloy`|
    ||`ja_echo`|
    ||`ja_fable`|
    ||`ja_nova`|
    ||`ja_onyx`|
    ||`ja_shimmer`|
    ||`kk_alloy`|
    ||`kk_echo`|
    ||`kk_fable`|
    ||`kk_nova`|
    ||`kk_onyx`|
    ||`kk_shimmer`|
    ||`kn_alloy`|
    ||`kn_echo`|
    ||`kn_fable`|
    ||`kn_nova`|
    ||`kn_onyx`|
    ||`kn_shimmer`|
    ||`ko_alloy`|
    ||`ko_echo`|
    ||`ko_fable`|
    ||`ko_nova`|
    ||`ko_onyx`|
    ||`ko_shimmer`|
    ||`lt_alloy`|
    ||`lt_echo`|
    ||`lt_fable`|
    ||`lt_nova`|
    ||`lt_onyx`|
    ||`lt_shimmer`|
    ||`lv_alloy`|
    ||`lv_echo`|
    ||`lv_fable`|
    ||`lv_nova`|
    ||`lv_onyx`|
    ||`lv_shimmer`|
    ||`mi_alloy`|
    ||`mi_echo`|
    ||`mi_fable`|
    ||`mi_nova`|
    ||`mi_onyx`|
    ||`mi_shimmer`|
    ||`mk_alloy`|
    ||`mk_echo`|
    ||`mk_fable`|
    ||`mk_nova`|
    ||`mk_onyx`|
    ||`mk_shimmer`|
    ||`mr_alloy`|
    ||`mr_echo`|
    ||`mr_fable`|
    ||`mr_nova`|
    ||`mr_onyx`|
    ||`mr_shimmer`|
    ||`ms_alloy`|
    ||`ms_echo`|
    ||`ms_fable`|
    ||`ms_nova`|
    ||`ms_onyx`|
    ||`ms_shimmer`|
    ||`ne_alloy`|
    ||`ne_echo`|
    ||`ne_fable`|
    ||`ne_nova`|
    ||`ne_onyx`|
    ||`ne_shimmer`|
    ||`nl_alloy`|
    ||`nl_echo`|
    ||`nl_fable`|
    ||`nl_nova`|
    ||`nl_onyx`|
    ||`nl_shimmer`|
    ||`no_alloy`|
    ||`no_echo`|
    ||`no_fable`|
    ||`no_nova`|
    ||`no_onyx`|
    ||`no_shimmer`|
    ||`pl_alloy`|
    ||`pl_echo`|
    ||`pl_fable`|
    ||`pl_nova`|
    ||`pl_onyx`|
    ||`pl_shimmer`|
    ||`pt_alloy`|
    ||`pt_echo`|
    ||`pt_fable`|
    ||`pt_nova`|
    ||`pt_onyx`|
    ||`pt_shimmer`|
    ||`ro_alloy`|
    ||`ro_echo`|
    ||`ro_fable`|
    ||`ro_nova`|
    ||`ro_onyx`|
    ||`ro_shimmer`|
    ||`ru_alloy`|
    ||`ru_echo`|
    ||`ru_fable`|
    ||`ru_nova`|
    ||`ru_onyx`|
    ||`ru_shimmer`|
    ||`sk_alloy`|
    ||`sk_echo`|
    ||`sk_fable`|
    ||`sk_nova`|
    ||`sk_onyx`|
    ||`sk_shimmer`|
    ||`sl_alloy`|
    ||`sl_echo`|
    ||`sl_fable`|
    ||`sl_nova`|
    ||`sl_onyx`|
    ||`sl_shimmer`|
    ||`sr_alloy`|
    ||`sr_echo`|
    ||`sr_fable`|
    ||`sr_nova`|
    ||`sr_onyx`|
    ||`sr_shimmer`|
    ||`sv_alloy`|
    ||`sv_echo`|
    ||`sv_fable`|
    ||`sv_nova`|
    ||`sv_onyx`|
    ||`sv_shimmer`|
    ||`sw_alloy`|
    ||`sw_echo`|
    ||`sw_fable`|
    ||`sw_nova`|
    ||`sw_onyx`|
    ||`sw_shimmer`|
    ||`ta_alloy`|
    ||`ta_echo`|
    ||`ta_fable`|
    ||`ta_nova`|
    ||`ta_onyx`|
    ||`ta_shimmer`|
    ||`th_alloy`|
    ||`th_echo`|
    ||`th_fable`|
    ||`th_nova`|
    ||`th_onyx`|
    ||`th_shimmer`|
    ||`tl_alloy`|
    ||`tl_echo`|
    ||`tl_fable`|
    ||`tl_nova`|
    ||`tl_onyx`|
    ||`tl_shimmer`|
    ||`tr_alloy`|
    ||`tr_echo`|
    ||`tr_fable`|
    ||`tr_nova`|
    ||`tr_onyx`|
    ||`tr_shimmer`|
    ||`uk_alloy`|
    ||`uk_echo`|
    ||`uk_fable`|
    ||`uk_nova`|
    ||`uk_onyx`|
    ||`uk_shimmer`|
    ||`ur_alloy`|
    ||`ur_echo`|
    ||`ur_fable`|
    ||`ur_nova`|
    ||`ur_onyx`|
    ||`ur_shimmer`|
    ||`vi_alloy`|
    ||`vi_echo`|
    ||`vi_fable`|
    ||`vi_nova`|
    ||`vi_onyx`|
    ||`vi_shimmer`|
    ||`zh_alloy`|
    ||`zh_echo`|
    ||`zh_fable`|
    ||`zh_nova`|
    ||`zh_onyx`|
    ||`zh_shimmer`|

    </details>

    </details>

    Args:
        body (AudiotextToSpeechTextToSpeechRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AudiotextToSpeechTextToSpeechRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Text to Speech

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**amazon**|-|`boto3 (v1.15.18)`|4.0 (per 1000000 char)|1 char
    |**amazon**|**Neural**|`boto3 (v1.15.18)`|16.0 (per 1000000 char)|1 char
    |**google**|-|`v1`|4.0 (per 1000000 char)|1 char
    |**google**|**Standard**|`v1`|4.0 (per 1000000 char)|1 char
    |**google**|**Neural**|`v1`|16.0 (per 1000000 char)|1 char
    |**google**|**Wavenet**|`v1`|16.0 (per 1000000 char)|1 char
    |**google**|**Studio**|`v1`|0.16 (per 1000 char)|1 char
    |**ibm**|-|`v1`|20.0 (per 1000000 char)|1000 char
    |**microsoft**|-|`v1.0`|16.0 (per 1000000 char)|1 char
    |**lovoai**|-|`v1`|160.0 (per 1000000 char)|1000 char
    |**elevenlabs**|-|`v1`|0.3 (per 1000 char)|1 char
    |**openai**|-|`v1.0`|0.015 (per 1000 char)|1 char


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
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bengali**|`bn`|
    |**Bosnian**|`bs`|
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
    |**Estonian**|`et`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Indonesian**|`id`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kannada**|`kn`|
    |**Kazakh**|`kk`|
    |**Korean**|`ko`|
    |**Lao**|`lo`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Macedonian**|`mk`|
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
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Serbian**|`sr`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**Spanish**|`es`|
    |**Standard Arabic**|`arb`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tamil**|`ta`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Turkish**|`tr`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Welsh**|`cy`|
    |**Wu Chinese**|`wuu`|
    |**Xhosa**|`xh`|
    |**Yue Chinese**|`yue`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans (South Africa)**|`af-ZA`|
    |**Albanian (Albania)**|`sq-AL`|
    |**Amharic (Ethiopia)**|`am-ET`|
    |**Arabic (Algeria)**|`ar-DZ`|
    |**Arabic (Bahrain)**|`ar-BH`|
    |**Arabic (Egypt)**|`ar-EG`|
    |**Arabic (Iraq)**|`ar-IQ`|
    |**Arabic (Jordan)**|`ar-JO`|
    |**Arabic (Kuwait)**|`ar-KW`|
    |**Arabic (Lebanon)**|`ar-LB`|
    |**Arabic (Libya)**|`ar-LY`|
    |**Arabic (Morocco)**|`ar-MA`|
    |**Arabic (Oman)**|`ar-OM`|
    |**Arabic (Pseudo-Accents)**|`ar-XA`|
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
    |**Cantonese (Hong Kong SAR China)**|`yue-HK`|
    |**Catalan (Spain)**|`ca-ES`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (China)**|`zh-CN-henan`|
    |**Chinese (China)**|`zh-CN-shandong`|
    |**Chinese (China)**|`zh-CN-sichuan`|
    |**Chinese (Hong Kong SAR China)**|`zh-HK`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Croatian (Croatia)**|`hr-HR`|
    |**Czech (Czechia)**|`cs-CZ`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Belgium)**|`nl-BE`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (Australia)**|`en-AU`|
    |**English (Canada)**|`en-CA`|
    |**English (Curaçao)**|`en-AN`|
    |**English (Hong Kong SAR China)**|`en-HK`|
    |**English (India)**|`en-IN`|
    |**English (Ireland)**|`en-IE`|
    |**English (Kenya)**|`en-KE`|
    |**English (New Zealand)**|`en-NZ`|
    |**English (Nigeria)**|`en-NG`|
    |**English (Philippines)**|`en-PH`|
    |**English (Singapore)**|`en-SG`|
    |**English (South Africa)**|`en-ZA`|
    |**English (Tanzania)**|`en-TZ`|
    |**English (United Kingdom)**|`en-GB`|
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
    |**Hindi (India)**|`hi-IN`|
    |**Hungarian (Hungary)**|`hu-HU`|
    |**Icelandic (Iceland)**|`is-IS`|
    |**Indonesian (Indonesia)**|`id-ID`|
    |**Irish (Ireland)**|`ga-IE`|
    |**Italian (Italy)**|`it-IT`|
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
    |**Mandarin Chinese (China)**|`cmn-CN`|
    |**Mandarin Chinese (Taiwan)**|`cmn-TW`|
    |**Marathi (India)**|`mr-IN`|
    |**Mongolian (Mongolia)**|`mn-MN`|
    |**Nepali (Nepal)**|`ne-NP`|
    |**Norwegian Bokmål (Norway)**|`nb-NO`|
    |**Pashto (Afghanistan)**|`ps-AF`|
    |**Persian (Iran)**|`fa-IR`|
    |**Polish (Poland)**|`pl-PL`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Punjabi (India)**|`pa-IN`|
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
    |**Uzbek (United Kingdom)**|`uz-UK`|
    |**Uzbek (Uzbekistan)**|`uz-UZ`|
    |**Vietnamese (Vietnam)**|`vi-VN`|
    |**Welsh (United Kingdom)**|`cy-GB`|
    |**Wu Chinese (China)**|`wuu-CN`|
    |**Xhosa (South Africa)**|`xh-ZA`|
    |**Zulu (South Africa)**|`zu-ZA`|

    </details><details><summary>Supported Models</summary><details><summary>amazon</summary>





    |Name|Value|
    |----|-----|
    |**amazon**|`ar-AE_Hala_Neural`|
    ||`arb_Zeina_Standard`|
    ||`ca-ES_Arlet_Neural`|
    ||`cmn-CN_Zhiyu_Neural`|
    ||`cmn-CN_Zhiyu_Standard`|
    ||`cy-GB_Gwyneth_Standard`|
    ||`da-DK_Mads_Standard`|
    ||`da-DK_Naja_Standard`|
    ||`de-AT_Hannah_Neural`|
    ||`de-DE_Daniel_Neural`|
    ||`de-DE_Hans_Standard`|
    ||`de-DE_Marlene_Standard`|
    ||`de-DE_Vicki_Neural`|
    ||`de-DE_Vicki_Standard`|
    ||`en-AU_Nicole_Neural`|
    ||`en-AU_Olivia_Standard`|
    ||`en-AU_Russell_Neural`|
    ||`en-GB_Amy_Neural`|
    ||`en-GB_Amy_Standard`|
    ||`en-GB_Arthur_Neural`|
    ||`en-GB_Brian_Neural`|
    ||`en-GB_Brian_Standard`|
    ||`en-GB_Emma_Neural`|
    ||`en-GB_Emma_Standard`|
    ||`en-IN_Aditi_Standard`|
    ||`en-IN_Kajal_Neural`|
    ||`en-IN_Raveena_Standard`|
    ||`en-NZ_Aria_Neural`|
    ||`en-US_Ivy_Neural`|
    ||`en-US_Ivy_Standard`|
    ||`en-US_Joanna_Neural`|
    ||`en-US_Joanna_Standard`|
    ||`en-US_Joey_Neural`|
    ||`en-US_Joey_Standard`|
    ||`en-US_Justin_Neural`|
    ||`en-US_Justin_Standard`|
    ||`en-US_Kendra_Neural`|
    ||`en-US_Kendra_Standard`|
    ||`en-US_Kevin_Neural`|
    ||`en-US_Kimberly_Neural`|
    ||`en-US_Kimberly_Standard`|
    ||`en-US_Matthew_Neural`|
    ||`en-US_Matthew_Standard`|
    ||`en-US_Ruth_Neural`|
    ||`en-US_Salli_Neural`|
    ||`en-US_Salli_Standard`|
    ||`en-US_Stephen_Neural`|
    ||`en-ZA_Ayanda_Neural`|
    ||`es-ES_Conchita_Standard`|
    ||`es-ES_Enrique_Standard`|
    ||`es-ES_Lucia_Neural`|
    ||`es-ES_Lucia_Standard`|
    ||`es-ES_Sergio_Neural`|
    ||`es-MX_Andres_Neural`|
    ||`es-MX_Mia_Neural`|
    ||`es-MX_Mia_Standard`|
    ||`es-US_Lupe_Neural`|
    ||`es-US_Lupe_Standard`|
    ||`es-US_Miguel_Standard`|
    ||`es-US_Pedro_Neural`|
    ||`es-US_Penelope_Standard`|
    ||`fi-FI_Suvi_Neural`|
    ||`fr-CA_Chantal_Standard`|
    ||`fr-CA_Gabrielle_Neural`|
    ||`fr-CA_Liam_Neural`|
    ||`fr-FR_Celine_Standard`|
    ||`fr-FR_Lea_Neural`|
    ||`fr-FR_Lea_Standard`|
    ||`fr-FR_Mathieu_Standard`|
    ||`fr-FR_Remi_Neural`|
    ||`hi-IN_Aditi_Standard`|
    ||`hi-IN_Kajal_Neural`|
    ||`is-IS_Dora_Standard`|
    ||`is-IS_Karl_Neural`|
    ||`is-IS_Karl_Standard`|
    ||`it-IT_Adriano_Neural`|
    ||`it-IT_Bianca_Neural`|
    ||`it-IT_Bianca_Standard`|
    ||`it-IT_Carla_Standard`|
    ||`it-IT_Giorgio_Standard`|
    ||`ja-JP_Kazuha_Neural`|
    ||`ja-JP_Mizuki_Standard`|
    ||`ja-JP_Takumi_Neural`|
    ||`ja-JP_Takumi_Standard`|
    ||`ja-JP_Tomoko_Neural`|
    ||`ko-KR_Seoyeon_Neural`|
    ||`ko-KR_Seoyeon_Standard`|
    ||`nb-NO_Liv_Standard`|
    ||`nl-NL_Laura_Neural`|
    ||`nl-NL_Lotte_Standard`|
    ||`nl-NL_Ruben_Standard`|
    ||`pl-PL_Ewa_Standard`|
    ||`pl-PL_Jacek_Standard`|
    ||`pl-PL_Jan_Standard`|
    ||`pl-PL_Maja_Standard`|
    ||`pl-PL_Ola_Neural`|
    ||`pt-BR_Camila_Neural`|
    ||`pt-BR_Camila_Standard`|
    ||`pt-BR_Ricardo_Standard`|
    ||`pt-BR_Thiago_Neural`|
    ||`pt-BR_Vitoria_Neural`|
    ||`pt-BR_Vitoria_Standard`|
    ||`pt-PT_Cristiano_Standard`|
    ||`pt-PT_Ines_Neural`|
    ||`pt-PT_Ines_Standard`|
    ||`ro-RO_Carmen_Standard`|
    ||`ru-RU_Maxim_Standard`|
    ||`ru-RU_Tatyana_Standard`|
    ||`sv-SE_Astrid_Standard`|
    ||`sv-SE_Elin_Neural`|
    ||`tr-TR_Filiz_Standard`|
    ||`yue-CN_Hiujin_Neural`|

    </details><details><summary>google</summary>





    |Name|Value|
    |----|-----|
    |**google**|`af-ZA-Standard-A`|
    ||`ar-XA-Standard-A`|
    ||`ar-XA-Standard-B`|
    ||`ar-XA-Standard-C`|
    ||`ar-XA-Standard-D`|
    ||`ar-XA-Wavenet-A`|
    ||`ar-XA-Wavenet-B`|
    ||`ar-XA-Wavenet-C`|
    ||`ar-XA-Wavenet-D`|
    ||`bg-BG-Standard-A`|
    ||`bn-IN-Standard-A`|
    ||`bn-IN-Standard-B`|
    ||`bn-IN-Wavenet-A`|
    ||`bn-IN-Wavenet-B`|
    ||`ca-ES-Standard-A`|
    ||`cmn-CN-Standard-A`|
    ||`cmn-CN-Standard-B`|
    ||`cmn-CN-Standard-C`|
    ||`cmn-CN-Standard-D`|
    ||`cmn-CN-Wavenet-A`|
    ||`cmn-CN-Wavenet-B`|
    ||`cmn-CN-Wavenet-C`|
    ||`cmn-CN-Wavenet-D`|
    ||`cmn-TW-Standard-A`|
    ||`cmn-TW-Standard-B`|
    ||`cmn-TW-Standard-C`|
    ||`cmn-TW-Wavenet-A`|
    ||`cmn-TW-Wavenet-B`|
    ||`cmn-TW-Wavenet-C`|
    ||`cs-CZ-Standard-A`|
    ||`cs-CZ-Wavenet-A`|
    ||`da-DK-Standard-A`|
    ||`da-DK-Standard-C`|
    ||`da-DK-Standard-D`|
    ||`da-DK-Standard-E`|
    ||`da-DK-Wavenet-A`|
    ||`da-DK-Wavenet-C`|
    ||`da-DK-Wavenet-D`|
    ||`da-DK-Wavenet-E`|
    ||`de-DE-Neural2-B`|
    ||`de-DE-Neural2-C`|
    ||`de-DE-Neural2-D`|
    ||`de-DE-Neural2-F`|
    ||`de-DE-Standard-A`|
    ||`de-DE-Standard-B`|
    ||`de-DE-Standard-C`|
    ||`de-DE-Standard-D`|
    ||`de-DE-Standard-E`|
    ||`de-DE-Standard-F`|
    ||`de-DE-Wavenet-A`|
    ||`de-DE-Wavenet-B`|
    ||`de-DE-Wavenet-C`|
    ||`de-DE-Wavenet-D`|
    ||`de-DE-Wavenet-E`|
    ||`de-DE-Wavenet-F`|
    ||`el-GR-Standard-A`|
    ||`el-GR-Wavenet-A`|
    ||`en-AU-Neural2-A`|
    ||`en-AU-Neural2-B`|
    ||`en-AU-Neural2-C`|
    ||`en-AU-Neural2-D`|
    ||`en-AU-News-E`|
    ||`en-AU-News-F`|
    ||`en-AU-News-G`|
    ||`en-AU-Standard-A`|
    ||`en-AU-Standard-B`|
    ||`en-AU-Standard-C`|
    ||`en-AU-Standard-D`|
    ||`en-AU-Wavenet-A`|
    ||`en-AU-Wavenet-B`|
    ||`en-AU-Wavenet-C`|
    ||`en-AU-Wavenet-D`|
    ||`en-GB-Neural2-A`|
    ||`en-GB-Neural2-B`|
    ||`en-GB-Neural2-C`|
    ||`en-GB-Neural2-D`|
    ||`en-GB-Neural2-F`|
    ||`en-GB-News-G`|
    ||`en-GB-News-H`|
    ||`en-GB-News-I`|
    ||`en-GB-News-J`|
    ||`en-GB-News-K`|
    ||`en-GB-News-L`|
    ||`en-GB-News-M`|
    ||`en-GB-Standard-A`|
    ||`en-GB-Standard-B`|
    ||`en-GB-Standard-C`|
    ||`en-GB-Standard-D`|
    ||`en-GB-Standard-F`|
    ||`en-GB-Wavenet-A`|
    ||`en-GB-Wavenet-B`|
    ||`en-GB-Wavenet-C`|
    ||`en-GB-Wavenet-D`|
    ||`en-GB-Wavenet-F`|
    ||`en-IN-Standard-A`|
    ||`en-IN-Standard-B`|
    ||`en-IN-Standard-C`|
    ||`en-IN-Standard-D`|
    ||`en-IN-Wavenet-A`|
    ||`en-IN-Wavenet-B`|
    ||`en-IN-Wavenet-C`|
    ||`en-IN-Wavenet-D`|
    ||`en-US-Neural2-A`|
    ||`en-US-Neural2-C`|
    ||`en-US-Neural2-D`|
    ||`en-US-Neural2-E`|
    ||`en-US-Neural2-F`|
    ||`en-US-Neural2-G`|
    ||`en-US-Neural2-H`|
    ||`en-US-Neural2-I`|
    ||`en-US-Neural2-J`|
    ||`en-US-News-K`|
    ||`en-US-News-L`|
    ||`en-US-News-M`|
    ||`en-US-News-N`|
    ||`en-US-Standard-A`|
    ||`en-US-Standard-B`|
    ||`en-US-Standard-C`|
    ||`en-US-Standard-D`|
    ||`en-US-Standard-E`|
    ||`en-US-Standard-F`|
    ||`en-US-Standard-G`|
    ||`en-US-Standard-H`|
    ||`en-US-Standard-I`|
    ||`en-US-Standard-J`|
    ||`en-US-Studio-M`|
    ||`en-US-Studio-O`|
    ||`en-US-Wavenet-A`|
    ||`en-US-Wavenet-B`|
    ||`en-US-Wavenet-C`|
    ||`en-US-Wavenet-D`|
    ||`en-US-Wavenet-E`|
    ||`en-US-Wavenet-F`|
    ||`en-US-Wavenet-G`|
    ||`en-US-Wavenet-H`|
    ||`en-US-Wavenet-I`|
    ||`en-US-Wavenet-J`|
    ||`es-ES-Neural2-A`|
    ||`es-ES-Neural2-B`|
    ||`es-ES-Neural2-C`|
    ||`es-ES-Neural2-D`|
    ||`es-ES-Neural2-E`|
    ||`es-ES-Neural2-F`|
    ||`es-ES-Standard-A`|
    ||`es-ES-Standard-B`|
    ||`es-ES-Standard-C`|
    ||`es-ES-Standard-D`|
    ||`es-ES-Wavenet-B`|
    ||`es-ES-Wavenet-C`|
    ||`es-ES-Wavenet-D`|
    ||`es-US-Neural2-A`|
    ||`es-US-Neural2-B`|
    ||`es-US-Neural2-C`|
    ||`es-US-News-D`|
    ||`es-US-News-E`|
    ||`es-US-News-F`|
    ||`es-US-News-G`|
    ||`es-US-Standard-A`|
    ||`es-US-Standard-B`|
    ||`es-US-Standard-C`|
    ||`es-US-Studio-B`|
    ||`es-US-Wavenet-A`|
    ||`es-US-Wavenet-B`|
    ||`es-US-Wavenet-C`|
    ||`eu-ES-Standard-A`|
    ||`fi-FI-Standard-A`|
    ||`fi-FI-Wavenet-A`|
    ||`fil-PH-Standard-A`|
    ||`fil-PH-Standard-B`|
    ||`fil-PH-Standard-C`|
    ||`fil-PH-Standard-D`|
    ||`fil-PH-Wavenet-A`|
    ||`fil-PH-Wavenet-B`|
    ||`fil-PH-Wavenet-C`|
    ||`fil-PH-Wavenet-D`|
    ||`fr-CA-Neural2-A`|
    ||`fr-CA-Neural2-B`|
    ||`fr-CA-Neural2-C`|
    ||`fr-CA-Neural2-D`|
    ||`fr-CA-Standard-A`|
    ||`fr-CA-Standard-B`|
    ||`fr-CA-Standard-C`|
    ||`fr-CA-Standard-D`|
    ||`fr-CA-Wavenet-A`|
    ||`fr-CA-Wavenet-B`|
    ||`fr-CA-Wavenet-C`|
    ||`fr-CA-Wavenet-D`|
    ||`fr-FR-Neural2-A`|
    ||`fr-FR-Neural2-B`|
    ||`fr-FR-Neural2-C`|
    ||`fr-FR-Neural2-D`|
    ||`fr-FR-Neural2-E`|
    ||`fr-FR-Standard-A`|
    ||`fr-FR-Standard-B`|
    ||`fr-FR-Standard-C`|
    ||`fr-FR-Standard-D`|
    ||`fr-FR-Standard-E`|
    ||`fr-FR-Wavenet-A`|
    ||`fr-FR-Wavenet-B`|
    ||`fr-FR-Wavenet-C`|
    ||`fr-FR-Wavenet-D`|
    ||`fr-FR-Wavenet-E`|
    ||`gl-ES-Standard-A`|
    ||`gu-IN-Standard-A`|
    ||`gu-IN-Standard-B`|
    ||`gu-IN-Wavenet-A`|
    ||`gu-IN-Wavenet-B`|
    ||`he-IL-Standard-A`|
    ||`he-IL-Standard-B`|
    ||`he-IL-Standard-C`|
    ||`he-IL-Standard-D`|
    ||`he-IL-Wavenet-A`|
    ||`he-IL-Wavenet-B`|
    ||`he-IL-Wavenet-C`|
    ||`he-IL-Wavenet-D`|
    ||`hi-IN-Neural2-A`|
    ||`hi-IN-Neural2-B`|
    ||`hi-IN-Neural2-C`|
    ||`hi-IN-Neural2-D`|
    ||`hi-IN-Standard-A`|
    ||`hi-IN-Standard-B`|
    ||`hi-IN-Standard-C`|
    ||`hi-IN-Standard-D`|
    ||`hi-IN-Wavenet-A`|
    ||`hi-IN-Wavenet-B`|
    ||`hi-IN-Wavenet-C`|
    ||`hi-IN-Wavenet-D`|
    ||`hu-HU-Standard-A`|
    ||`hu-HU-Wavenet-A`|
    ||`id-ID-Standard-A`|
    ||`id-ID-Standard-B`|
    ||`id-ID-Standard-C`|
    ||`id-ID-Standard-D`|
    ||`id-ID-Wavenet-A`|
    ||`id-ID-Wavenet-B`|
    ||`id-ID-Wavenet-C`|
    ||`id-ID-Wavenet-D`|
    ||`is-IS-Standard-A`|
    ||`it-IT-Neural2-A`|
    ||`it-IT-Neural2-C`|
    ||`it-IT-Standard-A`|
    ||`it-IT-Standard-B`|
    ||`it-IT-Standard-C`|
    ||`it-IT-Standard-D`|
    ||`it-IT-Wavenet-A`|
    ||`it-IT-Wavenet-B`|
    ||`it-IT-Wavenet-C`|
    ||`it-IT-Wavenet-D`|
    ||`ja-JP-Neural2-B`|
    ||`ja-JP-Neural2-C`|
    ||`ja-JP-Neural2-D`|
    ||`ja-JP-Standard-A`|
    ||`ja-JP-Standard-B`|
    ||`ja-JP-Standard-C`|
    ||`ja-JP-Standard-D`|
    ||`ja-JP-Wavenet-A`|
    ||`ja-JP-Wavenet-B`|
    ||`ja-JP-Wavenet-C`|
    ||`ja-JP-Wavenet-D`|
    ||`kn-IN-Standard-A`|
    ||`kn-IN-Standard-B`|
    ||`kn-IN-Wavenet-A`|
    ||`kn-IN-Wavenet-B`|
    ||`ko-KR-Neural2-A`|
    ||`ko-KR-Neural2-B`|
    ||`ko-KR-Neural2-C`|
    ||`ko-KR-Standard-A`|
    ||`ko-KR-Standard-B`|
    ||`ko-KR-Standard-C`|
    ||`ko-KR-Standard-D`|
    ||`ko-KR-Wavenet-A`|
    ||`ko-KR-Wavenet-B`|
    ||`ko-KR-Wavenet-C`|
    ||`ko-KR-Wavenet-D`|
    ||`lt-LT-Standard-A`|
    ||`lv-LV-Standard-A`|
    ||`ml-IN-Standard-A`|
    ||`ml-IN-Standard-B`|
    ||`ml-IN-Wavenet-A`|
    ||`ml-IN-Wavenet-B`|
    ||`ml-IN-Wavenet-C`|
    ||`ml-IN-Wavenet-D`|
    ||`mr-IN-Standard-A`|
    ||`mr-IN-Standard-B`|
    ||`mr-IN-Standard-C`|
    ||`mr-IN-Wavenet-A`|
    ||`mr-IN-Wavenet-B`|
    ||`mr-IN-Wavenet-C`|
    ||`ms-MY-Standard-A`|
    ||`ms-MY-Standard-B`|
    ||`ms-MY-Standard-C`|
    ||`ms-MY-Standard-D`|
    ||`ms-MY-Wavenet-A`|
    ||`ms-MY-Wavenet-B`|
    ||`ms-MY-Wavenet-C`|
    ||`ms-MY-Wavenet-D`|
    ||`nb-NO-Standard-A`|
    ||`nb-NO-Standard-B`|
    ||`nb-NO-Standard-C`|
    ||`nb-NO-Standard-D`|
    ||`nb-NO-Standard-E`|
    ||`nb-NO-Wavenet-A`|
    ||`nb-NO-Wavenet-B`|
    ||`nb-NO-Wavenet-C`|
    ||`nb-NO-Wavenet-D`|
    ||`nb-NO-Wavenet-E`|
    ||`nl-BE-Standard-A`|
    ||`nl-BE-Standard-B`|
    ||`nl-BE-Wavenet-A`|
    ||`nl-BE-Wavenet-B`|
    ||`nl-NL-Standard-A`|
    ||`nl-NL-Standard-B`|
    ||`nl-NL-Standard-C`|
    ||`nl-NL-Standard-D`|
    ||`nl-NL-Standard-E`|
    ||`nl-NL-Wavenet-A`|
    ||`nl-NL-Wavenet-B`|
    ||`nl-NL-Wavenet-C`|
    ||`nl-NL-Wavenet-D`|
    ||`nl-NL-Wavenet-E`|
    ||`pa-IN-Standard-A`|
    ||`pa-IN-Standard-B`|
    ||`pa-IN-Standard-C`|
    ||`pa-IN-Standard-D`|
    ||`pa-IN-Wavenet-A`|
    ||`pa-IN-Wavenet-B`|
    ||`pa-IN-Wavenet-C`|
    ||`pa-IN-Wavenet-D`|
    ||`pl-PL-Standard-A`|
    ||`pl-PL-Standard-B`|
    ||`pl-PL-Standard-C`|
    ||`pl-PL-Standard-D`|
    ||`pl-PL-Standard-E`|
    ||`pl-PL-Wavenet-A`|
    ||`pl-PL-Wavenet-B`|
    ||`pl-PL-Wavenet-C`|
    ||`pl-PL-Wavenet-D`|
    ||`pl-PL-Wavenet-E`|
    ||`pt-BR-Neural2-A`|
    ||`pt-BR-Neural2-B`|
    ||`pt-BR-Neural2-C`|
    ||`pt-BR-Standard-A`|
    ||`pt-BR-Standard-B`|
    ||`pt-BR-Standard-C`|
    ||`pt-BR-Wavenet-A`|
    ||`pt-BR-Wavenet-B`|
    ||`pt-BR-Wavenet-C`|
    ||`pt-PT-Standard-A`|
    ||`pt-PT-Standard-B`|
    ||`pt-PT-Standard-C`|
    ||`pt-PT-Standard-D`|
    ||`pt-PT-Wavenet-A`|
    ||`pt-PT-Wavenet-B`|
    ||`pt-PT-Wavenet-C`|
    ||`pt-PT-Wavenet-D`|
    ||`ro-RO-Standard-A`|
    ||`ro-RO-Wavenet-A`|
    ||`ru-RU-Standard-A`|
    ||`ru-RU-Standard-B`|
    ||`ru-RU-Standard-C`|
    ||`ru-RU-Standard-D`|
    ||`ru-RU-Standard-E`|
    ||`ru-RU-Wavenet-A`|
    ||`ru-RU-Wavenet-B`|
    ||`ru-RU-Wavenet-C`|
    ||`ru-RU-Wavenet-D`|
    ||`ru-RU-Wavenet-E`|
    ||`sk-SK-Standard-A`|
    ||`sk-SK-Wavenet-A`|
    ||`sr-RS-Standard-A`|
    ||`sv-SE-Standard-A`|
    ||`sv-SE-Standard-B`|
    ||`sv-SE-Standard-C`|
    ||`sv-SE-Standard-D`|
    ||`sv-SE-Standard-E`|
    ||`sv-SE-Wavenet-A`|
    ||`sv-SE-Wavenet-B`|
    ||`sv-SE-Wavenet-C`|
    ||`sv-SE-Wavenet-D`|
    ||`sv-SE-Wavenet-E`|
    ||`ta-IN-Standard-A`|
    ||`ta-IN-Standard-B`|
    ||`ta-IN-Standard-C`|
    ||`ta-IN-Standard-D`|
    ||`ta-IN-Wavenet-A`|
    ||`ta-IN-Wavenet-B`|
    ||`ta-IN-Wavenet-C`|
    ||`ta-IN-Wavenet-D`|
    ||`te-IN-Standard-A`|
    ||`te-IN-Standard-B`|
    ||`th-TH-Standard-A`|
    ||`tr-TR-Standard-A`|
    ||`tr-TR-Standard-B`|
    ||`tr-TR-Standard-C`|
    ||`tr-TR-Standard-D`|
    ||`tr-TR-Standard-E`|
    ||`tr-TR-Wavenet-A`|
    ||`tr-TR-Wavenet-B`|
    ||`tr-TR-Wavenet-C`|
    ||`tr-TR-Wavenet-D`|
    ||`tr-TR-Wavenet-E`|
    ||`uk-UA-Standard-A`|
    ||`uk-UA-Wavenet-A`|
    ||`vi-VN-Standard-A`|
    ||`vi-VN-Standard-B`|
    ||`vi-VN-Standard-C`|
    ||`vi-VN-Standard-D`|
    ||`vi-VN-Wavenet-A`|
    ||`vi-VN-Wavenet-B`|
    ||`vi-VN-Wavenet-C`|
    ||`vi-VN-Wavenet-D`|
    ||`yue-HK-Standard-A`|
    ||`yue-HK-Standard-B`|
    ||`yue-HK-Standard-C`|
    ||`yue-HK-Standard-D`|

    </details><details><summary>ibm</summary>





    |Name|Value|
    |----|-----|
    |**ibm**|`de-DE_BirgitV3Voice`|
    ||`de-DE_DieterV3Voice`|
    ||`de-DE_ErikaV3Voice`|
    ||`en-AU_HeidiExpressive`|
    ||`en-AU_JackExpressive`|
    ||`en-GB_CharlotteV3Voice`|
    ||`en-GB_JamesV3Voice`|
    ||`en-GB_KateV3Voice`|
    ||`en-US_AllisonExpressive`|
    ||`en-US_AllisonV3Voice`|
    ||`en-US_EmilyV3Voice`|
    ||`en-US_EmmaExpressive`|
    ||`en-US_HenryV3Voice`|
    ||`en-US_KevinV3Voice`|
    ||`en-US_LisaExpressive`|
    ||`en-US_LisaV3Voice`|
    ||`en-US_MichaelExpressive`|
    ||`en-US_MichaelV3Voice`|
    ||`en-US_OliviaV3Voice`|
    ||`es-ES_EnriqueV3Voice`|
    ||`es-ES_LauraV3Voice`|
    ||`es-LA_SofiaV3Voice`|
    ||`es-US_SofiaV3Voice`|
    ||`fr-CA_LouiseV3Voice`|
    ||`fr-FR_NicolasV3Voice`|
    ||`fr-FR_ReneeV3Voice`|
    ||`it-IT_FrancescaV3Voice`|
    ||`ja-JP_EmiV3Voice`|
    ||`ko-KR_JinV3Voice`|
    ||`nl-NL_MerelV3Voice`|
    ||`pt-BR_IsabelaV3Voice`|

    </details><details><summary>microsoft</summary>





    |Name|Value|
    |----|-----|
    |**microsoft**|`af-ZA-AdriNeural`|
    ||`af-ZA-WillemNeural`|
    ||`am-ET-AmehaNeural`|
    ||`am-ET-MekdesNeural`|
    ||`ar-AE-FatimaNeural`|
    ||`ar-AE-HamdanNeural`|
    ||`ar-BH-AliNeural`|
    ||`ar-BH-LailaNeural`|
    ||`ar-DZ-AminaNeural`|
    ||`ar-DZ-IsmaelNeural`|
    ||`ar-EG-SalmaNeural`|
    ||`ar-EG-ShakirNeural`|
    ||`ar-IQ-BasselNeural`|
    ||`ar-IQ-RanaNeural`|
    ||`ar-JO-SanaNeural`|
    ||`ar-JO-TaimNeural`|
    ||`ar-KW-FahedNeural`|
    ||`ar-KW-NouraNeural`|
    ||`ar-LB-LaylaNeural`|
    ||`ar-LB-RamiNeural`|
    ||`ar-LY-ImanNeural`|
    ||`ar-LY-OmarNeural`|
    ||`ar-MA-JamalNeural`|
    ||`ar-MA-MounaNeural`|
    ||`ar-OM-AbdullahNeural`|
    ||`ar-OM-AyshaNeural`|
    ||`ar-QA-AmalNeural`|
    ||`ar-QA-MoazNeural`|
    ||`ar-SA-HamedNeural`|
    ||`ar-SA-ZariyahNeural`|
    ||`ar-SY-AmanyNeural`|
    ||`ar-SY-LaithNeural`|
    ||`ar-TN-HediNeural`|
    ||`ar-TN-ReemNeural`|
    ||`ar-YE-MaryamNeural`|
    ||`ar-YE-SalehNeural`|
    ||`az-AZ-BabekNeural`|
    ||`az-AZ-BanuNeural`|
    ||`bg-BG-BorislavNeural`|
    ||`bg-BG-KalinaNeural`|
    ||`bn-BD-NabanitaNeural`|
    ||`bn-BD-PradeepNeural`|
    ||`bn-IN-BashkarNeural`|
    ||`bn-IN-TanishaaNeural`|
    ||`bs-BA-GoranNeural`|
    ||`bs-BA-VesnaNeural`|
    ||`ca-ES-AlbaNeural`|
    ||`ca-ES-EnricNeural`|
    ||`ca-ES-JoanaNeural`|
    ||`cs-CZ-AntoninNeural`|
    ||`cs-CZ-VlastaNeural`|
    ||`cy-GB-AledNeural`|
    ||`cy-GB-NiaNeural`|
    ||`da-DK-ChristelNeural`|
    ||`da-DK-JeppeNeural`|
    ||`de-AT-IngridNeural`|
    ||`de-AT-JonasNeural`|
    ||`de-CH-JanNeural`|
    ||`de-CH-LeniNeural`|
    ||`de-DE-AmalaNeural`|
    ||`de-DE-BerndNeural`|
    ||`de-DE-ChristophNeural`|
    ||`de-DE-ConradNeural`|
    ||`de-DE-ElkeNeural`|
    ||`de-DE-GiselaNeural`|
    ||`de-DE-KasperNeural`|
    ||`de-DE-KatjaNeural`|
    ||`de-DE-KillianNeural`|
    ||`de-DE-KlarissaNeural`|
    ||`de-DE-KlausNeural`|
    ||`de-DE-LouisaNeural`|
    ||`de-DE-MajaNeural`|
    ||`de-DE-RalfNeural`|
    ||`de-DE-TanjaNeural`|
    ||`el-GR-AthinaNeural`|
    ||`el-GR-NestorasNeural`|
    ||`en-AU-AnnetteNeural`|
    ||`en-AU-CarlyNeural`|
    ||`en-AU-DarrenNeural`|
    ||`en-AU-DuncanNeural`|
    ||`en-AU-ElsieNeural`|
    ||`en-AU-FreyaNeural`|
    ||`en-AU-JoanneNeural`|
    ||`en-AU-KenNeural`|
    ||`en-AU-KimNeural`|
    ||`en-AU-NatashaNeural`|
    ||`en-AU-NeilNeural`|
    ||`en-AU-TimNeural`|
    ||`en-AU-TinaNeural`|
    ||`en-AU-WilliamNeural`|
    ||`en-CA-ClaraNeural`|
    ||`en-CA-LiamNeural`|
    ||`en-GB-AbbiNeural`|
    ||`en-GB-AlfieNeural`|
    ||`en-GB-BellaNeural`|
    ||`en-GB-ElliotNeural`|
    ||`en-GB-EthanNeural`|
    ||`en-GB-HollieNeural`|
    ||`en-GB-LibbyNeural`|
    ||`en-GB-MaisieNeural`|
    ||`en-GB-NoahNeural`|
    ||`en-GB-OliverNeural`|
    ||`en-GB-OliviaNeural`|
    ||`en-GB-RyanNeural`|
    ||`en-GB-SoniaNeural`|
    ||`en-GB-ThomasNeural`|
    ||`en-HK-SamNeural`|
    ||`en-HK-YanNeural`|
    ||`en-IE-ConnorNeural`|
    ||`en-IE-EmilyNeural`|
    ||`en-IN-NeerjaNeural`|
    ||`en-IN-PrabhatNeural`|
    ||`en-KE-AsiliaNeural`|
    ||`en-KE-ChilembaNeural`|
    ||`en-NG-AbeoNeural`|
    ||`en-NG-EzinneNeural`|
    ||`en-NZ-MitchellNeural`|
    ||`en-NZ-MollyNeural`|
    ||`en-PH-JamesNeural`|
    ||`en-PH-RosaNeural`|
    ||`en-SG-LunaNeural`|
    ||`en-SG-WayneNeural`|
    ||`en-TZ-ElimuNeural`|
    ||`en-TZ-ImaniNeural`|
    ||`en-US-AIGenerate1Neural`|
    ||`en-US-AIGenerate2Neural`|
    ||`en-US-AmberNeural`|
    ||`en-US-AnaNeural`|
    ||`en-US-AriaNeural`|
    ||`en-US-AshleyNeural`|
    ||`en-US-BrandonNeural`|
    ||`en-US-ChristopherNeural`|
    ||`en-US-CoraNeural`|
    ||`en-US-DavisNeural`|
    ||`en-US-ElizabethNeural`|
    ||`en-US-EricNeural`|
    ||`en-US-GuyNeural`|
    ||`en-US-JacobNeural`|
    ||`en-US-JaneNeural`|
    ||`en-US-JasonNeural`|
    ||`en-US-JennyMultilingualNeural`|
    ||`en-US-JennyNeural`|
    ||`en-US-MichelleNeural`|
    ||`en-US-MonicaNeural`|
    ||`en-US-NancyNeural`|
    ||`en-US-RogerNeural`|
    ||`en-US-SaraNeural`|
    ||`en-US-SteffanNeural`|
    ||`en-US-TonyNeural`|
    ||`en-ZA-LeahNeural`|
    ||`en-ZA-LukeNeural`|
    ||`es-AR-ElenaNeural`|
    ||`es-AR-TomasNeural`|
    ||`es-BO-MarceloNeural`|
    ||`es-BO-SofiaNeural`|
    ||`es-CL-CatalinaNeural`|
    ||`es-CL-LorenzoNeural`|
    ||`es-CO-GonzaloNeural`|
    ||`es-CO-SalomeNeural`|
    ||`es-CR-JuanNeural`|
    ||`es-CR-MariaNeural`|
    ||`es-CU-BelkysNeural`|
    ||`es-CU-ManuelNeural`|
    ||`es-DO-EmilioNeural`|
    ||`es-DO-RamonaNeural`|
    ||`es-EC-AndreaNeural`|
    ||`es-EC-LuisNeural`|
    ||`es-ES-AbrilNeural`|
    ||`es-ES-AlvaroNeural`|
    ||`es-ES-ArnauNeural`|
    ||`es-ES-DarioNeural`|
    ||`es-ES-EliasNeural`|
    ||`es-ES-ElviraNeural`|
    ||`es-ES-EstrellaNeural`|
    ||`es-ES-IreneNeural`|
    ||`es-ES-LaiaNeural`|
    ||`es-ES-LiaNeural`|
    ||`es-ES-NilNeural`|
    ||`es-ES-SaulNeural`|
    ||`es-ES-TeoNeural`|
    ||`es-ES-TrianaNeural`|
    ||`es-ES-VeraNeural`|
    ||`es-GQ-JavierNeural`|
    ||`es-GQ-TeresaNeural`|
    ||`es-GT-AndresNeural`|
    ||`es-GT-MartaNeural`|
    ||`es-HN-CarlosNeural`|
    ||`es-HN-KarlaNeural`|
    ||`es-MX-BeatrizNeural`|
    ||`es-MX-CandelaNeural`|
    ||`es-MX-CarlotaNeural`|
    ||`es-MX-CecilioNeural`|
    ||`es-MX-DaliaNeural`|
    ||`es-MX-GerardoNeural`|
    ||`es-MX-JorgeNeural`|
    ||`es-MX-LarissaNeural`|
    ||`es-MX-LibertoNeural`|
    ||`es-MX-LucianoNeural`|
    ||`es-MX-MarinaNeural`|
    ||`es-MX-NuriaNeural`|
    ||`es-MX-PelayoNeural`|
    ||`es-MX-RenataNeural`|
    ||`es-MX-YagoNeural`|
    ||`es-NI-FedericoNeural`|
    ||`es-NI-YolandaNeural`|
    ||`es-PA-MargaritaNeural`|
    ||`es-PA-RobertoNeural`|
    ||`es-PE-AlexNeural`|
    ||`es-PE-CamilaNeural`|
    ||`es-PR-KarinaNeural`|
    ||`es-PR-VictorNeural`|
    ||`es-PY-MarioNeural`|
    ||`es-PY-TaniaNeural`|
    ||`es-SV-LorenaNeural`|
    ||`es-SV-RodrigoNeural`|
    ||`es-US-AlonsoNeural`|
    ||`es-US-PalomaNeural`|
    ||`es-UY-MateoNeural`|
    ||`es-UY-ValentinaNeural`|
    ||`es-VE-PaolaNeural`|
    ||`es-VE-SebastianNeural`|
    ||`et-EE-AnuNeural`|
    ||`et-EE-KertNeural`|
    ||`eu-ES-AinhoaNeural`|
    ||`eu-ES-AnderNeural`|
    ||`fa-IR-DilaraNeural`|
    ||`fa-IR-FaridNeural`|
    ||`fi-FI-HarriNeural`|
    ||`fi-FI-NooraNeural`|
    ||`fi-FI-SelmaNeural`|
    ||`fil-PH-AngeloNeural`|
    ||`fil-PH-BlessicaNeural`|
    ||`fr-BE-CharlineNeural`|
    ||`fr-BE-GerardNeural`|
    ||`fr-CA-AntoineNeural`|
    ||`fr-CA-JeanNeural`|
    ||`fr-CA-SylvieNeural`|
    ||`fr-CH-ArianeNeural`|
    ||`fr-CH-FabriceNeural`|
    ||`fr-FR-AlainNeural`|
    ||`fr-FR-BrigitteNeural`|
    ||`fr-FR-CelesteNeural`|
    ||`fr-FR-ClaudeNeural`|
    ||`fr-FR-CoralieNeural`|
    ||`fr-FR-DeniseNeural`|
    ||`fr-FR-EloiseNeural`|
    ||`fr-FR-HenriNeural`|
    ||`fr-FR-JacquelineNeural`|
    ||`fr-FR-JeromeNeural`|
    ||`fr-FR-JosephineNeural`|
    ||`fr-FR-MauriceNeural`|
    ||`fr-FR-YvesNeural`|
    ||`fr-FR-YvetteNeural`|
    ||`ga-IE-ColmNeural`|
    ||`ga-IE-OrlaNeural`|
    ||`gl-ES-RoiNeural`|
    ||`gl-ES-SabelaNeural`|
    ||`gu-IN-DhwaniNeural`|
    ||`gu-IN-NiranjanNeural`|
    ||`he-IL-AvriNeural`|
    ||`he-IL-HilaNeural`|
    ||`hi-IN-MadhurNeural`|
    ||`hi-IN-SwaraNeural`|
    ||`hr-HR-GabrijelaNeural`|
    ||`hr-HR-SreckoNeural`|
    ||`hu-HU-NoemiNeural`|
    ||`hu-HU-TamasNeural`|
    ||`hy-AM-AnahitNeural`|
    ||`hy-AM-HaykNeural`|
    ||`id-ID-ArdiNeural`|
    ||`id-ID-GadisNeural`|
    ||`is-IS-GudrunNeural`|
    ||`is-IS-GunnarNeural`|
    ||`it-IT-BenignoNeural`|
    ||`it-IT-CalimeroNeural`|
    ||`it-IT-CataldoNeural`|
    ||`it-IT-DiegoNeural`|
    ||`it-IT-ElsaNeural`|
    ||`it-IT-FabiolaNeural`|
    ||`it-IT-FiammaNeural`|
    ||`it-IT-GianniNeural`|
    ||`it-IT-ImeldaNeural`|
    ||`it-IT-IrmaNeural`|
    ||`it-IT-IsabellaNeural`|
    ||`it-IT-LisandroNeural`|
    ||`it-IT-PalmiraNeural`|
    ||`it-IT-PierinaNeural`|
    ||`it-IT-RinaldoNeural`|
    ||`ja-JP-AoiNeural`|
    ||`ja-JP-DaichiNeural`|
    ||`ja-JP-KeitaNeural`|
    ||`ja-JP-MayuNeural`|
    ||`ja-JP-NanamiNeural`|
    ||`ja-JP-NaokiNeural`|
    ||`ja-JP-ShioriNeural`|
    ||`jv-ID-DimasNeural`|
    ||`jv-ID-SitiNeural`|
    ||`ka-GE-EkaNeural`|
    ||`ka-GE-GiorgiNeural`|
    ||`kk-KZ-AigulNeural`|
    ||`kk-KZ-DauletNeural`|
    ||`km-KH-PisethNeural`|
    ||`km-KH-SreymomNeural`|
    ||`kn-IN-GaganNeural`|
    ||`kn-IN-SapnaNeural`|
    ||`ko-KR-BongJinNeural`|
    ||`ko-KR-GookMinNeural`|
    ||`ko-KR-InJoonNeural`|
    ||`ko-KR-JiMinNeural`|
    ||`ko-KR-SeoHyeonNeural`|
    ||`ko-KR-SoonBokNeural`|
    ||`ko-KR-SunHiNeural`|
    ||`ko-KR-YuJinNeural`|
    ||`lo-LA-ChanthavongNeural`|
    ||`lo-LA-KeomanyNeural`|
    ||`lt-LT-LeonasNeural`|
    ||`lt-LT-OnaNeural`|
    ||`lv-LV-EveritaNeural`|
    ||`lv-LV-NilsNeural`|
    ||`mk-MK-AleksandarNeural`|
    ||`mk-MK-MarijaNeural`|
    ||`ml-IN-MidhunNeural`|
    ||`ml-IN-SobhanaNeural`|
    ||`mn-MN-BataaNeural`|
    ||`mn-MN-YesuiNeural`|
    ||`mr-IN-AarohiNeural`|
    ||`mr-IN-ManoharNeural`|
    ||`ms-MY-OsmanNeural`|
    ||`ms-MY-YasminNeural`|
    ||`mt-MT-GraceNeural`|
    ||`mt-MT-JosephNeural`|
    ||`my-MM-NilarNeural`|
    ||`my-MM-ThihaNeural`|
    ||`nb-NO-FinnNeural`|
    ||`nb-NO-IselinNeural`|
    ||`nb-NO-PernilleNeural`|
    ||`ne-NP-HemkalaNeural`|
    ||`ne-NP-SagarNeural`|
    ||`nl-BE-ArnaudNeural`|
    ||`nl-BE-DenaNeural`|
    ||`nl-NL-ColetteNeural`|
    ||`nl-NL-FennaNeural`|
    ||`nl-NL-MaartenNeural`|
    ||`pl-PL-AgnieszkaNeural`|
    ||`pl-PL-MarekNeural`|
    ||`pl-PL-ZofiaNeural`|
    ||`ps-AF-GulNawazNeural`|
    ||`ps-AF-LatifaNeural`|
    ||`pt-BR-AntonioNeural`|
    ||`pt-BR-BrendaNeural`|
    ||`pt-BR-DonatoNeural`|
    ||`pt-BR-ElzaNeural`|
    ||`pt-BR-FabioNeural`|
    ||`pt-BR-FranciscaNeural`|
    ||`pt-BR-GiovannaNeural`|
    ||`pt-BR-HumbertoNeural`|
    ||`pt-BR-JulioNeural`|
    ||`pt-BR-LeilaNeural`|
    ||`pt-BR-LeticiaNeural`|
    ||`pt-BR-ManuelaNeural`|
    ||`pt-BR-NicolauNeural`|
    ||`pt-BR-ValerioNeural`|
    ||`pt-BR-YaraNeural`|
    ||`pt-PT-DuarteNeural`|
    ||`pt-PT-FernandaNeural`|
    ||`pt-PT-RaquelNeural`|
    ||`ro-RO-AlinaNeural`|
    ||`ro-RO-EmilNeural`|
    ||`ru-RU-DariyaNeural`|
    ||`ru-RU-DmitryNeural`|
    ||`ru-RU-SvetlanaNeural`|
    ||`si-LK-SameeraNeural`|
    ||`si-LK-ThiliniNeural`|
    ||`sk-SK-LukasNeural`|
    ||`sk-SK-ViktoriaNeural`|
    ||`sl-SI-PetraNeural`|
    ||`sl-SI-RokNeural`|
    ||`so-SO-MuuseNeural`|
    ||`so-SO-UbaxNeural`|
    ||`sq-AL-AnilaNeural`|
    ||`sq-AL-IlirNeural`|
    ||`sr-RS-NicholasNeural`|
    ||`sr-RS-SophieNeural`|
    ||`su-ID-JajangNeural`|
    ||`su-ID-TutiNeural`|
    ||`sv-SE-HilleviNeural`|
    ||`sv-SE-MattiasNeural`|
    ||`sv-SE-SofieNeural`|
    ||`sw-KE-RafikiNeural`|
    ||`sw-KE-ZuriNeural`|
    ||`sw-TZ-DaudiNeural`|
    ||`sw-TZ-RehemaNeural`|
    ||`ta-IN-PallaviNeural`|
    ||`ta-IN-ValluvarNeural`|
    ||`ta-LK-KumarNeural`|
    ||`ta-LK-SaranyaNeural`|
    ||`ta-MY-KaniNeural`|
    ||`ta-MY-SuryaNeural`|
    ||`ta-SG-AnbuNeural`|
    ||`ta-SG-VenbaNeural`|
    ||`te-IN-MohanNeural`|
    ||`te-IN-ShrutiNeural`|
    ||`th-TH-AcharaNeural`|
    ||`th-TH-NiwatNeural`|
    ||`th-TH-PremwadeeNeural`|
    ||`tr-TR-AhmetNeural`|
    ||`tr-TR-EmelNeural`|
    ||`uk-UA-OstapNeural`|
    ||`uk-UA-PolinaNeural`|
    ||`ur-IN-GulNeural`|
    ||`ur-IN-SalmanNeural`|
    ||`ur-PK-AsadNeural`|
    ||`ur-PK-UzmaNeural`|
    ||`uz-UZ-MadinaNeural`|
    ||`uz-UZ-SardorNeural`|
    ||`vi-VN-HoaiMyNeural`|
    ||`vi-VN-NamMinhNeural`|
    ||`wuu-CN-XiaotongNeural`|
    ||`wuu-CN-YunzheNeural`|
    ||`yue-CN-XiaoMinNeural`|
    ||`yue-CN-YunSongNeural`|
    ||`zh-CN-XiaochenNeural`|
    ||`zh-CN-XiaohanNeural`|
    ||`zh-CN-XiaomengNeural`|
    ||`zh-CN-XiaomoNeural`|
    ||`zh-CN-XiaoqiuNeural`|
    ||`zh-CN-XiaoruiNeural`|
    ||`zh-CN-XiaoshuangNeural`|
    ||`zh-CN-XiaoxiaoNeural`|
    ||`zh-CN-XiaoxuanNeural`|
    ||`zh-CN-XiaoyanNeural`|
    ||`zh-CN-XiaoyiNeural`|
    ||`zh-CN-XiaoyouNeural`|
    ||`zh-CN-XiaozhenNeural`|
    ||`zh-CN-YunfengNeural`|
    ||`zh-CN-YunhaoNeural`|
    ||`zh-CN-YunjianNeural`|
    ||`zh-CN-YunxiNeural`|
    ||`zh-CN-YunxiaNeural`|
    ||`zh-CN-YunyangNeural`|
    ||`zh-CN-YunyeNeural`|
    ||`zh-CN-YunzeNeural`|
    ||`zh-CN-henan-YundengNeural`|
    ||`zh-CN-liaoning-XiaobeiNeural`|
    ||`zh-CN-shaanxi-XiaoniNeural`|
    ||`zh-CN-shandong-YunxiangNeural`|
    ||`zh-CN-sichuan-YunxiNeural`|
    ||`zh-HK-HiuGaaiNeural`|
    ||`zh-HK-HiuMaanNeural`|
    ||`zh-HK-WanLungNeural`|
    ||`zh-TW-HsiaoChenNeural`|
    ||`zh-TW-HsiaoYuNeural`|
    ||`zh-TW-YunJheNeural`|
    ||`zu-ZA-ThandoNeural`|
    ||`zu-ZA-ThembaNeural`|

    </details><details><summary>lovoai</summary>





    |Name|Value|
    |----|-----|
    |**lovoai**|`af-ZA_Albertus Ruan`|
    ||`af-ZA_Danelle Wessel`|
    ||`am-ET_Abai Berhe`|
    ||`am-ET_Cherenet Tesfaye`|
    ||`ar-AE_Mansour Ahmed`|
    ||`ar-AE_Maryam Khan`|
    ||`ar-BH_Fatima Kumar`|
    ||`ar-BH_Omar Hassan`|
    ||`ar-DZ_Samia Touati`|
    ||`ar-DZ_Zuthimalin Brahimi`|
    ||`ar-EG_Ahmed Gamal`|
    ||`ar-EG_Reem Salah`|
    ||`ar-IQ_Aveen Majid`|
    ||`ar-IQ_Ismail Hashem`|
    ||`ar-JO_Fatima Jaber`|
    ||`ar-JO_Yousef Saleh`|
    ||`ar-KW_Areej Nair`|
    ||`ar-KW_Khaled Al Azmi`|
    ||`ar-LB_Abdel El Din`|
    ||`ar-LB_Eessa Kadifa`|
    ||`ar-LY_Abir Salem`|
    ||`ar-LY_Ahsan Omar`|
    ||`ar-MA_Hamid Bennani`|
    ||`ar-MA_Salma Naciri`|
    ||`ar-OM_Jabbar Singh`|
    ||`ar-OM_Zahra Sultan`|
    ||`ar-QA_Faizur Kumar`|
    ||`ar-QA_Noora Hussain`|
    ||`ar-SA_Majidah Khan`|
    ||`ar-SA_Omar Aziz`|
    ||`ar-SY_Oraida El-Assad`|
    ||`ar-SY_Rabah Ibrahim`|
    ||`ar-TN_Donia Cherif`|
    ||`ar-TN_Karim Dridi`|
    ||`ar-YE_Mansour Kasim`|
    ||`ar-YE_Mehdi Bawazeer`|
    ||`az-AZ_Ugur Quliyeva`|
    ||`az_AZ_Zeynab Cafarova`|
    ||`bg-BG_Damyan Ivanov`|
    ||`bg-BG_Fidanka Georgiev`|
    ||`bn-BD_Pranshu Akter`|
    ||`bn-BD_Vaagdevi Khatun`|
    ||`bn-IN_Gazi Mondal`|
    ||`bn-IN_Wali Ghosh`|
    ||`bs-BA_Esma Dodik`|
    ||`bs-BA_Ismet Rakic`|
    ||`ca-ES_Amada Fernando`|
    ||`ca-ES_Carmen Santiago`|
    ||`ca-ES_Miguel Torres`|
    ||`cs-CZ_Jana Rosicky`|
    ||`cs-CZ_Tomas Malecek`|
    ||`cy-GB_Branwen Jones`|
    ||`cy-GB_Elen Hughes`|
    ||`da-DK_Bjarne Jensen`|
    ||`da-DK_Helge Nielsen`|
    ||`de-AT_Lena Gruber`|
    ||`de-AT_Wilhelm Wagner`|
    ||`de-CH_Adolfus Meier`|
    ||`de-CH_Lara Keller`|
    ||`de-DE_Ada Weber`|
    ||`de-DE_Anna Schmidt`|
    ||`de-DE_Emma Muller`|
    ||`de-DE_Gerda Becker`|
    ||`de-DE_Hans Schulz`|
    ||`de-DE_Heidi Schneider`|
    ||`de-DE_Johanna Meyer`|
    ||`de-DE_Joshua Bauer`|
    ||`de-DE_Julian Koch`|
    ||`de-DE_Karl Hummels`|
    ||`de-DE_Maria Fischer`|
    ||`de-DE_Oliver Richter`|
    ||`de-DE_Otto Schaefer`|
    ||`de-DE_Petra Hoffman`|
    ||`de-DE_Walter Kimmich`|
    ||`el-GR_Petros Andino`|
    ||`el-GR_Thalia Klisiaris`|
    ||`en-AU_Amelia Taylor`|
    ||`en-AU_Charlotte Brown`|
    ||`en-AU_Darrell Robinson`|
    ||`en-AU_George Thompson`|
    ||`en-AU_Georgie Smith`|
    ||`en-AU_Isla Johnson`|
    ||`en-AU_Jake Nguyen`|
    ||`en-AU_Keegan Walker`|
    ||`en-AU_Kelly Opie`|
    ||`en-AU_Kevin Turner`|
    ||`en-AU_Mia White`|
    ||`en-AU_Nancy Jones`|
    ||`en-AU_Ryan Murphy`|
    ||`en-AU_Willow Martin`|
    ||`en-CA_Emily Salo`|
    ||`en-CA_Eric Fidyk`|
    ||`en-GB_Abigail Fraser`|
    ||`en-GB_Annie Smith`|
    ||`en-GB_Gertrude Baker`|
    ||`en-GB_Ian Kensington`|
    ||`en-GB_Kane Tooney`|
    ||`en-GB_Kelsey Michaels`|
    ||`en-GB_Kerrington Pacey`|
    ||`en-GB_Lizzy Wright`|
    ||`en-GB_Marcus O'Donell`|
    ||`en-GB_Nathaniel Jacobs`|
    ||`en-GB_Samuel Lee-Richards`|
    ||`en-GB_T.S. Cooper`|
    ||`en-GB_Theresa King`|
    ||`en-GB_William Tripp`|
    ||`en-HK_Heather Yiu`|
    ||`en-HK_Kevin Lau`|
    ||`en-IE_Aoife Byrne`|
    ||`en-IE_Bill Parkin`|
    ||`en-IN_Isha Singh`|
    ||`en-IN_Prabhdeep Patel`|
    ||`en-KE_Almasi Otieno`|
    ||`en-KE_Chitundu Mwangi`|
    ||`en-NG_Blessing Musa`|
    ||`en-NG_Kehinde Sade`|
    ||`en-NZ_Benson Duncan`|
    ||`en-NZ_Destiny Mitchell`|
    ||`en-PH_Angel dela Cruz`|
    ||`en-PH_Francis Reynaldo`|
    ||`en-SG_Chris Tan`|
    ||`en-SG_Rachel Ng`|
    ||`en-TZ_Busara Charles`|
    ||`en-TZ_Darweshi Juma`|
    ||`en-US_Alysha Imani`|
    ||`en-US_Betty Parker`|
    ||`en-US_Catherine Zania`|
    ||`en-US_Christopher Navarrez`|
    ||`en-US_Clara Ho`|
    ||`en-US_Eric Gonzalez`|
    ||`en-US_Heather Everett`|
    ||`en-US_Jamal Starke`|
    ||`en-US_Jasonna Johnson`|
    ||`en-US_Kaylee Montana`|
    ||`en-US_Ken hunter`|
    ||`en-US_Kim Howard`|
    ||`en-US_Kyle Moreno`|
    ||`en-US_Leroy Alshak`|
    ||`en-US_Micah Washington`|
    ||`en-US_Molly Richardson`|
    ||`en-US_Peter Lee`|
    ||`en-US_Phil Gough`|
    ||`en-US_Phoebe Nicholson`|
    ||`en-US_Samantha Hawthorne`|
    ||`en-US_Sean Orson`|
    ||`en-US_Serena Yang`|
    ||`en-US_Shannon Mechare`|
    ||`en-US_Thelma Browne`|
    ||`en-US_Tim Hardway`|
    ||`en-ZA_Cody Fergudson`|
    ||`en-ZA_Elna VanDijk`|
    ||`es-AR_Hyacinthe Castro`|
    ||`es-AR_Lautaro Gomez`|
    ||`es-BO_Elena Lopez`|
    ||`es-BO_Juan Perez`|
    ||`es-CL_Francisca Batistuta`|
    ||`es-CL_Gabriel Rodriguez`|
    ||`es-CO_Lorenzo Vazquez`|
    ||`es-CO_Sofia Garcia`|
    ||`es-CR_Guadalupe Suarez`|
    ||`es-CR_Sebastian Ramos`|
    ||`es-CU_Isabel Molina`|
    ||`es-CU_Luis Ortega`|
    ||`es-DO_Gabriela Serrano`|
    ||`es-DO_Raul Dominguez`|
    ||`es-EC_Angelina Romero`|
    ||`es-EC_Christian Diaz`|
    ||`es-EN_Carmen Martinela`|
    ||`es-ES_Andres Marin`|
    ||`es-ES_Emiliano Delgado`|
    ||`es-ES_Esmeralda Molina`|
    ||`es-ES_Hector Gavi`|
    ||`es-ES_Leo Gil`|
    ||`es-ES_Liliana Sanz`|
    ||`es-ES_Maria Ruiz`|
    ||`es-ES_Martin Enrique`|
    ||`es-ES_Miranda Navarro`|
    ||`es-ES_Pablo Iniesta`|
    ||`es-ES_Silvia Alvarez`|
    ||`es-ES_Teresa Iglesias`|
    ||`es-ES_Valentina Blanco`|
    ||`es-GQ_Elena Rubio`|
    ||`es-GQ_Teo Jimenez`|
    ||`es-GT_Ceciah Mendoza`|
    ||`es-GT_Paolo Ortiz`|
    ||`es-HN_Juana Flores`|
    ||`es-HN_Roberto Gutierrez`|
    ||`es-MX_Agata Albiol`|
    ||`es-MX_Darion Nunez`|
    ||`es-MX_Elias Lorenzo`|
    ||`es-MX_Elvira de Paul`|
    ||`es-MX_Enzo Paqueta`|
    ||`es-MX_Ezequiel Pacheco`|
    ||`es-MX_Iago Domingo`|
    ||`es-MX_Irene Vasquez`|
    ||`es-MX_Julieta Aguilar`|
    ||`es-MX_Lia Medina`|
    ||`es-MX_Nil Alvarez`|
    ||`es-MX_Pedro Rojas`|
    ||`es-MX_Rosa Valdoza`|
    ||`es-MX_Valencia Alba`|
    ||`es-MX_Veronica Mairal`|
    ||`es-NI_Abril Santacruz`|
    ||`es-NI_Lorenzo Llorente`|
    ||`es-PA_Liberto Marcos`|
    ||`es-PA_Yolanda Ezequiel`|
    ||`es-PE_Margarita de Fuentes`|
    ||`es-PE_Rey Sancho`|
    ||`es-PR_Alex de Santos`|
    ||`es-PR_Carlota Almiron`|
    ||`es-PY_Karina Diego`|
    ||`es-PY_Victor Mariela`|
    ||`es-SV_Jacinta Vela`|
    ||`es-SV_Marina Llorente`|
    ||`es-US_Jodrigo Alonso`|
    ||`es-US_Laia Paloma`|
    ||`es-US_Sergio Morata`|
    ||`es-UY_Lia Valentina`|
    ||`es-UY_Luis Ramon`|
    ||`es-VE_Manuel Rojos`|
    ||`es-VE_Sofia Vargas`|
    ||`et-EE_Barba Sepp`|
    ||`et-EE_Eduk Tamm`|
    ||`eu-ES_Markel Zubiri`|
    ||`eu-ES_Nahia Texpare`|
    ||`fa-IR_Bizhan Gilgamesh`|
    ||`fa-IR_Yasmina Hakimi`|
    ||`fi-FI_Anneli Niemnien`|
    ||`fi-FI_Kristiina Koskinen`|
    ||`fi-FI_Tapanni Korhonen`|
    ||`fil-PH_Amihan Reyes`|
    ||`fil-PH_Dennis de Saul`|
    ||`fr-BE_Louis Maes`|
    ||`fr-BE_Noah Peeters`|
    ||`fr-CA_Cherise DuPont`|
    ||`fr-CA_Olivier Varane`|
    ||`fr-CA_Raphael Jacques`|
    ||`fr-CH_Luca Dalot`|
    ||`fr-CH_Sylvie Gallace`|
    ||`fr-FR_Alain Hamel`|
    ||`fr-FR_Albertine Dubois`|
    ||`fr-FR_Antoine Petit`|
    ||`fr-FR_Brigitte Richard`|
    ||`fr-FR_Celeste Lefevre`|
    ||`fr-FR_Celine Bundchen`|
    ||`fr-FR_Damian Trezeguet`|
    ||`fr-FR_Diogo Pavard`|
    ||`fr-FR_Francoise LaFont`|
    ||`fr-FR_Gisele Guerin`|
    ||`fr-FR_Hugo Duval`|
    ||`fr-FR_Jacqueline Simon`|
    ||`fr-FR_Lois Allaire`|
    ||`fr-FR_Theo Bernard`|
    ||`ga-IE_Anja O'Brien`|
    ||`ga-IE_Liam Murphy`|
    ||`gl-ES_Clara Campos`|
    ||`gl-ES_Nicolas Montoya`|
    ||`gu-IN_Arzoo Chowdhury`|
    ||`gu-IN_Pramukh Barot`|
    ||`he-IL_Avi Goldmann`|
    ||`he-IL_Yael Haddad`|
    ||`hi-IN_Ashwin Nikhil`|
    ||`hi-IN_Uma Aravind`|
    ||`hr-HR_Krasna Perisic`|
    ||`hr-HR_Luka Horvat`|
    ||`hu-HU_Endre Szabo`|
    ||`hu-HU_Zoe Nagy`|
    ||`hy-AM_Arpi Hovhannisyan`|
    ||`hy-AM_Gor Grigoryan`|
    ||`id-ID_Bagaskoro Ulunjandi`|
    ||`id-ID_Diah Sukatendel`|
    ||`is-IS_Fridrika Sigurdsson`|
    ||`is-IS_Olafur Jonsdottir`|
    ||`it-IT_Alessandro Ferrari`|
    ||`it-IT_Alessia Ricci`|
    ||`it-IT_Allegra Greco`|
    ||`it-IT_Angelo Bianchi`|
    ||`it-IT_Antonio Colombo`|
    ||`it-IT_Eva De Luca`|
    ||`it-IT_Filomena Mancini`|
    ||`it-IT_Francesco Rossi`|
    ||`it-IT_Gaia Marino`|
    ||`it-IT_Gemma Conti`|
    ||`it-IT_Gianluigi Russo`|
    ||`it-IT_Greta Bruno`|
    ||`it-IT_Marco Romano`|
    ||`it-IT_Paul Esposito`|
    ||`it-IT_Serafina Gallo`|
    ||`ja-JP_Ayaka Musashi`|
    ||`ja-JP_Hiromi Tanaka`|
    ||`ja-JP_Hiroshi Maeda`|
    ||`ja-JP_Ichiro Sayaka`|
    ||`ja-JP_Naomi Sora`|
    ||`ja-JP_Sartoshi Juno`|
    ||`ja-JP_Sayuri Watanabe`|
    ||`jv-ID_Anom Zees`|
    ||`jv-ID_Bratawati Pulukadang`|
    ||`ka-GE_Ava Lomidze`|
    ||`ka-GE_Elijah Maisuradze`|
    ||`kk-KZ_Nurislam Omarov`|
    ||`kk-KZ_Rayana Kenes`|
    ||`km-KH_Chanthou Sok`|
    ||`km-KH_Kaliyanei Chea`|
    ||`kn-IN_Aadesh Madar`|
    ||`kn-IN_Rhyah Nayka`|
    ||`ko-KR_Eunjin Bae`|
    ||`ko-KR_Heechul Kim`|
    ||`ko-KR_Isu Choi`|
    ||`ko-KR_Jisoo Han`|
    ||`ko-KR_Meesun Kang`|
    ||`ko-KR_Minjoon Lee`|
    ||`ko-KR_Seung Hee Hwang`|
    ||`ko-KR_Yoosung Park`|
    ||`lo-LA_Lawan Vang`|
    ||`lo-LA_Sengphet Inthavong`|
    ||`lt-LT_Nojus Antanas`|
    ||`lt-LT_Ruta Bagdonas`|
    ||`lv-LV_Mozus Berzina`|
    ||`lv-LV_Santa Ozola`|
    ||`mk-MK_Berislav Stojanovski`|
    ||`mk-MK_Smaragda Jovanovska`|
    ||`ml-IN_Abha Nair`|
    ||`ml-IN_Akhil Kumar`|
    ||`mn-MN_Altan Batbayar`|
    ||`mn-MN_Enkhjargal Ganbold`|
    ||`mr-IN_Mihir Chitre`|
    ||`mr-IN_Vedvika Deo`|
    ||`ms-MY_Nur Tengku`|
    ||`ms-MY_Zikri Wan`|
    ||`mt-MT_Lola Farrugia`|
    ||`mt-MT_Milo Borg`|
    ||`my-MM_Dedan Khin`|
    ||`my-MM_Eindra Aung`|
    ||`nb-NO_Henrik Larsen`|
    ||`nb-NO_Vilde Hansen`|
    ||`nb_NO_Malin Pedersen`|
    ||`ne-NP_Batsal Khadka`|
    ||`ne-NP_Druhi Mahat`|
    ||`nl-BE_Arthur Mertens`|
    ||`nl-BE_Martine Claes`|
    ||`nl-NL_Adriana De Vries`|
    ||`nl-NL_Helena De Jong`|
    ||`nl-NL_Jan Visser`|
    ||`pl-PL_Ewa Grabowski`|
    ||`pl-PL_Piotr Duda`|
    ||`pl-PL_Zuzanna Kackz`|
    ||`ps-AF_Abdul-Alim Sayyid`|
    ||`ps-AF_Zahra Qurban`|
    ||`pt-BR_Adriana Rocha`|
    ||`pt-BR_Ana Bahiense`|
    ||`pt-BR_Anabella Teixeira`|
    ||`pt-BR_Antonia Macedo`|
    ||`pt-BR_Antonio Barros`|
    ||`pt-BR_Fernanda Pedreira`|
    ||`pt-BR_Francisco Guimaraes`|
    ||`pt-BR_Joao Azevedo`|
    ||`pt-BR_Jose Almeida`|
    ||`pt-BR_Juliana Costa`|
    ||`pt-BR_Marcia Ribeiro`|
    ||`pt-BR_Maria Cardoso`|
    ||`pt-BR_Paulo Correia`|
    ||`pt-BR_Pedro Magalhaes`|
    ||`pt-BR_Roberto Braga`|
    ||`pt-PT_Benedita Motta`|
    ||`pt-PT_Renato Matos`|
    ||`pt-PT_Rita Oliveira`|
    ||`ro-RO_Cristian Ionescu`|
    ||`ro-RO_Mirabela Gheata`|
    ||`ru-RU_Galina Ivanov`|
    ||`ru-RU_Nadezhda Smirnoff`|
    ||`ru-RU_Pyotr Semenov`|
    ||`si-LK_Kasun Perera`|
    ||`si-LK_Saanvi de Silva`|
    ||`sk-SK_Havel Varga`|
    ||`sk-SK_Olga Kovac`|
    ||`sl-SI_Neza Mlakar`|
    ||`sl-SI_Nik Krajnc`|
    ||`so-SO_Axado Ibrahim`|
    ||`so-SO_Taifa Mohamed`|
    ||`sq-AL_Bora Marku`|
    ||`sq-AL_Dren Kedare`|
    ||`sr-RS_Lara Markovic`|
    ||`sr-RS_Vlado Popovic`|
    ||`su-ID_Aarifa Bol`|
    ||`su-ID_Mustafa Deng`|
    ||`sv-SE_Agnes Lidstrom`|
    ||`sv-SE_Nicklas Forsberg`|
    ||`sv-SE_Wilma Sundin`|
    ||`sw-KE_Akeyo Njoroge`|
    ||`sw-KE_Chege Odhiambo`|
    ||`sw-TZ_Binti Ramadhani`|
    ||`sw-TZ_Darweshi Ally`|
    ||`ta-IN_Ashwin Kumar`|
    ||`ta-IN_Nila Suresh`|
    ||`ta-LK_Adya Pillai`|
    ||`ta-LK_Prahan Aachari`|
    ||`ta-MY_Aahna Konar`|
    ||`ta-MY_Kethan Nadar`|
    ||`ta-SG_Abilasha Naicker`|
    ||`ta-SG_Nemi Udayar`|
    ||`te-IN_Aarkash Reddy`|
    ||`te-IN_Tanvi Sharma`|
    ||`th-TH_Buppha Prasit`|
    ||`th-TH_Kanchana Sangthong`|
    ||`th-TH_Somchai Thongkham`|
    ||`tr-TR_Emre Ozdemir`|
    ||`tr-TR_Nehir Celik`|
    ||`uk-UA_Artem Shevchenko`|
    ||`uk-UA_Daryna Kovalenko`|
    ||`ur-IN_Farah Abbasi`|
    ||`ur-IN_Sharyar Alvi`|
    ||`ur-PK_Hamza Farooqi`|
    ||`ur-PK_Sana Dhanial`|
    ||`uz-UK_Javlonbek Yusupov`|
    ||`uz-UZ_Rustam Karimova`|
    ||`vi-VN_Huu Duong`|
    ||`vi-VN_Vi Ly`|
    ||`wuu-CN_Muchen Li`|
    ||`wuu-CN_Ruoxi Wang`|
    ||`yue-CN_Ah-lam Lei`|
    ||`yue-CN_Xiaoxiao Wong`|
    ||`zh-CN-henan_Genji Zhou`|
    ||`zh-CN-liaoning_Chu Zhang`|
    ||`zh-CN-shaanxi_Chunhua Lin`|
    ||`zh-CN-shandong_Jiayi Wu`|
    ||`zh-CN-sichuan_Juan Yang`|
    ||`zh-CN_An Liu`|
    ||`zh-CN_Bai Yang`|
    ||`zh-CN_Bao Huang`|
    ||`zh-CN_Chao Zhou`|
    ||`zh-CN_Chen Chen Huo`|
    ||`zh-CN_Cheng Sun`|
    ||`zh-CN_Chichi Wu`|
    ||`zh-CN_Chin Ma`|
    ||`zh-CN_Chun Hu`|
    ||`zh-CN_Cong Zhang`|
    ||`zh-CN_Da Xia Li`|
    ||`zh-CN_Daiyu Zhu`|
    ||`zh-CN_Diu Wang`|
    ||`zh-CN_Huan Luo`|
    ||`zh-CN_Huifen Chen`|
    ||`zh-CN_Huiqing Wang`|
    ||`zh-CN_Meng Li`|
    ||`zh-CN_Xuan Xu`|
    ||`zh-CN_Yifu Wu`|
    ||`zh-CN_Yihan Chen`|
    ||`zh-CN_Yinuo Zhang`|
    ||`zh-HK_Kun Lo`|
    ||`zh-HK_Lanying Lei`|
    ||`zh-HK_Lee Lam`|
    ||`zh-TW_Mingxia Luo`|
    ||`zh-TW_Mingzhu Gao`|
    ||`zh-TW_Susu Song`|
    ||`zu-ZA_Bonginkosi Masina`|
    ||`zu-ZA_Ulwazi Mangede`|

    </details><details><summary>elevenlabs</summary>





    |Name|Value|
    |----|-----|
    |**elevenlabs**|`de-DE_Multilingual_Callum`|
    ||`de-DE_Multilingual_Charlie`|
    ||`de-DE_Multilingual_Charlotte`|
    ||`de-DE_Multilingual_Clyde`|
    ||`de-DE_Multilingual_Daniel`|
    ||`de-DE_Multilingual_Dave`|
    ||`de-DE_Multilingual_Dorothy`|
    ||`de-DE_Multilingual_Emily`|
    ||`de-DE_Multilingual_Ethan`|
    ||`de-DE_Multilingual_Fin`|
    ||`de-DE_Multilingual_Freya`|
    ||`de-DE_Multilingual_Gigi`|
    ||`de-DE_Multilingual_Giovanni`|
    ||`de-DE_Multilingual_Grace`|
    ||`de-DE_Multilingual_Harry`|
    ||`de-DE_Multilingual_James`|
    ||`de-DE_Multilingual_Jeremy`|
    ||`de-DE_Multilingual_Jessie`|
    ||`de-DE_Multilingual_Joseph`|
    ||`de-DE_Multilingual_Liam`|
    ||`de-DE_Multilingual_Matilda`|
    ||`de-DE_Multilingual_Matthew`|
    ||`de-DE_Multilingual_Michael`|
    ||`de-DE_Multilingual_Mimi`|
    ||`de-DE_Multilingual_Nicole`|
    ||`de-DE_Multilingual_Patrick`|
    ||`de-DE_Multilingual_Ryan`|
    ||`de-DE_Multilingual_Serena`|
    ||`de-DE_Multilingual_Thomas`|
    ||`en-AU_Monolingual_Charlie`|
    ||`en-AU_Monolingual_James`|
    ||`en-GB_Monolingual_Daniel`|
    ||`en-GB_Monolingual_Dave`|
    ||`en-GB_Monolingual_Dorothy`|
    ||`en-GB_Monolingual_Joseph`|
    ||`en-GB_Monolingual_Matthew`|
    ||`en-IE_Monolingual_Fin`|
    ||`en-IT_Monolingual_Giovanni`|
    ||`en-SWE_Monolingual_Charlotte`|
    ||`en-SWE_Monolingual_Mimi`|
    ||`en-US_Monolingual_Adam`|
    ||`en-US_Monolingual_Antoni`|
    ||`en-US_Monolingual_Arnold`|
    ||`en-US_Monolingual_Bella`|
    ||`en-US_Monolingual_Callum`|
    ||`en-US_Monolingual_Clyde`|
    ||`en-US_Monolingual_Domi`|
    ||`en-US_Monolingual_Elli`|
    ||`en-US_Monolingual_Emily`|
    ||`en-US_Monolingual_Ethan`|
    ||`en-US_Monolingual_Freya`|
    ||`en-US_Monolingual_Gigi`|
    ||`en-US_Monolingual_Glinda`|
    ||`en-US_Monolingual_Grace`|
    ||`en-US_Monolingual_Harry`|
    ||`en-US_Monolingual_Jeremy`|
    ||`en-US_Monolingual_Jessie`|
    ||`en-US_Monolingual_Josh`|
    ||`en-US_Monolingual_Liam`|
    ||`en-US_Monolingual_Matilda`|
    ||`en-US_Monolingual_Michael`|
    ||`en-US_Monolingual_Nicole`|
    ||`en-US_Monolingual_Patrick`|
    ||`en-US_Monolingual_Rachel`|
    ||`en-US_Monolingual_Ryan`|
    ||`en-US_Monolingual_Sam`|
    ||`en-US_Monolingual_Sarah`|
    ||`en-US_Monolingual_Serena`|
    ||`en-US_Monolingual_Thomas`|
    ||`es-ES_Multilingual_Callum`|
    ||`es-ES_Multilingual_Charlie`|
    ||`es-ES_Multilingual_Charlotte`|
    ||`es-ES_Multilingual_Clyde`|
    ||`es-ES_Multilingual_Daniel`|
    ||`es-ES_Multilingual_Dave`|
    ||`es-ES_Multilingual_Dorothy`|
    ||`es-ES_Multilingual_Emily`|
    ||`es-ES_Multilingual_Ethan`|
    ||`es-ES_Multilingual_Fin`|
    ||`es-ES_Multilingual_Freya`|
    ||`es-ES_Multilingual_Gigi`|
    ||`es-ES_Multilingual_Giovanni`|
    ||`es-ES_Multilingual_Grace`|
    ||`es-ES_Multilingual_James`|
    ||`es-ES_Multilingual_Jeremy`|
    ||`es-ES_Multilingual_Jessie`|
    ||`es-ES_Multilingual_Joseph`|
    ||`es-ES_Multilingual_Liam`|
    ||`es-ES_Multilingual_Matilda`|
    ||`es-ES_Multilingual_Matthew`|
    ||`es-ES_Multilingual_Michael`|
    ||`es-ES_Multilingual_Mimi`|
    ||`es-ES_Multilingual_Nicole`|
    ||`es-ES_Multilingual_Patrick`|
    ||`es-ES_Multilingual_Ryan`|
    ||`es-ES_Multilingual_Serena`|
    ||`es-ES_Multilingual_Thomas`|
    ||`es-US_Multilingual_Harry`|
    ||`fr-FR_Multilingual_Callum`|
    ||`fr-FR_Multilingual_Charlie`|
    ||`fr-FR_Multilingual_Charlotte`|
    ||`fr-FR_Multilingual_Clyde`|
    ||`fr-FR_Multilingual_Daniel`|
    ||`fr-FR_Multilingual_Dave`|
    ||`fr-FR_Multilingual_Dorothy`|
    ||`fr-FR_Multilingual_Emily`|
    ||`fr-FR_Multilingual_Ethan`|
    ||`fr-FR_Multilingual_Fin`|
    ||`fr-FR_Multilingual_Freya`|
    ||`fr-FR_Multilingual_Gigi`|
    ||`fr-FR_Multilingual_Giovanni`|
    ||`fr-FR_Multilingual_Grace`|
    ||`fr-FR_Multilingual_Harry`|
    ||`fr-FR_Multilingual_James`|
    ||`fr-FR_Multilingual_Jeremy`|
    ||`fr-FR_Multilingual_Jessie`|
    ||`fr-FR_Multilingual_Joseph`|
    ||`fr-FR_Multilingual_Liam`|
    ||`fr-FR_Multilingual_Matilda`|
    ||`fr-FR_Multilingual_Matthew`|
    ||`fr-FR_Multilingual_Michael`|
    ||`fr-FR_Multilingual_Mimi`|
    ||`fr-FR_Multilingual_Nicole`|
    ||`fr-FR_Multilingual_Patrick`|
    ||`fr-FR_Multilingual_Ryan`|
    ||`fr-FR_Multilingual_Serena`|
    ||`fr-FR_Multilingual_Thomas`|
    ||`hi-IN_Multilingual_Callum`|
    ||`hi-IN_Multilingual_Charlie`|
    ||`hi-IN_Multilingual_Charlotte`|
    ||`hi-IN_Multilingual_Clyde`|
    ||`hi-IN_Multilingual_Daniel`|
    ||`hi-IN_Multilingual_Dave`|
    ||`hi-IN_Multilingual_Dorothy`|
    ||`hi-IN_Multilingual_Emily`|
    ||`hi-IN_Multilingual_Ethan`|
    ||`hi-IN_Multilingual_Fin`|
    ||`hi-IN_Multilingual_Freya`|
    ||`hi-IN_Multilingual_Gigi`|
    ||`hi-IN_Multilingual_Giovanni`|
    ||`hi-IN_Multilingual_Grace`|
    ||`hi-IN_Multilingual_Harry`|
    ||`hi-IN_Multilingual_James`|
    ||`hi-IN_Multilingual_Jeremy`|
    ||`hi-IN_Multilingual_Jessie`|
    ||`hi-IN_Multilingual_Joseph`|
    ||`hi-IN_Multilingual_Liam`|
    ||`hi-IN_Multilingual_Matilda`|
    ||`hi-IN_Multilingual_Matthew`|
    ||`hi-IN_Multilingual_Michael`|
    ||`hi-IN_Multilingual_Mimi`|
    ||`hi-IN_Multilingual_Nicole`|
    ||`hi-IN_Multilingual_Patrick`|
    ||`hi-IN_Multilingual_Ryan`|
    ||`hi-IN_Multilingual_Serena`|
    ||`hi-IN_Multilingual_Thomas`|
    ||`it-IT_Multilingual_Callum`|
    ||`it-IT_Multilingual_Charlie`|
    ||`it-IT_Multilingual_Charlotte`|
    ||`it-IT_Multilingual_Clyde`|
    ||`it-IT_Multilingual_Daniel`|
    ||`it-IT_Multilingual_Dave`|
    ||`it-IT_Multilingual_Dorothy`|
    ||`it-IT_Multilingual_Emily`|
    ||`it-IT_Multilingual_Ethan`|
    ||`it-IT_Multilingual_Fin`|
    ||`it-IT_Multilingual_Freya`|
    ||`it-IT_Multilingual_Gigi`|
    ||`it-IT_Multilingual_Giovanni`|
    ||`it-IT_Multilingual_Grace`|
    ||`it-IT_Multilingual_Harry`|
    ||`it-IT_Multilingual_James`|
    ||`it-IT_Multilingual_Jeremy`|
    ||`it-IT_Multilingual_Jessie`|
    ||`it-IT_Multilingual_Joseph`|
    ||`it-IT_Multilingual_Liam`|
    ||`it-IT_Multilingual_Matilda`|
    ||`it-IT_Multilingual_Matthew`|
    ||`it-IT_Multilingual_Michael`|
    ||`it-IT_Multilingual_Mimi`|
    ||`it-IT_Multilingual_Nicole`|
    ||`it-IT_Multilingual_Patrick`|
    ||`it-IT_Multilingual_Ryan`|
    ||`it-IT_Multilingual_Serena`|
    ||`it-IT_Multilingual_Thomas`|
    ||`pl-PL_Multilingual_Callum`|
    ||`pl-PL_Multilingual_Charlie`|
    ||`pl-PL_Multilingual_Charlotte`|
    ||`pl-PL_Multilingual_Clyde`|
    ||`pl-PL_Multilingual_Daniel`|
    ||`pl-PL_Multilingual_Dave`|
    ||`pl-PL_Multilingual_Dorothy`|
    ||`pl-PL_Multilingual_Emily`|
    ||`pl-PL_Multilingual_Ethan`|
    ||`pl-PL_Multilingual_Fin`|
    ||`pl-PL_Multilingual_Freya`|
    ||`pl-PL_Multilingual_Gigi`|
    ||`pl-PL_Multilingual_Giovanni`|
    ||`pl-PL_Multilingual_Grace`|
    ||`pl-PL_Multilingual_Harry`|
    ||`pl-PL_Multilingual_James`|
    ||`pl-PL_Multilingual_Jeremy`|
    ||`pl-PL_Multilingual_Jessie`|
    ||`pl-PL_Multilingual_Joseph`|
    ||`pl-PL_Multilingual_Liam`|
    ||`pl-PL_Multilingual_Matilda`|
    ||`pl-PL_Multilingual_Matthew`|
    ||`pl-PL_Multilingual_Michael`|
    ||`pl-PL_Multilingual_Mimi`|
    ||`pl-PL_Multilingual_Nicole`|
    ||`pl-PL_Multilingual_Patrick`|
    ||`pl-PL_Multilingual_Ryan`|
    ||`pl-PL_Multilingual_Serena`|
    ||`pl-PL_Multilingual_Thomas`|
    ||`pt-PT_Multilingual_Callum`|
    ||`pt-PT_Multilingual_Charlie`|
    ||`pt-PT_Multilingual_Charlotte`|
    ||`pt-PT_Multilingual_Clyde`|
    ||`pt-PT_Multilingual_Daniel`|
    ||`pt-PT_Multilingual_Dave`|
    ||`pt-PT_Multilingual_Dorothy`|
    ||`pt-PT_Multilingual_Emily`|
    ||`pt-PT_Multilingual_Ethan`|
    ||`pt-PT_Multilingual_Fin`|
    ||`pt-PT_Multilingual_Freya`|
    ||`pt-PT_Multilingual_Gigi`|
    ||`pt-PT_Multilingual_Giovanni`|
    ||`pt-PT_Multilingual_Grace`|
    ||`pt-PT_Multilingual_Harry`|
    ||`pt-PT_Multilingual_James`|
    ||`pt-PT_Multilingual_Jeremy`|
    ||`pt-PT_Multilingual_Jessie`|
    ||`pt-PT_Multilingual_Joseph`|
    ||`pt-PT_Multilingual_Liam`|
    ||`pt-PT_Multilingual_Matilda`|
    ||`pt-PT_Multilingual_Matthew`|
    ||`pt-PT_Multilingual_Michael`|
    ||`pt-PT_Multilingual_Mimi`|
    ||`pt-PT_Multilingual_Nicole`|
    ||`pt-PT_Multilingual_Patrick`|
    ||`pt-PT_Multilingual_Ryan`|
    ||`pt-PT_Multilingual_Serena`|
    ||`pt-PT_Multilingual_Thomas`|

    </details><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`af_alloy`|
    ||`af_echo`|
    ||`af_fable`|
    ||`af_nova`|
    ||`af_onyx`|
    ||`af_shimmer`|
    ||`ar_alloy`|
    ||`ar_echo`|
    ||`ar_fable`|
    ||`ar_nova`|
    ||`ar_onyx`|
    ||`ar_shimmer`|
    ||`az_alloy`|
    ||`az_echo`|
    ||`az_fable`|
    ||`az_nova`|
    ||`az_onyx`|
    ||`az_shimmer`|
    ||`be_alloy`|
    ||`be_echo`|
    ||`be_fable`|
    ||`be_nova`|
    ||`be_onyx`|
    ||`be_shimmer`|
    ||`bg_alloy`|
    ||`bg_echo`|
    ||`bg_fable`|
    ||`bg_nova`|
    ||`bg_onyx`|
    ||`bg_shimmer`|
    ||`bs_alloy`|
    ||`bs_echo`|
    ||`bs_fable`|
    ||`bs_nova`|
    ||`bs_onyx`|
    ||`bs_shimmer`|
    ||`ca_alloy`|
    ||`ca_echo`|
    ||`ca_fable`|
    ||`ca_nova`|
    ||`ca_onyx`|
    ||`ca_shimmer`|
    ||`cs_alloy`|
    ||`cs_echo`|
    ||`cs_fable`|
    ||`cs_nova`|
    ||`cs_onyx`|
    ||`cs_shimmer`|
    ||`cy_alloy`|
    ||`cy_echo`|
    ||`cy_fable`|
    ||`cy_nova`|
    ||`cy_onyx`|
    ||`cy_shimmer`|
    ||`da_alloy`|
    ||`da_echo`|
    ||`da_fable`|
    ||`da_nova`|
    ||`da_onyx`|
    ||`da_shimmer`|
    ||`de_alloy`|
    ||`de_echo`|
    ||`de_fable`|
    ||`de_nova`|
    ||`de_onyx`|
    ||`de_shimmer`|
    ||`el_alloy`|
    ||`el_echo`|
    ||`el_fable`|
    ||`el_nova`|
    ||`el_onyx`|
    ||`el_shimmer`|
    ||`en_alloy`|
    ||`en_echo`|
    ||`en_fable`|
    ||`en_nova`|
    ||`en_onyx`|
    ||`en_shimmer`|
    ||`es_alloy`|
    ||`es_echo`|
    ||`es_fable`|
    ||`es_nova`|
    ||`es_onyx`|
    ||`es_shimmer`|
    ||`et_alloy`|
    ||`et_echo`|
    ||`et_fable`|
    ||`et_nova`|
    ||`et_onyx`|
    ||`et_shimmer`|
    ||`fa_alloy`|
    ||`fa_echo`|
    ||`fa_fable`|
    ||`fa_nova`|
    ||`fa_onyx`|
    ||`fa_shimmer`|
    ||`fi_alloy`|
    ||`fi_echo`|
    ||`fi_fable`|
    ||`fi_nova`|
    ||`fi_onyx`|
    ||`fi_shimmer`|
    ||`fr_alloy`|
    ||`fr_echo`|
    ||`fr_fable`|
    ||`fr_nova`|
    ||`fr_onyx`|
    ||`fr_shimmer`|
    ||`gl_alloy`|
    ||`gl_echo`|
    ||`gl_fable`|
    ||`gl_nova`|
    ||`gl_onyx`|
    ||`gl_shimmer`|
    ||`he_alloy`|
    ||`he_echo`|
    ||`he_fable`|
    ||`he_nova`|
    ||`he_onyx`|
    ||`he_shimmer`|
    ||`hi_alloy`|
    ||`hi_echo`|
    ||`hi_fable`|
    ||`hi_nova`|
    ||`hi_onyx`|
    ||`hi_shimmer`|
    ||`hr_alloy`|
    ||`hr_echo`|
    ||`hr_fable`|
    ||`hr_nova`|
    ||`hr_onyx`|
    ||`hr_shimmer`|
    ||`hu_alloy`|
    ||`hu_echo`|
    ||`hu_fable`|
    ||`hu_nova`|
    ||`hu_onyx`|
    ||`hu_shimmer`|
    ||`hy_alloy`|
    ||`hy_echo`|
    ||`hy_fable`|
    ||`hy_nova`|
    ||`hy_onyx`|
    ||`hy_shimmer`|
    ||`id_alloy`|
    ||`id_echo`|
    ||`id_fable`|
    ||`id_nova`|
    ||`id_onyx`|
    ||`id_shimmer`|
    ||`is_alloy`|
    ||`is_echo`|
    ||`is_fable`|
    ||`is_nova`|
    ||`is_onyx`|
    ||`is_shimmer`|
    ||`it_alloy`|
    ||`it_echo`|
    ||`it_fable`|
    ||`it_nova`|
    ||`it_onyx`|
    ||`it_shimmer`|
    ||`ja_alloy`|
    ||`ja_echo`|
    ||`ja_fable`|
    ||`ja_nova`|
    ||`ja_onyx`|
    ||`ja_shimmer`|
    ||`kk_alloy`|
    ||`kk_echo`|
    ||`kk_fable`|
    ||`kk_nova`|
    ||`kk_onyx`|
    ||`kk_shimmer`|
    ||`kn_alloy`|
    ||`kn_echo`|
    ||`kn_fable`|
    ||`kn_nova`|
    ||`kn_onyx`|
    ||`kn_shimmer`|
    ||`ko_alloy`|
    ||`ko_echo`|
    ||`ko_fable`|
    ||`ko_nova`|
    ||`ko_onyx`|
    ||`ko_shimmer`|
    ||`lt_alloy`|
    ||`lt_echo`|
    ||`lt_fable`|
    ||`lt_nova`|
    ||`lt_onyx`|
    ||`lt_shimmer`|
    ||`lv_alloy`|
    ||`lv_echo`|
    ||`lv_fable`|
    ||`lv_nova`|
    ||`lv_onyx`|
    ||`lv_shimmer`|
    ||`mi_alloy`|
    ||`mi_echo`|
    ||`mi_fable`|
    ||`mi_nova`|
    ||`mi_onyx`|
    ||`mi_shimmer`|
    ||`mk_alloy`|
    ||`mk_echo`|
    ||`mk_fable`|
    ||`mk_nova`|
    ||`mk_onyx`|
    ||`mk_shimmer`|
    ||`mr_alloy`|
    ||`mr_echo`|
    ||`mr_fable`|
    ||`mr_nova`|
    ||`mr_onyx`|
    ||`mr_shimmer`|
    ||`ms_alloy`|
    ||`ms_echo`|
    ||`ms_fable`|
    ||`ms_nova`|
    ||`ms_onyx`|
    ||`ms_shimmer`|
    ||`ne_alloy`|
    ||`ne_echo`|
    ||`ne_fable`|
    ||`ne_nova`|
    ||`ne_onyx`|
    ||`ne_shimmer`|
    ||`nl_alloy`|
    ||`nl_echo`|
    ||`nl_fable`|
    ||`nl_nova`|
    ||`nl_onyx`|
    ||`nl_shimmer`|
    ||`no_alloy`|
    ||`no_echo`|
    ||`no_fable`|
    ||`no_nova`|
    ||`no_onyx`|
    ||`no_shimmer`|
    ||`pl_alloy`|
    ||`pl_echo`|
    ||`pl_fable`|
    ||`pl_nova`|
    ||`pl_onyx`|
    ||`pl_shimmer`|
    ||`pt_alloy`|
    ||`pt_echo`|
    ||`pt_fable`|
    ||`pt_nova`|
    ||`pt_onyx`|
    ||`pt_shimmer`|
    ||`ro_alloy`|
    ||`ro_echo`|
    ||`ro_fable`|
    ||`ro_nova`|
    ||`ro_onyx`|
    ||`ro_shimmer`|
    ||`ru_alloy`|
    ||`ru_echo`|
    ||`ru_fable`|
    ||`ru_nova`|
    ||`ru_onyx`|
    ||`ru_shimmer`|
    ||`sk_alloy`|
    ||`sk_echo`|
    ||`sk_fable`|
    ||`sk_nova`|
    ||`sk_onyx`|
    ||`sk_shimmer`|
    ||`sl_alloy`|
    ||`sl_echo`|
    ||`sl_fable`|
    ||`sl_nova`|
    ||`sl_onyx`|
    ||`sl_shimmer`|
    ||`sr_alloy`|
    ||`sr_echo`|
    ||`sr_fable`|
    ||`sr_nova`|
    ||`sr_onyx`|
    ||`sr_shimmer`|
    ||`sv_alloy`|
    ||`sv_echo`|
    ||`sv_fable`|
    ||`sv_nova`|
    ||`sv_onyx`|
    ||`sv_shimmer`|
    ||`sw_alloy`|
    ||`sw_echo`|
    ||`sw_fable`|
    ||`sw_nova`|
    ||`sw_onyx`|
    ||`sw_shimmer`|
    ||`ta_alloy`|
    ||`ta_echo`|
    ||`ta_fable`|
    ||`ta_nova`|
    ||`ta_onyx`|
    ||`ta_shimmer`|
    ||`th_alloy`|
    ||`th_echo`|
    ||`th_fable`|
    ||`th_nova`|
    ||`th_onyx`|
    ||`th_shimmer`|
    ||`tl_alloy`|
    ||`tl_echo`|
    ||`tl_fable`|
    ||`tl_nova`|
    ||`tl_onyx`|
    ||`tl_shimmer`|
    ||`tr_alloy`|
    ||`tr_echo`|
    ||`tr_fable`|
    ||`tr_nova`|
    ||`tr_onyx`|
    ||`tr_shimmer`|
    ||`uk_alloy`|
    ||`uk_echo`|
    ||`uk_fable`|
    ||`uk_nova`|
    ||`uk_onyx`|
    ||`uk_shimmer`|
    ||`ur_alloy`|
    ||`ur_echo`|
    ||`ur_fable`|
    ||`ur_nova`|
    ||`ur_onyx`|
    ||`ur_shimmer`|
    ||`vi_alloy`|
    ||`vi_echo`|
    ||`vi_fable`|
    ||`vi_nova`|
    ||`vi_onyx`|
    ||`vi_shimmer`|
    ||`zh_alloy`|
    ||`zh_echo`|
    ||`zh_fable`|
    ||`zh_nova`|
    ||`zh_onyx`|
    ||`zh_shimmer`|

    </details>

    </details>

    Args:
        body (AudiotextToSpeechTextToSpeechRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, NotFoundResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
