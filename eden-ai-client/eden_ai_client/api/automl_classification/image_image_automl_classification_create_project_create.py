from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.imageautoml_classification_response_model import ImageautomlClassificationResponseModel
from ...models.imageautoml_classificationcreate_project_automl_classification_create_project_request import (
    ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest,
)
from ...models.not_found_response import NotFoundResponse
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest,
        ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/image/automl_classification/create_project",
    }

    if isinstance(body, ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequest, Error, ImageautomlClassificationResponseModel, NotFoundResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ImageautomlClassificationResponseModel.from_dict(response.json())

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
) -> Response[Union[BadRequest, Error, ImageautomlClassificationResponseModel, NotFoundResponse]]:
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
        ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest,
        ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest,
    ],
) -> Response[Union[BadRequest, Error, ImageautomlClassificationResponseModel, NotFoundResponse]]:
    """Automl Classification - Create Project

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**nyckel**|`v1.0.0`|free|-


    </details>


    Args:
        body (ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest):
        body (ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, ImageautomlClassificationResponseModel, NotFoundResponse]]
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
        ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest,
        ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest,
    ],
) -> Optional[Union[BadRequest, Error, ImageautomlClassificationResponseModel, NotFoundResponse]]:
    """Automl Classification - Create Project

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**nyckel**|`v1.0.0`|free|-


    </details>


    Args:
        body (ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest):
        body (ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, ImageautomlClassificationResponseModel, NotFoundResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest,
        ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest,
    ],
) -> Response[Union[BadRequest, Error, ImageautomlClassificationResponseModel, NotFoundResponse]]:
    """Automl Classification - Create Project

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**nyckel**|`v1.0.0`|free|-


    </details>


    Args:
        body (ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest):
        body (ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, ImageautomlClassificationResponseModel, NotFoundResponse]]
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
        ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest,
        ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest,
    ],
) -> Optional[Union[BadRequest, Error, ImageautomlClassificationResponseModel, NotFoundResponse]]:
    """Automl Classification - Create Project

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**nyckel**|`v1.0.0`|free|-


    </details>


    Args:
        body (ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest):
        body (ImageautomlClassificationcreateProjectAutomlClassificationCreateProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, ImageautomlClassificationResponseModel, NotFoundResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
