from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.execution import Execution
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    execution_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/workflow/{workflow_id}/execution/{execution_id}/",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Execution]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Execution.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Execution]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: str,
    execution_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Execution]:
    """Retrieve a specific execution.

    Args:
        workflow_id (str):
        execution_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Execution]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        execution_id=execution_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    execution_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Execution]:
    """Retrieve a specific execution.

    Args:
        workflow_id (str):
        execution_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Execution
    """

    return sync_detailed(
        workflow_id=workflow_id,
        execution_id=execution_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    execution_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Execution]:
    """Retrieve a specific execution.

    Args:
        workflow_id (str):
        execution_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Execution]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        execution_id=execution_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    execution_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Execution]:
    """Retrieve a specific execution.

    Args:
        workflow_id (str):
        execution_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Execution
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            execution_id=execution_id,
            client=client,
        )
    ).parsed
