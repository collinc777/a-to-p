from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_ask_yoda_project_update_request import PatchedAskYodaProjectUpdateRequest
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: PatchedAskYodaProjectUpdateRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/aiproducts/askyoda/v2/{project_id}/update_project",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    body: PatchedAskYodaProjectUpdateRequest,
) -> Response[Any]:
    """Update Project

     Update the default settings of the Yoda project.
    It allows you to modify the project's default settings,
    specifically changing the llm_provider (language model provider),
    llm_model (language model), ocr_provider (upload pdf), speech_to_text provider (upload audio)
    and the default chunks parameter associated with the default project.

    Args:
        project_id (str):
        body (PatchedAskYodaProjectUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedAskYodaProjectUpdateRequest,
) -> Response[Any]:
    """Update Project

     Update the default settings of the Yoda project.
    It allows you to modify the project's default settings,
    specifically changing the llm_provider (language model provider),
    llm_model (language model), ocr_provider (upload pdf), speech_to_text provider (upload audio)
    and the default chunks parameter associated with the default project.

    Args:
        project_id (str):
        body (PatchedAskYodaProjectUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
