from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.feature_batch_retrieve_status import FeatureBatchRetrieveStatus
from ...models.not_found_response import NotFoundResponse
from ...models.paginated_batch_response import PaginatedBatchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    feature: str,
    subfeature: str,
    name_path: str,
    *,
    name_query: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    public_id: Union[Unset, int] = UNSET,
    status: Union[Unset, FeatureBatchRetrieveStatus] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["name"] = name_query

    params["page"] = page

    params["public_id"] = public_id

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{feature}/{subfeature}/batch/{name_path}/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequest, Error, NotFoundResponse, PaginatedBatchResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedBatchResponse.from_dict(response.json())

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
) -> Response[Union[BadRequest, Error, NotFoundResponse, PaginatedBatchResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    feature: str,
    subfeature: str,
    name_path: str,
    *,
    client: AuthenticatedClient,
    name_query: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    public_id: Union[Unset, int] = UNSET,
    status: Union[Unset, FeatureBatchRetrieveStatus] = UNSET,
) -> Response[Union[BadRequest, Error, NotFoundResponse, PaginatedBatchResponse]]:
    """Get Batch Job Result

     Return paginated response of requests with their status and their
    responses if the request succeeded or errror if failed

    Args:
        feature (str):
        subfeature (str):
        name_path (str):
        name_query (Union[Unset, str]):
        page (Union[Unset, int]):
        public_id (Union[Unset, int]):
        status (Union[Unset, FeatureBatchRetrieveStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse, PaginatedBatchResponse]]
    """

    kwargs = _get_kwargs(
        feature=feature,
        subfeature=subfeature,
        name_path=name_path,
        name_query=name_query,
        page=page,
        public_id=public_id,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    feature: str,
    subfeature: str,
    name_path: str,
    *,
    client: AuthenticatedClient,
    name_query: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    public_id: Union[Unset, int] = UNSET,
    status: Union[Unset, FeatureBatchRetrieveStatus] = UNSET,
) -> Optional[Union[BadRequest, Error, NotFoundResponse, PaginatedBatchResponse]]:
    """Get Batch Job Result

     Return paginated response of requests with their status and their
    responses if the request succeeded or errror if failed

    Args:
        feature (str):
        subfeature (str):
        name_path (str):
        name_query (Union[Unset, str]):
        page (Union[Unset, int]):
        public_id (Union[Unset, int]):
        status (Union[Unset, FeatureBatchRetrieveStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, NotFoundResponse, PaginatedBatchResponse]
    """

    return sync_detailed(
        feature=feature,
        subfeature=subfeature,
        name_path=name_path,
        client=client,
        name_query=name_query,
        page=page,
        public_id=public_id,
        status=status,
    ).parsed


async def asyncio_detailed(
    feature: str,
    subfeature: str,
    name_path: str,
    *,
    client: AuthenticatedClient,
    name_query: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    public_id: Union[Unset, int] = UNSET,
    status: Union[Unset, FeatureBatchRetrieveStatus] = UNSET,
) -> Response[Union[BadRequest, Error, NotFoundResponse, PaginatedBatchResponse]]:
    """Get Batch Job Result

     Return paginated response of requests with their status and their
    responses if the request succeeded or errror if failed

    Args:
        feature (str):
        subfeature (str):
        name_path (str):
        name_query (Union[Unset, str]):
        page (Union[Unset, int]):
        public_id (Union[Unset, int]):
        status (Union[Unset, FeatureBatchRetrieveStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse, PaginatedBatchResponse]]
    """

    kwargs = _get_kwargs(
        feature=feature,
        subfeature=subfeature,
        name_path=name_path,
        name_query=name_query,
        page=page,
        public_id=public_id,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    feature: str,
    subfeature: str,
    name_path: str,
    *,
    client: AuthenticatedClient,
    name_query: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    public_id: Union[Unset, int] = UNSET,
    status: Union[Unset, FeatureBatchRetrieveStatus] = UNSET,
) -> Optional[Union[BadRequest, Error, NotFoundResponse, PaginatedBatchResponse]]:
    """Get Batch Job Result

     Return paginated response of requests with their status and their
    responses if the request succeeded or errror if failed

    Args:
        feature (str):
        subfeature (str):
        name_path (str):
        name_query (Union[Unset, str]):
        page (Union[Unset, int]):
        public_id (Union[Unset, int]):
        status (Union[Unset, FeatureBatchRetrieveStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, NotFoundResponse, PaginatedBatchResponse]
    """

    return (
        await asyncio_detailed(
            feature=feature,
            subfeature=subfeature,
            name_path=name_path,
            client=client,
            name_query=name_query,
            page=page,
            public_id=public_id,
            status=status,
        )
    ).parsed
