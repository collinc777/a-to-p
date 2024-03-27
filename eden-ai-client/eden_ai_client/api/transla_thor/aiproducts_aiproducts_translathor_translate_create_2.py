from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.aiproducts_aiproducts_translathor_translate_create_2_response_200 import (
    AiproductsAiproductsTranslathorTranslateCreate2Response200,
)
from ...models.universal_translator_call_request import UniversalTranslatorCallRequest
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: Union[
        UniversalTranslatorCallRequest,
        UniversalTranslatorCallRequest,
        UniversalTranslatorCallRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/aiproducts/translathor/{project_id}/translate",
    }

    if isinstance(body, UniversalTranslatorCallRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, UniversalTranslatorCallRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UniversalTranslatorCallRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AiproductsAiproductsTranslathorTranslateCreate2Response200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AiproductsAiproductsTranslathorTranslateCreate2Response200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AiproductsAiproductsTranslathorTranslateCreate2Response200]:
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
        UniversalTranslatorCallRequest,
        UniversalTranslatorCallRequest,
        UniversalTranslatorCallRequest,
    ],
) -> Response[AiproductsAiproductsTranslathorTranslateCreate2Response200]:
    """Translate

    Args:
        project_id (str):
        body (UniversalTranslatorCallRequest):
        body (UniversalTranslatorCallRequest):
        body (UniversalTranslatorCallRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiproductsAiproductsTranslathorTranslateCreate2Response200]
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
        UniversalTranslatorCallRequest,
        UniversalTranslatorCallRequest,
        UniversalTranslatorCallRequest,
    ],
) -> Optional[AiproductsAiproductsTranslathorTranslateCreate2Response200]:
    """Translate

    Args:
        project_id (str):
        body (UniversalTranslatorCallRequest):
        body (UniversalTranslatorCallRequest):
        body (UniversalTranslatorCallRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiproductsAiproductsTranslathorTranslateCreate2Response200
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
        UniversalTranslatorCallRequest,
        UniversalTranslatorCallRequest,
        UniversalTranslatorCallRequest,
    ],
) -> Response[AiproductsAiproductsTranslathorTranslateCreate2Response200]:
    """Translate

    Args:
        project_id (str):
        body (UniversalTranslatorCallRequest):
        body (UniversalTranslatorCallRequest):
        body (UniversalTranslatorCallRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiproductsAiproductsTranslathorTranslateCreate2Response200]
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
        UniversalTranslatorCallRequest,
        UniversalTranslatorCallRequest,
        UniversalTranslatorCallRequest,
    ],
) -> Optional[AiproductsAiproductsTranslathorTranslateCreate2Response200]:
    """Translate

    Args:
        project_id (str):
        body (UniversalTranslatorCallRequest):
        body (UniversalTranslatorCallRequest):
        body (UniversalTranslatorCallRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiproductsAiproductsTranslathorTranslateCreate2Response200
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
