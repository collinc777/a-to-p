from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.not_found_response import NotFoundResponse
from ...models.textembeddings_embeddings_request import TextembeddingsEmbeddingsRequest
from ...types import Response


def _get_kwargs(
    *,
    body: TextembeddingsEmbeddingsRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/text/embeddings",
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
    body: TextembeddingsEmbeddingsRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Embeddings

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**openai**|-|`v3.0.0`|0.1 (per 1000000 token)|1 token
    |**google**|-|`v1`|0.1 (per 1000000 char)|1 char
    |**cohere**|-|`v1`|0.1 (per 1000000 char)|1 char
    |**cohere**|**4096embed-english-v2.0**|`v1`|0.1 (per 1000000 char)|1 char
    |**cohere**|**1024embed-english-light-v2.0**|`v1`|0.1 (per 1000000 char)|1 char
    |**cohere**|**768__embed-multilingual-v2.0**|`v1`|0.1 (per 1000000 char)|1 char
    |**mistral**|-|`v0.0.1`|0.1 (per 1000000 token)|1 token
    |**jina**|-|`v1`|0.018 (per 1000000 token)|1 token


    </details>

    <details><summary>Supported Models</summary><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`1536__text-embedding-ada-002`|

    </details><details><summary>google</summary>





    |Name|Value|
    |----|-----|
    |**google**|`768__textembedding-gecko`|

    </details><details><summary>cohere</summary>





    |Name|Value|
    |----|-----|
    |**cohere**|`1024__embed-english-light-v2.0`|
    ||`4096__embed-english-v2.0`|
    ||`768__embed-multilingual-v2.0`|

    </details><details><summary>mistral</summary>





    |Name|Value|
    |----|-----|
    |**mistral**|`1024__mistral-embed`|

    </details><details><summary>jina</summary>





    |Name|Value|
    |----|-----|
    |**jina**|`jina-embeddings-v2-base-code`|
    ||`jina-embeddings-v2-base-de`|
    ||`jina-embeddings-v2-base-en`|
    ||`jina-embeddings-v2-base-es`|
    ||`jina-embeddings-v2-base-zh`|

    </details>

    </details>

    Args:
        body (TextembeddingsEmbeddingsRequest):

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
    body: TextembeddingsEmbeddingsRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Embeddings

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**openai**|-|`v3.0.0`|0.1 (per 1000000 token)|1 token
    |**google**|-|`v1`|0.1 (per 1000000 char)|1 char
    |**cohere**|-|`v1`|0.1 (per 1000000 char)|1 char
    |**cohere**|**4096embed-english-v2.0**|`v1`|0.1 (per 1000000 char)|1 char
    |**cohere**|**1024embed-english-light-v2.0**|`v1`|0.1 (per 1000000 char)|1 char
    |**cohere**|**768__embed-multilingual-v2.0**|`v1`|0.1 (per 1000000 char)|1 char
    |**mistral**|-|`v0.0.1`|0.1 (per 1000000 token)|1 token
    |**jina**|-|`v1`|0.018 (per 1000000 token)|1 token


    </details>

    <details><summary>Supported Models</summary><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`1536__text-embedding-ada-002`|

    </details><details><summary>google</summary>





    |Name|Value|
    |----|-----|
    |**google**|`768__textembedding-gecko`|

    </details><details><summary>cohere</summary>





    |Name|Value|
    |----|-----|
    |**cohere**|`1024__embed-english-light-v2.0`|
    ||`4096__embed-english-v2.0`|
    ||`768__embed-multilingual-v2.0`|

    </details><details><summary>mistral</summary>





    |Name|Value|
    |----|-----|
    |**mistral**|`1024__mistral-embed`|

    </details><details><summary>jina</summary>





    |Name|Value|
    |----|-----|
    |**jina**|`jina-embeddings-v2-base-code`|
    ||`jina-embeddings-v2-base-de`|
    ||`jina-embeddings-v2-base-en`|
    ||`jina-embeddings-v2-base-es`|
    ||`jina-embeddings-v2-base-zh`|

    </details>

    </details>

    Args:
        body (TextembeddingsEmbeddingsRequest):

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
    body: TextembeddingsEmbeddingsRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Embeddings

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**openai**|-|`v3.0.0`|0.1 (per 1000000 token)|1 token
    |**google**|-|`v1`|0.1 (per 1000000 char)|1 char
    |**cohere**|-|`v1`|0.1 (per 1000000 char)|1 char
    |**cohere**|**4096embed-english-v2.0**|`v1`|0.1 (per 1000000 char)|1 char
    |**cohere**|**1024embed-english-light-v2.0**|`v1`|0.1 (per 1000000 char)|1 char
    |**cohere**|**768__embed-multilingual-v2.0**|`v1`|0.1 (per 1000000 char)|1 char
    |**mistral**|-|`v0.0.1`|0.1 (per 1000000 token)|1 token
    |**jina**|-|`v1`|0.018 (per 1000000 token)|1 token


    </details>

    <details><summary>Supported Models</summary><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`1536__text-embedding-ada-002`|

    </details><details><summary>google</summary>





    |Name|Value|
    |----|-----|
    |**google**|`768__textembedding-gecko`|

    </details><details><summary>cohere</summary>





    |Name|Value|
    |----|-----|
    |**cohere**|`1024__embed-english-light-v2.0`|
    ||`4096__embed-english-v2.0`|
    ||`768__embed-multilingual-v2.0`|

    </details><details><summary>mistral</summary>





    |Name|Value|
    |----|-----|
    |**mistral**|`1024__mistral-embed`|

    </details><details><summary>jina</summary>





    |Name|Value|
    |----|-----|
    |**jina**|`jina-embeddings-v2-base-code`|
    ||`jina-embeddings-v2-base-de`|
    ||`jina-embeddings-v2-base-en`|
    ||`jina-embeddings-v2-base-es`|
    ||`jina-embeddings-v2-base-zh`|

    </details>

    </details>

    Args:
        body (TextembeddingsEmbeddingsRequest):

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
    body: TextembeddingsEmbeddingsRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Embeddings

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**openai**|-|`v3.0.0`|0.1 (per 1000000 token)|1 token
    |**google**|-|`v1`|0.1 (per 1000000 char)|1 char
    |**cohere**|-|`v1`|0.1 (per 1000000 char)|1 char
    |**cohere**|**4096embed-english-v2.0**|`v1`|0.1 (per 1000000 char)|1 char
    |**cohere**|**1024embed-english-light-v2.0**|`v1`|0.1 (per 1000000 char)|1 char
    |**cohere**|**768__embed-multilingual-v2.0**|`v1`|0.1 (per 1000000 char)|1 char
    |**mistral**|-|`v0.0.1`|0.1 (per 1000000 token)|1 token
    |**jina**|-|`v1`|0.018 (per 1000000 token)|1 token


    </details>

    <details><summary>Supported Models</summary><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`1536__text-embedding-ada-002`|

    </details><details><summary>google</summary>





    |Name|Value|
    |----|-----|
    |**google**|`768__textembedding-gecko`|

    </details><details><summary>cohere</summary>





    |Name|Value|
    |----|-----|
    |**cohere**|`1024__embed-english-light-v2.0`|
    ||`4096__embed-english-v2.0`|
    ||`768__embed-multilingual-v2.0`|

    </details><details><summary>mistral</summary>





    |Name|Value|
    |----|-----|
    |**mistral**|`1024__mistral-embed`|

    </details><details><summary>jina</summary>





    |Name|Value|
    |----|-----|
    |**jina**|`jina-embeddings-v2-base-code`|
    ||`jina-embeddings-v2-base-de`|
    ||`jina-embeddings-v2-base-en`|
    ||`jina-embeddings-v2-base-es`|
    ||`jina-embeddings-v2-base-zh`|

    </details>

    </details>

    Args:
        body (TextembeddingsEmbeddingsRequest):

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
