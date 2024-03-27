from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ask_llm_request import AskLLMRequest
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.not_found_response import NotFoundResponse
from ...models.yoda_query_response import YodaQueryResponse
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: AskLLMRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/aiproducts/askyoda/v2/{project_id}/ask_llm",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequest, Error, NotFoundResponse, YodaQueryResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = YodaQueryResponse.from_dict(response.json())

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
) -> Response[Union[BadRequest, Error, NotFoundResponse, YodaQueryResponse]]:
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
    body: AskLLMRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse, YodaQueryResponse]]:
    """Ask LLM

     Retrieve a list of search query responses and compare them to your
    input. Provide a query, and in return, receive scores for the most relevant items from your project,
    ranked by their proximity to your query.

    Args:
        project_id (str):
        body (AskLLMRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse, YodaQueryResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: AskLLMRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse, YodaQueryResponse]]:
    """Ask LLM

     Retrieve a list of search query responses and compare them to your
    input. Provide a query, and in return, receive scores for the most relevant items from your project,
    ranked by their proximity to your query.

    Args:
        project_id (str):
        body (AskLLMRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, NotFoundResponse, YodaQueryResponse]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: AskLLMRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse, YodaQueryResponse]]:
    """Ask LLM

     Retrieve a list of search query responses and compare them to your
    input. Provide a query, and in return, receive scores for the most relevant items from your project,
    ranked by their proximity to your query.

    Args:
        project_id (str):
        body (AskLLMRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse, YodaQueryResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: AskLLMRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse, YodaQueryResponse]]:
    """Ask LLM

     Retrieve a list of search query responses and compare them to your
    input. Provide a query, and in return, receive scores for the most relevant items from your project,
    ranked by their proximity to your query.

    Args:
        project_id (str):
        body (AskLLMRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, NotFoundResponse, YodaQueryResponse]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
