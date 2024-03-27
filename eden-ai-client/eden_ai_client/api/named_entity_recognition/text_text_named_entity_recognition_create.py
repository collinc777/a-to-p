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
        "url": "/text/named_entity_recognition",
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
    """Named Entity Recognition

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char
    |**google**|`v1`|1.0 (per 1000000 char)|1000 char
    |**ibm**|`v1 (2021-08-01)`|0.3 (per 1000000 char)|10000 char
    |**lettria**|`v5.5.2`|2.0 (per 1000000 char)|1000 char
    |**microsoft**|`v3.1`|1.0 (per 1000000 char)|1000 char
    |**neuralspace**|`v1`|0.007 (per 1 request)|1 request
    |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token
    |**tenstorrent**|`v1.0.0`|1.0 (per 1000000 char)|1000 char
    |**nlpcloud**|`v1`|25.0 (per 1000 request)|1 request


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Arabic**|`ar`|
    |**Aragonese**|`an`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
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
    |**Chechen**|`ce`|
    |**Chinese**|`zh`|
    |**Chuvash**|`cv`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Estonian**|`et`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
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
    |**Kirghiz**|`ky`|
    |**Korean**|`ko`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Marathi**|`mr`|
    |**Modern Greek (1453-)**|`el`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Occitan (post 1500)**|`oc`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Serbian**|`sr`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Spanish**|`es`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tajik**|`tg`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Turkish**|`tr`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Welsh**|`cy`|
    |**Yoruba**|`yo`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**English (United States)**|`en-US`|
    |**French (France)**|`fr-FR`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|

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
    """Named Entity Recognition

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char
    |**google**|`v1`|1.0 (per 1000000 char)|1000 char
    |**ibm**|`v1 (2021-08-01)`|0.3 (per 1000000 char)|10000 char
    |**lettria**|`v5.5.2`|2.0 (per 1000000 char)|1000 char
    |**microsoft**|`v3.1`|1.0 (per 1000000 char)|1000 char
    |**neuralspace**|`v1`|0.007 (per 1 request)|1 request
    |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token
    |**tenstorrent**|`v1.0.0`|1.0 (per 1000000 char)|1000 char
    |**nlpcloud**|`v1`|25.0 (per 1000 request)|1 request


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Arabic**|`ar`|
    |**Aragonese**|`an`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
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
    |**Chechen**|`ce`|
    |**Chinese**|`zh`|
    |**Chuvash**|`cv`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Estonian**|`et`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
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
    |**Kirghiz**|`ky`|
    |**Korean**|`ko`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Marathi**|`mr`|
    |**Modern Greek (1453-)**|`el`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Occitan (post 1500)**|`oc`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Serbian**|`sr`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Spanish**|`es`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tajik**|`tg`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Turkish**|`tr`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Welsh**|`cy`|
    |**Yoruba**|`yo`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**English (United States)**|`en-US`|
    |**French (France)**|`fr-FR`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|

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
    """Named Entity Recognition

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char
    |**google**|`v1`|1.0 (per 1000000 char)|1000 char
    |**ibm**|`v1 (2021-08-01)`|0.3 (per 1000000 char)|10000 char
    |**lettria**|`v5.5.2`|2.0 (per 1000000 char)|1000 char
    |**microsoft**|`v3.1`|1.0 (per 1000000 char)|1000 char
    |**neuralspace**|`v1`|0.007 (per 1 request)|1 request
    |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token
    |**tenstorrent**|`v1.0.0`|1.0 (per 1000000 char)|1000 char
    |**nlpcloud**|`v1`|25.0 (per 1000 request)|1 request


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Arabic**|`ar`|
    |**Aragonese**|`an`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
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
    |**Chechen**|`ce`|
    |**Chinese**|`zh`|
    |**Chuvash**|`cv`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Estonian**|`et`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
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
    |**Kirghiz**|`ky`|
    |**Korean**|`ko`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Marathi**|`mr`|
    |**Modern Greek (1453-)**|`el`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Occitan (post 1500)**|`oc`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Serbian**|`sr`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Spanish**|`es`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tajik**|`tg`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Turkish**|`tr`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Welsh**|`cy`|
    |**Yoruba**|`yo`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**English (United States)**|`en-US`|
    |**French (France)**|`fr-FR`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|

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
    """Named Entity Recognition

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char
    |**google**|`v1`|1.0 (per 1000000 char)|1000 char
    |**ibm**|`v1 (2021-08-01)`|0.3 (per 1000000 char)|10000 char
    |**lettria**|`v5.5.2`|2.0 (per 1000000 char)|1000 char
    |**microsoft**|`v3.1`|1.0 (per 1000000 char)|1000 char
    |**neuralspace**|`v1`|0.007 (per 1 request)|1 request
    |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token
    |**tenstorrent**|`v1.0.0`|1.0 (per 1000000 char)|1000 char
    |**nlpcloud**|`v1`|25.0 (per 1000 request)|1 request


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Arabic**|`ar`|
    |**Aragonese**|`an`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
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
    |**Chechen**|`ce`|
    |**Chinese**|`zh`|
    |**Chuvash**|`cv`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Estonian**|`et`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**Galician**|`gl`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
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
    |**Kirghiz**|`ky`|
    |**Korean**|`ko`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Marathi**|`mr`|
    |**Modern Greek (1453-)**|`el`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Occitan (post 1500)**|`oc`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Serbian**|`sr`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Spanish**|`es`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tajik**|`tg`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Turkish**|`tr`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Vietnamese**|`vi`|
    |**Welsh**|`cy`|
    |**Yoruba**|`yo`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**English (United States)**|`en-US`|
    |**French (France)**|`fr-FR`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|

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
