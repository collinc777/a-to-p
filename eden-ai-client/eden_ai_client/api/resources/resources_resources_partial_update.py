from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_resource_update_request import PatchedResourceUpdateRequest
from ...models.resource_update import ResourceUpdate
from ...types import Response


def _get_kwargs(
    resource: str,
    *,
    body: PatchedResourceUpdateRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/resources/{resource}/",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ResourceUpdate]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ResourceUpdate.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ResourceUpdate]:
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
    body: PatchedResourceUpdateRequest,
) -> Response[ResourceUpdate]:
    """
    Args:
        resource (str):
        body (PatchedResourceUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceUpdate]
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
    body: PatchedResourceUpdateRequest,
) -> Optional[ResourceUpdate]:
    """
    Args:
        resource (str):
        body (PatchedResourceUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceUpdate
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
    body: PatchedResourceUpdateRequest,
) -> Response[ResourceUpdate]:
    """
    Args:
        resource (str):
        body (PatchedResourceUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceUpdate]
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
    body: PatchedResourceUpdateRequest,
) -> Optional[ResourceUpdate]:
    """
    Args:
        resource (str):
        body (PatchedResourceUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceUpdate
    """

    return (
        await asyncio_detailed(
            resource=resource,
            client=client,
            body=body,
        )
    ).parsed
