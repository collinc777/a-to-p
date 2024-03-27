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
        "url": "/text/anonymization",
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
    """Anonymization

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**emvista**|`v1.0`|3.0 (per 1000000 char)|1 char
    |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token
    |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char
    |**microsoft**|`v3.1`|0.25 (per 1000000 char)|1000 char


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Arabic**|`ar`|
    |**Chinese**|`zh`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**German**|`de`|
    |**Hindi**|`hi`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Korean**|`ko`|
    |**Modern Greek (1453-)**|`el`|
    |**Norwegian**|`no`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Russian**|`ru`|
    |**Spanish**|`es`|
    |**Swedish**|`sv`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Traditional)**|`zh-Hant`|
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
    """Anonymization

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**emvista**|`v1.0`|3.0 (per 1000000 char)|1 char
    |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token
    |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char
    |**microsoft**|`v3.1`|0.25 (per 1000000 char)|1000 char


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Arabic**|`ar`|
    |**Chinese**|`zh`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**German**|`de`|
    |**Hindi**|`hi`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Korean**|`ko`|
    |**Modern Greek (1453-)**|`el`|
    |**Norwegian**|`no`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Russian**|`ru`|
    |**Spanish**|`es`|
    |**Swedish**|`sv`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Traditional)**|`zh-Hant`|
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
    """Anonymization

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**emvista**|`v1.0`|3.0 (per 1000000 char)|1 char
    |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token
    |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char
    |**microsoft**|`v3.1`|0.25 (per 1000000 char)|1000 char


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Arabic**|`ar`|
    |**Chinese**|`zh`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**German**|`de`|
    |**Hindi**|`hi`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Korean**|`ko`|
    |**Modern Greek (1453-)**|`el`|
    |**Norwegian**|`no`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Russian**|`ru`|
    |**Spanish**|`es`|
    |**Swedish**|`sv`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Traditional)**|`zh-Hant`|
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
    """Anonymization

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**emvista**|`v1.0`|3.0 (per 1000000 char)|1 char
    |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token
    |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char
    |**microsoft**|`v3.1`|0.25 (per 1000000 char)|1000 char


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Arabic**|`ar`|
    |**Chinese**|`zh`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**German**|`de`|
    |**Hindi**|`hi`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Korean**|`ko`|
    |**Modern Greek (1453-)**|`el`|
    |**Norwegian**|`no`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Russian**|`ru`|
    |**Spanish**|`es`|
    |**Swedish**|`sv`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Traditional)**|`zh-Hant`|
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
