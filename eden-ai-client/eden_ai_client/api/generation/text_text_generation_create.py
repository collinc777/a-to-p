from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.not_found_response import NotFoundResponse
from ...models.textgeneration_generation_request import TextgenerationGenerationRequest
from ...types import Response


def _get_kwargs(
    *,
    body: TextgenerationGenerationRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/text/generation",
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
    body: TextgenerationGenerationRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Generation

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**cohere**|**command**|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**cohere**|**command-light**|`2022-12-06`|0.6 (per 1000000 token)|1 token
    |**cohere**|**command-light-nightly**|`2022-12-06`|0.6 (per 1000000 token)|1 token
    |**cohere**|**command-nightly**|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**openai**|-|`v1`|2.0 (per 1000000 token)|1 token
    |**openai**|**gpt-3.5-turbo-instruct**|`v1`|2.0 (per 1000000 token)|1 token
    |**openai**|**text-babbage-002**|`v1`|0.4 (per 1000000 token)|1 token
    |**openai**|**text-davinci-002**|`v1`|2.0 (per 1000000 token)|1 token
    |**google**|-|`v1`|0.375 (per 1000000 char)|1000 char
    |**google**|**gemini-pro**|`v1`|0.375 (per 1000000 char)|1000 char
    |**google**|**text-bison**|`v1`|0.5 (per 1000000 char)|1000 char
    |**ai21labs**|-|`v1`|0.0188 (per 1000 token)|1 token
    |**ai21labs**|**j2-mid**|`v1`|0.0125 (per 1000 token)|1 token
    |**ai21labs**|**j2-ultra**|`v1`|0.0188 (per 1000 token)|1 token
    |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token
    |**anthropic**|**claude-v1**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**anthropic**|-|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**mistral**|-|`v0.0.1`|24.0 (per 1000000 token)|1 token
    |**mistral**|**large-latest**|`v0.0.1`|24.0 (per 1000000 token)|1 token
    |**mistral**|**mistral-medium**|`v0.0.1`|8.1 (per 1000000 token)|1 token
    |**mistral**|**mistral-small**|`v0.0.1`|6.0 (per 1000000 token)|1 token
    |**mistral**|**mistral-tiny**|`v0.0.1`|0.42 (per 1000000 token)|1 token
    |**amazon**|-|`v1`|1.6 (per 1000000 token)|1 token
    |**amazon**|**titan-text-express-v1**|`v1`|1.6 (per 1000000 token)|1 token
    |**amazon**|**titan-text-lite-v1**|`v1`|0.4 (per 1000000 token)|1 token
    |**amazon**|**titan-tg1-large**|`v1`|1.6 (per 1000000 token)|1 token
    |**meta**|-|`v1`|2.56 (per 1000000 token)|1 token
    |**meta**|**llama2-13b-chat-v1**|`v1`|1.0 (per 1000000 token)|1 token
    |**meta**|**llama2-70b-chat-v1**|`v1`|2.56 (per 1000000 token)|1 token


    </details>

    <details><summary>Supported Models</summary><details><summary>cohere</summary>





    |Name|Value|
    |----|-----|
    |**cohere**|`command`|
    ||`command-light`|
    ||`command-light-nightly`|
    ||`command-nightly`|

    </details><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`babbage-002`|
    ||`davinci-002`|
    ||`gpt-3.5-turbo-instruct`|

    </details><details><summary>google</summary>





    |Name|Value|
    |----|-----|
    |**google**|`gemini-pro`|
    ||`text-bison`|

    </details><details><summary>ai21labs</summary>





    |Name|Value|
    |----|-----|
    |**ai21labs**|`j2-grande-instruct`|
    ||`j2-jumbo-instruct`|
    ||`j2-mid`|
    ||`j2-ultra`|

    </details><details><summary>anthropic</summary>





    |Name|Value|
    |----|-----|
    |**anthropic**|`claude-instant-v1`|
    ||`claude-v1`|
    ||`claude-v2`|

    </details><details><summary>mistral</summary>





    |Name|Value|
    |----|-----|
    |**mistral**|`large-latest`|
    ||`medium`|
    ||`small`|
    ||`tiny`|

    </details><details><summary>amazon</summary>





    |Name|Value|
    |----|-----|
    |**amazon**|`titan-text-express-v1`|
    ||`titan-text-lite-v1`|
    ||`titan-tg1-large`|

    </details><details><summary>meta</summary>





    |Name|Value|
    |----|-----|
    |**meta**|`llama2-13b-chat-v1`|
    ||`llama2-70b-chat-v1`|

    </details>

    </details>

    Args:
        body (TextgenerationGenerationRequest):

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
    body: TextgenerationGenerationRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Generation

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**cohere**|**command**|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**cohere**|**command-light**|`2022-12-06`|0.6 (per 1000000 token)|1 token
    |**cohere**|**command-light-nightly**|`2022-12-06`|0.6 (per 1000000 token)|1 token
    |**cohere**|**command-nightly**|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**openai**|-|`v1`|2.0 (per 1000000 token)|1 token
    |**openai**|**gpt-3.5-turbo-instruct**|`v1`|2.0 (per 1000000 token)|1 token
    |**openai**|**text-babbage-002**|`v1`|0.4 (per 1000000 token)|1 token
    |**openai**|**text-davinci-002**|`v1`|2.0 (per 1000000 token)|1 token
    |**google**|-|`v1`|0.375 (per 1000000 char)|1000 char
    |**google**|**gemini-pro**|`v1`|0.375 (per 1000000 char)|1000 char
    |**google**|**text-bison**|`v1`|0.5 (per 1000000 char)|1000 char
    |**ai21labs**|-|`v1`|0.0188 (per 1000 token)|1 token
    |**ai21labs**|**j2-mid**|`v1`|0.0125 (per 1000 token)|1 token
    |**ai21labs**|**j2-ultra**|`v1`|0.0188 (per 1000 token)|1 token
    |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token
    |**anthropic**|**claude-v1**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**anthropic**|-|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**mistral**|-|`v0.0.1`|24.0 (per 1000000 token)|1 token
    |**mistral**|**large-latest**|`v0.0.1`|24.0 (per 1000000 token)|1 token
    |**mistral**|**mistral-medium**|`v0.0.1`|8.1 (per 1000000 token)|1 token
    |**mistral**|**mistral-small**|`v0.0.1`|6.0 (per 1000000 token)|1 token
    |**mistral**|**mistral-tiny**|`v0.0.1`|0.42 (per 1000000 token)|1 token
    |**amazon**|-|`v1`|1.6 (per 1000000 token)|1 token
    |**amazon**|**titan-text-express-v1**|`v1`|1.6 (per 1000000 token)|1 token
    |**amazon**|**titan-text-lite-v1**|`v1`|0.4 (per 1000000 token)|1 token
    |**amazon**|**titan-tg1-large**|`v1`|1.6 (per 1000000 token)|1 token
    |**meta**|-|`v1`|2.56 (per 1000000 token)|1 token
    |**meta**|**llama2-13b-chat-v1**|`v1`|1.0 (per 1000000 token)|1 token
    |**meta**|**llama2-70b-chat-v1**|`v1`|2.56 (per 1000000 token)|1 token


    </details>

    <details><summary>Supported Models</summary><details><summary>cohere</summary>





    |Name|Value|
    |----|-----|
    |**cohere**|`command`|
    ||`command-light`|
    ||`command-light-nightly`|
    ||`command-nightly`|

    </details><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`babbage-002`|
    ||`davinci-002`|
    ||`gpt-3.5-turbo-instruct`|

    </details><details><summary>google</summary>





    |Name|Value|
    |----|-----|
    |**google**|`gemini-pro`|
    ||`text-bison`|

    </details><details><summary>ai21labs</summary>





    |Name|Value|
    |----|-----|
    |**ai21labs**|`j2-grande-instruct`|
    ||`j2-jumbo-instruct`|
    ||`j2-mid`|
    ||`j2-ultra`|

    </details><details><summary>anthropic</summary>





    |Name|Value|
    |----|-----|
    |**anthropic**|`claude-instant-v1`|
    ||`claude-v1`|
    ||`claude-v2`|

    </details><details><summary>mistral</summary>





    |Name|Value|
    |----|-----|
    |**mistral**|`large-latest`|
    ||`medium`|
    ||`small`|
    ||`tiny`|

    </details><details><summary>amazon</summary>





    |Name|Value|
    |----|-----|
    |**amazon**|`titan-text-express-v1`|
    ||`titan-text-lite-v1`|
    ||`titan-tg1-large`|

    </details><details><summary>meta</summary>





    |Name|Value|
    |----|-----|
    |**meta**|`llama2-13b-chat-v1`|
    ||`llama2-70b-chat-v1`|

    </details>

    </details>

    Args:
        body (TextgenerationGenerationRequest):

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
    body: TextgenerationGenerationRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Generation

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**cohere**|**command**|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**cohere**|**command-light**|`2022-12-06`|0.6 (per 1000000 token)|1 token
    |**cohere**|**command-light-nightly**|`2022-12-06`|0.6 (per 1000000 token)|1 token
    |**cohere**|**command-nightly**|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**openai**|-|`v1`|2.0 (per 1000000 token)|1 token
    |**openai**|**gpt-3.5-turbo-instruct**|`v1`|2.0 (per 1000000 token)|1 token
    |**openai**|**text-babbage-002**|`v1`|0.4 (per 1000000 token)|1 token
    |**openai**|**text-davinci-002**|`v1`|2.0 (per 1000000 token)|1 token
    |**google**|-|`v1`|0.375 (per 1000000 char)|1000 char
    |**google**|**gemini-pro**|`v1`|0.375 (per 1000000 char)|1000 char
    |**google**|**text-bison**|`v1`|0.5 (per 1000000 char)|1000 char
    |**ai21labs**|-|`v1`|0.0188 (per 1000 token)|1 token
    |**ai21labs**|**j2-mid**|`v1`|0.0125 (per 1000 token)|1 token
    |**ai21labs**|**j2-ultra**|`v1`|0.0188 (per 1000 token)|1 token
    |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token
    |**anthropic**|**claude-v1**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**anthropic**|-|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**mistral**|-|`v0.0.1`|24.0 (per 1000000 token)|1 token
    |**mistral**|**large-latest**|`v0.0.1`|24.0 (per 1000000 token)|1 token
    |**mistral**|**mistral-medium**|`v0.0.1`|8.1 (per 1000000 token)|1 token
    |**mistral**|**mistral-small**|`v0.0.1`|6.0 (per 1000000 token)|1 token
    |**mistral**|**mistral-tiny**|`v0.0.1`|0.42 (per 1000000 token)|1 token
    |**amazon**|-|`v1`|1.6 (per 1000000 token)|1 token
    |**amazon**|**titan-text-express-v1**|`v1`|1.6 (per 1000000 token)|1 token
    |**amazon**|**titan-text-lite-v1**|`v1`|0.4 (per 1000000 token)|1 token
    |**amazon**|**titan-tg1-large**|`v1`|1.6 (per 1000000 token)|1 token
    |**meta**|-|`v1`|2.56 (per 1000000 token)|1 token
    |**meta**|**llama2-13b-chat-v1**|`v1`|1.0 (per 1000000 token)|1 token
    |**meta**|**llama2-70b-chat-v1**|`v1`|2.56 (per 1000000 token)|1 token


    </details>

    <details><summary>Supported Models</summary><details><summary>cohere</summary>





    |Name|Value|
    |----|-----|
    |**cohere**|`command`|
    ||`command-light`|
    ||`command-light-nightly`|
    ||`command-nightly`|

    </details><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`babbage-002`|
    ||`davinci-002`|
    ||`gpt-3.5-turbo-instruct`|

    </details><details><summary>google</summary>





    |Name|Value|
    |----|-----|
    |**google**|`gemini-pro`|
    ||`text-bison`|

    </details><details><summary>ai21labs</summary>





    |Name|Value|
    |----|-----|
    |**ai21labs**|`j2-grande-instruct`|
    ||`j2-jumbo-instruct`|
    ||`j2-mid`|
    ||`j2-ultra`|

    </details><details><summary>anthropic</summary>





    |Name|Value|
    |----|-----|
    |**anthropic**|`claude-instant-v1`|
    ||`claude-v1`|
    ||`claude-v2`|

    </details><details><summary>mistral</summary>





    |Name|Value|
    |----|-----|
    |**mistral**|`large-latest`|
    ||`medium`|
    ||`small`|
    ||`tiny`|

    </details><details><summary>amazon</summary>





    |Name|Value|
    |----|-----|
    |**amazon**|`titan-text-express-v1`|
    ||`titan-text-lite-v1`|
    ||`titan-tg1-large`|

    </details><details><summary>meta</summary>





    |Name|Value|
    |----|-----|
    |**meta**|`llama2-13b-chat-v1`|
    ||`llama2-70b-chat-v1`|

    </details>

    </details>

    Args:
        body (TextgenerationGenerationRequest):

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
    body: TextgenerationGenerationRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Generation

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**cohere**|**command**|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**cohere**|**command-light**|`2022-12-06`|0.6 (per 1000000 token)|1 token
    |**cohere**|**command-light-nightly**|`2022-12-06`|0.6 (per 1000000 token)|1 token
    |**cohere**|**command-nightly**|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**openai**|-|`v1`|2.0 (per 1000000 token)|1 token
    |**openai**|**gpt-3.5-turbo-instruct**|`v1`|2.0 (per 1000000 token)|1 token
    |**openai**|**text-babbage-002**|`v1`|0.4 (per 1000000 token)|1 token
    |**openai**|**text-davinci-002**|`v1`|2.0 (per 1000000 token)|1 token
    |**google**|-|`v1`|0.375 (per 1000000 char)|1000 char
    |**google**|**gemini-pro**|`v1`|0.375 (per 1000000 char)|1000 char
    |**google**|**text-bison**|`v1`|0.5 (per 1000000 char)|1000 char
    |**ai21labs**|-|`v1`|0.0188 (per 1000 token)|1 token
    |**ai21labs**|**j2-mid**|`v1`|0.0125 (per 1000 token)|1 token
    |**ai21labs**|**j2-ultra**|`v1`|0.0188 (per 1000 token)|1 token
    |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token
    |**anthropic**|**claude-v1**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**anthropic**|-|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**mistral**|-|`v0.0.1`|24.0 (per 1000000 token)|1 token
    |**mistral**|**large-latest**|`v0.0.1`|24.0 (per 1000000 token)|1 token
    |**mistral**|**mistral-medium**|`v0.0.1`|8.1 (per 1000000 token)|1 token
    |**mistral**|**mistral-small**|`v0.0.1`|6.0 (per 1000000 token)|1 token
    |**mistral**|**mistral-tiny**|`v0.0.1`|0.42 (per 1000000 token)|1 token
    |**amazon**|-|`v1`|1.6 (per 1000000 token)|1 token
    |**amazon**|**titan-text-express-v1**|`v1`|1.6 (per 1000000 token)|1 token
    |**amazon**|**titan-text-lite-v1**|`v1`|0.4 (per 1000000 token)|1 token
    |**amazon**|**titan-tg1-large**|`v1`|1.6 (per 1000000 token)|1 token
    |**meta**|-|`v1`|2.56 (per 1000000 token)|1 token
    |**meta**|**llama2-13b-chat-v1**|`v1`|1.0 (per 1000000 token)|1 token
    |**meta**|**llama2-70b-chat-v1**|`v1`|2.56 (per 1000000 token)|1 token


    </details>

    <details><summary>Supported Models</summary><details><summary>cohere</summary>





    |Name|Value|
    |----|-----|
    |**cohere**|`command`|
    ||`command-light`|
    ||`command-light-nightly`|
    ||`command-nightly`|

    </details><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`babbage-002`|
    ||`davinci-002`|
    ||`gpt-3.5-turbo-instruct`|

    </details><details><summary>google</summary>





    |Name|Value|
    |----|-----|
    |**google**|`gemini-pro`|
    ||`text-bison`|

    </details><details><summary>ai21labs</summary>





    |Name|Value|
    |----|-----|
    |**ai21labs**|`j2-grande-instruct`|
    ||`j2-jumbo-instruct`|
    ||`j2-mid`|
    ||`j2-ultra`|

    </details><details><summary>anthropic</summary>





    |Name|Value|
    |----|-----|
    |**anthropic**|`claude-instant-v1`|
    ||`claude-v1`|
    ||`claude-v2`|

    </details><details><summary>mistral</summary>





    |Name|Value|
    |----|-----|
    |**mistral**|`large-latest`|
    ||`medium`|
    ||`small`|
    ||`tiny`|

    </details><details><summary>amazon</summary>





    |Name|Value|
    |----|-----|
    |**amazon**|`titan-text-express-v1`|
    ||`titan-text-lite-v1`|
    ||`titan-tg1-large`|

    </details><details><summary>meta</summary>





    |Name|Value|
    |----|-----|
    |**meta**|`llama2-13b-chat-v1`|
    ||`llama2-70b-chat-v1`|

    </details>

    </details>

    Args:
        body (TextgenerationGenerationRequest):

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
