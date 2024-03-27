from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.execution_list import ExecutionList
from ...models.execution_list_request import ExecutionListRequest
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    *,
    body: Union[
        ExecutionListRequest,
        ExecutionListRequest,
        ExecutionListRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/workflow/{workflow_id}/execution/",
    }

    if isinstance(body, ExecutionListRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ExecutionListRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ExecutionListRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ExecutionList]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ExecutionList.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ExecutionList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        ExecutionListRequest,
        ExecutionListRequest,
        ExecutionListRequest,
    ],
) -> Response[ExecutionList]:
    """
    Args:
        workflow_id (str):
        body (ExecutionListRequest):
        body (ExecutionListRequest):
        body (ExecutionListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecutionList]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        ExecutionListRequest,
        ExecutionListRequest,
        ExecutionListRequest,
    ],
) -> Optional[ExecutionList]:
    """
    Args:
        workflow_id (str):
        body (ExecutionListRequest):
        body (ExecutionListRequest):
        body (ExecutionListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecutionList
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        ExecutionListRequest,
        ExecutionListRequest,
        ExecutionListRequest,
    ],
) -> Response[ExecutionList]:
    """
    Args:
        workflow_id (str):
        body (ExecutionListRequest):
        body (ExecutionListRequest):
        body (ExecutionListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecutionList]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        ExecutionListRequest,
        ExecutionListRequest,
        ExecutionListRequest,
    ],
) -> Optional[ExecutionList]:
    """
    Args:
        workflow_id (str):
        body (ExecutionListRequest):
        body (ExecutionListRequest):
        body (ExecutionListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecutionList
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            body=body,
        )
    ).parsed
