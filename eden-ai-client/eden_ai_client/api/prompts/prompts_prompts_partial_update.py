from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_prompt_text_request import PatchedPromptTextRequest
from ...models.prompt_text import PromptText
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    body: Union[
        PatchedPromptTextRequest,
        PatchedPromptTextRequest,
        PatchedPromptTextRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/prompts/{name}/",
    }

    if isinstance(body, PatchedPromptTextRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedPromptTextRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedPromptTextRequest):
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
        PatchedPromptTextRequest,
        PatchedPromptTextRequest,
        PatchedPromptTextRequest,
    ],
) -> Response[PromptText]:
    """Update Prompt

    Args:
        name (str):
        body (PatchedPromptTextRequest):
        body (PatchedPromptTextRequest):
        body (PatchedPromptTextRequest):

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
        PatchedPromptTextRequest,
        PatchedPromptTextRequest,
        PatchedPromptTextRequest,
    ],
) -> Optional[PromptText]:
    """Update Prompt

    Args:
        name (str):
        body (PatchedPromptTextRequest):
        body (PatchedPromptTextRequest):
        body (PatchedPromptTextRequest):

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
        PatchedPromptTextRequest,
        PatchedPromptTextRequest,
        PatchedPromptTextRequest,
    ],
) -> Response[PromptText]:
    """Update Prompt

    Args:
        name (str):
        body (PatchedPromptTextRequest):
        body (PatchedPromptTextRequest):
        body (PatchedPromptTextRequest):

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
        PatchedPromptTextRequest,
        PatchedPromptTextRequest,
        PatchedPromptTextRequest,
    ],
) -> Optional[PromptText]:
    """Update Prompt

    Args:
        name (str):
        body (PatchedPromptTextRequest):
        body (PatchedPromptTextRequest):
        body (PatchedPromptTextRequest):

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
