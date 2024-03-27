from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.not_found_response import NotFoundResponse
from ...models.translationautomatic_translation_automatic_translation_request import (
    TranslationautomaticTranslationAutomaticTranslationRequest,
)
from ...types import Response


def _get_kwargs(
    *,
    body: TranslationautomaticTranslationAutomaticTranslationRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/translation/automatic_translation",
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
    body: TranslationautomaticTranslationAutomaticTranslationRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Automatic Translation

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|15.0 (per 1000000 char)|1 char
    |**google**|`v3`|20.0 (per 1000000 char)|1 char
    |**ibm**|`v3 (2018-05-01)`|20.0 (per 1000000 char)|1000 char
    |**microsoft**|`v3.0`|10.0 (per 1000000 char)|1 char
    |**neuralspace**|`v1`|7.0 (per 1000 request)|1 request
    |**phedone**|`-`|4.0 (per 1000000 char)|1000 char
    |**deepl**|`v2`|20.0 (per 1000000 char)|1 char
    |**modernmt**|`1.2.8`|8.0 (per 1000000 char)|1 char
    |**openai**|`v1`|20.0 (per 1000000 token)|1 token


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Abkhazian**|`ab`|
    |**Acoli**|`ach`|
    |**Afar**|`aa`|
    |**Afrikaans**|`af`|
    |**Akan**|`ak`|
    |**Albanian**|`sq`|
    |**American Sign Language**|`ase`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Aragonese**|`an`|
    |**Argentine Sign Language**|`aed`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
    |**Avaric**|`av`|
    |**Avestan**|`ae`|
    |**Aymara**|`ay`|
    |**Azerbaijani**|`az`|
    |**Bambara**|`bm`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bemba (Zambia)**|`bem`|
    |**Bengali**|`bn`|
    |**Berber languages**|`ber`|
    |**Bihari languages**|`bh`|
    |**Bislama**|`bi`|
    |**Bosnian**|`bs`|
    |**Brazilian Sign Language**|`bzs`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Celtic languages**|`cel`|
    |**Central Bikol**|`bcl`|
    |**Central Khmer**|`km`|
    |**Chamorro**|`ch`|
    |**Chechen**|`ce`|
    |**Chilean Sign Language**|`csg`|
    |**Chinese**|`zh`|
    |**Church Slavic**|`cu`|
    |**Chuukese**|`chk`|
    |**Chuvash**|`cv`|
    |**Colombian Sign Language**|`csn`|
    |**Congo Swahili**|`swc`|
    |**Cornish**|`kw`|
    |**Corsican**|`co`|
    |**Cree**|`cr`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dari**|`prs`|
    |**Dhivehi**|`dv`|
    |**Dutch**|`nl`|
    |**Dzongkha**|`dz`|
    |**Efik**|`efi`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Ewe**|`ee`|
    |**Faroese**|`fo`|
    |**Fijian**|`fj`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**Finnish Sign Language**|`fse`|
    |**Fon**|`fon`|
    |**French**|`fr`|
    |**Fulah**|`ff`|
    |**Ga**|`gaa`|
    |**Galician**|`gl`|
    |**Ganda**|`lg`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gilbertese**|`gil`|
    |**Guarani**|`gn`|
    |**Gujarati**|`gu`|
    |**Gun**|`guw`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hawaiian**|`haw`|
    |**Hebrew**|`he`|
    |**Herero**|`hz`|
    |**Hiligaynon**|`hil`|
    |**Hindi**|`hi`|
    |**Hiri Motu**|`ho`|
    |**Hmong**|`hmn`|
    |**Hmong Daw**|`mww`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Ido**|`io`|
    |**Igbo**|`ig`|
    |**Iloko**|`ilo`|
    |**Indonesian**|`id`|
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Interlingue**|`ie`|
    |**Inuinnaqtun**|`ikt`|
    |**Inuktitut**|`iu`|
    |**Inupiaq**|`ik`|
    |**Irish**|`ga`|
    |**Isoko**|`iso`|
    |**Isthmus Zapotec**|`zai`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kabyle**|`kab`|
    |**Kalaallisut**|`kl`|
    |**Kannada**|`kn`|
    |**Kanuri**|`kr`|
    |**Kaonde**|`kqn`|
    |**Kashmiri**|`ks`|
    |**Kazakh**|`kk`|
    |**Kikuyu**|`ki`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Klingon**|`tlh`|
    |**Komi**|`kv`|
    |**Kongo**|`kg`|
    |**Korean**|`ko`|
    |**Kuanyama**|`kj`|
    |**Kurdish**|`ku`|
    |**Kwangali**|`kwn`|
    |**Lao**|`lo`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Limburgan**|`li`|
    |**Lingala**|`ln`|
    |**Literary Chinese**|`lzh`|
    |**Lithuanian**|`lt`|
    |**Lozi**|`loz`|
    |**Luba-Katanga**|`lu`|
    |**Luba-Lulua**|`lua`|
    |**Lunda**|`lun`|
    |**Luo (Kenya and Tanzania)**|`luo`|
    |**Lushai**|`lus`|
    |**Luvale**|`lue`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Manx**|`gv`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Marshallese**|`mh`|
    |**Mexican Sign Language**|`mfs`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Morisyen**|`mfe`|
    |**Mossi**|`mos`|
    |**Nauru**|`na`|
    |**Navajo**|`nv`|
    |**Ndonga**|`ng`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Niuean**|`niu`|
    |**North Ndebele**|`nd`|
    |**Northern Kurdish**|`kmr`|
    |**Northern Sami**|`se`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Norwegian Nynorsk**|`nn`|
    |**Nyaneka**|`nyk`|
    |**Nyanja**|`ny`|
    |**Occitan (post 1500)**|`oc`|
    |**Ojibwa**|`oj`|
    |**Oriya (macrolanguage)**|`or`|
    |**Oromo**|`om`|
    |**Ossetian**|`os`|
    |**Pali**|`pi`|
    |**Pangasinan**|`pag`|
    |**Panjabi**|`pa`|
    |**Papiamento**|`pap`|
    |**Pedi**|`nso`|
    |**Persian**|`fa`|
    |**Peruvian Sign Language**|`prl`|
    |**Pijin**|`pis`|
    |**Pohnpeian**|`pon`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Quechua**|`qu`|
    |**Querétaro Otomi**|`otq`|
    |**Romance languages**|`roa`|
    |**Romanian**|`ro`|
    |**Romansh**|`rm`|
    |**Rundi**|`rn`|
    |**Russian**|`ru`|
    |**Ruund**|`rnd`|
    |**Samoan**|`sm`|
    |**San Salvador Kongo**|`kwy`|
    |**Sango**|`sg`|
    |**Sanskrit**|`sa`|
    |**Sardinian**|`sc`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Serbo-Croatian**|`sh`|
    |**Seselwa Creole French**|`crs`|
    |**Shona**|`sn`|
    |**Sichuan Yi**|`ii`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**South Ndebele**|`nr`|
    |**Southern Sotho**|`st`|
    |**Spanish**|`es`|
    |**Spanish Sign Language**|`ssp`|
    |**Sranan Tongo**|`srn`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swati**|`ss`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tahitian**|`ty`|
    |**Tajik**|`tg`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Tetela**|`tll`|
    |**Tetun Dili**|`tdt`|
    |**Thai**|`th`|
    |**Tibetan**|`bo`|
    |**Tigrinya**|`ti`|
    |**Tiv**|`tiv`|
    |**Tok Pisin**|`tpi`|
    |**Tonga (Tonga Islands)**|`to`|
    |**Tonga (Zambia)**|`toi`|
    |**Tsonga**|`ts`|
    |**Tswana**|`tn`|
    |**Tumbuka**|`tum`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Tuvalu**|`tvl`|
    |**Twi**|`tw`|
    |**Tzotzil**|`tzo`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Umbundu**|`umb`|
    |**Upper Sorbian**|`hsb`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Venda**|`ve`|
    |**Venezuelan Sign Language**|`vsl`|
    |**Vietnamese**|`vi`|
    |**Volapük**|`vo`|
    |**Wallisian**|`wls`|
    |**Walloon**|`wa`|
    |**Waray (Philippines)**|`war`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Wolaytta**|`wal`|
    |**Wolof**|`wo`|
    |**Xhosa**|`xh`|
    |**Yapese**|`yap`|
    |**Yiddish**|`yi`|
    |**Yoruba**|`yo`|
    |**Yucateco**|`yua`|
    |**Yue Chinese**|`yue`|
    |**Zande (individual language)**|`zne`|
    |**Zhuang**|`za`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Arabic (Argentina)**|`ar-AR`|
    |**Bangla (Bangladesh)**|`bn-BD`|
    |**Basque (Spain)**|`eu-ES`|
    |**Bosnian (Bosnia & Herzegovina)**|`bs-BA`|
    |**Bulgarian (Bulgaria)**|`bg-BG`|
    |**Catalan (Spain)**|`ca-ES`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Croatian (Croatia)**|`hr-HR`|
    |**Czech (Czechia)**|`cs-CZ`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (United Kingdom)**|`en-GB`|
    |**English (United States)**|`en-US`|
    |**Estonian (Estonia)**|`et-EE`|
    |**Finnish (Finland)**|`fi-FI`|
    |**French (Canada)**|`fr-CA`|
    |**French (France)**|`fr-FR`|
    |**German (Germany)**|`de-DE`|
    |**Greek (Greece)**|`el-GR`|
    |**Gujarati (India)**|`gu-IN`|
    |**Hebrew (Israel)**|`he-IL`|
    |**Hindi (India)**|`hi-IN`|
    |**Hungarian (Hungary)**|`hu-HU`|
    |**Indonesian (Indonesia)**|`id-ID`|
    |**Inuktitut (Latin)**|`iu-Latn`|
    |**Irish (Ireland)**|`ga-IE`|
    |**Italian (Italy)**|`it-IT`|
    |**Japanese (Japan)**|`ja-JP`|
    |**Kannada (India)**|`kn-IN`|
    |**Klingon (Klingon (KLI pIqaD))**|`tlh-Piqd`|
    |**Klingon (Latin)**|`tlh-Latn`|
    |**Korean (South Korea)**|`ko-KR`|
    |**Latvian (Latvia)**|`lv-LV`|
    |**Lithuanian (Lithuania)**|`lt-LT`|
    |**Malay (Malaysia)**|`ms-MY`|
    |**Malayalam (India)**|`ml-IN`|
    |**Maltese (Malta)**|`mt-MT`|
    |**Marathi (India)**|`mr-IN`|
    |**Mongolian (Cyrillic)**|`mn-Cyrl`|
    |**Mongolian (Mongolian)**|`mn-Mong`|
    |**Nepali (Nepal)**|`ne-NP`|
    |**Norwegian Bokmål (Norway)**|`nb-NO`|
    |**Persian (Afghanistan)**|`fa-AF`|
    |**Polish (Poland)**|`pl-PL`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Punjabi (India)**|`pa-IN`|
    |**Romanian (Romania)**|`ro-RO`|
    |**Russian (Russia)**|`ru-RU`|
    |**Serbian (Cyrillic)**|`sr-Cyrl`|
    |**Serbian (Latin)**|`sr-Latn`|
    |**Serbian (Montenegro)**|`sr-ME`|
    |**Serbian (Serbia)**|`sr-RS`|
    |**Sinhala (Sri Lanka)**|`si-LK`|
    |**Slovak (Slovakia)**|`sk-SK`|
    |**Slovenian (Slovenia)**|`sl-SI`|
    |**Spanish (Latin America)**|`es-419`|
    |**Spanish (Mexico)**|`es-MX`|
    |**Spanish (Spain)**|`es-ES`|
    |**Swedish (Sweden)**|`sv-SE`|
    |**Tamil (India)**|`ta-IN`|
    |**Telugu (India)**|`te-IN`|
    |**Thai (Thailand)**|`th-TH`|
    |**Turkish (Turkey)**|`tr-TR`|
    |**Ukrainian (Ukraine)**|`uk-UA`|
    |**Urdu (Pakistan)**|`ur-PK`|
    |**Vietnamese (Vietnam)**|`vi-VN`|
    |**Welsh (United Kingdom)**|`cy-GB`|

    </details>

    Args:
        body (TranslationautomaticTranslationAutomaticTranslationRequest):

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
    body: TranslationautomaticTranslationAutomaticTranslationRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Automatic Translation

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|15.0 (per 1000000 char)|1 char
    |**google**|`v3`|20.0 (per 1000000 char)|1 char
    |**ibm**|`v3 (2018-05-01)`|20.0 (per 1000000 char)|1000 char
    |**microsoft**|`v3.0`|10.0 (per 1000000 char)|1 char
    |**neuralspace**|`v1`|7.0 (per 1000 request)|1 request
    |**phedone**|`-`|4.0 (per 1000000 char)|1000 char
    |**deepl**|`v2`|20.0 (per 1000000 char)|1 char
    |**modernmt**|`1.2.8`|8.0 (per 1000000 char)|1 char
    |**openai**|`v1`|20.0 (per 1000000 token)|1 token


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Abkhazian**|`ab`|
    |**Acoli**|`ach`|
    |**Afar**|`aa`|
    |**Afrikaans**|`af`|
    |**Akan**|`ak`|
    |**Albanian**|`sq`|
    |**American Sign Language**|`ase`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Aragonese**|`an`|
    |**Argentine Sign Language**|`aed`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
    |**Avaric**|`av`|
    |**Avestan**|`ae`|
    |**Aymara**|`ay`|
    |**Azerbaijani**|`az`|
    |**Bambara**|`bm`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bemba (Zambia)**|`bem`|
    |**Bengali**|`bn`|
    |**Berber languages**|`ber`|
    |**Bihari languages**|`bh`|
    |**Bislama**|`bi`|
    |**Bosnian**|`bs`|
    |**Brazilian Sign Language**|`bzs`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Celtic languages**|`cel`|
    |**Central Bikol**|`bcl`|
    |**Central Khmer**|`km`|
    |**Chamorro**|`ch`|
    |**Chechen**|`ce`|
    |**Chilean Sign Language**|`csg`|
    |**Chinese**|`zh`|
    |**Church Slavic**|`cu`|
    |**Chuukese**|`chk`|
    |**Chuvash**|`cv`|
    |**Colombian Sign Language**|`csn`|
    |**Congo Swahili**|`swc`|
    |**Cornish**|`kw`|
    |**Corsican**|`co`|
    |**Cree**|`cr`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dari**|`prs`|
    |**Dhivehi**|`dv`|
    |**Dutch**|`nl`|
    |**Dzongkha**|`dz`|
    |**Efik**|`efi`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Ewe**|`ee`|
    |**Faroese**|`fo`|
    |**Fijian**|`fj`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**Finnish Sign Language**|`fse`|
    |**Fon**|`fon`|
    |**French**|`fr`|
    |**Fulah**|`ff`|
    |**Ga**|`gaa`|
    |**Galician**|`gl`|
    |**Ganda**|`lg`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gilbertese**|`gil`|
    |**Guarani**|`gn`|
    |**Gujarati**|`gu`|
    |**Gun**|`guw`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hawaiian**|`haw`|
    |**Hebrew**|`he`|
    |**Herero**|`hz`|
    |**Hiligaynon**|`hil`|
    |**Hindi**|`hi`|
    |**Hiri Motu**|`ho`|
    |**Hmong**|`hmn`|
    |**Hmong Daw**|`mww`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Ido**|`io`|
    |**Igbo**|`ig`|
    |**Iloko**|`ilo`|
    |**Indonesian**|`id`|
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Interlingue**|`ie`|
    |**Inuinnaqtun**|`ikt`|
    |**Inuktitut**|`iu`|
    |**Inupiaq**|`ik`|
    |**Irish**|`ga`|
    |**Isoko**|`iso`|
    |**Isthmus Zapotec**|`zai`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kabyle**|`kab`|
    |**Kalaallisut**|`kl`|
    |**Kannada**|`kn`|
    |**Kanuri**|`kr`|
    |**Kaonde**|`kqn`|
    |**Kashmiri**|`ks`|
    |**Kazakh**|`kk`|
    |**Kikuyu**|`ki`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Klingon**|`tlh`|
    |**Komi**|`kv`|
    |**Kongo**|`kg`|
    |**Korean**|`ko`|
    |**Kuanyama**|`kj`|
    |**Kurdish**|`ku`|
    |**Kwangali**|`kwn`|
    |**Lao**|`lo`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Limburgan**|`li`|
    |**Lingala**|`ln`|
    |**Literary Chinese**|`lzh`|
    |**Lithuanian**|`lt`|
    |**Lozi**|`loz`|
    |**Luba-Katanga**|`lu`|
    |**Luba-Lulua**|`lua`|
    |**Lunda**|`lun`|
    |**Luo (Kenya and Tanzania)**|`luo`|
    |**Lushai**|`lus`|
    |**Luvale**|`lue`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Manx**|`gv`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Marshallese**|`mh`|
    |**Mexican Sign Language**|`mfs`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Morisyen**|`mfe`|
    |**Mossi**|`mos`|
    |**Nauru**|`na`|
    |**Navajo**|`nv`|
    |**Ndonga**|`ng`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Niuean**|`niu`|
    |**North Ndebele**|`nd`|
    |**Northern Kurdish**|`kmr`|
    |**Northern Sami**|`se`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Norwegian Nynorsk**|`nn`|
    |**Nyaneka**|`nyk`|
    |**Nyanja**|`ny`|
    |**Occitan (post 1500)**|`oc`|
    |**Ojibwa**|`oj`|
    |**Oriya (macrolanguage)**|`or`|
    |**Oromo**|`om`|
    |**Ossetian**|`os`|
    |**Pali**|`pi`|
    |**Pangasinan**|`pag`|
    |**Panjabi**|`pa`|
    |**Papiamento**|`pap`|
    |**Pedi**|`nso`|
    |**Persian**|`fa`|
    |**Peruvian Sign Language**|`prl`|
    |**Pijin**|`pis`|
    |**Pohnpeian**|`pon`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Quechua**|`qu`|
    |**Querétaro Otomi**|`otq`|
    |**Romance languages**|`roa`|
    |**Romanian**|`ro`|
    |**Romansh**|`rm`|
    |**Rundi**|`rn`|
    |**Russian**|`ru`|
    |**Ruund**|`rnd`|
    |**Samoan**|`sm`|
    |**San Salvador Kongo**|`kwy`|
    |**Sango**|`sg`|
    |**Sanskrit**|`sa`|
    |**Sardinian**|`sc`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Serbo-Croatian**|`sh`|
    |**Seselwa Creole French**|`crs`|
    |**Shona**|`sn`|
    |**Sichuan Yi**|`ii`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**South Ndebele**|`nr`|
    |**Southern Sotho**|`st`|
    |**Spanish**|`es`|
    |**Spanish Sign Language**|`ssp`|
    |**Sranan Tongo**|`srn`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swati**|`ss`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tahitian**|`ty`|
    |**Tajik**|`tg`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Tetela**|`tll`|
    |**Tetun Dili**|`tdt`|
    |**Thai**|`th`|
    |**Tibetan**|`bo`|
    |**Tigrinya**|`ti`|
    |**Tiv**|`tiv`|
    |**Tok Pisin**|`tpi`|
    |**Tonga (Tonga Islands)**|`to`|
    |**Tonga (Zambia)**|`toi`|
    |**Tsonga**|`ts`|
    |**Tswana**|`tn`|
    |**Tumbuka**|`tum`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Tuvalu**|`tvl`|
    |**Twi**|`tw`|
    |**Tzotzil**|`tzo`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Umbundu**|`umb`|
    |**Upper Sorbian**|`hsb`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Venda**|`ve`|
    |**Venezuelan Sign Language**|`vsl`|
    |**Vietnamese**|`vi`|
    |**Volapük**|`vo`|
    |**Wallisian**|`wls`|
    |**Walloon**|`wa`|
    |**Waray (Philippines)**|`war`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Wolaytta**|`wal`|
    |**Wolof**|`wo`|
    |**Xhosa**|`xh`|
    |**Yapese**|`yap`|
    |**Yiddish**|`yi`|
    |**Yoruba**|`yo`|
    |**Yucateco**|`yua`|
    |**Yue Chinese**|`yue`|
    |**Zande (individual language)**|`zne`|
    |**Zhuang**|`za`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Arabic (Argentina)**|`ar-AR`|
    |**Bangla (Bangladesh)**|`bn-BD`|
    |**Basque (Spain)**|`eu-ES`|
    |**Bosnian (Bosnia & Herzegovina)**|`bs-BA`|
    |**Bulgarian (Bulgaria)**|`bg-BG`|
    |**Catalan (Spain)**|`ca-ES`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Croatian (Croatia)**|`hr-HR`|
    |**Czech (Czechia)**|`cs-CZ`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (United Kingdom)**|`en-GB`|
    |**English (United States)**|`en-US`|
    |**Estonian (Estonia)**|`et-EE`|
    |**Finnish (Finland)**|`fi-FI`|
    |**French (Canada)**|`fr-CA`|
    |**French (France)**|`fr-FR`|
    |**German (Germany)**|`de-DE`|
    |**Greek (Greece)**|`el-GR`|
    |**Gujarati (India)**|`gu-IN`|
    |**Hebrew (Israel)**|`he-IL`|
    |**Hindi (India)**|`hi-IN`|
    |**Hungarian (Hungary)**|`hu-HU`|
    |**Indonesian (Indonesia)**|`id-ID`|
    |**Inuktitut (Latin)**|`iu-Latn`|
    |**Irish (Ireland)**|`ga-IE`|
    |**Italian (Italy)**|`it-IT`|
    |**Japanese (Japan)**|`ja-JP`|
    |**Kannada (India)**|`kn-IN`|
    |**Klingon (Klingon (KLI pIqaD))**|`tlh-Piqd`|
    |**Klingon (Latin)**|`tlh-Latn`|
    |**Korean (South Korea)**|`ko-KR`|
    |**Latvian (Latvia)**|`lv-LV`|
    |**Lithuanian (Lithuania)**|`lt-LT`|
    |**Malay (Malaysia)**|`ms-MY`|
    |**Malayalam (India)**|`ml-IN`|
    |**Maltese (Malta)**|`mt-MT`|
    |**Marathi (India)**|`mr-IN`|
    |**Mongolian (Cyrillic)**|`mn-Cyrl`|
    |**Mongolian (Mongolian)**|`mn-Mong`|
    |**Nepali (Nepal)**|`ne-NP`|
    |**Norwegian Bokmål (Norway)**|`nb-NO`|
    |**Persian (Afghanistan)**|`fa-AF`|
    |**Polish (Poland)**|`pl-PL`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Punjabi (India)**|`pa-IN`|
    |**Romanian (Romania)**|`ro-RO`|
    |**Russian (Russia)**|`ru-RU`|
    |**Serbian (Cyrillic)**|`sr-Cyrl`|
    |**Serbian (Latin)**|`sr-Latn`|
    |**Serbian (Montenegro)**|`sr-ME`|
    |**Serbian (Serbia)**|`sr-RS`|
    |**Sinhala (Sri Lanka)**|`si-LK`|
    |**Slovak (Slovakia)**|`sk-SK`|
    |**Slovenian (Slovenia)**|`sl-SI`|
    |**Spanish (Latin America)**|`es-419`|
    |**Spanish (Mexico)**|`es-MX`|
    |**Spanish (Spain)**|`es-ES`|
    |**Swedish (Sweden)**|`sv-SE`|
    |**Tamil (India)**|`ta-IN`|
    |**Telugu (India)**|`te-IN`|
    |**Thai (Thailand)**|`th-TH`|
    |**Turkish (Turkey)**|`tr-TR`|
    |**Ukrainian (Ukraine)**|`uk-UA`|
    |**Urdu (Pakistan)**|`ur-PK`|
    |**Vietnamese (Vietnam)**|`vi-VN`|
    |**Welsh (United Kingdom)**|`cy-GB`|

    </details>

    Args:
        body (TranslationautomaticTranslationAutomaticTranslationRequest):

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
    body: TranslationautomaticTranslationAutomaticTranslationRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Automatic Translation

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|15.0 (per 1000000 char)|1 char
    |**google**|`v3`|20.0 (per 1000000 char)|1 char
    |**ibm**|`v3 (2018-05-01)`|20.0 (per 1000000 char)|1000 char
    |**microsoft**|`v3.0`|10.0 (per 1000000 char)|1 char
    |**neuralspace**|`v1`|7.0 (per 1000 request)|1 request
    |**phedone**|`-`|4.0 (per 1000000 char)|1000 char
    |**deepl**|`v2`|20.0 (per 1000000 char)|1 char
    |**modernmt**|`1.2.8`|8.0 (per 1000000 char)|1 char
    |**openai**|`v1`|20.0 (per 1000000 token)|1 token


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Abkhazian**|`ab`|
    |**Acoli**|`ach`|
    |**Afar**|`aa`|
    |**Afrikaans**|`af`|
    |**Akan**|`ak`|
    |**Albanian**|`sq`|
    |**American Sign Language**|`ase`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Aragonese**|`an`|
    |**Argentine Sign Language**|`aed`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
    |**Avaric**|`av`|
    |**Avestan**|`ae`|
    |**Aymara**|`ay`|
    |**Azerbaijani**|`az`|
    |**Bambara**|`bm`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bemba (Zambia)**|`bem`|
    |**Bengali**|`bn`|
    |**Berber languages**|`ber`|
    |**Bihari languages**|`bh`|
    |**Bislama**|`bi`|
    |**Bosnian**|`bs`|
    |**Brazilian Sign Language**|`bzs`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Celtic languages**|`cel`|
    |**Central Bikol**|`bcl`|
    |**Central Khmer**|`km`|
    |**Chamorro**|`ch`|
    |**Chechen**|`ce`|
    |**Chilean Sign Language**|`csg`|
    |**Chinese**|`zh`|
    |**Church Slavic**|`cu`|
    |**Chuukese**|`chk`|
    |**Chuvash**|`cv`|
    |**Colombian Sign Language**|`csn`|
    |**Congo Swahili**|`swc`|
    |**Cornish**|`kw`|
    |**Corsican**|`co`|
    |**Cree**|`cr`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dari**|`prs`|
    |**Dhivehi**|`dv`|
    |**Dutch**|`nl`|
    |**Dzongkha**|`dz`|
    |**Efik**|`efi`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Ewe**|`ee`|
    |**Faroese**|`fo`|
    |**Fijian**|`fj`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**Finnish Sign Language**|`fse`|
    |**Fon**|`fon`|
    |**French**|`fr`|
    |**Fulah**|`ff`|
    |**Ga**|`gaa`|
    |**Galician**|`gl`|
    |**Ganda**|`lg`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gilbertese**|`gil`|
    |**Guarani**|`gn`|
    |**Gujarati**|`gu`|
    |**Gun**|`guw`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hawaiian**|`haw`|
    |**Hebrew**|`he`|
    |**Herero**|`hz`|
    |**Hiligaynon**|`hil`|
    |**Hindi**|`hi`|
    |**Hiri Motu**|`ho`|
    |**Hmong**|`hmn`|
    |**Hmong Daw**|`mww`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Ido**|`io`|
    |**Igbo**|`ig`|
    |**Iloko**|`ilo`|
    |**Indonesian**|`id`|
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Interlingue**|`ie`|
    |**Inuinnaqtun**|`ikt`|
    |**Inuktitut**|`iu`|
    |**Inupiaq**|`ik`|
    |**Irish**|`ga`|
    |**Isoko**|`iso`|
    |**Isthmus Zapotec**|`zai`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kabyle**|`kab`|
    |**Kalaallisut**|`kl`|
    |**Kannada**|`kn`|
    |**Kanuri**|`kr`|
    |**Kaonde**|`kqn`|
    |**Kashmiri**|`ks`|
    |**Kazakh**|`kk`|
    |**Kikuyu**|`ki`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Klingon**|`tlh`|
    |**Komi**|`kv`|
    |**Kongo**|`kg`|
    |**Korean**|`ko`|
    |**Kuanyama**|`kj`|
    |**Kurdish**|`ku`|
    |**Kwangali**|`kwn`|
    |**Lao**|`lo`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Limburgan**|`li`|
    |**Lingala**|`ln`|
    |**Literary Chinese**|`lzh`|
    |**Lithuanian**|`lt`|
    |**Lozi**|`loz`|
    |**Luba-Katanga**|`lu`|
    |**Luba-Lulua**|`lua`|
    |**Lunda**|`lun`|
    |**Luo (Kenya and Tanzania)**|`luo`|
    |**Lushai**|`lus`|
    |**Luvale**|`lue`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Manx**|`gv`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Marshallese**|`mh`|
    |**Mexican Sign Language**|`mfs`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Morisyen**|`mfe`|
    |**Mossi**|`mos`|
    |**Nauru**|`na`|
    |**Navajo**|`nv`|
    |**Ndonga**|`ng`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Niuean**|`niu`|
    |**North Ndebele**|`nd`|
    |**Northern Kurdish**|`kmr`|
    |**Northern Sami**|`se`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Norwegian Nynorsk**|`nn`|
    |**Nyaneka**|`nyk`|
    |**Nyanja**|`ny`|
    |**Occitan (post 1500)**|`oc`|
    |**Ojibwa**|`oj`|
    |**Oriya (macrolanguage)**|`or`|
    |**Oromo**|`om`|
    |**Ossetian**|`os`|
    |**Pali**|`pi`|
    |**Pangasinan**|`pag`|
    |**Panjabi**|`pa`|
    |**Papiamento**|`pap`|
    |**Pedi**|`nso`|
    |**Persian**|`fa`|
    |**Peruvian Sign Language**|`prl`|
    |**Pijin**|`pis`|
    |**Pohnpeian**|`pon`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Quechua**|`qu`|
    |**Querétaro Otomi**|`otq`|
    |**Romance languages**|`roa`|
    |**Romanian**|`ro`|
    |**Romansh**|`rm`|
    |**Rundi**|`rn`|
    |**Russian**|`ru`|
    |**Ruund**|`rnd`|
    |**Samoan**|`sm`|
    |**San Salvador Kongo**|`kwy`|
    |**Sango**|`sg`|
    |**Sanskrit**|`sa`|
    |**Sardinian**|`sc`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Serbo-Croatian**|`sh`|
    |**Seselwa Creole French**|`crs`|
    |**Shona**|`sn`|
    |**Sichuan Yi**|`ii`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**South Ndebele**|`nr`|
    |**Southern Sotho**|`st`|
    |**Spanish**|`es`|
    |**Spanish Sign Language**|`ssp`|
    |**Sranan Tongo**|`srn`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swati**|`ss`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tahitian**|`ty`|
    |**Tajik**|`tg`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Tetela**|`tll`|
    |**Tetun Dili**|`tdt`|
    |**Thai**|`th`|
    |**Tibetan**|`bo`|
    |**Tigrinya**|`ti`|
    |**Tiv**|`tiv`|
    |**Tok Pisin**|`tpi`|
    |**Tonga (Tonga Islands)**|`to`|
    |**Tonga (Zambia)**|`toi`|
    |**Tsonga**|`ts`|
    |**Tswana**|`tn`|
    |**Tumbuka**|`tum`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Tuvalu**|`tvl`|
    |**Twi**|`tw`|
    |**Tzotzil**|`tzo`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Umbundu**|`umb`|
    |**Upper Sorbian**|`hsb`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Venda**|`ve`|
    |**Venezuelan Sign Language**|`vsl`|
    |**Vietnamese**|`vi`|
    |**Volapük**|`vo`|
    |**Wallisian**|`wls`|
    |**Walloon**|`wa`|
    |**Waray (Philippines)**|`war`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Wolaytta**|`wal`|
    |**Wolof**|`wo`|
    |**Xhosa**|`xh`|
    |**Yapese**|`yap`|
    |**Yiddish**|`yi`|
    |**Yoruba**|`yo`|
    |**Yucateco**|`yua`|
    |**Yue Chinese**|`yue`|
    |**Zande (individual language)**|`zne`|
    |**Zhuang**|`za`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Arabic (Argentina)**|`ar-AR`|
    |**Bangla (Bangladesh)**|`bn-BD`|
    |**Basque (Spain)**|`eu-ES`|
    |**Bosnian (Bosnia & Herzegovina)**|`bs-BA`|
    |**Bulgarian (Bulgaria)**|`bg-BG`|
    |**Catalan (Spain)**|`ca-ES`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Croatian (Croatia)**|`hr-HR`|
    |**Czech (Czechia)**|`cs-CZ`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (United Kingdom)**|`en-GB`|
    |**English (United States)**|`en-US`|
    |**Estonian (Estonia)**|`et-EE`|
    |**Finnish (Finland)**|`fi-FI`|
    |**French (Canada)**|`fr-CA`|
    |**French (France)**|`fr-FR`|
    |**German (Germany)**|`de-DE`|
    |**Greek (Greece)**|`el-GR`|
    |**Gujarati (India)**|`gu-IN`|
    |**Hebrew (Israel)**|`he-IL`|
    |**Hindi (India)**|`hi-IN`|
    |**Hungarian (Hungary)**|`hu-HU`|
    |**Indonesian (Indonesia)**|`id-ID`|
    |**Inuktitut (Latin)**|`iu-Latn`|
    |**Irish (Ireland)**|`ga-IE`|
    |**Italian (Italy)**|`it-IT`|
    |**Japanese (Japan)**|`ja-JP`|
    |**Kannada (India)**|`kn-IN`|
    |**Klingon (Klingon (KLI pIqaD))**|`tlh-Piqd`|
    |**Klingon (Latin)**|`tlh-Latn`|
    |**Korean (South Korea)**|`ko-KR`|
    |**Latvian (Latvia)**|`lv-LV`|
    |**Lithuanian (Lithuania)**|`lt-LT`|
    |**Malay (Malaysia)**|`ms-MY`|
    |**Malayalam (India)**|`ml-IN`|
    |**Maltese (Malta)**|`mt-MT`|
    |**Marathi (India)**|`mr-IN`|
    |**Mongolian (Cyrillic)**|`mn-Cyrl`|
    |**Mongolian (Mongolian)**|`mn-Mong`|
    |**Nepali (Nepal)**|`ne-NP`|
    |**Norwegian Bokmål (Norway)**|`nb-NO`|
    |**Persian (Afghanistan)**|`fa-AF`|
    |**Polish (Poland)**|`pl-PL`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Punjabi (India)**|`pa-IN`|
    |**Romanian (Romania)**|`ro-RO`|
    |**Russian (Russia)**|`ru-RU`|
    |**Serbian (Cyrillic)**|`sr-Cyrl`|
    |**Serbian (Latin)**|`sr-Latn`|
    |**Serbian (Montenegro)**|`sr-ME`|
    |**Serbian (Serbia)**|`sr-RS`|
    |**Sinhala (Sri Lanka)**|`si-LK`|
    |**Slovak (Slovakia)**|`sk-SK`|
    |**Slovenian (Slovenia)**|`sl-SI`|
    |**Spanish (Latin America)**|`es-419`|
    |**Spanish (Mexico)**|`es-MX`|
    |**Spanish (Spain)**|`es-ES`|
    |**Swedish (Sweden)**|`sv-SE`|
    |**Tamil (India)**|`ta-IN`|
    |**Telugu (India)**|`te-IN`|
    |**Thai (Thailand)**|`th-TH`|
    |**Turkish (Turkey)**|`tr-TR`|
    |**Ukrainian (Ukraine)**|`uk-UA`|
    |**Urdu (Pakistan)**|`ur-PK`|
    |**Vietnamese (Vietnam)**|`vi-VN`|
    |**Welsh (United Kingdom)**|`cy-GB`|

    </details>

    Args:
        body (TranslationautomaticTranslationAutomaticTranslationRequest):

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
    body: TranslationautomaticTranslationAutomaticTranslationRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Automatic Translation

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|15.0 (per 1000000 char)|1 char
    |**google**|`v3`|20.0 (per 1000000 char)|1 char
    |**ibm**|`v3 (2018-05-01)`|20.0 (per 1000000 char)|1000 char
    |**microsoft**|`v3.0`|10.0 (per 1000000 char)|1 char
    |**neuralspace**|`v1`|7.0 (per 1000 request)|1 request
    |**phedone**|`-`|4.0 (per 1000000 char)|1000 char
    |**deepl**|`v2`|20.0 (per 1000000 char)|1 char
    |**modernmt**|`1.2.8`|8.0 (per 1000000 char)|1 char
    |**openai**|`v1`|20.0 (per 1000000 token)|1 token


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Abkhazian**|`ab`|
    |**Acoli**|`ach`|
    |**Afar**|`aa`|
    |**Afrikaans**|`af`|
    |**Akan**|`ak`|
    |**Albanian**|`sq`|
    |**American Sign Language**|`ase`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Aragonese**|`an`|
    |**Argentine Sign Language**|`aed`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
    |**Avaric**|`av`|
    |**Avestan**|`ae`|
    |**Aymara**|`ay`|
    |**Azerbaijani**|`az`|
    |**Bambara**|`bm`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bemba (Zambia)**|`bem`|
    |**Bengali**|`bn`|
    |**Berber languages**|`ber`|
    |**Bihari languages**|`bh`|
    |**Bislama**|`bi`|
    |**Bosnian**|`bs`|
    |**Brazilian Sign Language**|`bzs`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Celtic languages**|`cel`|
    |**Central Bikol**|`bcl`|
    |**Central Khmer**|`km`|
    |**Chamorro**|`ch`|
    |**Chechen**|`ce`|
    |**Chilean Sign Language**|`csg`|
    |**Chinese**|`zh`|
    |**Church Slavic**|`cu`|
    |**Chuukese**|`chk`|
    |**Chuvash**|`cv`|
    |**Colombian Sign Language**|`csn`|
    |**Congo Swahili**|`swc`|
    |**Cornish**|`kw`|
    |**Corsican**|`co`|
    |**Cree**|`cr`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dari**|`prs`|
    |**Dhivehi**|`dv`|
    |**Dutch**|`nl`|
    |**Dzongkha**|`dz`|
    |**Efik**|`efi`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Ewe**|`ee`|
    |**Faroese**|`fo`|
    |**Fijian**|`fj`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**Finnish Sign Language**|`fse`|
    |**Fon**|`fon`|
    |**French**|`fr`|
    |**Fulah**|`ff`|
    |**Ga**|`gaa`|
    |**Galician**|`gl`|
    |**Ganda**|`lg`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gilbertese**|`gil`|
    |**Guarani**|`gn`|
    |**Gujarati**|`gu`|
    |**Gun**|`guw`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hawaiian**|`haw`|
    |**Hebrew**|`he`|
    |**Herero**|`hz`|
    |**Hiligaynon**|`hil`|
    |**Hindi**|`hi`|
    |**Hiri Motu**|`ho`|
    |**Hmong**|`hmn`|
    |**Hmong Daw**|`mww`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Ido**|`io`|
    |**Igbo**|`ig`|
    |**Iloko**|`ilo`|
    |**Indonesian**|`id`|
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Interlingue**|`ie`|
    |**Inuinnaqtun**|`ikt`|
    |**Inuktitut**|`iu`|
    |**Inupiaq**|`ik`|
    |**Irish**|`ga`|
    |**Isoko**|`iso`|
    |**Isthmus Zapotec**|`zai`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kabyle**|`kab`|
    |**Kalaallisut**|`kl`|
    |**Kannada**|`kn`|
    |**Kanuri**|`kr`|
    |**Kaonde**|`kqn`|
    |**Kashmiri**|`ks`|
    |**Kazakh**|`kk`|
    |**Kikuyu**|`ki`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Klingon**|`tlh`|
    |**Komi**|`kv`|
    |**Kongo**|`kg`|
    |**Korean**|`ko`|
    |**Kuanyama**|`kj`|
    |**Kurdish**|`ku`|
    |**Kwangali**|`kwn`|
    |**Lao**|`lo`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Limburgan**|`li`|
    |**Lingala**|`ln`|
    |**Literary Chinese**|`lzh`|
    |**Lithuanian**|`lt`|
    |**Lozi**|`loz`|
    |**Luba-Katanga**|`lu`|
    |**Luba-Lulua**|`lua`|
    |**Lunda**|`lun`|
    |**Luo (Kenya and Tanzania)**|`luo`|
    |**Lushai**|`lus`|
    |**Luvale**|`lue`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Manx**|`gv`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Marshallese**|`mh`|
    |**Mexican Sign Language**|`mfs`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Morisyen**|`mfe`|
    |**Mossi**|`mos`|
    |**Nauru**|`na`|
    |**Navajo**|`nv`|
    |**Ndonga**|`ng`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Niuean**|`niu`|
    |**North Ndebele**|`nd`|
    |**Northern Kurdish**|`kmr`|
    |**Northern Sami**|`se`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Norwegian Nynorsk**|`nn`|
    |**Nyaneka**|`nyk`|
    |**Nyanja**|`ny`|
    |**Occitan (post 1500)**|`oc`|
    |**Ojibwa**|`oj`|
    |**Oriya (macrolanguage)**|`or`|
    |**Oromo**|`om`|
    |**Ossetian**|`os`|
    |**Pali**|`pi`|
    |**Pangasinan**|`pag`|
    |**Panjabi**|`pa`|
    |**Papiamento**|`pap`|
    |**Pedi**|`nso`|
    |**Persian**|`fa`|
    |**Peruvian Sign Language**|`prl`|
    |**Pijin**|`pis`|
    |**Pohnpeian**|`pon`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Quechua**|`qu`|
    |**Querétaro Otomi**|`otq`|
    |**Romance languages**|`roa`|
    |**Romanian**|`ro`|
    |**Romansh**|`rm`|
    |**Rundi**|`rn`|
    |**Russian**|`ru`|
    |**Ruund**|`rnd`|
    |**Samoan**|`sm`|
    |**San Salvador Kongo**|`kwy`|
    |**Sango**|`sg`|
    |**Sanskrit**|`sa`|
    |**Sardinian**|`sc`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Serbo-Croatian**|`sh`|
    |**Seselwa Creole French**|`crs`|
    |**Shona**|`sn`|
    |**Sichuan Yi**|`ii`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**South Ndebele**|`nr`|
    |**Southern Sotho**|`st`|
    |**Spanish**|`es`|
    |**Spanish Sign Language**|`ssp`|
    |**Sranan Tongo**|`srn`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swati**|`ss`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tahitian**|`ty`|
    |**Tajik**|`tg`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Tetela**|`tll`|
    |**Tetun Dili**|`tdt`|
    |**Thai**|`th`|
    |**Tibetan**|`bo`|
    |**Tigrinya**|`ti`|
    |**Tiv**|`tiv`|
    |**Tok Pisin**|`tpi`|
    |**Tonga (Tonga Islands)**|`to`|
    |**Tonga (Zambia)**|`toi`|
    |**Tsonga**|`ts`|
    |**Tswana**|`tn`|
    |**Tumbuka**|`tum`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Tuvalu**|`tvl`|
    |**Twi**|`tw`|
    |**Tzotzil**|`tzo`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Umbundu**|`umb`|
    |**Upper Sorbian**|`hsb`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Venda**|`ve`|
    |**Venezuelan Sign Language**|`vsl`|
    |**Vietnamese**|`vi`|
    |**Volapük**|`vo`|
    |**Wallisian**|`wls`|
    |**Walloon**|`wa`|
    |**Waray (Philippines)**|`war`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Wolaytta**|`wal`|
    |**Wolof**|`wo`|
    |**Xhosa**|`xh`|
    |**Yapese**|`yap`|
    |**Yiddish**|`yi`|
    |**Yoruba**|`yo`|
    |**Yucateco**|`yua`|
    |**Yue Chinese**|`yue`|
    |**Zande (individual language)**|`zne`|
    |**Zhuang**|`za`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Arabic (Argentina)**|`ar-AR`|
    |**Bangla (Bangladesh)**|`bn-BD`|
    |**Basque (Spain)**|`eu-ES`|
    |**Bosnian (Bosnia & Herzegovina)**|`bs-BA`|
    |**Bulgarian (Bulgaria)**|`bg-BG`|
    |**Catalan (Spain)**|`ca-ES`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Croatian (Croatia)**|`hr-HR`|
    |**Czech (Czechia)**|`cs-CZ`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (United Kingdom)**|`en-GB`|
    |**English (United States)**|`en-US`|
    |**Estonian (Estonia)**|`et-EE`|
    |**Finnish (Finland)**|`fi-FI`|
    |**French (Canada)**|`fr-CA`|
    |**French (France)**|`fr-FR`|
    |**German (Germany)**|`de-DE`|
    |**Greek (Greece)**|`el-GR`|
    |**Gujarati (India)**|`gu-IN`|
    |**Hebrew (Israel)**|`he-IL`|
    |**Hindi (India)**|`hi-IN`|
    |**Hungarian (Hungary)**|`hu-HU`|
    |**Indonesian (Indonesia)**|`id-ID`|
    |**Inuktitut (Latin)**|`iu-Latn`|
    |**Irish (Ireland)**|`ga-IE`|
    |**Italian (Italy)**|`it-IT`|
    |**Japanese (Japan)**|`ja-JP`|
    |**Kannada (India)**|`kn-IN`|
    |**Klingon (Klingon (KLI pIqaD))**|`tlh-Piqd`|
    |**Klingon (Latin)**|`tlh-Latn`|
    |**Korean (South Korea)**|`ko-KR`|
    |**Latvian (Latvia)**|`lv-LV`|
    |**Lithuanian (Lithuania)**|`lt-LT`|
    |**Malay (Malaysia)**|`ms-MY`|
    |**Malayalam (India)**|`ml-IN`|
    |**Maltese (Malta)**|`mt-MT`|
    |**Marathi (India)**|`mr-IN`|
    |**Mongolian (Cyrillic)**|`mn-Cyrl`|
    |**Mongolian (Mongolian)**|`mn-Mong`|
    |**Nepali (Nepal)**|`ne-NP`|
    |**Norwegian Bokmål (Norway)**|`nb-NO`|
    |**Persian (Afghanistan)**|`fa-AF`|
    |**Polish (Poland)**|`pl-PL`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Punjabi (India)**|`pa-IN`|
    |**Romanian (Romania)**|`ro-RO`|
    |**Russian (Russia)**|`ru-RU`|
    |**Serbian (Cyrillic)**|`sr-Cyrl`|
    |**Serbian (Latin)**|`sr-Latn`|
    |**Serbian (Montenegro)**|`sr-ME`|
    |**Serbian (Serbia)**|`sr-RS`|
    |**Sinhala (Sri Lanka)**|`si-LK`|
    |**Slovak (Slovakia)**|`sk-SK`|
    |**Slovenian (Slovenia)**|`sl-SI`|
    |**Spanish (Latin America)**|`es-419`|
    |**Spanish (Mexico)**|`es-MX`|
    |**Spanish (Spain)**|`es-ES`|
    |**Swedish (Sweden)**|`sv-SE`|
    |**Tamil (India)**|`ta-IN`|
    |**Telugu (India)**|`te-IN`|
    |**Thai (Thailand)**|`th-TH`|
    |**Turkish (Turkey)**|`tr-TR`|
    |**Ukrainian (Ukraine)**|`uk-UA`|
    |**Urdu (Pakistan)**|`ur-PK`|
    |**Vietnamese (Vietnam)**|`vi-VN`|
    |**Welsh (United Kingdom)**|`cy-GB`|

    </details>

    Args:
        body (TranslationautomaticTranslationAutomaticTranslationRequest):

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
