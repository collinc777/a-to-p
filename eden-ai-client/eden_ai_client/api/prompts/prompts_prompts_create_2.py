from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.prompt_text import PromptText
from ...models.prompt_text_request import PromptTextRequest
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    body: Union[
        PromptTextRequest,
        PromptTextRequest,
        PromptTextRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/prompts/{name}/",
    }

    if isinstance(body, PromptTextRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PromptTextRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PromptTextRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[PromptText]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PromptText.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[PromptText]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        PromptTextRequest,
        PromptTextRequest,
        PromptTextRequest,
    ],
) -> Response[PromptText]:
    """Call Feature with Prompt

     Call a feature using a saved Prompt.

    Args:
        name (str):
        body (PromptTextRequest):
        body (PromptTextRequest):
        body (PromptTextRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PromptText]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        PromptTextRequest,
        PromptTextRequest,
        PromptTextRequest,
    ],
) -> Optional[PromptText]:
    """Call Feature with Prompt

     Call a feature using a saved Prompt.

    Args:
        name (str):
        body (PromptTextRequest):
        body (PromptTextRequest):
        body (PromptTextRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PromptText
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        PromptTextRequest,
        PromptTextRequest,
        PromptTextRequest,
    ],
) -> Response[PromptText]:
    """Call Feature with Prompt

     Call a feature using a saved Prompt.

    Args:
        name (str):
        body (PromptTextRequest):
        body (PromptTextRequest):
        body (PromptTextRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PromptText]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        PromptTextRequest,
        PromptTextRequest,
        PromptTextRequest,
    ],
) -> Optional[PromptText]:
    """Call Feature with Prompt

     Call a feature using a saved Prompt.

    Args:
        name (str):
        body (PromptTextRequest):
        body (PromptTextRequest):
        body (PromptTextRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PromptText
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
        )
    ).parsed