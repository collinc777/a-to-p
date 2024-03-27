from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.provider_subfeature import ProviderSubfeature
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    feature_name: Union[Unset, str] = UNSET,
    gender: Union[Unset, str] = UNSET,
    is_working: Union[Unset, bool] = UNSET,
    language: Union[Unset, str] = UNSET,
    phase_name: Union[Unset, str] = UNSET,
    provider_name: Union[Unset, str] = UNSET,
    subfeature_name: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["feature__name"] = feature_name

    params["gender"] = gender

    params["is_working"] = is_working

    params["language"] = language

    params["phase__name"] = phase_name

    params["provider__name"] = provider_name

    params["subfeature__name"] = subfeature_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/info/provider_subfeatures",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["ProviderSubfeature"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProviderSubfeature.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["ProviderSubfeature"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    feature_name: Union[Unset, str] = UNSET,
    gender: Union[Unset, str] = UNSET,
    is_working: Union[Unset, bool] = UNSET,
    language: Union[Unset, str] = UNSET,
    phase_name: Union[Unset, str] = UNSET,
    provider_name: Union[Unset, str] = UNSET,
    subfeature_name: Union[Unset, str] = UNSET,
) -> Response[List["ProviderSubfeature"]]:
    """List Providers Subfeatures

     List Provider and features relations : You can get a list of *all providers* for a *feature* or *all
    features* for a *given provider*.

    You can have the detailed information on the **pricing**, **supported languages** as well as the
    **models** for providers who propose different models (eg: voice models available for a text to
    speech provider).

    Example : If you want the detailed list of all providers that can analyse the sentiment of a text
    written in french, you'd need to set `feature__name=text`,  `subfeature__name=sentiment_analysis`
    and `languages=fr`.

    Which will look like the following :


    ```bash
    curl --request GET  https://api.edenai.run/v2/info/provider_subfeatures?subfeature__name=sentiment_a
    nalysis&feature__name=text&languages=fr
    ```

    Args:
        feature_name (Union[Unset, str]):
        gender (Union[Unset, str]):
        is_working (Union[Unset, bool]):
        language (Union[Unset, str]):
        phase_name (Union[Unset, str]):
        provider_name (Union[Unset, str]):
        subfeature_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ProviderSubfeature']]
    """

    kwargs = _get_kwargs(
        feature_name=feature_name,
        gender=gender,
        is_working=is_working,
        language=language,
        phase_name=phase_name,
        provider_name=provider_name,
        subfeature_name=subfeature_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    feature_name: Union[Unset, str] = UNSET,
    gender: Union[Unset, str] = UNSET,
    is_working: Union[Unset, bool] = UNSET,
    language: Union[Unset, str] = UNSET,
    phase_name: Union[Unset, str] = UNSET,
    provider_name: Union[Unset, str] = UNSET,
    subfeature_name: Union[Unset, str] = UNSET,
) -> Optional[List["ProviderSubfeature"]]:
    """List Providers Subfeatures

     List Provider and features relations : You can get a list of *all providers* for a *feature* or *all
    features* for a *given provider*.

    You can have the detailed information on the **pricing**, **supported languages** as well as the
    **models** for providers who propose different models (eg: voice models available for a text to
    speech provider).

    Example : If you want the detailed list of all providers that can analyse the sentiment of a text
    written in french, you'd need to set `feature__name=text`,  `subfeature__name=sentiment_analysis`
    and `languages=fr`.

    Which will look like the following :


    ```bash
    curl --request GET  https://api.edenai.run/v2/info/provider_subfeatures?subfeature__name=sentiment_a
    nalysis&feature__name=text&languages=fr
    ```

    Args:
        feature_name (Union[Unset, str]):
        gender (Union[Unset, str]):
        is_working (Union[Unset, bool]):
        language (Union[Unset, str]):
        phase_name (Union[Unset, str]):
        provider_name (Union[Unset, str]):
        subfeature_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ProviderSubfeature']
    """

    return sync_detailed(
        client=client,
        feature_name=feature_name,
        gender=gender,
        is_working=is_working,
        language=language,
        phase_name=phase_name,
        provider_name=provider_name,
        subfeature_name=subfeature_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    feature_name: Union[Unset, str] = UNSET,
    gender: Union[Unset, str] = UNSET,
    is_working: Union[Unset, bool] = UNSET,
    language: Union[Unset, str] = UNSET,
    phase_name: Union[Unset, str] = UNSET,
    provider_name: Union[Unset, str] = UNSET,
    subfeature_name: Union[Unset, str] = UNSET,
) -> Response[List["ProviderSubfeature"]]:
    """List Providers Subfeatures

     List Provider and features relations : You can get a list of *all providers* for a *feature* or *all
    features* for a *given provider*.

    You can have the detailed information on the **pricing**, **supported languages** as well as the
    **models** for providers who propose different models (eg: voice models available for a text to
    speech provider).

    Example : If you want the detailed list of all providers that can analyse the sentiment of a text
    written in french, you'd need to set `feature__name=text`,  `subfeature__name=sentiment_analysis`
    and `languages=fr`.

    Which will look like the following :


    ```bash
    curl --request GET  https://api.edenai.run/v2/info/provider_subfeatures?subfeature__name=sentiment_a
    nalysis&feature__name=text&languages=fr
    ```

    Args:
        feature_name (Union[Unset, str]):
        gender (Union[Unset, str]):
        is_working (Union[Unset, bool]):
        language (Union[Unset, str]):
        phase_name (Union[Unset, str]):
        provider_name (Union[Unset, str]):
        subfeature_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ProviderSubfeature']]
    """

    kwargs = _get_kwargs(
        feature_name=feature_name,
        gender=gender,
        is_working=is_working,
        language=language,
        phase_name=phase_name,
        provider_name=provider_name,
        subfeature_name=subfeature_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    feature_name: Union[Unset, str] = UNSET,
    gender: Union[Unset, str] = UNSET,
    is_working: Union[Unset, bool] = UNSET,
    language: Union[Unset, str] = UNSET,
    phase_name: Union[Unset, str] = UNSET,
    provider_name: Union[Unset, str] = UNSET,
    subfeature_name: Union[Unset, str] = UNSET,
) -> Optional[List["ProviderSubfeature"]]:
    """List Providers Subfeatures

     List Provider and features relations : You can get a list of *all providers* for a *feature* or *all
    features* for a *given provider*.

    You can have the detailed information on the **pricing**, **supported languages** as well as the
    **models** for providers who propose different models (eg: voice models available for a text to
    speech provider).

    Example : If you want the detailed list of all providers that can analyse the sentiment of a text
    written in french, you'd need to set `feature__name=text`,  `subfeature__name=sentiment_analysis`
    and `languages=fr`.

    Which will look like the following :


    ```bash
    curl --request GET  https://api.edenai.run/v2/info/provider_subfeatures?subfeature__name=sentiment_a
    nalysis&feature__name=text&languages=fr
    ```

    Args:
        feature_name (Union[Unset, str]):
        gender (Union[Unset, str]):
        is_working (Union[Unset, bool]):
        language (Union[Unset, str]):
        phase_name (Union[Unset, str]):
        provider_name (Union[Unset, str]):
        subfeature_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ProviderSubfeature']
    """

    return (
        await asyncio_detailed(
            client=client,
            feature_name=feature_name,
            gender=gender,
            is_working=is_working,
            language=language,
            phase_name=phase_name,
            provider_name=provider_name,
            subfeature_name=subfeature_name,
        )
    ).parsed
