from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.universal_translator_list import UniversalTranslatorList
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
        "method": "get",
        "url": f"/aiproducts/translathor/{project_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UniversalTranslatorList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UniversalTranslatorList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UniversalTranslatorList]:
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
) -> Response[UniversalTranslatorList]:
    """List languages

     List all language pairs withing a `project_name`. You should at leat provide one or both of
    `source_lang` and `target_lang`
            query parameters.

    **Example**: to retreive this language pair (Any, Enlish):
    aiproducts/translathor/{project_name}?source_lang=`all`&target_lang=`en`

    Args:
        project_id (str):
        source_lang (str):
        target_lang (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UniversalTranslatorList]
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


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    source_lang: str,
    target_lang: str,
) -> Optional[UniversalTranslatorList]:
    """List languages

     List all language pairs withing a `project_name`. You should at leat provide one or both of
    `source_lang` and `target_lang`
            query parameters.

    **Example**: to retreive this language pair (Any, Enlish):
    aiproducts/translathor/{project_name}?source_lang=`all`&target_lang=`en`

    Args:
        project_id (str):
        source_lang (str):
        target_lang (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UniversalTranslatorList
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        source_lang=source_lang,
        target_lang=target_lang,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    source_lang: str,
    target_lang: str,
) -> Response[UniversalTranslatorList]:
    """List languages

     List all language pairs withing a `project_name`. You should at leat provide one or both of
    `source_lang` and `target_lang`
            query parameters.

    **Example**: to retreive this language pair (Any, Enlish):
    aiproducts/translathor/{project_name}?source_lang=`all`&target_lang=`en`

    Args:
        project_id (str):
        source_lang (str):
        target_lang (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UniversalTranslatorList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        source_lang=source_lang,
        target_lang=target_lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    source_lang: str,
    target_lang: str,
) -> Optional[UniversalTranslatorList]:
    """List languages

     List all language pairs withing a `project_name`. You should at leat provide one or both of
    `source_lang` and `target_lang`
            query parameters.

    **Example**: to retreive this language pair (Any, Enlish):
    aiproducts/translathor/{project_name}?source_lang=`all`&target_lang=`en`

    Args:
        project_id (str):
        source_lang (str):
        target_lang (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UniversalTranslatorList
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            source_lang=source_lang,
            target_lang=target_lang,
        )
    ).parsed
