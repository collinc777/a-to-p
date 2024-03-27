from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.not_found_response import NotFoundResponse
from ...models.translationdocument_translation_document_translation_request import (
    TranslationdocumentTranslationDocumentTranslationRequest,
)
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        TranslationdocumentTranslationDocumentTranslationRequest,
        TranslationdocumentTranslationDocumentTranslationRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/translation/document_translation",
    }

    if isinstance(body, TranslationdocumentTranslationDocumentTranslationRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, TranslationdocumentTranslationDocumentTranslationRequest):
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
        TranslationdocumentTranslationDocumentTranslationRequest,
        TranslationdocumentTranslationDocumentTranslationRequest,
    ],
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Document Translation

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**deepl**|`v2`|2.0 (per 20 page)|20 page
    |**google**|`v3`|0.08 (per 1 page)|1 page


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
    |**Cebuano**|`ceb`|
    |**Central Khmer**|`km`|
    |**Chinese**|`zh`|
    |**Corsican**|`co`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hawaiian**|`haw`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hmong**|`hmn`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Igbo**|`ig`|
    |**Indonesian**|`id`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kannada**|`kn`|
    |**Kazakh**|`kk`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Korean**|`ko`|
    |**Kurdish**|`ku`|
    |**Lao**|`lo`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Nyanja**|`ny`|
    |**Oriya (macrolanguage)**|`or`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Samoan**|`sm`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Shona**|`sn`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
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
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Xhosa**|`xh`|
    |**Yiddish**|`yi`|
    |**Yoruba**|`yo`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (Taiwan)**|`zh-TW`|

    </details>

    Args:
        body (TranslationdocumentTranslationDocumentTranslationRequest):
        body (TranslationdocumentTranslationDocumentTranslationRequest):

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
        TranslationdocumentTranslationDocumentTranslationRequest,
        TranslationdocumentTranslationDocumentTranslationRequest,
    ],
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Document Translation

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**deepl**|`v2`|2.0 (per 20 page)|20 page
    |**google**|`v3`|0.08 (per 1 page)|1 page


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
    |**Cebuano**|`ceb`|
    |**Central Khmer**|`km`|
    |**Chinese**|`zh`|
    |**Corsican**|`co`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hawaiian**|`haw`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hmong**|`hmn`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Igbo**|`ig`|
    |**Indonesian**|`id`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kannada**|`kn`|
    |**Kazakh**|`kk`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Korean**|`ko`|
    |**Kurdish**|`ku`|
    |**Lao**|`lo`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Nyanja**|`ny`|
    |**Oriya (macrolanguage)**|`or`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Samoan**|`sm`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Shona**|`sn`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
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
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Xhosa**|`xh`|
    |**Yiddish**|`yi`|
    |**Yoruba**|`yo`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (Taiwan)**|`zh-TW`|

    </details>

    Args:
        body (TranslationdocumentTranslationDocumentTranslationRequest):
        body (TranslationdocumentTranslationDocumentTranslationRequest):

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
        TranslationdocumentTranslationDocumentTranslationRequest,
        TranslationdocumentTranslationDocumentTranslationRequest,
    ],
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Document Translation

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**deepl**|`v2`|2.0 (per 20 page)|20 page
    |**google**|`v3`|0.08 (per 1 page)|1 page


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
    |**Cebuano**|`ceb`|
    |**Central Khmer**|`km`|
    |**Chinese**|`zh`|
    |**Corsican**|`co`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hawaiian**|`haw`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hmong**|`hmn`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Igbo**|`ig`|
    |**Indonesian**|`id`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kannada**|`kn`|
    |**Kazakh**|`kk`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Korean**|`ko`|
    |**Kurdish**|`ku`|
    |**Lao**|`lo`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Nyanja**|`ny`|
    |**Oriya (macrolanguage)**|`or`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Samoan**|`sm`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Shona**|`sn`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
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
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Xhosa**|`xh`|
    |**Yiddish**|`yi`|
    |**Yoruba**|`yo`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (Taiwan)**|`zh-TW`|

    </details>

    Args:
        body (TranslationdocumentTranslationDocumentTranslationRequest):
        body (TranslationdocumentTranslationDocumentTranslationRequest):

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
        TranslationdocumentTranslationDocumentTranslationRequest,
        TranslationdocumentTranslationDocumentTranslationRequest,
    ],
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Document Translation

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**deepl**|`v2`|2.0 (per 20 page)|20 page
    |**google**|`v3`|0.08 (per 1 page)|1 page


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
    |**Cebuano**|`ceb`|
    |**Central Khmer**|`km`|
    |**Chinese**|`zh`|
    |**Corsican**|`co`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hawaiian**|`haw`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hmong**|`hmn`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Igbo**|`ig`|
    |**Indonesian**|`id`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kannada**|`kn`|
    |**Kazakh**|`kk`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Korean**|`ko`|
    |**Kurdish**|`ku`|
    |**Lao**|`lo`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Nyanja**|`ny`|
    |**Oriya (macrolanguage)**|`or`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Samoan**|`sm`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Shona**|`sn`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
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
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Xhosa**|`xh`|
    |**Yiddish**|`yi`|
    |**Yoruba**|`yo`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (China)**|`zh-CN`|
    |**Chinese (Taiwan)**|`zh-TW`|

    </details>

    Args:
        body (TranslationdocumentTranslationDocumentTranslationRequest):
        body (TranslationdocumentTranslationDocumentTranslationRequest):

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
