from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.universal_translator_createt import UniversalTranslatorCreatet
from ...models.universal_translator_createt_request import UniversalTranslatorCreatetRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        UniversalTranslatorCreatetRequest,
        UniversalTranslatorCreatetRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/aiproducts/translathor/",
    }

    if isinstance(body, UniversalTranslatorCreatetRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, UniversalTranslatorCreatetRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UniversalTranslatorCreatet]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = UniversalTranslatorCreatet.from_dict(response.json())

        return response_201
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
    *,
    client: AuthenticatedClient,
    body: Union[
        UniversalTranslatorCreatetRequest,
        UniversalTranslatorCreatetRequest,
    ],
) -> Response[UniversalTranslatorCreatet]:
    """Create Language Provider Pair

     Create a new language pair, and associate it to an existing project. If the project does not exist,
    a new project will be
            created

    Args:
        body (UniversalTranslatorCreatetRequest):
        body (UniversalTranslatorCreatetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UniversalTranslatorCreatet]
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
        UniversalTranslatorCreatetRequest,
        UniversalTranslatorCreatetRequest,
    ],
) -> Optional[UniversalTranslatorCreatet]:
    """Create Language Provider Pair

     Create a new language pair, and associate it to an existing project. If the project does not exist,
    a new project will be
            created

    Args:
        body (UniversalTranslatorCreatetRequest):
        body (UniversalTranslatorCreatetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UniversalTranslatorCreatet
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        UniversalTranslatorCreatetRequest,
        UniversalTranslatorCreatetRequest,
    ],
) -> Response[UniversalTranslatorCreatet]:
    """Create Language Provider Pair

     Create a new language pair, and associate it to an existing project. If the project does not exist,
    a new project will be
            created

    Args:
        body (UniversalTranslatorCreatetRequest):
        body (UniversalTranslatorCreatetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UniversalTranslatorCreatet]
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
        UniversalTranslatorCreatetRequest,
        UniversalTranslatorCreatetRequest,
    ],
) -> Optional[UniversalTranslatorCreatet]:
    """Create Language Provider Pair

     Create a new language pair, and associate it to an existing project. If the project does not exist,
    a new project will be
            created

    Args:
        body (UniversalTranslatorCreatetRequest):
        body (UniversalTranslatorCreatetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UniversalTranslatorCreatet
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
