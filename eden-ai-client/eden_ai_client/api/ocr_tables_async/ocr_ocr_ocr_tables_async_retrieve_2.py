from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.not_found_response import NotFoundResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    public_id: str,
    *,
    response_as_dict: Union[Unset, bool] = True,
    show_original_response: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["response_as_dict"] = response_as_dict

    params["show_original_response"] = show_original_response

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/ocr/ocr_tables_async/{public_id}",
        "params": params,
    }

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
    public_id: str,
    *,
    client: AuthenticatedClient,
    response_as_dict: Union[Unset, bool] = True,
    show_original_response: Union[Unset, bool] = False,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """OCR Tables Get Job Results

     Get the status and results of an async job given its ID.

    Args:
        public_id (str):
        response_as_dict (Union[Unset, bool]):  Default: True.
        show_original_response (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse]]
    """

    kwargs = _get_kwargs(
        public_id=public_id,
        response_as_dict=response_as_dict,
        show_original_response=show_original_response,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    public_id: str,
    *,
    client: AuthenticatedClient,
    response_as_dict: Union[Unset, bool] = True,
    show_original_response: Union[Unset, bool] = False,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """OCR Tables Get Job Results

     Get the status and results of an async job given its ID.

    Args:
        public_id (str):
        response_as_dict (Union[Unset, bool]):  Default: True.
        show_original_response (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, NotFoundResponse]
    """

    return sync_detailed(
        public_id=public_id,
        client=client,
        response_as_dict=response_as_dict,
        show_original_response=show_original_response,
    ).parsed


async def asyncio_detailed(
    public_id: str,
    *,
    client: AuthenticatedClient,
    response_as_dict: Union[Unset, bool] = True,
    show_original_response: Union[Unset, bool] = False,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """OCR Tables Get Job Results

     Get the status and results of an async job given its ID.

    Args:
        public_id (str):
        response_as_dict (Union[Unset, bool]):  Default: True.
        show_original_response (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse]]
    """

    kwargs = _get_kwargs(
        public_id=public_id,
        response_as_dict=response_as_dict,
        show_original_response=show_original_response,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    public_id: str,
    *,
    client: AuthenticatedClient,
    response_as_dict: Union[Unset, bool] = True,
    show_original_response: Union[Unset, bool] = False,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """OCR Tables Get Job Results

     Get the status and results of an async job given its ID.

    Args:
        public_id (str):
        response_as_dict (Union[Unset, bool]):  Default: True.
        show_original_response (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, NotFoundResponse]
    """

    return (
        await asyncio_detailed(
            public_id=public_id,
            client=client,
            response_as_dict=response_as_dict,
            show_original_response=show_original_response,
        )
    ).parsed
