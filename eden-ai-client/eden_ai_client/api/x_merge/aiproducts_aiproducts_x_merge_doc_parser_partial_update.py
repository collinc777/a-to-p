from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.doc_parser_update import DocParserUpdate
from ...models.patched_doc_parser_update_request import PatchedDocParserUpdateRequest
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: Union[
        PatchedDocParserUpdateRequest,
        PatchedDocParserUpdateRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/aiproducts/x_merge/doc_parser/{project_id}",
    }

    if isinstance(body, PatchedDocParserUpdateRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedDocParserUpdateRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DocParserUpdate]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DocParserUpdate.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DocParserUpdate]:
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
    body: Union[
        PatchedDocParserUpdateRequest,
        PatchedDocParserUpdateRequest,
    ],
) -> Response[DocParserUpdate]:
    """Update doc_parser project

    Args:
        project_id (str):
        body (PatchedDocParserUpdateRequest):
        body (PatchedDocParserUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DocParserUpdate]
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
    body: Union[
        PatchedDocParserUpdateRequest,
        PatchedDocParserUpdateRequest,
    ],
) -> Optional[DocParserUpdate]:
    """Update doc_parser project

    Args:
        project_id (str):
        body (PatchedDocParserUpdateRequest):
        body (PatchedDocParserUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DocParserUpdate
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
    body: Union[
        PatchedDocParserUpdateRequest,
        PatchedDocParserUpdateRequest,
    ],
) -> Response[DocParserUpdate]:
    """Update doc_parser project

    Args:
        project_id (str):
        body (PatchedDocParserUpdateRequest):
        body (PatchedDocParserUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DocParserUpdate]
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
    body: Union[
        PatchedDocParserUpdateRequest,
        PatchedDocParserUpdateRequest,
    ],
) -> Optional[DocParserUpdate]:
    """Update doc_parser project

    Args:
        project_id (str):
        body (PatchedDocParserUpdateRequest):
        body (PatchedDocParserUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DocParserUpdate
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
