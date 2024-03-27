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
    *,
    attributes_as_list: Union[Unset, bool] = False,
    fallback_providers: Union[None, Unset, str] = UNSET,
    providers: str,
    response_as_dict: Union[Unset, bool] = True,
    show_original_response: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["attributes_as_list"] = attributes_as_list

    json_fallback_providers: Union[None, Unset, str]
    if isinstance(fallback_providers, Unset):
        json_fallback_providers = UNSET
    else:
        json_fallback_providers = fallback_providers
    params["fallback_providers"] = json_fallback_providers

    params["providers"] = providers

    params["response_as_dict"] = response_as_dict

    params["show_original_response"] = show_original_response

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/image/face_recognition/list_faces",
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
    *,
    client: AuthenticatedClient,
    attributes_as_list: Union[Unset, bool] = False,
    fallback_providers: Union[None, Unset, str] = UNSET,
    providers: str,
    response_as_dict: Union[Unset, bool] = True,
    show_original_response: Union[Unset, bool] = False,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Face Recognition - List Faces

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 1.26.8`|free|-
    |**facepp**|`v3`|0.1 (per 1000 request)|1 request


    </details>


    Args:
        attributes_as_list (Union[Unset, bool]):  Default: False.
        fallback_providers (Union[None, Unset, str]):
        providers (str):
        response_as_dict (Union[Unset, bool]):  Default: True.
        show_original_response (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse]]
    """

    kwargs = _get_kwargs(
        attributes_as_list=attributes_as_list,
        fallback_providers=fallback_providers,
        providers=providers,
        response_as_dict=response_as_dict,
        show_original_response=show_original_response,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    attributes_as_list: Union[Unset, bool] = False,
    fallback_providers: Union[None, Unset, str] = UNSET,
    providers: str,
    response_as_dict: Union[Unset, bool] = True,
    show_original_response: Union[Unset, bool] = False,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Face Recognition - List Faces

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 1.26.8`|free|-
    |**facepp**|`v3`|0.1 (per 1000 request)|1 request


    </details>


    Args:
        attributes_as_list (Union[Unset, bool]):  Default: False.
        fallback_providers (Union[None, Unset, str]):
        providers (str):
        response_as_dict (Union[Unset, bool]):  Default: True.
        show_original_response (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, NotFoundResponse]
    """

    return sync_detailed(
        client=client,
        attributes_as_list=attributes_as_list,
        fallback_providers=fallback_providers,
        providers=providers,
        response_as_dict=response_as_dict,
        show_original_response=show_original_response,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    attributes_as_list: Union[Unset, bool] = False,
    fallback_providers: Union[None, Unset, str] = UNSET,
    providers: str,
    response_as_dict: Union[Unset, bool] = True,
    show_original_response: Union[Unset, bool] = False,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Face Recognition - List Faces

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 1.26.8`|free|-
    |**facepp**|`v3`|0.1 (per 1000 request)|1 request


    </details>


    Args:
        attributes_as_list (Union[Unset, bool]):  Default: False.
        fallback_providers (Union[None, Unset, str]):
        providers (str):
        response_as_dict (Union[Unset, bool]):  Default: True.
        show_original_response (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse]]
    """

    kwargs = _get_kwargs(
        attributes_as_list=attributes_as_list,
        fallback_providers=fallback_providers,
        providers=providers,
        response_as_dict=response_as_dict,
        show_original_response=show_original_response,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    attributes_as_list: Union[Unset, bool] = False,
    fallback_providers: Union[None, Unset, str] = UNSET,
    providers: str,
    response_as_dict: Union[Unset, bool] = True,
    show_original_response: Union[Unset, bool] = False,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Face Recognition - List Faces

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 1.26.8`|free|-
    |**facepp**|`v3`|0.1 (per 1000 request)|1 request


    </details>


    Args:
        attributes_as_list (Union[Unset, bool]):  Default: False.
        fallback_providers (Union[None, Unset, str]):
        providers (str):
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
            client=client,
            attributes_as_list=attributes_as_list,
            fallback_providers=fallback_providers,
            providers=providers,
            response_as_dict=response_as_dict,
            show_original_response=show_original_response,
        )
    ).parsed
