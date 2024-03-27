from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ask_your_data_project_request import AskYourDataProjectRequest
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.not_found_response import NotFoundResponse
from ...models.yoda_create_project_response import YodaCreateProjectResponse
from ...types import Response


def _get_kwargs(
    *,
    body: AskYourDataProjectRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/aiproducts/askyoda/v2/",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequest, Error, NotFoundResponse, YodaCreateProjectResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = YodaCreateProjectResponse.from_dict(response.json())

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
) -> Response[Union[BadRequest, Error, NotFoundResponse, YodaCreateProjectResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AskYourDataProjectRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse, YodaCreateProjectResponse]]:
    """Create Project

     Allows you to create a new Ask YODA project with specified details.

    Args:
        body (AskYourDataProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse, YodaCreateProjectResponse]]
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
    body: AskYourDataProjectRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse, YodaCreateProjectResponse]]:
    """Create Project

     Allows you to create a new Ask YODA project with specified details.

    Args:
        body (AskYourDataProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, NotFoundResponse, YodaCreateProjectResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AskYourDataProjectRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse, YodaCreateProjectResponse]]:
    """Create Project

     Allows you to create a new Ask YODA project with specified details.

    Args:
        body (AskYourDataProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse, YodaCreateProjectResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AskYourDataProjectRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse, YodaCreateProjectResponse]]:
    """Create Project

     Allows you to create a new Ask YODA project with specified details.

    Args:
        body (AskYourDataProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, NotFoundResponse, YodaCreateProjectResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
