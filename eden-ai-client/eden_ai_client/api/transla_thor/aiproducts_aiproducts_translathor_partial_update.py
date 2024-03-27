from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_universal_translator_createt_request import PatchedUniversalTranslatorCreatetRequest
from ...models.universal_translator_createt import UniversalTranslatorCreatet
from ...types import UNSET, Response


def _get_kwargs(
    project_id: str,
    *,
    body: Union[
        PatchedUniversalTranslatorCreatetRequest,
        PatchedUniversalTranslatorCreatetRequest,
    ],
    source_lang: str,
    target_lang: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["source_lang"] = source_lang

    params["target_lang"] = target_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/aiproducts/translathor/{project_id}",
        "params": params,
    }

    if isinstance(body, PatchedUniversalTranslatorCreatetRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedUniversalTranslatorCreatetRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UniversalTranslatorCreatet]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UniversalTranslatorCreatet.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UniversalTranslatorCreatet]:
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
        PatchedUniversalTranslatorCreatetRequest,
        PatchedUniversalTranslatorCreatetRequest,
    ],
    source_lang: str,
    target_lang: str,
) -> Response[UniversalTranslatorCreatet]:
    """Update language

     Update a language pair withing a `project_name`. Both `source_lang` and `target_lang` query
    parameters should be provided.

    **NB**: If  your source or target language references `any language`, use `all` as value for the
    query parameter

    Args:
        project_id (str):
        source_lang (str):
        target_lang (str):
        body (PatchedUniversalTranslatorCreatetRequest):
        body (PatchedUniversalTranslatorCreatetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UniversalTranslatorCreatet]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        source_lang=source_lang,
        target_lang=target_lang,
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
        PatchedUniversalTranslatorCreatetRequest,
        PatchedUniversalTranslatorCreatetRequest,
    ],
    source_lang: str,
    target_lang: str,
) -> Optional[UniversalTranslatorCreatet]:
    """Update language

     Update a language pair withing a `project_name`. Both `source_lang` and `target_lang` query
    parameters should be provided.

    **NB**: If  your source or target language references `any language`, use `all` as value for the
    query parameter

    Args:
        project_id (str):
        source_lang (str):
        target_lang (str):
        body (PatchedUniversalTranslatorCreatetRequest):
        body (PatchedUniversalTranslatorCreatetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UniversalTranslatorCreatet
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
        source_lang=source_lang,
        target_lang=target_lang,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedUniversalTranslatorCreatetRequest,
        PatchedUniversalTranslatorCreatetRequest,
    ],
    source_lang: str,
    target_lang: str,
) -> Response[UniversalTranslatorCreatet]:
    """Update language

     Update a language pair withing a `project_name`. Both `source_lang` and `target_lang` query
    parameters should be provided.

    **NB**: If  your source or target language references `any language`, use `all` as value for the
    query parameter

    Args:
        project_id (str):
        source_lang (str):
        target_lang (str):
        body (PatchedUniversalTranslatorCreatetRequest):
        body (PatchedUniversalTranslatorCreatetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UniversalTranslatorCreatet]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        source_lang=source_lang,
        target_lang=target_lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedUniversalTranslatorCreatetRequest,
        PatchedUniversalTranslatorCreatetRequest,
    ],
    source_lang: str,
    target_lang: str,
) -> Optional[UniversalTranslatorCreatet]:
    """Update language

     Update a language pair withing a `project_name`. Both `source_lang` and `target_lang` query
    parameters should be provided.

    **NB**: If  your source or target language references `any language`, use `all` as value for the
    query parameter

    Args:
        project_id (str):
        source_lang (str):
        target_lang (str):
        body (PatchedUniversalTranslatorCreatetRequest):
        body (PatchedUniversalTranslatorCreatetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UniversalTranslatorCreatet
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
            source_lang=source_lang,
            target_lang=target_lang,
        )
    ).parsed
