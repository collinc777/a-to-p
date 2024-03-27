from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.not_found_response import NotFoundResponse
from ...models.yoda_delete_response import YodaDeleteResponse
from ...types import UNSET, Response


def _get_kwargs(
    project_id: str,
    *,
    id: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["id"] = id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/aiproducts/askyoda/v2/{project_id}/delete_chunk",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequest, Error, NotFoundResponse, YodaDeleteResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = YodaDeleteResponse.from_dict(response.json())

        return response_200
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
) -> Response[Union[BadRequest, Error, NotFoundResponse, YodaDeleteResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    id: str,
) -> Response[Union[BadRequest, Error, NotFoundResponse, YodaDeleteResponse]]:
    """Delete Chunk

     Delete a query from your project by its ID.

    Args:
        project_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse, YodaDeleteResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    id: str,
) -> Optional[Union[BadRequest, Error, NotFoundResponse, YodaDeleteResponse]]:
    """Delete Chunk

     Delete a query from your project by its ID.

    Args:
        project_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, NotFoundResponse, YodaDeleteResponse]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    id: str,
) -> Response[Union[BadRequest, Error, NotFoundResponse, YodaDeleteResponse]]:
    """Delete Chunk

     Delete a query from your project by its ID.

    Args:
        project_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse, YodaDeleteResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    id: str,
) -> Optional[Union[BadRequest, Error, NotFoundResponse, YodaDeleteResponse]]:
    """Delete Chunk

     Delete a query from your project by its ID.

    Args:
        project_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, NotFoundResponse, YodaDeleteResponse]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            id=id,
        )
    ).parsed
