from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.not_found_response import NotFoundResponse
from ...models.texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request import (
    TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest,
)
from ...types import Response


def _get_kwargs(
    *,
    body: TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/text/moderation",
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
    body: TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Moderation

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**microsoft**|`v1.0`|1.0 (per 1000 request)|1 request
    |**openai**|`v3.0.0`|free|-
    |**clarifai**|`8.0.0`|1.2 (per 1000 request)|1 request
    |**google**|`v1`|5.0 (per 1000000 char)|100 char


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Aragonese**|`an`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
    |**Asturian**|`ast`|
    |**Azerbaijani**|`az`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Bavarian**|`bar`|
    |**Belarusian**|`be`|
    |**Bengali**|`bn`|
    |**Bishnupriya**|`bpy`|
    |**Bosnian**|`bs`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Central Khmer**|`km`|
    |**Central Kurdish**|`ckb`|
    |**Chechen**|`ce`|
    |**Cherokee**|`chr`|
    |**Chinese**|`zh`|
    |**Chuvash**|`cv`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Estonian**|`et`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Fulah**|`ff`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Ido**|`io`|
    |**Igbo**|`ig`|
    |**Indonesian**|`id`|
    |**Inuktitut**|`iu`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kannada**|`kn`|
    |**Kazakh**|`kk`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Konkani (macrolanguage)**|`kok`|
    |**Korean**|`ko`|
    |**Lahnda**|`lah`|
    |**Lao**|`lo`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Lombard**|`lmo`|
    |**Low German**|`nds`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Minangkabau**|`min`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Norwegian Nynorsk**|`nn`|
    |**Occitan (post 1500)**|`oc`|
    |**Oriya (macrolanguage)**|`or`|
    |**Panjabi**|`pa`|
    |**Pedi**|`nso`|
    |**Persian**|`fa`|
    |**Piemontese**|`pms`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Quechua**|`qu`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Scots**|`sco`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Serbo-Croatian**|`sh`|
    |**Sicilian**|`scn`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**South Azerbaijani**|`azb`|
    |**Southern Sotho**|`st`|
    |**Spanish**|`es`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tajik**|`tg`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Tigrinya**|`ti`|
    |**Tswana**|`tn`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Volapük**|`vo`|
    |**Waray (Philippines)**|`war`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Wolof**|`wo`|
    |**Xhosa**|`xh`|
    |**Yoruba**|`yo`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Low German (Netherlands)**|`nds-NL`|

    </details>

    Args:
        body (TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeyw
            ordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest):

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
    body: TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Moderation

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**microsoft**|`v1.0`|1.0 (per 1000 request)|1 request
    |**openai**|`v3.0.0`|free|-
    |**clarifai**|`8.0.0`|1.2 (per 1000 request)|1 request
    |**google**|`v1`|5.0 (per 1000000 char)|100 char


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Aragonese**|`an`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
    |**Asturian**|`ast`|
    |**Azerbaijani**|`az`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Bavarian**|`bar`|
    |**Belarusian**|`be`|
    |**Bengali**|`bn`|
    |**Bishnupriya**|`bpy`|
    |**Bosnian**|`bs`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Central Khmer**|`km`|
    |**Central Kurdish**|`ckb`|
    |**Chechen**|`ce`|
    |**Cherokee**|`chr`|
    |**Chinese**|`zh`|
    |**Chuvash**|`cv`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Estonian**|`et`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Fulah**|`ff`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Ido**|`io`|
    |**Igbo**|`ig`|
    |**Indonesian**|`id`|
    |**Inuktitut**|`iu`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kannada**|`kn`|
    |**Kazakh**|`kk`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Konkani (macrolanguage)**|`kok`|
    |**Korean**|`ko`|
    |**Lahnda**|`lah`|
    |**Lao**|`lo`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Lombard**|`lmo`|
    |**Low German**|`nds`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Minangkabau**|`min`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Norwegian Nynorsk**|`nn`|
    |**Occitan (post 1500)**|`oc`|
    |**Oriya (macrolanguage)**|`or`|
    |**Panjabi**|`pa`|
    |**Pedi**|`nso`|
    |**Persian**|`fa`|
    |**Piemontese**|`pms`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Quechua**|`qu`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Scots**|`sco`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Serbo-Croatian**|`sh`|
    |**Sicilian**|`scn`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**South Azerbaijani**|`azb`|
    |**Southern Sotho**|`st`|
    |**Spanish**|`es`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tajik**|`tg`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Tigrinya**|`ti`|
    |**Tswana**|`tn`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Volapük**|`vo`|
    |**Waray (Philippines)**|`war`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Wolof**|`wo`|
    |**Xhosa**|`xh`|
    |**Yoruba**|`yo`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Low German (Netherlands)**|`nds-NL`|

    </details>

    Args:
        body (TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeyw
            ordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest):

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
    body: TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Moderation

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**microsoft**|`v1.0`|1.0 (per 1000 request)|1 request
    |**openai**|`v3.0.0`|free|-
    |**clarifai**|`8.0.0`|1.2 (per 1000 request)|1 request
    |**google**|`v1`|5.0 (per 1000000 char)|100 char


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Aragonese**|`an`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
    |**Asturian**|`ast`|
    |**Azerbaijani**|`az`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Bavarian**|`bar`|
    |**Belarusian**|`be`|
    |**Bengali**|`bn`|
    |**Bishnupriya**|`bpy`|
    |**Bosnian**|`bs`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Central Khmer**|`km`|
    |**Central Kurdish**|`ckb`|
    |**Chechen**|`ce`|
    |**Cherokee**|`chr`|
    |**Chinese**|`zh`|
    |**Chuvash**|`cv`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Estonian**|`et`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Fulah**|`ff`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Ido**|`io`|
    |**Igbo**|`ig`|
    |**Indonesian**|`id`|
    |**Inuktitut**|`iu`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kannada**|`kn`|
    |**Kazakh**|`kk`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Konkani (macrolanguage)**|`kok`|
    |**Korean**|`ko`|
    |**Lahnda**|`lah`|
    |**Lao**|`lo`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Lombard**|`lmo`|
    |**Low German**|`nds`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Minangkabau**|`min`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Norwegian Nynorsk**|`nn`|
    |**Occitan (post 1500)**|`oc`|
    |**Oriya (macrolanguage)**|`or`|
    |**Panjabi**|`pa`|
    |**Pedi**|`nso`|
    |**Persian**|`fa`|
    |**Piemontese**|`pms`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Quechua**|`qu`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Scots**|`sco`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Serbo-Croatian**|`sh`|
    |**Sicilian**|`scn`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**South Azerbaijani**|`azb`|
    |**Southern Sotho**|`st`|
    |**Spanish**|`es`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tajik**|`tg`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Tigrinya**|`ti`|
    |**Tswana**|`tn`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Volapük**|`vo`|
    |**Waray (Philippines)**|`war`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Wolof**|`wo`|
    |**Xhosa**|`xh`|
    |**Yoruba**|`yo`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Low German (Netherlands)**|`nds-NL`|

    </details>

    Args:
        body (TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeyw
            ordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest):

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
    body: TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Moderation

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**microsoft**|`v1.0`|1.0 (per 1000 request)|1 request
    |**openai**|`v3.0.0`|free|-
    |**clarifai**|`8.0.0`|1.2 (per 1000 request)|1 request
    |**google**|`v1`|5.0 (per 1000000 char)|100 char


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Aragonese**|`an`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
    |**Asturian**|`ast`|
    |**Azerbaijani**|`az`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Bavarian**|`bar`|
    |**Belarusian**|`be`|
    |**Bengali**|`bn`|
    |**Bishnupriya**|`bpy`|
    |**Bosnian**|`bs`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Central Khmer**|`km`|
    |**Central Kurdish**|`ckb`|
    |**Chechen**|`ce`|
    |**Cherokee**|`chr`|
    |**Chinese**|`zh`|
    |**Chuvash**|`cv`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Estonian**|`et`|
    |**Filipino**|`fil`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Fulah**|`ff`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Ido**|`io`|
    |**Igbo**|`ig`|
    |**Indonesian**|`id`|
    |**Inuktitut**|`iu`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kannada**|`kn`|
    |**Kazakh**|`kk`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Konkani (macrolanguage)**|`kok`|
    |**Korean**|`ko`|
    |**Lahnda**|`lah`|
    |**Lao**|`lo`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Lombard**|`lmo`|
    |**Low German**|`nds`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Minangkabau**|`min`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Norwegian Nynorsk**|`nn`|
    |**Occitan (post 1500)**|`oc`|
    |**Oriya (macrolanguage)**|`or`|
    |**Panjabi**|`pa`|
    |**Pedi**|`nso`|
    |**Persian**|`fa`|
    |**Piemontese**|`pms`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Quechua**|`qu`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Scots**|`sco`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Serbo-Croatian**|`sh`|
    |**Sicilian**|`scn`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**South Azerbaijani**|`azb`|
    |**Southern Sotho**|`st`|
    |**Spanish**|`es`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tajik**|`tg`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Tigrinya**|`ti`|
    |**Tswana**|`tn`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Volapük**|`vo`|
    |**Waray (Philippines)**|`war`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Wolof**|`wo`|
    |**Xhosa**|`xh`|
    |**Yoruba**|`yo`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Low German (Netherlands)**|`nds-NL`|

    </details>

    Args:
        body (TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeyw
            ordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest):

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
