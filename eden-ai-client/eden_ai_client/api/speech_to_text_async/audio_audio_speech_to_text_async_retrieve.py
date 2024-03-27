from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_async_job_response import ListAsyncJobResponse
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/audio/speech_to_text_async",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListAsyncJobResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListAsyncJobResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListAsyncJobResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ListAsyncJobResponse]:
    """Speech to Text List Jobs

     Get a list of all jobs launched for this feature. You'll then be able to use the ID of each one to
    get its status and results.<br>
                            Please note that a **job status doesn't get updated until a get request** is
    sent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAsyncJobResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[ListAsyncJobResponse]:
    """Speech to Text List Jobs

     Get a list of all jobs launched for this feature. You'll then be able to use the ID of each one to
    get its status and results.<br>
                            Please note that a **job status doesn't get updated until a get request** is
    sent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAsyncJobResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ListAsyncJobResponse]:
    """Speech to Text List Jobs

     Get a list of all jobs launched for this feature. You'll then be able to use the ID of each one to
    get its status and results.<br>
                            Please note that a **job status doesn't get updated until a get request** is
    sent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAsyncJobResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[ListAsyncJobResponse]:
    """Speech to Text List Jobs

     Get a list of all jobs launched for this feature. You'll then be able to use the ID of each one to
    get its status and results.<br>
                            Please note that a **job status doesn't get updated until a get request** is
    sent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAsyncJobResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
