from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.batch_launch_response import BatchLaunchResponse
from ...models.batch_request import BatchRequest
from ...models.error import Error
from ...models.not_found_response import NotFoundResponse
from ...types import Response


def _get_kwargs(
    feature: str,
    subfeature: str,
    name: str,
    *,
    body: BatchRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/{feature}/{subfeature}/batch/{name}/",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequest, BatchLaunchResponse, Error, NotFoundResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BatchLaunchResponse.from_dict(response.json())

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
) -> Response[Union[BadRequest, BatchLaunchResponse, Error, NotFoundResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    feature: str,
    subfeature: str,
    name: str,
    *,
    client: AuthenticatedClient,
    body: BatchRequest,
) -> Response[Union[BadRequest, BatchLaunchResponse, Error, NotFoundResponse]]:
    r"""Launch Batch Job


    Launch a async Batch job, given a job name that will be used as its id.

    Each request should have the same parameters as you would normally pass to a feature.


    You can also pass an optional paramater `name` to help better identify each requests you send.


    Example with `text`/`sentiment_analysis`:

    ```json
    \"requests\": [
        {
            \"text\": \"It's -25 outside and I am so hot.\",
            \"language\": \"en\",
            \"providers\": \"google,amazon\"
        },
        {
            \"name\": \"mixed\",
            \"text\": \"Overall I am satisfied with my experience at Amazon, but two areas of major
    improvement needed.\",
            \"language\": \"en\",
            \"providers\": \"google\"
        },
        ...
    ]
    ```


    ### Limitations:
    You can have up to `5` concurrent running Jobs & input up to `500` requests per Batch


    <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Features</strong></summary>



    |Feature Name|Subfeature Name|
    |------------|---------------|
    |`text`|`moderation`|
    |`text`|`chat`|
    |`text`|`question_answer`|
    |`image`|`logo_detection`|
    |`image`|`anonymization`|
    |`text`|`anonymization`|
    |`text`|`embeddings`|
    |`text`|`spell_check`|
    |`audio`|`speech_to_text_async`|
    |`image`|`landmark_detection`|
    |`audio`|`text_to_speech`|
    |`text`|`custom_named_entity_recognition`|
    |`image`|`face_detection`|
    |`text`|`custom_classification`|
    |`translation`|`automatic_translation`|
    |`translation`|`document_translation`|
    |`text`|`topic_extraction`|
    |`text`|`generation`|
    |`text`|`code_generation`|
    |`image`|`generation`|
    |`video`|`text_detection_async`|
    |`text`|`sentiment_analysis`|
    |`text`|`syntax_analysis`|
    |`text`|`keyword_extraction`|
    |`text`|`named_entity_recognition`|
    |`text`|`search`|
    |`text`|`summarize`|
    |`translation`|`language_detection`|
    |`image`|`object_detection`|
    |`image`|`explicit_content`|
    |`ocr`|`invoice_parser`|
    |`ocr`|`resume_parser`|
    |`ocr`|`receipt_parser`|
    |`ocr`|`identity_parser`|

    </details>


    Args:
        feature (str):
        subfeature (str):
        name (str):
        body (BatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, BatchLaunchResponse, Error, NotFoundResponse]]
    """

    kwargs = _get_kwargs(
        feature=feature,
        subfeature=subfeature,
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    feature: str,
    subfeature: str,
    name: str,
    *,
    client: AuthenticatedClient,
    body: BatchRequest,
) -> Optional[Union[BadRequest, BatchLaunchResponse, Error, NotFoundResponse]]:
    r"""Launch Batch Job


    Launch a async Batch job, given a job name that will be used as its id.

    Each request should have the same parameters as you would normally pass to a feature.


    You can also pass an optional paramater `name` to help better identify each requests you send.


    Example with `text`/`sentiment_analysis`:

    ```json
    \"requests\": [
        {
            \"text\": \"It's -25 outside and I am so hot.\",
            \"language\": \"en\",
            \"providers\": \"google,amazon\"
        },
        {
            \"name\": \"mixed\",
            \"text\": \"Overall I am satisfied with my experience at Amazon, but two areas of major
    improvement needed.\",
            \"language\": \"en\",
            \"providers\": \"google\"
        },
        ...
    ]
    ```


    ### Limitations:
    You can have up to `5` concurrent running Jobs & input up to `500` requests per Batch


    <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Features</strong></summary>



    |Feature Name|Subfeature Name|
    |------------|---------------|
    |`text`|`moderation`|
    |`text`|`chat`|
    |`text`|`question_answer`|
    |`image`|`logo_detection`|
    |`image`|`anonymization`|
    |`text`|`anonymization`|
    |`text`|`embeddings`|
    |`text`|`spell_check`|
    |`audio`|`speech_to_text_async`|
    |`image`|`landmark_detection`|
    |`audio`|`text_to_speech`|
    |`text`|`custom_named_entity_recognition`|
    |`image`|`face_detection`|
    |`text`|`custom_classification`|
    |`translation`|`automatic_translation`|
    |`translation`|`document_translation`|
    |`text`|`topic_extraction`|
    |`text`|`generation`|
    |`text`|`code_generation`|
    |`image`|`generation`|
    |`video`|`text_detection_async`|
    |`text`|`sentiment_analysis`|
    |`text`|`syntax_analysis`|
    |`text`|`keyword_extraction`|
    |`text`|`named_entity_recognition`|
    |`text`|`search`|
    |`text`|`summarize`|
    |`translation`|`language_detection`|
    |`image`|`object_detection`|
    |`image`|`explicit_content`|
    |`ocr`|`invoice_parser`|
    |`ocr`|`resume_parser`|
    |`ocr`|`receipt_parser`|
    |`ocr`|`identity_parser`|

    </details>


    Args:
        feature (str):
        subfeature (str):
        name (str):
        body (BatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, BatchLaunchResponse, Error, NotFoundResponse]
    """

    return sync_detailed(
        feature=feature,
        subfeature=subfeature,
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    feature: str,
    subfeature: str,
    name: str,
    *,
    client: AuthenticatedClient,
    body: BatchRequest,
) -> Response[Union[BadRequest, BatchLaunchResponse, Error, NotFoundResponse]]:
    r"""Launch Batch Job


    Launch a async Batch job, given a job name that will be used as its id.

    Each request should have the same parameters as you would normally pass to a feature.


    You can also pass an optional paramater `name` to help better identify each requests you send.


    Example with `text`/`sentiment_analysis`:

    ```json
    \"requests\": [
        {
            \"text\": \"It's -25 outside and I am so hot.\",
            \"language\": \"en\",
            \"providers\": \"google,amazon\"
        },
        {
            \"name\": \"mixed\",
            \"text\": \"Overall I am satisfied with my experience at Amazon, but two areas of major
    improvement needed.\",
            \"language\": \"en\",
            \"providers\": \"google\"
        },
        ...
    ]
    ```


    ### Limitations:
    You can have up to `5` concurrent running Jobs & input up to `500` requests per Batch


    <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Features</strong></summary>



    |Feature Name|Subfeature Name|
    |------------|---------------|
    |`text`|`moderation`|
    |`text`|`chat`|
    |`text`|`question_answer`|
    |`image`|`logo_detection`|
    |`image`|`anonymization`|
    |`text`|`anonymization`|
    |`text`|`embeddings`|
    |`text`|`spell_check`|
    |`audio`|`speech_to_text_async`|
    |`image`|`landmark_detection`|
    |`audio`|`text_to_speech`|
    |`text`|`custom_named_entity_recognition`|
    |`image`|`face_detection`|
    |`text`|`custom_classification`|
    |`translation`|`automatic_translation`|
    |`translation`|`document_translation`|
    |`text`|`topic_extraction`|
    |`text`|`generation`|
    |`text`|`code_generation`|
    |`image`|`generation`|
    |`video`|`text_detection_async`|
    |`text`|`sentiment_analysis`|
    |`text`|`syntax_analysis`|
    |`text`|`keyword_extraction`|
    |`text`|`named_entity_recognition`|
    |`text`|`search`|
    |`text`|`summarize`|
    |`translation`|`language_detection`|
    |`image`|`object_detection`|
    |`image`|`explicit_content`|
    |`ocr`|`invoice_parser`|
    |`ocr`|`resume_parser`|
    |`ocr`|`receipt_parser`|
    |`ocr`|`identity_parser`|

    </details>


    Args:
        feature (str):
        subfeature (str):
        name (str):
        body (BatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, BatchLaunchResponse, Error, NotFoundResponse]]
    """

    kwargs = _get_kwargs(
        feature=feature,
        subfeature=subfeature,
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    feature: str,
    subfeature: str,
    name: str,
    *,
    client: AuthenticatedClient,
    body: BatchRequest,
) -> Optional[Union[BadRequest, BatchLaunchResponse, Error, NotFoundResponse]]:
    r"""Launch Batch Job


    Launch a async Batch job, given a job name that will be used as its id.

    Each request should have the same parameters as you would normally pass to a feature.


    You can also pass an optional paramater `name` to help better identify each requests you send.


    Example with `text`/`sentiment_analysis`:

    ```json
    \"requests\": [
        {
            \"text\": \"It's -25 outside and I am so hot.\",
            \"language\": \"en\",
            \"providers\": \"google,amazon\"
        },
        {
            \"name\": \"mixed\",
            \"text\": \"Overall I am satisfied with my experience at Amazon, but two areas of major
    improvement needed.\",
            \"language\": \"en\",
            \"providers\": \"google\"
        },
        ...
    ]
    ```


    ### Limitations:
    You can have up to `5` concurrent running Jobs & input up to `500` requests per Batch


    <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Features</strong></summary>



    |Feature Name|Subfeature Name|
    |------------|---------------|
    |`text`|`moderation`|
    |`text`|`chat`|
    |`text`|`question_answer`|
    |`image`|`logo_detection`|
    |`image`|`anonymization`|
    |`text`|`anonymization`|
    |`text`|`embeddings`|
    |`text`|`spell_check`|
    |`audio`|`speech_to_text_async`|
    |`image`|`landmark_detection`|
    |`audio`|`text_to_speech`|
    |`text`|`custom_named_entity_recognition`|
    |`image`|`face_detection`|
    |`text`|`custom_classification`|
    |`translation`|`automatic_translation`|
    |`translation`|`document_translation`|
    |`text`|`topic_extraction`|
    |`text`|`generation`|
    |`text`|`code_generation`|
    |`image`|`generation`|
    |`video`|`text_detection_async`|
    |`text`|`sentiment_analysis`|
    |`text`|`syntax_analysis`|
    |`text`|`keyword_extraction`|
    |`text`|`named_entity_recognition`|
    |`text`|`search`|
    |`text`|`summarize`|
    |`translation`|`language_detection`|
    |`image`|`object_detection`|
    |`image`|`explicit_content`|
    |`ocr`|`invoice_parser`|
    |`ocr`|`resume_parser`|
    |`ocr`|`receipt_parser`|
    |`ocr`|`identity_parser`|

    </details>


    Args:
        feature (str):
        subfeature (str):
        name (str):
        body (BatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, BatchLaunchResponse, Error, NotFoundResponse]
    """

    return (
        await asyncio_detailed(
            feature=feature,
            subfeature=subfeature,
            name=name,
            client=client,
            body=body,
        )
    ).parsed
