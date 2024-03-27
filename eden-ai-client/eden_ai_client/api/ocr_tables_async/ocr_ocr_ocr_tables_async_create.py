from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.launch_async_job_response import LaunchAsyncJobResponse
from ...models.ocr_tables_async_request import OcrTablesAsyncRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        OcrTablesAsyncRequest,
        OcrTablesAsyncRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/ocr/ocr_tables_async",
    }

    if isinstance(body, OcrTablesAsyncRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"
    if isinstance(body, OcrTablesAsyncRequest):
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
        OcrTablesAsyncRequest,
        OcrTablesAsyncRequest,
    ],
) -> Response[LaunchAsyncJobResponse]:
    """OCR Tables Launch Job

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|15.0 (per 1000 page)|1 page
    |**google**|`DocumentAI v1 beta3`|65.0 (per 1000 page)|1 page
    |**microsoft**|`rest API 3.0`|10.0 (per 1000 page)|1 page


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Angika**|`anp`|
    |**Arabic**|`ar`|
    |**Asturian**|`ast`|
    |**Awadhi**|`awa`|
    |**Azerbaijani**|`az`|
    |**Bagheli**|`bfy`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bhojpuri**|`bho`|
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
    |**Chhattisgarhi**|`hne`|
    |**Chinese**|`zh`|
    |**Cornish**|`kw`|
    |**Corsican**|`co`|
    |**Crimean Tatar**|`crh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
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
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Inuktitut**|`iu`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Jaunsari**|`jns`|
    |**Javanese**|`jv`|
    |**K'iche'**|`quc`|
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
    |**Lakota**|`lkt`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Lower Sorbian**|`dsb`|
    |**Lule Sami**|`smj`|
    |**Luxembourgish**|`lb`|
    |**Mahasu Pahari**|`bfz`|
    |**Malay (macrolanguage)**|`ms`|
    |**Maltese**|`mt`|
    |**Manx**|`gv`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Mongolian**|`mn`|
    |**Neapolitan**|`nap`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Niuean**|`niu`|
    |**Nogai**|`nog`|
    |**Northern Sami**|`se`|
    |**Norwegian**|`no`|
    |**Occitan (post 1500)**|`oc`|
    |**Ossetian**|`os`|
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
    |**Belarusian**|`be-Cyrl`|
    |**Belarusian (Latin)**|`be-Latn`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Kara-Kalpak (Cyrillic)**|`kaa-Cyrl`|
    |**Kazakh**|`kk-Cyrl`|
    |**Kazakh (Latin)**|`kk-Latn`|
    |**Kurdish (Arabic)**|`ku-Arab`|
    |**Kurdish (Latin)**|`ku-Latn`|
    |**Serbian (Cyrillic)**|`sr-Cyrl`|
    |**Serbian (Cyrillic, Montenegro)**|`sr-Cyrl-ME`|
    |**Serbian (Latin)**|`sr-Latn`|
    |**Serbian (Latin, Montenegro)**|`sr-Latn-ME`|
    |**Serbian (Montenegro)**|`sr-ME`|
    |**Uzbek (Arabic)**|`uz-Arab`|
    |**Uzbek (Cyrillic)**|`uz-cyrl`|

    </details>

    Args:
        body (OcrTablesAsyncRequest):
        body (OcrTablesAsyncRequest):

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
        OcrTablesAsyncRequest,
        OcrTablesAsyncRequest,
    ],
) -> Optional[LaunchAsyncJobResponse]:
    """OCR Tables Launch Job

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|15.0 (per 1000 page)|1 page
    |**google**|`DocumentAI v1 beta3`|65.0 (per 1000 page)|1 page
    |**microsoft**|`rest API 3.0`|10.0 (per 1000 page)|1 page


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Angika**|`anp`|
    |**Arabic**|`ar`|
    |**Asturian**|`ast`|
    |**Awadhi**|`awa`|
    |**Azerbaijani**|`az`|
    |**Bagheli**|`bfy`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bhojpuri**|`bho`|
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
    |**Chhattisgarhi**|`hne`|
    |**Chinese**|`zh`|
    |**Cornish**|`kw`|
    |**Corsican**|`co`|
    |**Crimean Tatar**|`crh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
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
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Inuktitut**|`iu`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Jaunsari**|`jns`|
    |**Javanese**|`jv`|
    |**K'iche'**|`quc`|
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
    |**Lakota**|`lkt`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Lower Sorbian**|`dsb`|
    |**Lule Sami**|`smj`|
    |**Luxembourgish**|`lb`|
    |**Mahasu Pahari**|`bfz`|
    |**Malay (macrolanguage)**|`ms`|
    |**Maltese**|`mt`|
    |**Manx**|`gv`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Mongolian**|`mn`|
    |**Neapolitan**|`nap`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Niuean**|`niu`|
    |**Nogai**|`nog`|
    |**Northern Sami**|`se`|
    |**Norwegian**|`no`|
    |**Occitan (post 1500)**|`oc`|
    |**Ossetian**|`os`|
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
    |**Belarusian**|`be-Cyrl`|
    |**Belarusian (Latin)**|`be-Latn`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Kara-Kalpak (Cyrillic)**|`kaa-Cyrl`|
    |**Kazakh**|`kk-Cyrl`|
    |**Kazakh (Latin)**|`kk-Latn`|
    |**Kurdish (Arabic)**|`ku-Arab`|
    |**Kurdish (Latin)**|`ku-Latn`|
    |**Serbian (Cyrillic)**|`sr-Cyrl`|
    |**Serbian (Cyrillic, Montenegro)**|`sr-Cyrl-ME`|
    |**Serbian (Latin)**|`sr-Latn`|
    |**Serbian (Latin, Montenegro)**|`sr-Latn-ME`|
    |**Serbian (Montenegro)**|`sr-ME`|
    |**Uzbek (Arabic)**|`uz-Arab`|
    |**Uzbek (Cyrillic)**|`uz-cyrl`|

    </details>

    Args:
        body (OcrTablesAsyncRequest):
        body (OcrTablesAsyncRequest):

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
        OcrTablesAsyncRequest,
        OcrTablesAsyncRequest,
    ],
) -> Response[LaunchAsyncJobResponse]:
    """OCR Tables Launch Job

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|15.0 (per 1000 page)|1 page
    |**google**|`DocumentAI v1 beta3`|65.0 (per 1000 page)|1 page
    |**microsoft**|`rest API 3.0`|10.0 (per 1000 page)|1 page


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Angika**|`anp`|
    |**Arabic**|`ar`|
    |**Asturian**|`ast`|
    |**Awadhi**|`awa`|
    |**Azerbaijani**|`az`|
    |**Bagheli**|`bfy`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bhojpuri**|`bho`|
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
    |**Chhattisgarhi**|`hne`|
    |**Chinese**|`zh`|
    |**Cornish**|`kw`|
    |**Corsican**|`co`|
    |**Crimean Tatar**|`crh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
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
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Inuktitut**|`iu`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Jaunsari**|`jns`|
    |**Javanese**|`jv`|
    |**K'iche'**|`quc`|
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
    |**Lakota**|`lkt`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Lower Sorbian**|`dsb`|
    |**Lule Sami**|`smj`|
    |**Luxembourgish**|`lb`|
    |**Mahasu Pahari**|`bfz`|
    |**Malay (macrolanguage)**|`ms`|
    |**Maltese**|`mt`|
    |**Manx**|`gv`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Mongolian**|`mn`|
    |**Neapolitan**|`nap`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Niuean**|`niu`|
    |**Nogai**|`nog`|
    |**Northern Sami**|`se`|
    |**Norwegian**|`no`|
    |**Occitan (post 1500)**|`oc`|
    |**Ossetian**|`os`|
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
    |**Belarusian**|`be-Cyrl`|
    |**Belarusian (Latin)**|`be-Latn`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Kara-Kalpak (Cyrillic)**|`kaa-Cyrl`|
    |**Kazakh**|`kk-Cyrl`|
    |**Kazakh (Latin)**|`kk-Latn`|
    |**Kurdish (Arabic)**|`ku-Arab`|
    |**Kurdish (Latin)**|`ku-Latn`|
    |**Serbian (Cyrillic)**|`sr-Cyrl`|
    |**Serbian (Cyrillic, Montenegro)**|`sr-Cyrl-ME`|
    |**Serbian (Latin)**|`sr-Latn`|
    |**Serbian (Latin, Montenegro)**|`sr-Latn-ME`|
    |**Serbian (Montenegro)**|`sr-ME`|
    |**Uzbek (Arabic)**|`uz-Arab`|
    |**Uzbek (Cyrillic)**|`uz-cyrl`|

    </details>

    Args:
        body (OcrTablesAsyncRequest):
        body (OcrTablesAsyncRequest):

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
        OcrTablesAsyncRequest,
        OcrTablesAsyncRequest,
    ],
) -> Optional[LaunchAsyncJobResponse]:
    """OCR Tables Launch Job

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|15.0 (per 1000 page)|1 page
    |**google**|`DocumentAI v1 beta3`|65.0 (per 1000 page)|1 page
    |**microsoft**|`rest API 3.0`|10.0 (per 1000 page)|1 page


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Angika**|`anp`|
    |**Arabic**|`ar`|
    |**Asturian**|`ast`|
    |**Awadhi**|`awa`|
    |**Azerbaijani**|`az`|
    |**Bagheli**|`bfy`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bhojpuri**|`bho`|
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
    |**Chhattisgarhi**|`hne`|
    |**Chinese**|`zh`|
    |**Cornish**|`kw`|
    |**Corsican**|`co`|
    |**Crimean Tatar**|`crh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
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
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Inuktitut**|`iu`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Jaunsari**|`jns`|
    |**Javanese**|`jv`|
    |**K'iche'**|`quc`|
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
    |**Lakota**|`lkt`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Lower Sorbian**|`dsb`|
    |**Lule Sami**|`smj`|
    |**Luxembourgish**|`lb`|
    |**Mahasu Pahari**|`bfz`|
    |**Malay (macrolanguage)**|`ms`|
    |**Maltese**|`mt`|
    |**Manx**|`gv`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Mongolian**|`mn`|
    |**Neapolitan**|`nap`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Niuean**|`niu`|
    |**Nogai**|`nog`|
    |**Northern Sami**|`se`|
    |**Norwegian**|`no`|
    |**Occitan (post 1500)**|`oc`|
    |**Ossetian**|`os`|
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
    |**Belarusian**|`be-Cyrl`|
    |**Belarusian (Latin)**|`be-Latn`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Kara-Kalpak (Cyrillic)**|`kaa-Cyrl`|
    |**Kazakh**|`kk-Cyrl`|
    |**Kazakh (Latin)**|`kk-Latn`|
    |**Kurdish (Arabic)**|`ku-Arab`|
    |**Kurdish (Latin)**|`ku-Latn`|
    |**Serbian (Cyrillic)**|`sr-Cyrl`|
    |**Serbian (Cyrillic, Montenegro)**|`sr-Cyrl-ME`|
    |**Serbian (Latin)**|`sr-Latn`|
    |**Serbian (Latin, Montenegro)**|`sr-Latn-ME`|
    |**Serbian (Montenegro)**|`sr-ME`|
    |**Uzbek (Arabic)**|`uz-Arab`|
    |**Uzbek (Cyrillic)**|`uz-cyrl`|

    </details>

    Args:
        body (OcrTablesAsyncRequest):
        body (OcrTablesAsyncRequest):

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
