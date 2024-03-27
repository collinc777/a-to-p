from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_create import AssetCreate
from ...models.asset_create_request import AssetCreateRequest
from ...types import Response


def _get_kwargs(
    resource: str,
    *,
    body: AssetCreateRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/resources/{resource}/asset/",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[AssetCreate]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = AssetCreate.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[AssetCreate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource: str,
    *,
    client: AuthenticatedClient,
    body: AssetCreateRequest,
) -> Response[AssetCreate]:
    """
    Args:
        resource (str):
        body (AssetCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetCreate]
    """

    kwargs = _get_kwargs(
        resource=resource,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource: str,
    *,
    client: AuthenticatedClient,
    body: AssetCreateRequest,
) -> Optional[AssetCreate]:
    """
    Args:
        resource (str):
        body (AssetCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetCreate
    """

    return sync_detailed(
        resource=resource,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    resource: str,
    *,
    client: AuthenticatedClient,
    body: AssetCreateRequest,
) -> Response[AssetCreate]:
    """
    Args:
        resource (str):
        body (AssetCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetCreate]
    """

    kwargs = _get_kwargs(
        resource=resource,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource: str,
    *,
    client: AuthenticatedClient,
    body: AssetCreateRequest,
) -> Optional[AssetCreate]:
    """
    Args:
        resource (str):
        body (AssetCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetCreate
    """

    return (
        await asyncio_detailed(
            resource=resource,
            client=client,
            body=body,
        )
    ).parsed
