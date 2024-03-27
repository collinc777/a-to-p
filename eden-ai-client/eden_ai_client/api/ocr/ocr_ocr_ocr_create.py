from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.not_found_response import NotFoundResponse
from ...models.ocrocr_ocr_request import OcrocrOcrRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        OcrocrOcrRequest,
        OcrocrOcrRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/ocr/ocr",
    }

    if isinstance(body, OcrocrOcrRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, OcrocrOcrRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

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
    body: Union[
        OcrocrOcrRequest,
        OcrocrOcrRequest,
    ],
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """OCR

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|1.5 (per 1000 page)|1 page
    |**clarifai**|`8.0.0`|2.0 (per 1000 page)|1 page
    |**google**|`v1`|1.5 (per 1000 page)|1 page
    |**microsoft**|`v3.2`|1.0 (per 1000 page)|1 page
    |**sentisight**|`v3.3.1`|1.0 (per 1000 file)|1 file
    |**api4ai**|`v1.0.0`|3.0 (per 1000 request)|1 request


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Abaza**|`abq`|
    |**Adyghe**|`ady`|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Angika**|`anp`|
    |**Arabic**|`ar`|
    |**Assamese**|`as`|
    |**Asturian**|`ast`|
    |**Avaric**|`av`|
    |**Awadhi**|`awa`|
    |**Azerbaijani**|`az`|
    |**Bagheli**|`bfy`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bengali**|`bn`|
    |**Bhojpuri**|`bho`|
    |**Bihari languages**|`bh`|
    |**Bislama**|`bi`|
    |**Bodo (India)**|`brx`|
    |**Bosnian**|`bs`|
    |**Braj**|`bra`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Bundeli**|`bns`|
    |**Buriat**|`bua`|
    |**Camling**|`rab`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Chamorro**|`ch`|
    |**Chechen**|`ce`|
    |**Chhattisgarhi**|`hne`|
    |**Chinese**|`zh`|
    |**Cornish**|`kw`|
    |**Corsican**|`co`|
    |**Crimean Tatar**|`crh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dargwa**|`dar`|
    |**Dari**|`prs`|
    |**Dhimal**|`dhi`|
    |**Dogri (macrolanguage)**|`doi`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Erzya**|`myv`|
    |**Estonian**|`et`|
    |**Faroese**|`fo`|
    |**Fijian**|`fj`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Friulian**|`fur`|
    |**Gagauz**|`gag`|
    |**Galician**|`gl`|
    |**German**|`de`|
    |**Gilbertese**|`gil`|
    |**Goan Konkani**|`gom`|
    |**Gondi**|`gon`|
    |**Gurung**|`gvr`|
    |**Haitian**|`ht`|
    |**Halbi**|`hlb`|
    |**Hani**|`hni`|
    |**Haryanvi**|`bgc`|
    |**Hawaiian**|`haw`|
    |**Hindi**|`hi`|
    |**Hmong Daw**|`mww`|
    |**Ho**|`hoc`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Inari Sami**|`smn`|
    |**Indonesian**|`id`|
    |**Ingush**|`inh`|
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Inuktitut**|`iu`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Jaunsari**|`jns`|
    |**Javanese**|`jv`|
    |**K'iche'**|`quc`|
    |**Kabardian**|`kbd`|
    |**Kabuverdianu**|`kea`|
    |**Kachin**|`kac`|
    |**Kalaallisut**|`kl`|
    |**Kangri**|`xnr`|
    |**Kara-Kalpak**|`kaa`|
    |**Karachay-Balkar**|`krc`|
    |**Kashubian**|`csb`|
    |**Kazakh**|`kk`|
    |**Khaling**|`klr`|
    |**Khasi**|`kha`|
    |**Kirghiz**|`ky`|
    |**Korean**|`ko`|
    |**Korku**|`kfq`|
    |**Koryak**|`kpy`|
    |**Kosraean**|`kos`|
    |**Kumarbhag Paharia**|`kmj`|
    |**Kumyk**|`kum`|
    |**Kurdish**|`ku`|
    |**Kurukh**|`kru`|
    |**Kölsch**|`ksh`|
    |**Lak**|`lbe`|
    |**Lakota**|`lkt`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lezghian**|`lez`|
    |**Lithuanian**|`lt`|
    |**Lower Sorbian**|`dsb`|
    |**Lule Sami**|`smj`|
    |**Luxembourgish**|`lb`|
    |**Mahasu Pahari**|`bfz`|
    |**Maithili**|`mai`|
    |**Malay (macrolanguage)**|`ms`|
    |**Maltese**|`mt`|
    |**Manx**|`gv`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Marshallese**|`mh`|
    |**Mongolian**|`mn`|
    |**Neapolitan**|`nap`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Newari**|`new`|
    |**Niuean**|`niu`|
    |**Nogai**|`nog`|
    |**Northern Sami**|`se`|
    |**Norwegian**|`no`|
    |**Occitan (post 1500)**|`oc`|
    |**Old English (ca. 450-1100)**|`ang`|
    |**Ossetian**|`os`|
    |**Pali**|`pi`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Romanian**|`ro`|
    |**Romansh**|`rm`|
    |**Russian**|`ru`|
    |**Sadri**|`sck`|
    |**Samoan**|`sm`|
    |**Sanskrit**|`sa`|
    |**Santali**|`sat`|
    |**Scots**|`sco`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Sherpa**|`xsr`|
    |**Sirmauri**|`srx`|
    |**Skolt Sami**|`sms`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**Southern Sami**|`sma`|
    |**Spanish**|`es`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tabassaran**|`tab`|
    |**Tagalog**|`tl`|
    |**Tajik**|`tg`|
    |**Tatar**|`tt`|
    |**Tetum**|`tet`|
    |**Thangmi**|`thf`|
    |**Tonga (Tonga Islands)**|`to`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Tuvinian**|`tyv`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Upper Sorbian**|`hsb`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Volapük**|`vo`|
    |**Walser**|`wae`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Yucateco**|`yua`|
    |**Zhuang**|`za`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Arabic (Pseudo-Accents)**|`ar-XA`|
    |**Belarusian**|`be-cyrl`|
    |**Belarusian (Latin)**|`be-latn`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (United States)**|`en-US`|
    |**Finnish (Finland)**|`fi-FI`|
    |**French (France)**|`fr-FR`|
    |**German (Germany)**|`de-DE`|
    |**Hungarian (Hungary)**|`hu-HU`|
    |**Italian (Italy)**|`it-IT`|
    |**Japanese (Japan)**|`ja-JP`|
    |**Kara-Kalpak (Cyrillic)**|`kaa-Cyrl`|
    |**Kazakh**|`kk-cyrl`|
    |**Kazakh (Latin)**|`kk-latn`|
    |**Korean (South Korea)**|`ko-KR`|
    |**Kurdish (Arabic)**|`ku-arab`|
    |**Kurdish (Latin)**|`ku-latn`|
    |**Polish**|`pl-PO`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Region: Czechia**|`cz-CZ`|
    |**Region: Greece**|`gr-GR`|
    |**Russian (Russia)**|`ru-RU`|
    |**Serbian (Cyrillic, Montenegro)**|`sr-Cyrl-ME`|
    |**Serbian (Latin)**|`sr-latn`|
    |**Serbian (Latin, Montenegro)**|`sr-Latn-ME`|
    |**Serbian (Montenegro)**|`sr-ME`|
    |**Spanish (Spain)**|`es-ES`|
    |**Swedish (Sweden)**|`sv-SE`|
    |**Turkish (Turkey)**|`tr-TR`|
    |**Uzbek (Arabic)**|`uz-arab`|
    |**Uzbek (Cyrillic)**|`uz-cyrl`|

    </details>

    Args:
        body (OcrocrOcrRequest):
        body (OcrocrOcrRequest):

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
    body: Union[
        OcrocrOcrRequest,
        OcrocrOcrRequest,
    ],
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """OCR

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|1.5 (per 1000 page)|1 page
    |**clarifai**|`8.0.0`|2.0 (per 1000 page)|1 page
    |**google**|`v1`|1.5 (per 1000 page)|1 page
    |**microsoft**|`v3.2`|1.0 (per 1000 page)|1 page
    |**sentisight**|`v3.3.1`|1.0 (per 1000 file)|1 file
    |**api4ai**|`v1.0.0`|3.0 (per 1000 request)|1 request


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Abaza**|`abq`|
    |**Adyghe**|`ady`|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Angika**|`anp`|
    |**Arabic**|`ar`|
    |**Assamese**|`as`|
    |**Asturian**|`ast`|
    |**Avaric**|`av`|
    |**Awadhi**|`awa`|
    |**Azerbaijani**|`az`|
    |**Bagheli**|`bfy`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bengali**|`bn`|
    |**Bhojpuri**|`bho`|
    |**Bihari languages**|`bh`|
    |**Bislama**|`bi`|
    |**Bodo (India)**|`brx`|
    |**Bosnian**|`bs`|
    |**Braj**|`bra`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Bundeli**|`bns`|
    |**Buriat**|`bua`|
    |**Camling**|`rab`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Chamorro**|`ch`|
    |**Chechen**|`ce`|
    |**Chhattisgarhi**|`hne`|
    |**Chinese**|`zh`|
    |**Cornish**|`kw`|
    |**Corsican**|`co`|
    |**Crimean Tatar**|`crh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dargwa**|`dar`|
    |**Dari**|`prs`|
    |**Dhimal**|`dhi`|
    |**Dogri (macrolanguage)**|`doi`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Erzya**|`myv`|
    |**Estonian**|`et`|
    |**Faroese**|`fo`|
    |**Fijian**|`fj`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Friulian**|`fur`|
    |**Gagauz**|`gag`|
    |**Galician**|`gl`|
    |**German**|`de`|
    |**Gilbertese**|`gil`|
    |**Goan Konkani**|`gom`|
    |**Gondi**|`gon`|
    |**Gurung**|`gvr`|
    |**Haitian**|`ht`|
    |**Halbi**|`hlb`|
    |**Hani**|`hni`|
    |**Haryanvi**|`bgc`|
    |**Hawaiian**|`haw`|
    |**Hindi**|`hi`|
    |**Hmong Daw**|`mww`|
    |**Ho**|`hoc`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Inari Sami**|`smn`|
    |**Indonesian**|`id`|
    |**Ingush**|`inh`|
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Inuktitut**|`iu`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Jaunsari**|`jns`|
    |**Javanese**|`jv`|
    |**K'iche'**|`quc`|
    |**Kabardian**|`kbd`|
    |**Kabuverdianu**|`kea`|
    |**Kachin**|`kac`|
    |**Kalaallisut**|`kl`|
    |**Kangri**|`xnr`|
    |**Kara-Kalpak**|`kaa`|
    |**Karachay-Balkar**|`krc`|
    |**Kashubian**|`csb`|
    |**Kazakh**|`kk`|
    |**Khaling**|`klr`|
    |**Khasi**|`kha`|
    |**Kirghiz**|`ky`|
    |**Korean**|`ko`|
    |**Korku**|`kfq`|
    |**Koryak**|`kpy`|
    |**Kosraean**|`kos`|
    |**Kumarbhag Paharia**|`kmj`|
    |**Kumyk**|`kum`|
    |**Kurdish**|`ku`|
    |**Kurukh**|`kru`|
    |**Kölsch**|`ksh`|
    |**Lak**|`lbe`|
    |**Lakota**|`lkt`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lezghian**|`lez`|
    |**Lithuanian**|`lt`|
    |**Lower Sorbian**|`dsb`|
    |**Lule Sami**|`smj`|
    |**Luxembourgish**|`lb`|
    |**Mahasu Pahari**|`bfz`|
    |**Maithili**|`mai`|
    |**Malay (macrolanguage)**|`ms`|
    |**Maltese**|`mt`|
    |**Manx**|`gv`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Marshallese**|`mh`|
    |**Mongolian**|`mn`|
    |**Neapolitan**|`nap`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Newari**|`new`|
    |**Niuean**|`niu`|
    |**Nogai**|`nog`|
    |**Northern Sami**|`se`|
    |**Norwegian**|`no`|
    |**Occitan (post 1500)**|`oc`|
    |**Old English (ca. 450-1100)**|`ang`|
    |**Ossetian**|`os`|
    |**Pali**|`pi`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Romanian**|`ro`|
    |**Romansh**|`rm`|
    |**Russian**|`ru`|
    |**Sadri**|`sck`|
    |**Samoan**|`sm`|
    |**Sanskrit**|`sa`|
    |**Santali**|`sat`|
    |**Scots**|`sco`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Sherpa**|`xsr`|
    |**Sirmauri**|`srx`|
    |**Skolt Sami**|`sms`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**Southern Sami**|`sma`|
    |**Spanish**|`es`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tabassaran**|`tab`|
    |**Tagalog**|`tl`|
    |**Tajik**|`tg`|
    |**Tatar**|`tt`|
    |**Tetum**|`tet`|
    |**Thangmi**|`thf`|
    |**Tonga (Tonga Islands)**|`to`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Tuvinian**|`tyv`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Upper Sorbian**|`hsb`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Volapük**|`vo`|
    |**Walser**|`wae`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Yucateco**|`yua`|
    |**Zhuang**|`za`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Arabic (Pseudo-Accents)**|`ar-XA`|
    |**Belarusian**|`be-cyrl`|
    |**Belarusian (Latin)**|`be-latn`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (United States)**|`en-US`|
    |**Finnish (Finland)**|`fi-FI`|
    |**French (France)**|`fr-FR`|
    |**German (Germany)**|`de-DE`|
    |**Hungarian (Hungary)**|`hu-HU`|
    |**Italian (Italy)**|`it-IT`|
    |**Japanese (Japan)**|`ja-JP`|
    |**Kara-Kalpak (Cyrillic)**|`kaa-Cyrl`|
    |**Kazakh**|`kk-cyrl`|
    |**Kazakh (Latin)**|`kk-latn`|
    |**Korean (South Korea)**|`ko-KR`|
    |**Kurdish (Arabic)**|`ku-arab`|
    |**Kurdish (Latin)**|`ku-latn`|
    |**Polish**|`pl-PO`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Region: Czechia**|`cz-CZ`|
    |**Region: Greece**|`gr-GR`|
    |**Russian (Russia)**|`ru-RU`|
    |**Serbian (Cyrillic, Montenegro)**|`sr-Cyrl-ME`|
    |**Serbian (Latin)**|`sr-latn`|
    |**Serbian (Latin, Montenegro)**|`sr-Latn-ME`|
    |**Serbian (Montenegro)**|`sr-ME`|
    |**Spanish (Spain)**|`es-ES`|
    |**Swedish (Sweden)**|`sv-SE`|
    |**Turkish (Turkey)**|`tr-TR`|
    |**Uzbek (Arabic)**|`uz-arab`|
    |**Uzbek (Cyrillic)**|`uz-cyrl`|

    </details>

    Args:
        body (OcrocrOcrRequest):
        body (OcrocrOcrRequest):

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
    body: Union[
        OcrocrOcrRequest,
        OcrocrOcrRequest,
    ],
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """OCR

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|1.5 (per 1000 page)|1 page
    |**clarifai**|`8.0.0`|2.0 (per 1000 page)|1 page
    |**google**|`v1`|1.5 (per 1000 page)|1 page
    |**microsoft**|`v3.2`|1.0 (per 1000 page)|1 page
    |**sentisight**|`v3.3.1`|1.0 (per 1000 file)|1 file
    |**api4ai**|`v1.0.0`|3.0 (per 1000 request)|1 request


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Abaza**|`abq`|
    |**Adyghe**|`ady`|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Angika**|`anp`|
    |**Arabic**|`ar`|
    |**Assamese**|`as`|
    |**Asturian**|`ast`|
    |**Avaric**|`av`|
    |**Awadhi**|`awa`|
    |**Azerbaijani**|`az`|
    |**Bagheli**|`bfy`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bengali**|`bn`|
    |**Bhojpuri**|`bho`|
    |**Bihari languages**|`bh`|
    |**Bislama**|`bi`|
    |**Bodo (India)**|`brx`|
    |**Bosnian**|`bs`|
    |**Braj**|`bra`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Bundeli**|`bns`|
    |**Buriat**|`bua`|
    |**Camling**|`rab`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Chamorro**|`ch`|
    |**Chechen**|`ce`|
    |**Chhattisgarhi**|`hne`|
    |**Chinese**|`zh`|
    |**Cornish**|`kw`|
    |**Corsican**|`co`|
    |**Crimean Tatar**|`crh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dargwa**|`dar`|
    |**Dari**|`prs`|
    |**Dhimal**|`dhi`|
    |**Dogri (macrolanguage)**|`doi`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Erzya**|`myv`|
    |**Estonian**|`et`|
    |**Faroese**|`fo`|
    |**Fijian**|`fj`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Friulian**|`fur`|
    |**Gagauz**|`gag`|
    |**Galician**|`gl`|
    |**German**|`de`|
    |**Gilbertese**|`gil`|
    |**Goan Konkani**|`gom`|
    |**Gondi**|`gon`|
    |**Gurung**|`gvr`|
    |**Haitian**|`ht`|
    |**Halbi**|`hlb`|
    |**Hani**|`hni`|
    |**Haryanvi**|`bgc`|
    |**Hawaiian**|`haw`|
    |**Hindi**|`hi`|
    |**Hmong Daw**|`mww`|
    |**Ho**|`hoc`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Inari Sami**|`smn`|
    |**Indonesian**|`id`|
    |**Ingush**|`inh`|
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Inuktitut**|`iu`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Jaunsari**|`jns`|
    |**Javanese**|`jv`|
    |**K'iche'**|`quc`|
    |**Kabardian**|`kbd`|
    |**Kabuverdianu**|`kea`|
    |**Kachin**|`kac`|
    |**Kalaallisut**|`kl`|
    |**Kangri**|`xnr`|
    |**Kara-Kalpak**|`kaa`|
    |**Karachay-Balkar**|`krc`|
    |**Kashubian**|`csb`|
    |**Kazakh**|`kk`|
    |**Khaling**|`klr`|
    |**Khasi**|`kha`|
    |**Kirghiz**|`ky`|
    |**Korean**|`ko`|
    |**Korku**|`kfq`|
    |**Koryak**|`kpy`|
    |**Kosraean**|`kos`|
    |**Kumarbhag Paharia**|`kmj`|
    |**Kumyk**|`kum`|
    |**Kurdish**|`ku`|
    |**Kurukh**|`kru`|
    |**Kölsch**|`ksh`|
    |**Lak**|`lbe`|
    |**Lakota**|`lkt`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lezghian**|`lez`|
    |**Lithuanian**|`lt`|
    |**Lower Sorbian**|`dsb`|
    |**Lule Sami**|`smj`|
    |**Luxembourgish**|`lb`|
    |**Mahasu Pahari**|`bfz`|
    |**Maithili**|`mai`|
    |**Malay (macrolanguage)**|`ms`|
    |**Maltese**|`mt`|
    |**Manx**|`gv`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Marshallese**|`mh`|
    |**Mongolian**|`mn`|
    |**Neapolitan**|`nap`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Newari**|`new`|
    |**Niuean**|`niu`|
    |**Nogai**|`nog`|
    |**Northern Sami**|`se`|
    |**Norwegian**|`no`|
    |**Occitan (post 1500)**|`oc`|
    |**Old English (ca. 450-1100)**|`ang`|
    |**Ossetian**|`os`|
    |**Pali**|`pi`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Romanian**|`ro`|
    |**Romansh**|`rm`|
    |**Russian**|`ru`|
    |**Sadri**|`sck`|
    |**Samoan**|`sm`|
    |**Sanskrit**|`sa`|
    |**Santali**|`sat`|
    |**Scots**|`sco`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Sherpa**|`xsr`|
    |**Sirmauri**|`srx`|
    |**Skolt Sami**|`sms`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**Southern Sami**|`sma`|
    |**Spanish**|`es`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tabassaran**|`tab`|
    |**Tagalog**|`tl`|
    |**Tajik**|`tg`|
    |**Tatar**|`tt`|
    |**Tetum**|`tet`|
    |**Thangmi**|`thf`|
    |**Tonga (Tonga Islands)**|`to`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Tuvinian**|`tyv`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Upper Sorbian**|`hsb`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Volapük**|`vo`|
    |**Walser**|`wae`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Yucateco**|`yua`|
    |**Zhuang**|`za`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Arabic (Pseudo-Accents)**|`ar-XA`|
    |**Belarusian**|`be-cyrl`|
    |**Belarusian (Latin)**|`be-latn`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (United States)**|`en-US`|
    |**Finnish (Finland)**|`fi-FI`|
    |**French (France)**|`fr-FR`|
    |**German (Germany)**|`de-DE`|
    |**Hungarian (Hungary)**|`hu-HU`|
    |**Italian (Italy)**|`it-IT`|
    |**Japanese (Japan)**|`ja-JP`|
    |**Kara-Kalpak (Cyrillic)**|`kaa-Cyrl`|
    |**Kazakh**|`kk-cyrl`|
    |**Kazakh (Latin)**|`kk-latn`|
    |**Korean (South Korea)**|`ko-KR`|
    |**Kurdish (Arabic)**|`ku-arab`|
    |**Kurdish (Latin)**|`ku-latn`|
    |**Polish**|`pl-PO`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Region: Czechia**|`cz-CZ`|
    |**Region: Greece**|`gr-GR`|
    |**Russian (Russia)**|`ru-RU`|
    |**Serbian (Cyrillic, Montenegro)**|`sr-Cyrl-ME`|
    |**Serbian (Latin)**|`sr-latn`|
    |**Serbian (Latin, Montenegro)**|`sr-Latn-ME`|
    |**Serbian (Montenegro)**|`sr-ME`|
    |**Spanish (Spain)**|`es-ES`|
    |**Swedish (Sweden)**|`sv-SE`|
    |**Turkish (Turkey)**|`tr-TR`|
    |**Uzbek (Arabic)**|`uz-arab`|
    |**Uzbek (Cyrillic)**|`uz-cyrl`|

    </details>

    Args:
        body (OcrocrOcrRequest):
        body (OcrocrOcrRequest):

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
    body: Union[
        OcrocrOcrRequest,
        OcrocrOcrRequest,
    ],
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """OCR

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|1.5 (per 1000 page)|1 page
    |**clarifai**|`8.0.0`|2.0 (per 1000 page)|1 page
    |**google**|`v1`|1.5 (per 1000 page)|1 page
    |**microsoft**|`v3.2`|1.0 (per 1000 page)|1 page
    |**sentisight**|`v3.3.1`|1.0 (per 1000 file)|1 file
    |**api4ai**|`v1.0.0`|3.0 (per 1000 request)|1 request


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Abaza**|`abq`|
    |**Adyghe**|`ady`|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Angika**|`anp`|
    |**Arabic**|`ar`|
    |**Assamese**|`as`|
    |**Asturian**|`ast`|
    |**Avaric**|`av`|
    |**Awadhi**|`awa`|
    |**Azerbaijani**|`az`|
    |**Bagheli**|`bfy`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bengali**|`bn`|
    |**Bhojpuri**|`bho`|
    |**Bihari languages**|`bh`|
    |**Bislama**|`bi`|
    |**Bodo (India)**|`brx`|
    |**Bosnian**|`bs`|
    |**Braj**|`bra`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Bundeli**|`bns`|
    |**Buriat**|`bua`|
    |**Camling**|`rab`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Chamorro**|`ch`|
    |**Chechen**|`ce`|
    |**Chhattisgarhi**|`hne`|
    |**Chinese**|`zh`|
    |**Cornish**|`kw`|
    |**Corsican**|`co`|
    |**Crimean Tatar**|`crh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dargwa**|`dar`|
    |**Dari**|`prs`|
    |**Dhimal**|`dhi`|
    |**Dogri (macrolanguage)**|`doi`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Erzya**|`myv`|
    |**Estonian**|`et`|
    |**Faroese**|`fo`|
    |**Fijian**|`fj`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Friulian**|`fur`|
    |**Gagauz**|`gag`|
    |**Galician**|`gl`|
    |**German**|`de`|
    |**Gilbertese**|`gil`|
    |**Goan Konkani**|`gom`|
    |**Gondi**|`gon`|
    |**Gurung**|`gvr`|
    |**Haitian**|`ht`|
    |**Halbi**|`hlb`|
    |**Hani**|`hni`|
    |**Haryanvi**|`bgc`|
    |**Hawaiian**|`haw`|
    |**Hindi**|`hi`|
    |**Hmong Daw**|`mww`|
    |**Ho**|`hoc`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Inari Sami**|`smn`|
    |**Indonesian**|`id`|
    |**Ingush**|`inh`|
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Inuktitut**|`iu`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Jaunsari**|`jns`|
    |**Javanese**|`jv`|
    |**K'iche'**|`quc`|
    |**Kabardian**|`kbd`|
    |**Kabuverdianu**|`kea`|
    |**Kachin**|`kac`|
    |**Kalaallisut**|`kl`|
    |**Kangri**|`xnr`|
    |**Kara-Kalpak**|`kaa`|
    |**Karachay-Balkar**|`krc`|
    |**Kashubian**|`csb`|
    |**Kazakh**|`kk`|
    |**Khaling**|`klr`|
    |**Khasi**|`kha`|
    |**Kirghiz**|`ky`|
    |**Korean**|`ko`|
    |**Korku**|`kfq`|
    |**Koryak**|`kpy`|
    |**Kosraean**|`kos`|
    |**Kumarbhag Paharia**|`kmj`|
    |**Kumyk**|`kum`|
    |**Kurdish**|`ku`|
    |**Kurukh**|`kru`|
    |**Kölsch**|`ksh`|
    |**Lak**|`lbe`|
    |**Lakota**|`lkt`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lezghian**|`lez`|
    |**Lithuanian**|`lt`|
    |**Lower Sorbian**|`dsb`|
    |**Lule Sami**|`smj`|
    |**Luxembourgish**|`lb`|
    |**Mahasu Pahari**|`bfz`|
    |**Maithili**|`mai`|
    |**Malay (macrolanguage)**|`ms`|
    |**Maltese**|`mt`|
    |**Manx**|`gv`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Marshallese**|`mh`|
    |**Mongolian**|`mn`|
    |**Neapolitan**|`nap`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Newari**|`new`|
    |**Niuean**|`niu`|
    |**Nogai**|`nog`|
    |**Northern Sami**|`se`|
    |**Norwegian**|`no`|
    |**Occitan (post 1500)**|`oc`|
    |**Old English (ca. 450-1100)**|`ang`|
    |**Ossetian**|`os`|
    |**Pali**|`pi`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Romanian**|`ro`|
    |**Romansh**|`rm`|
    |**Russian**|`ru`|
    |**Sadri**|`sck`|
    |**Samoan**|`sm`|
    |**Sanskrit**|`sa`|
    |**Santali**|`sat`|
    |**Scots**|`sco`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Sherpa**|`xsr`|
    |**Sirmauri**|`srx`|
    |**Skolt Sami**|`sms`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**Southern Sami**|`sma`|
    |**Spanish**|`es`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tabassaran**|`tab`|
    |**Tagalog**|`tl`|
    |**Tajik**|`tg`|
    |**Tatar**|`tt`|
    |**Tetum**|`tet`|
    |**Thangmi**|`thf`|
    |**Tonga (Tonga Islands)**|`to`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Tuvinian**|`tyv`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Upper Sorbian**|`hsb`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Volapük**|`vo`|
    |**Walser**|`wae`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Yucateco**|`yua`|
    |**Zhuang**|`za`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Arabic (Pseudo-Accents)**|`ar-XA`|
    |**Belarusian**|`be-cyrl`|
    |**Belarusian (Latin)**|`be-latn`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (United States)**|`en-US`|
    |**Finnish (Finland)**|`fi-FI`|
    |**French (France)**|`fr-FR`|
    |**German (Germany)**|`de-DE`|
    |**Hungarian (Hungary)**|`hu-HU`|
    |**Italian (Italy)**|`it-IT`|
    |**Japanese (Japan)**|`ja-JP`|
    |**Kara-Kalpak (Cyrillic)**|`kaa-Cyrl`|
    |**Kazakh**|`kk-cyrl`|
    |**Kazakh (Latin)**|`kk-latn`|
    |**Korean (South Korea)**|`ko-KR`|
    |**Kurdish (Arabic)**|`ku-arab`|
    |**Kurdish (Latin)**|`ku-latn`|
    |**Polish**|`pl-PO`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Region: Czechia**|`cz-CZ`|
    |**Region: Greece**|`gr-GR`|
    |**Russian (Russia)**|`ru-RU`|
    |**Serbian (Cyrillic, Montenegro)**|`sr-Cyrl-ME`|
    |**Serbian (Latin)**|`sr-latn`|
    |**Serbian (Latin, Montenegro)**|`sr-Latn-ME`|
    |**Serbian (Montenegro)**|`sr-ME`|
    |**Spanish (Spain)**|`es-ES`|
    |**Swedish (Sweden)**|`sv-SE`|
    |**Turkish (Turkey)**|`tr-TR`|
    |**Uzbek (Arabic)**|`uz-arab`|
    |**Uzbek (Cyrillic)**|`uz-cyrl`|

    </details>

    Args:
        body (OcrocrOcrRequest):
        body (OcrocrOcrRequest):

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
