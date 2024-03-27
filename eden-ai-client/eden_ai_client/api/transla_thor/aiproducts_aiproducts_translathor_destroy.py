from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    project_id: str,
    *,
    source_lang: str,
    target_lang: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["source_lang"] = source_lang

    params["target_lang"] = target_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/aiproducts/translathor/{project_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
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
    source_lang: str,
    target_lang: str,
) -> Response[Any]:
    """Delete language

     Delete a language pair withing a `project_name`. Both `source_lang` and `target_lang` query
    parameters should be provided.

    **NB**: If  your source or target language references `any language`, use `all` as value for the
    query parameter

    Args:
        project_id (str):
        source_lang (str):
        target_lang (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        source_lang=source_lang,
        target_lang=target_lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    source_lang: str,
    target_lang: str,
) -> Response[Any]:
    """Delete language

     Delete a language pair withing a `project_name`. Both `source_lang` and `target_lang` query
    parameters should be provided.

    **NB**: If  your source or target language references `any language`, use `all` as value for the
    query parameter

    Args:
        project_id (str):
        source_lang (str):
        target_lang (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        source_lang=source_lang,
        target_lang=target_lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
