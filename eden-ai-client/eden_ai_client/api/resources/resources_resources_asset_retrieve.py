from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_update import AssetUpdate
from ...types import Response


def _get_kwargs(
    resource: str,
    asset: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/resources/{resource}/asset/{asset}/",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[AssetUpdate]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AssetUpdate.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[AssetUpdate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource: str,
    asset: str,
    *,
    client: AuthenticatedClient,
) -> Response[AssetUpdate]:
    """
    Args:
        resource (str):
        asset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetUpdate]
    """

    kwargs = _get_kwargs(
        resource=resource,
        asset=asset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource: str,
    asset: str,
    *,
    client: AuthenticatedClient,
) -> Optional[AssetUpdate]:
    """
    Args:
        resource (str):
        asset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetUpdate
    """

    return sync_detailed(
        resource=resource,
        asset=asset,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource: str,
    asset: str,
    *,
    client: AuthenticatedClient,
) -> Response[AssetUpdate]:
    """
    Args:
        resource (str):
        asset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetUpdate]
    """

    kwargs = _get_kwargs(
        resource=resource,
        asset=asset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource: str,
    asset: str,
    *,
    client: AuthenticatedClient,
) -> Optional[AssetUpdate]:
    """
    Args:
        resource (str):
        asset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetUpdate
    """

    return (
        await asyncio_detailed(
            resource=resource,
            asset=asset,
            client=client,
        )
    ).parsed
