from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.imagebackground_removal_background_removal_request import ImagebackgroundRemovalBackgroundRemovalRequest
from ...models.not_found_response import NotFoundResponse
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        ImagebackgroundRemovalBackgroundRemovalRequest,
        ImagebackgroundRemovalBackgroundRemovalRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/image/background_removal",
    }

    if isinstance(body, ImagebackgroundRemovalBackgroundRemovalRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ImagebackgroundRemovalBackgroundRemovalRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

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
    body: Union[
        ImagebackgroundRemovalBackgroundRemovalRequest,
        ImagebackgroundRemovalBackgroundRemovalRequest,
    ],
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Background Removal

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**api4ai**|`v1.0.0`|50.0 (per 1000 file)|1 file
    |**microsoft**|`v3.2`|1.0 (per 1000 file)|1 file
    |**photoroom**|`v1`|16.0 (per 1000 file)|1 file
    |**sentisight**|`v3.3.1`|1.0 (per 1000 file)|1 file
    |**stabilityai**|`v1Beta`|58.0 (per 1000 file)|1 file


    </details>


    Args:
        body (ImagebackgroundRemovalBackgroundRemovalRequest):
        body (ImagebackgroundRemovalBackgroundRemovalRequest):

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
    body: Union[
        ImagebackgroundRemovalBackgroundRemovalRequest,
        ImagebackgroundRemovalBackgroundRemovalRequest,
    ],
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Background Removal

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**api4ai**|`v1.0.0`|50.0 (per 1000 file)|1 file
    |**microsoft**|`v3.2`|1.0 (per 1000 file)|1 file
    |**photoroom**|`v1`|16.0 (per 1000 file)|1 file
    |**sentisight**|`v3.3.1`|1.0 (per 1000 file)|1 file
    |**stabilityai**|`v1Beta`|58.0 (per 1000 file)|1 file


    </details>


    Args:
        body (ImagebackgroundRemovalBackgroundRemovalRequest):
        body (ImagebackgroundRemovalBackgroundRemovalRequest):

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
    body: Union[
        ImagebackgroundRemovalBackgroundRemovalRequest,
        ImagebackgroundRemovalBackgroundRemovalRequest,
    ],
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Background Removal

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**api4ai**|`v1.0.0`|50.0 (per 1000 file)|1 file
    |**microsoft**|`v3.2`|1.0 (per 1000 file)|1 file
    |**photoroom**|`v1`|16.0 (per 1000 file)|1 file
    |**sentisight**|`v3.3.1`|1.0 (per 1000 file)|1 file
    |**stabilityai**|`v1Beta`|58.0 (per 1000 file)|1 file


    </details>


    Args:
        body (ImagebackgroundRemovalBackgroundRemovalRequest):
        body (ImagebackgroundRemovalBackgroundRemovalRequest):

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
    body: Union[
        ImagebackgroundRemovalBackgroundRemovalRequest,
        ImagebackgroundRemovalBackgroundRemovalRequest,
    ],
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Background Removal

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**api4ai**|`v1.0.0`|50.0 (per 1000 file)|1 file
    |**microsoft**|`v3.2`|1.0 (per 1000 file)|1 file
    |**photoroom**|`v1`|16.0 (per 1000 file)|1 file
    |**sentisight**|`v3.3.1`|1.0 (per 1000 file)|1 file
    |**stabilityai**|`v1Beta`|58.0 (per 1000 file)|1 file


    </details>


    Args:
        body (ImagebackgroundRemovalBackgroundRemovalRequest):
        body (ImagebackgroundRemovalBackgroundRemovalRequest):

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
