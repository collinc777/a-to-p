from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.not_found_response import NotFoundResponse
from ...models.translationlanguage_detection_language_detection_request import (
    TranslationlanguageDetectionLanguageDetectionRequest,
)
from ...types import Response


def _get_kwargs(
    *,
    body: TranslationlanguageDetectionLanguageDetectionRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/translation/language_detection",
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
    body: TranslationlanguageDetectionLanguageDetectionRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Language Detection

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char
    |**google**|`v1`|20.0 (per 1000000 char)|1 char
    |**ibm**|`v1 (2021-08-01)`|20.0 (per 1000000 char)|1000 char
    |**microsoft**|`v3.1`|1.0 (per 1000000 char)|1000 char
    |**neuralspace**|`v1`|7.0 (per 1000 request)|1 request
    |**modernmt**|`1.1.0`|8.0 (per 1000000 char)|1 char
    |**openai**|`v1`|20.0 (per 1000000 token)|1 token


    </details>


    Args:
        body (TranslationlanguageDetectionLanguageDetectionRequest):

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
    body: TranslationlanguageDetectionLanguageDetectionRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Language Detection

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char
    |**google**|`v1`|20.0 (per 1000000 char)|1 char
    |**ibm**|`v1 (2021-08-01)`|20.0 (per 1000000 char)|1000 char
    |**microsoft**|`v3.1`|1.0 (per 1000000 char)|1000 char
    |**neuralspace**|`v1`|7.0 (per 1000 request)|1 request
    |**modernmt**|`1.1.0`|8.0 (per 1000000 char)|1 char
    |**openai**|`v1`|20.0 (per 1000000 token)|1 token


    </details>


    Args:
        body (TranslationlanguageDetectionLanguageDetectionRequest):

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
    body: TranslationlanguageDetectionLanguageDetectionRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Language Detection

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char
    |**google**|`v1`|20.0 (per 1000000 char)|1 char
    |**ibm**|`v1 (2021-08-01)`|20.0 (per 1000000 char)|1000 char
    |**microsoft**|`v3.1`|1.0 (per 1000000 char)|1000 char
    |**neuralspace**|`v1`|7.0 (per 1000 request)|1 request
    |**modernmt**|`1.1.0`|8.0 (per 1000000 char)|1 char
    |**openai**|`v1`|20.0 (per 1000000 token)|1 token


    </details>


    Args:
        body (TranslationlanguageDetectionLanguageDetectionRequest):

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
    body: TranslationlanguageDetectionLanguageDetectionRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Language Detection

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char
    |**google**|`v1`|20.0 (per 1000000 char)|1 char
    |**ibm**|`v1 (2021-08-01)`|20.0 (per 1000000 char)|1000 char
    |**microsoft**|`v3.1`|1.0 (per 1000000 char)|1000 char
    |**neuralspace**|`v1`|7.0 (per 1000 request)|1 request
    |**modernmt**|`1.1.0`|8.0 (per 1000000 char)|1 char
    |**openai**|`v1`|20.0 (per 1000000 token)|1 token


    </details>


    Args:
        body (TranslationlanguageDetectionLanguageDetectionRequest):

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
