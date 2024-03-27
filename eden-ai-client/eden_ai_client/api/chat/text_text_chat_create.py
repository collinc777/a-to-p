from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.not_found_response import NotFoundResponse
from ...models.textchat_chat_request import TextchatChatRequest
from ...types import Response


def _get_kwargs(
    *,
    body: TextchatChatRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/text/chat",
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
    body: TextchatChatRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Chat

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**openai**|**gpt-3.5-turbo**|`v1Beta`|0.002 (per 1000 token)|1 token
    |**openai**|**gpt-3.5-turbo-1106**|`v1Beta`|0.002 (per 1000 token)|1 token
    |**openai**|-|`v1Beta`|0.002 (per 1000 token)|1 token
    |**openai**|**gpt-4**|`v1Beta`|0.06 (per 1000 token)|1 token
    |**openai**|**gpt-3.5-turbo-0301**|`v1Beta`|0.002 (per 1000 token)|1 token
    |**openai**|**gpt-4-0314**|`v1Beta`|0.06 (per 1000 token)|1 token
    |**openai**|**gpt-3.5-turbo-16k**|`v1Beta`|0.004 (per 1000 token)|1 token
    |**openai**|**gpt-4-1106-preview**|`v1Beta`|0.03 (per 1000 token)|1 token
    |**openai**|**gpt-4-vision-preview**|`v1Beta`|0.03 (per 1000 token)|1 token
    |**google**|-|`v1`|0.5 (per 1000000 char)|1000 char
    |**replicate**|-|`v1`|0.0032 (per 1 exec_time)|1 exec_time
    |**cohere**|**command**|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**cohere**|**command-light**|`2022-12-06`|0.6 (per 1000000 token)|1 token
    |**cohere**|**command-light-nightly**|`2022-12-06`|0.6 (per 1000000 token)|1 token
    |**cohere**|**command-nightly**|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**meta**|-|`v1`|2.56 (per 1000000 token)|1 token
    |**meta**|**llama2-13b-chat-v1**|`v1`|1.0 (per 1000000 token)|1 token
    |**meta**|**llama2-70b-chat-v1**|`v1`|2.56 (per 1000000 token)|1 token
    |**mistral**|-|`v0.0.1`|0.42 (per 1000000 token)|1 token
    |**mistral**|**mistral-medium**|`v0.0.1`|8.1 (per 1000000 token)|1 token
    |**mistral**|**mistral-small**|`v0.0.1`|6.0 (per 1000000 token)|1 token
    |**mistral**|**mistral-tiny**|`v0.0.1`|0.42 (per 1000000 token)|1 token
    |**perplexityai**|**mistral-7b-instruct**|`v1.0`|0.28 (per 1000000 token)|1 token
    |**perplexityai**|**mixtral-8x7b-instruct**|`v1.0`|0.28 (per 1000000 token)|1 token
    |**perplexityai**|**pplx-7b-chat**|`v1.0`|0.28 (per 1000000 token)|1 token
    |**perplexityai**|**pplx-7b-online**|`v1.0`|0.28 (per 1000000 token)|1 token
    |**perplexityai**|**codellama-34b-instruct**|`v1.0`|1.4 (per 1000000 token)|1 token
    |**perplexityai**|**llama-2-70b-chat**|`v1.0`|2.8 (per 1000000 token)|1 token
    |**perplexityai**|**pplx-70b-chat**|`v1.0`|2.8 (per 1000000 token)|1 token
    |**perplexityai**|**pplx-70b-online**|`v1.0`|2.8 (per 1000000 token)|1 token
    |**perplexityai**|-|`v1.0`|2.8 (per 1000000 token)|1 token
    |**anthropic**|-|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1 token
    |**anthropic**|**claude-3-sonnet-20240229-v1:0**|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1
    token
    |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token
    |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**anthropic**|**claude-3-haiku-20240307-v1:0**|`bedrock-2023-05-31`|1.25 (per 1000000 token)|1
    token


    </details>

    <details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|

    </details><details><summary>Supported Models</summary><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`gpt-3.5-turbo`|
    ||`gpt-3.5-turbo-0301`|
    ||`gpt-3.5-turbo-1106`|
    ||`gpt-3.5-turbo-16k`|
    ||`gpt-4`|
    ||`gpt-4-0314`|
    ||`gpt-4-1106-preview`|
    ||`gpt-4-vision-preview`|

    </details><details><summary>google</summary>





    |Name|Value|
    |----|-----|
    |**google**|`chat-bison`|

    </details><details><summary>replicate</summary>





    |Name|Value|
    |----|-----|
    |**replicate**|`llama-2-70b-chat`|

    </details><details><summary>cohere</summary>





    |Name|Value|
    |----|-----|
    |**cohere**|`command`|
    ||`command-light`|
    ||`command-light-nightly`|
    ||`command-nightly`|

    </details><details><summary>meta</summary>





    |Name|Value|
    |----|-----|
    |**meta**|`llama2-13b-chat-v1`|
    ||`llama2-70b-chat-v1`|

    </details><details><summary>mistral</summary>





    |Name|Value|
    |----|-----|
    |**mistral**|`large-latest`|
    ||`medium`|
    ||`small`|
    ||`tiny`|

    </details><details><summary>perplexityai</summary>





    |Name|Value|
    |----|-----|
    |**perplexityai**|`codellama-34b-instruct`|
    ||`llama-2-70b-chat`|
    ||`mistral-7b-instruct`|
    ||`mixtral-8x7b-instruct`|
    ||`pplx-70b-chat`|
    ||`pplx-70b-online`|
    ||`pplx-7b-chat`|
    ||`pplx-7b-online`|

    </details><details><summary>anthropic</summary>





    |Name|Value|
    |----|-----|
    |**anthropic**|`claude-3-sonnet-20240229-v1:0`|
    ||`claude-instant-v1`|
    ||`claude-v2`|

    </details>

    </details>

    Args:
        body (TextchatChatRequest):

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
    body: TextchatChatRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Chat

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**openai**|**gpt-3.5-turbo**|`v1Beta`|0.002 (per 1000 token)|1 token
    |**openai**|**gpt-3.5-turbo-1106**|`v1Beta`|0.002 (per 1000 token)|1 token
    |**openai**|-|`v1Beta`|0.002 (per 1000 token)|1 token
    |**openai**|**gpt-4**|`v1Beta`|0.06 (per 1000 token)|1 token
    |**openai**|**gpt-3.5-turbo-0301**|`v1Beta`|0.002 (per 1000 token)|1 token
    |**openai**|**gpt-4-0314**|`v1Beta`|0.06 (per 1000 token)|1 token
    |**openai**|**gpt-3.5-turbo-16k**|`v1Beta`|0.004 (per 1000 token)|1 token
    |**openai**|**gpt-4-1106-preview**|`v1Beta`|0.03 (per 1000 token)|1 token
    |**openai**|**gpt-4-vision-preview**|`v1Beta`|0.03 (per 1000 token)|1 token
    |**google**|-|`v1`|0.5 (per 1000000 char)|1000 char
    |**replicate**|-|`v1`|0.0032 (per 1 exec_time)|1 exec_time
    |**cohere**|**command**|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**cohere**|**command-light**|`2022-12-06`|0.6 (per 1000000 token)|1 token
    |**cohere**|**command-light-nightly**|`2022-12-06`|0.6 (per 1000000 token)|1 token
    |**cohere**|**command-nightly**|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**meta**|-|`v1`|2.56 (per 1000000 token)|1 token
    |**meta**|**llama2-13b-chat-v1**|`v1`|1.0 (per 1000000 token)|1 token
    |**meta**|**llama2-70b-chat-v1**|`v1`|2.56 (per 1000000 token)|1 token
    |**mistral**|-|`v0.0.1`|0.42 (per 1000000 token)|1 token
    |**mistral**|**mistral-medium**|`v0.0.1`|8.1 (per 1000000 token)|1 token
    |**mistral**|**mistral-small**|`v0.0.1`|6.0 (per 1000000 token)|1 token
    |**mistral**|**mistral-tiny**|`v0.0.1`|0.42 (per 1000000 token)|1 token
    |**perplexityai**|**mistral-7b-instruct**|`v1.0`|0.28 (per 1000000 token)|1 token
    |**perplexityai**|**mixtral-8x7b-instruct**|`v1.0`|0.28 (per 1000000 token)|1 token
    |**perplexityai**|**pplx-7b-chat**|`v1.0`|0.28 (per 1000000 token)|1 token
    |**perplexityai**|**pplx-7b-online**|`v1.0`|0.28 (per 1000000 token)|1 token
    |**perplexityai**|**codellama-34b-instruct**|`v1.0`|1.4 (per 1000000 token)|1 token
    |**perplexityai**|**llama-2-70b-chat**|`v1.0`|2.8 (per 1000000 token)|1 token
    |**perplexityai**|**pplx-70b-chat**|`v1.0`|2.8 (per 1000000 token)|1 token
    |**perplexityai**|**pplx-70b-online**|`v1.0`|2.8 (per 1000000 token)|1 token
    |**perplexityai**|-|`v1.0`|2.8 (per 1000000 token)|1 token
    |**anthropic**|-|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1 token
    |**anthropic**|**claude-3-sonnet-20240229-v1:0**|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1
    token
    |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token
    |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**anthropic**|**claude-3-haiku-20240307-v1:0**|`bedrock-2023-05-31`|1.25 (per 1000000 token)|1
    token


    </details>

    <details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|

    </details><details><summary>Supported Models</summary><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`gpt-3.5-turbo`|
    ||`gpt-3.5-turbo-0301`|
    ||`gpt-3.5-turbo-1106`|
    ||`gpt-3.5-turbo-16k`|
    ||`gpt-4`|
    ||`gpt-4-0314`|
    ||`gpt-4-1106-preview`|
    ||`gpt-4-vision-preview`|

    </details><details><summary>google</summary>





    |Name|Value|
    |----|-----|
    |**google**|`chat-bison`|

    </details><details><summary>replicate</summary>





    |Name|Value|
    |----|-----|
    |**replicate**|`llama-2-70b-chat`|

    </details><details><summary>cohere</summary>





    |Name|Value|
    |----|-----|
    |**cohere**|`command`|
    ||`command-light`|
    ||`command-light-nightly`|
    ||`command-nightly`|

    </details><details><summary>meta</summary>





    |Name|Value|
    |----|-----|
    |**meta**|`llama2-13b-chat-v1`|
    ||`llama2-70b-chat-v1`|

    </details><details><summary>mistral</summary>





    |Name|Value|
    |----|-----|
    |**mistral**|`large-latest`|
    ||`medium`|
    ||`small`|
    ||`tiny`|

    </details><details><summary>perplexityai</summary>





    |Name|Value|
    |----|-----|
    |**perplexityai**|`codellama-34b-instruct`|
    ||`llama-2-70b-chat`|
    ||`mistral-7b-instruct`|
    ||`mixtral-8x7b-instruct`|
    ||`pplx-70b-chat`|
    ||`pplx-70b-online`|
    ||`pplx-7b-chat`|
    ||`pplx-7b-online`|

    </details><details><summary>anthropic</summary>





    |Name|Value|
    |----|-----|
    |**anthropic**|`claude-3-sonnet-20240229-v1:0`|
    ||`claude-instant-v1`|
    ||`claude-v2`|

    </details>

    </details>

    Args:
        body (TextchatChatRequest):

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
    body: TextchatChatRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Chat

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**openai**|**gpt-3.5-turbo**|`v1Beta`|0.002 (per 1000 token)|1 token
    |**openai**|**gpt-3.5-turbo-1106**|`v1Beta`|0.002 (per 1000 token)|1 token
    |**openai**|-|`v1Beta`|0.002 (per 1000 token)|1 token
    |**openai**|**gpt-4**|`v1Beta`|0.06 (per 1000 token)|1 token
    |**openai**|**gpt-3.5-turbo-0301**|`v1Beta`|0.002 (per 1000 token)|1 token
    |**openai**|**gpt-4-0314**|`v1Beta`|0.06 (per 1000 token)|1 token
    |**openai**|**gpt-3.5-turbo-16k**|`v1Beta`|0.004 (per 1000 token)|1 token
    |**openai**|**gpt-4-1106-preview**|`v1Beta`|0.03 (per 1000 token)|1 token
    |**openai**|**gpt-4-vision-preview**|`v1Beta`|0.03 (per 1000 token)|1 token
    |**google**|-|`v1`|0.5 (per 1000000 char)|1000 char
    |**replicate**|-|`v1`|0.0032 (per 1 exec_time)|1 exec_time
    |**cohere**|**command**|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**cohere**|**command-light**|`2022-12-06`|0.6 (per 1000000 token)|1 token
    |**cohere**|**command-light-nightly**|`2022-12-06`|0.6 (per 1000000 token)|1 token
    |**cohere**|**command-nightly**|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**meta**|-|`v1`|2.56 (per 1000000 token)|1 token
    |**meta**|**llama2-13b-chat-v1**|`v1`|1.0 (per 1000000 token)|1 token
    |**meta**|**llama2-70b-chat-v1**|`v1`|2.56 (per 1000000 token)|1 token
    |**mistral**|-|`v0.0.1`|0.42 (per 1000000 token)|1 token
    |**mistral**|**mistral-medium**|`v0.0.1`|8.1 (per 1000000 token)|1 token
    |**mistral**|**mistral-small**|`v0.0.1`|6.0 (per 1000000 token)|1 token
    |**mistral**|**mistral-tiny**|`v0.0.1`|0.42 (per 1000000 token)|1 token
    |**perplexityai**|**mistral-7b-instruct**|`v1.0`|0.28 (per 1000000 token)|1 token
    |**perplexityai**|**mixtral-8x7b-instruct**|`v1.0`|0.28 (per 1000000 token)|1 token
    |**perplexityai**|**pplx-7b-chat**|`v1.0`|0.28 (per 1000000 token)|1 token
    |**perplexityai**|**pplx-7b-online**|`v1.0`|0.28 (per 1000000 token)|1 token
    |**perplexityai**|**codellama-34b-instruct**|`v1.0`|1.4 (per 1000000 token)|1 token
    |**perplexityai**|**llama-2-70b-chat**|`v1.0`|2.8 (per 1000000 token)|1 token
    |**perplexityai**|**pplx-70b-chat**|`v1.0`|2.8 (per 1000000 token)|1 token
    |**perplexityai**|**pplx-70b-online**|`v1.0`|2.8 (per 1000000 token)|1 token
    |**perplexityai**|-|`v1.0`|2.8 (per 1000000 token)|1 token
    |**anthropic**|-|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1 token
    |**anthropic**|**claude-3-sonnet-20240229-v1:0**|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1
    token
    |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token
    |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**anthropic**|**claude-3-haiku-20240307-v1:0**|`bedrock-2023-05-31`|1.25 (per 1000000 token)|1
    token


    </details>

    <details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|

    </details><details><summary>Supported Models</summary><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`gpt-3.5-turbo`|
    ||`gpt-3.5-turbo-0301`|
    ||`gpt-3.5-turbo-1106`|
    ||`gpt-3.5-turbo-16k`|
    ||`gpt-4`|
    ||`gpt-4-0314`|
    ||`gpt-4-1106-preview`|
    ||`gpt-4-vision-preview`|

    </details><details><summary>google</summary>





    |Name|Value|
    |----|-----|
    |**google**|`chat-bison`|

    </details><details><summary>replicate</summary>





    |Name|Value|
    |----|-----|
    |**replicate**|`llama-2-70b-chat`|

    </details><details><summary>cohere</summary>





    |Name|Value|
    |----|-----|
    |**cohere**|`command`|
    ||`command-light`|
    ||`command-light-nightly`|
    ||`command-nightly`|

    </details><details><summary>meta</summary>





    |Name|Value|
    |----|-----|
    |**meta**|`llama2-13b-chat-v1`|
    ||`llama2-70b-chat-v1`|

    </details><details><summary>mistral</summary>





    |Name|Value|
    |----|-----|
    |**mistral**|`large-latest`|
    ||`medium`|
    ||`small`|
    ||`tiny`|

    </details><details><summary>perplexityai</summary>





    |Name|Value|
    |----|-----|
    |**perplexityai**|`codellama-34b-instruct`|
    ||`llama-2-70b-chat`|
    ||`mistral-7b-instruct`|
    ||`mixtral-8x7b-instruct`|
    ||`pplx-70b-chat`|
    ||`pplx-70b-online`|
    ||`pplx-7b-chat`|
    ||`pplx-7b-online`|

    </details><details><summary>anthropic</summary>





    |Name|Value|
    |----|-----|
    |**anthropic**|`claude-3-sonnet-20240229-v1:0`|
    ||`claude-instant-v1`|
    ||`claude-v2`|

    </details>

    </details>

    Args:
        body (TextchatChatRequest):

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
    body: TextchatChatRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Chat

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**openai**|**gpt-3.5-turbo**|`v1Beta`|0.002 (per 1000 token)|1 token
    |**openai**|**gpt-3.5-turbo-1106**|`v1Beta`|0.002 (per 1000 token)|1 token
    |**openai**|-|`v1Beta`|0.002 (per 1000 token)|1 token
    |**openai**|**gpt-4**|`v1Beta`|0.06 (per 1000 token)|1 token
    |**openai**|**gpt-3.5-turbo-0301**|`v1Beta`|0.002 (per 1000 token)|1 token
    |**openai**|**gpt-4-0314**|`v1Beta`|0.06 (per 1000 token)|1 token
    |**openai**|**gpt-3.5-turbo-16k**|`v1Beta`|0.004 (per 1000 token)|1 token
    |**openai**|**gpt-4-1106-preview**|`v1Beta`|0.03 (per 1000 token)|1 token
    |**openai**|**gpt-4-vision-preview**|`v1Beta`|0.03 (per 1000 token)|1 token
    |**google**|-|`v1`|0.5 (per 1000000 char)|1000 char
    |**replicate**|-|`v1`|0.0032 (per 1 exec_time)|1 exec_time
    |**cohere**|**command**|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**cohere**|**command-light**|`2022-12-06`|0.6 (per 1000000 token)|1 token
    |**cohere**|**command-light-nightly**|`2022-12-06`|0.6 (per 1000000 token)|1 token
    |**cohere**|**command-nightly**|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**meta**|-|`v1`|2.56 (per 1000000 token)|1 token
    |**meta**|**llama2-13b-chat-v1**|`v1`|1.0 (per 1000000 token)|1 token
    |**meta**|**llama2-70b-chat-v1**|`v1`|2.56 (per 1000000 token)|1 token
    |**mistral**|-|`v0.0.1`|0.42 (per 1000000 token)|1 token
    |**mistral**|**mistral-medium**|`v0.0.1`|8.1 (per 1000000 token)|1 token
    |**mistral**|**mistral-small**|`v0.0.1`|6.0 (per 1000000 token)|1 token
    |**mistral**|**mistral-tiny**|`v0.0.1`|0.42 (per 1000000 token)|1 token
    |**perplexityai**|**mistral-7b-instruct**|`v1.0`|0.28 (per 1000000 token)|1 token
    |**perplexityai**|**mixtral-8x7b-instruct**|`v1.0`|0.28 (per 1000000 token)|1 token
    |**perplexityai**|**pplx-7b-chat**|`v1.0`|0.28 (per 1000000 token)|1 token
    |**perplexityai**|**pplx-7b-online**|`v1.0`|0.28 (per 1000000 token)|1 token
    |**perplexityai**|**codellama-34b-instruct**|`v1.0`|1.4 (per 1000000 token)|1 token
    |**perplexityai**|**llama-2-70b-chat**|`v1.0`|2.8 (per 1000000 token)|1 token
    |**perplexityai**|**pplx-70b-chat**|`v1.0`|2.8 (per 1000000 token)|1 token
    |**perplexityai**|**pplx-70b-online**|`v1.0`|2.8 (per 1000000 token)|1 token
    |**perplexityai**|-|`v1.0`|2.8 (per 1000000 token)|1 token
    |**anthropic**|-|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1 token
    |**anthropic**|**claude-3-sonnet-20240229-v1:0**|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1
    token
    |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token
    |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**anthropic**|**claude-3-haiku-20240307-v1:0**|`bedrock-2023-05-31`|1.25 (per 1000000 token)|1
    token


    </details>

    <details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|

    </details><details><summary>Supported Models</summary><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`gpt-3.5-turbo`|
    ||`gpt-3.5-turbo-0301`|
    ||`gpt-3.5-turbo-1106`|
    ||`gpt-3.5-turbo-16k`|
    ||`gpt-4`|
    ||`gpt-4-0314`|
    ||`gpt-4-1106-preview`|
    ||`gpt-4-vision-preview`|

    </details><details><summary>google</summary>





    |Name|Value|
    |----|-----|
    |**google**|`chat-bison`|

    </details><details><summary>replicate</summary>





    |Name|Value|
    |----|-----|
    |**replicate**|`llama-2-70b-chat`|

    </details><details><summary>cohere</summary>





    |Name|Value|
    |----|-----|
    |**cohere**|`command`|
    ||`command-light`|
    ||`command-light-nightly`|
    ||`command-nightly`|

    </details><details><summary>meta</summary>





    |Name|Value|
    |----|-----|
    |**meta**|`llama2-13b-chat-v1`|
    ||`llama2-70b-chat-v1`|

    </details><details><summary>mistral</summary>





    |Name|Value|
    |----|-----|
    |**mistral**|`large-latest`|
    ||`medium`|
    ||`small`|
    ||`tiny`|

    </details><details><summary>perplexityai</summary>





    |Name|Value|
    |----|-----|
    |**perplexityai**|`codellama-34b-instruct`|
    ||`llama-2-70b-chat`|
    ||`mistral-7b-instruct`|
    ||`mixtral-8x7b-instruct`|
    ||`pplx-70b-chat`|
    ||`pplx-70b-online`|
    ||`pplx-7b-chat`|
    ||`pplx-7b-online`|

    </details><details><summary>anthropic</summary>





    |Name|Value|
    |----|-----|
    |**anthropic**|`claude-3-sonnet-20240229-v1:0`|
    ||`claude-instant-v1`|
    ||`claude-v2`|

    </details>

    </details>

    Args:
        body (TextchatChatRequest):

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
