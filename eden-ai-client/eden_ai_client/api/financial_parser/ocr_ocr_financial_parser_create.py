from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.not_found_response import NotFoundResponse
from ...models.ocrfinancial_parser_financial_parser_request import OcrfinancialParserFinancialParserRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        OcrfinancialParserFinancialParserRequest,
        OcrfinancialParserFinancialParserRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/ocr/financial_parser",
    }

    if isinstance(body, OcrfinancialParserFinancialParserRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, OcrfinancialParserFinancialParserRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
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
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
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
        OcrfinancialParserFinancialParserRequest,
        OcrfinancialParserFinancialParserRequest,
    ],
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Financial Parser

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Document Type|Price|Billing unit|
    |----|-------|------|-----|------------|
    |**affinda**|`v3`|`invoice`|0.08 (per 1 page)|1 page
    |**affinda**|`v3`|`receipt`|0.07 (per 1 page)|1 page
    |**amazon**|`boto3 1.26.8`|-|0.01 (per 1 page)|1 page
    |**base64**|`latest`|-|0.25 (per 1 page)|1 page
    |**dataleon**|`v4.0.0`|-|0.05 (per 1 page)|1 page
    |**google**|`DocumentAI v1 beta3`|-|0.01 (per 1 page)|10 page
    |**klippa**|`v1`|-|0.1 (per 1 file)|1 file
    |**microsoft**|`v2.1-preview.3`|-|0.01 (per 1 page)|1 page
    |**mindee**|`v1.2`|-|0.1 (per 1 page)|1 page
    |**tabscanner**|`latest`|-|0.08 (per 1 page)|1 page
    |**veryfi**|`v8`|`receipt`|0.08 (per 1 file)|1 file
    |**veryfi**|`v8`|`invoice`|0.16 (per 1 file)|1 file


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Arabic**|`ar`|
    |**Bengali**|`bn`|
    |**Bulgarian**|`bg`|
    |**Catalan**|`ca`|
    |**Chinese**|`zh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Estonian**|`et`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Indonesian**|`id`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Kannada**|`kn`|
    |**Korean**|`ko`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Macedonian**|`mk`|
    |**Malayalam**|`ml`|
    |**Marathi**|`mr`|
    |**Modern Greek (1453-)**|`el`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**Spanish**|`es`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tamil**|`ta`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Turkish**|`tr`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Vietnamese**|`vi`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Catalan (Spain)**|`ca-ES`|
    |**Chinese (China)**|`zh-cn`|
    |**Chinese (Taiwan)**|`zh-tw`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (United Kingdom)**|`en-GB`|
    |**English (United States)**|`en-US`|
    |**French (Canada)**|`fr-CA`|
    |**French (France)**|`fr-FR`|
    |**French (Switzerland)**|`fr-CH`|
    |**German (Germany)**|`de-DE`|
    |**German (Switzerland)**|`de-CH`|
    |**Italian (Italy)**|`it-IT`|
    |**Italian (Switzerland)**|`it-CH`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Spanish (Spain)**|`es-ES`|

    </details>

    Args:
        body (OcrfinancialParserFinancialParserRequest):
        body (OcrfinancialParserFinancialParserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse]]
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
        OcrfinancialParserFinancialParserRequest,
        OcrfinancialParserFinancialParserRequest,
    ],
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Financial Parser

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Document Type|Price|Billing unit|
    |----|-------|------|-----|------------|
    |**affinda**|`v3`|`invoice`|0.08 (per 1 page)|1 page
    |**affinda**|`v3`|`receipt`|0.07 (per 1 page)|1 page
    |**amazon**|`boto3 1.26.8`|-|0.01 (per 1 page)|1 page
    |**base64**|`latest`|-|0.25 (per 1 page)|1 page
    |**dataleon**|`v4.0.0`|-|0.05 (per 1 page)|1 page
    |**google**|`DocumentAI v1 beta3`|-|0.01 (per 1 page)|10 page
    |**klippa**|`v1`|-|0.1 (per 1 file)|1 file
    |**microsoft**|`v2.1-preview.3`|-|0.01 (per 1 page)|1 page
    |**mindee**|`v1.2`|-|0.1 (per 1 page)|1 page
    |**tabscanner**|`latest`|-|0.08 (per 1 page)|1 page
    |**veryfi**|`v8`|`receipt`|0.08 (per 1 file)|1 file
    |**veryfi**|`v8`|`invoice`|0.16 (per 1 file)|1 file


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Arabic**|`ar`|
    |**Bengali**|`bn`|
    |**Bulgarian**|`bg`|
    |**Catalan**|`ca`|
    |**Chinese**|`zh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Estonian**|`et`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Indonesian**|`id`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Kannada**|`kn`|
    |**Korean**|`ko`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Macedonian**|`mk`|
    |**Malayalam**|`ml`|
    |**Marathi**|`mr`|
    |**Modern Greek (1453-)**|`el`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**Spanish**|`es`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tamil**|`ta`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Turkish**|`tr`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Vietnamese**|`vi`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Catalan (Spain)**|`ca-ES`|
    |**Chinese (China)**|`zh-cn`|
    |**Chinese (Taiwan)**|`zh-tw`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (United Kingdom)**|`en-GB`|
    |**English (United States)**|`en-US`|
    |**French (Canada)**|`fr-CA`|
    |**French (France)**|`fr-FR`|
    |**French (Switzerland)**|`fr-CH`|
    |**German (Germany)**|`de-DE`|
    |**German (Switzerland)**|`de-CH`|
    |**Italian (Italy)**|`it-IT`|
    |**Italian (Switzerland)**|`it-CH`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Spanish (Spain)**|`es-ES`|

    </details>

    Args:
        body (OcrfinancialParserFinancialParserRequest):
        body (OcrfinancialParserFinancialParserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, NotFoundResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        OcrfinancialParserFinancialParserRequest,
        OcrfinancialParserFinancialParserRequest,
    ],
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Financial Parser

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Document Type|Price|Billing unit|
    |----|-------|------|-----|------------|
    |**affinda**|`v3`|`invoice`|0.08 (per 1 page)|1 page
    |**affinda**|`v3`|`receipt`|0.07 (per 1 page)|1 page
    |**amazon**|`boto3 1.26.8`|-|0.01 (per 1 page)|1 page
    |**base64**|`latest`|-|0.25 (per 1 page)|1 page
    |**dataleon**|`v4.0.0`|-|0.05 (per 1 page)|1 page
    |**google**|`DocumentAI v1 beta3`|-|0.01 (per 1 page)|10 page
    |**klippa**|`v1`|-|0.1 (per 1 file)|1 file
    |**microsoft**|`v2.1-preview.3`|-|0.01 (per 1 page)|1 page
    |**mindee**|`v1.2`|-|0.1 (per 1 page)|1 page
    |**tabscanner**|`latest`|-|0.08 (per 1 page)|1 page
    |**veryfi**|`v8`|`receipt`|0.08 (per 1 file)|1 file
    |**veryfi**|`v8`|`invoice`|0.16 (per 1 file)|1 file


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Arabic**|`ar`|
    |**Bengali**|`bn`|
    |**Bulgarian**|`bg`|
    |**Catalan**|`ca`|
    |**Chinese**|`zh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Estonian**|`et`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Indonesian**|`id`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Kannada**|`kn`|
    |**Korean**|`ko`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Macedonian**|`mk`|
    |**Malayalam**|`ml`|
    |**Marathi**|`mr`|
    |**Modern Greek (1453-)**|`el`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**Spanish**|`es`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tamil**|`ta`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Turkish**|`tr`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Vietnamese**|`vi`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Catalan (Spain)**|`ca-ES`|
    |**Chinese (China)**|`zh-cn`|
    |**Chinese (Taiwan)**|`zh-tw`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (United Kingdom)**|`en-GB`|
    |**English (United States)**|`en-US`|
    |**French (Canada)**|`fr-CA`|
    |**French (France)**|`fr-FR`|
    |**French (Switzerland)**|`fr-CH`|
    |**German (Germany)**|`de-DE`|
    |**German (Switzerland)**|`de-CH`|
    |**Italian (Italy)**|`it-IT`|
    |**Italian (Switzerland)**|`it-CH`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Spanish (Spain)**|`es-ES`|

    </details>

    Args:
        body (OcrfinancialParserFinancialParserRequest):
        body (OcrfinancialParserFinancialParserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse]]
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
        OcrfinancialParserFinancialParserRequest,
        OcrfinancialParserFinancialParserRequest,
    ],
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Financial Parser

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Document Type|Price|Billing unit|
    |----|-------|------|-----|------------|
    |**affinda**|`v3`|`invoice`|0.08 (per 1 page)|1 page
    |**affinda**|`v3`|`receipt`|0.07 (per 1 page)|1 page
    |**amazon**|`boto3 1.26.8`|-|0.01 (per 1 page)|1 page
    |**base64**|`latest`|-|0.25 (per 1 page)|1 page
    |**dataleon**|`v4.0.0`|-|0.05 (per 1 page)|1 page
    |**google**|`DocumentAI v1 beta3`|-|0.01 (per 1 page)|10 page
    |**klippa**|`v1`|-|0.1 (per 1 file)|1 file
    |**microsoft**|`v2.1-preview.3`|-|0.01 (per 1 page)|1 page
    |**mindee**|`v1.2`|-|0.1 (per 1 page)|1 page
    |**tabscanner**|`latest`|-|0.08 (per 1 page)|1 page
    |**veryfi**|`v8`|`receipt`|0.08 (per 1 file)|1 file
    |**veryfi**|`v8`|`invoice`|0.16 (per 1 file)|1 file


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Afrikaans**|`af`|
    |**Albanian**|`sq`|
    |**Arabic**|`ar`|
    |**Bengali**|`bn`|
    |**Bulgarian**|`bg`|
    |**Catalan**|`ca`|
    |**Chinese**|`zh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**English**|`en`|
    |**Estonian**|`et`|
    |**Finnish**|`fi`|
    |**French**|`fr`|
    |**German**|`de`|
    |**Gujarati**|`gu`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Indonesian**|`id`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Kannada**|`kn`|
    |**Korean**|`ko`|
    |**Latvian**|`lv`|
    |**Lithuanian**|`lt`|
    |**Macedonian**|`mk`|
    |**Malayalam**|`ml`|
    |**Marathi**|`mr`|
    |**Modern Greek (1453-)**|`el`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Norwegian**|`no`|
    |**Panjabi**|`pa`|
    |**Persian**|`fa`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Romanian**|`ro`|
    |**Russian**|`ru`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**Spanish**|`es`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tamil**|`ta`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Turkish**|`tr`|
    |**Ukrainian**|`uk`|
    |**Urdu**|`ur`|
    |**Vietnamese**|`vi`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Catalan (Spain)**|`ca-ES`|
    |**Chinese (China)**|`zh-cn`|
    |**Chinese (Taiwan)**|`zh-tw`|
    |**Danish (Denmark)**|`da-DK`|
    |**Dutch (Netherlands)**|`nl-NL`|
    |**English (United Kingdom)**|`en-GB`|
    |**English (United States)**|`en-US`|
    |**French (Canada)**|`fr-CA`|
    |**French (France)**|`fr-FR`|
    |**French (Switzerland)**|`fr-CH`|
    |**German (Germany)**|`de-DE`|
    |**German (Switzerland)**|`de-CH`|
    |**Italian (Italy)**|`it-IT`|
    |**Italian (Switzerland)**|`it-CH`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Spanish (Spain)**|`es-ES`|

    </details>

    Args:
        body (OcrfinancialParserFinancialParserRequest):
        body (OcrfinancialParserFinancialParserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, NotFoundResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
