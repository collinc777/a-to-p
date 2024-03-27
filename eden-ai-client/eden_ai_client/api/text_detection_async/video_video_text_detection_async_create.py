from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_video_analysis_request import AsyncVideoAnalysisRequest
from ...models.launch_async_job_response import LaunchAsyncJobResponse
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        AsyncVideoAnalysisRequest,
        AsyncVideoAnalysisRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/video/text_detection_async",
    }

    if isinstance(body, AsyncVideoAnalysisRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"
    if isinstance(body, AsyncVideoAnalysisRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[LaunchAsyncJobResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LaunchAsyncJobResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[LaunchAsyncJobResponse]:
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
        AsyncVideoAnalysisRequest,
        AsyncVideoAnalysisRequest,
    ],
) -> Response[LaunchAsyncJobResponse]:
    """Text Detection Launch Job

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3`|0.1 (per 60 seconde)|60 seconde
    |**google**|`Video intelligence v1`|0.15 (per 60 seconde)|1 seconde
    |**twelvelabs**|`v1.1.2`|0.067 (per 60 seconde)|60 seconde


    </details>


    Args:
        body (AsyncVideoAnalysisRequest):
        body (AsyncVideoAnalysisRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LaunchAsyncJobResponse]
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
        AsyncVideoAnalysisRequest,
        AsyncVideoAnalysisRequest,
    ],
) -> Optional[LaunchAsyncJobResponse]:
    """Text Detection Launch Job

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3`|0.1 (per 60 seconde)|60 seconde
    |**google**|`Video intelligence v1`|0.15 (per 60 seconde)|1 seconde
    |**twelvelabs**|`v1.1.2`|0.067 (per 60 seconde)|60 seconde


    </details>


    Args:
        body (AsyncVideoAnalysisRequest):
        body (AsyncVideoAnalysisRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LaunchAsyncJobResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        AsyncVideoAnalysisRequest,
        AsyncVideoAnalysisRequest,
    ],
) -> Response[LaunchAsyncJobResponse]:
    """Text Detection Launch Job

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3`|0.1 (per 60 seconde)|60 seconde
    |**google**|`Video intelligence v1`|0.15 (per 60 seconde)|1 seconde
    |**twelvelabs**|`v1.1.2`|0.067 (per 60 seconde)|60 seconde


    </details>


    Args:
        body (AsyncVideoAnalysisRequest):
        body (AsyncVideoAnalysisRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LaunchAsyncJobResponse]
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
        AsyncVideoAnalysisRequest,
        AsyncVideoAnalysisRequest,
    ],
) -> Optional[LaunchAsyncJobResponse]:
    """Text Detection Launch Job

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3`|0.1 (per 60 seconde)|60 seconde
    |**google**|`Video intelligence v1`|0.15 (per 60 seconde)|1 seconde
    |**twelvelabs**|`v1.1.2`|0.067 (per 60 seconde)|60 seconde


    </details>


    Args:
        body (AsyncVideoAnalysisRequest):
        body (AsyncVideoAnalysisRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LaunchAsyncJobResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
