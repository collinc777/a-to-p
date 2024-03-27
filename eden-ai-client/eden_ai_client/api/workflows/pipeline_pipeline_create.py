from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pipeline_request import PipelineRequest
from ...types import Response


def _get_kwargs(
    *,
    body: PipelineRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/pipeline/",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

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
    *,
    client: AuthenticatedClient,
    body: PipelineRequest,
) -> Response[Any]:
    r"""Launch a Workflow


    Workflow let you create a pipeline of subfeature by inputing an entry data, letting it pass through
    all the subfeatures and retreiving the result


    **Note**: You can try Workflow on our [developer portal](https://app.edenai.run/bricks/workflows)
    and a `description` snippet will automatically get generated as you build your workflow

    **Example:**

    Schema: ocr --> automatic_translation --> summarize
    In this workflow we pass a file as input, ocr parse the text, pass it to translate, and summarize
    will return a summary of the translated text

    **Inputs:**

    Depending on the first subfeature you have three choice for the inital input data: `file`, `text` or
    `texts`.

    To create a workflow you have to pass an object to the `description` parameter, the object should
    look like this:


    ```
    [
      {
        \"feature\": \"ocr\",
        \"subfeature\": \"ocr\",
        \"params\": {
          \"language\": \"auto-detect\",
          \"providers\": \"google\"
        }
      },
      {
        \"feature\": \"translation\",
        \"subfeature\": \"automatic_translation\",
        \"params\": {
          \"source_language\": \"auto-detect\",
          \"target_language\": \"fr\",
          \"providers\": \"google\"
        }
      },
      {
        \"feature\": \"text\",
        \"subfeature\": \"summarize\",
        \"params\": {
          \"providers\": \"openai\"
        }
      }
    ]
    ```

    - `description` should be a list of *nodes* each node representing a subfeature.Inside each node,
    enter the desired feature and subfeature and its params. `params` are the parameters you should
    normally send to the subfeature as if you were doing a direct call but with a few constraints:
        + `providers` should take only one provider name, if you input multiple providers, the response
    of all the other providers will be ignored
        + `file`, `text`, `texts` shouldn't be present in `params` as these are initial inputs

    **Important!**: description should be sent as a string since the content-type is a form-data

    - `return_only_last` allows you to chose wether you want a list of all the response returned by each
    providers or just getting the last response. If set to `true` the response will be the last
    subfeature result, if set to `false` the reponse will be a list of all subfeature results.


    Args:
        body (PipelineRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PipelineRequest,
) -> Response[Any]:
    r"""Launch a Workflow


    Workflow let you create a pipeline of subfeature by inputing an entry data, letting it pass through
    all the subfeatures and retreiving the result


    **Note**: You can try Workflow on our [developer portal](https://app.edenai.run/bricks/workflows)
    and a `description` snippet will automatically get generated as you build your workflow

    **Example:**

    Schema: ocr --> automatic_translation --> summarize
    In this workflow we pass a file as input, ocr parse the text, pass it to translate, and summarize
    will return a summary of the translated text

    **Inputs:**

    Depending on the first subfeature you have three choice for the inital input data: `file`, `text` or
    `texts`.

    To create a workflow you have to pass an object to the `description` parameter, the object should
    look like this:


    ```
    [
      {
        \"feature\": \"ocr\",
        \"subfeature\": \"ocr\",
        \"params\": {
          \"language\": \"auto-detect\",
          \"providers\": \"google\"
        }
      },
      {
        \"feature\": \"translation\",
        \"subfeature\": \"automatic_translation\",
        \"params\": {
          \"source_language\": \"auto-detect\",
          \"target_language\": \"fr\",
          \"providers\": \"google\"
        }
      },
      {
        \"feature\": \"text\",
        \"subfeature\": \"summarize\",
        \"params\": {
          \"providers\": \"openai\"
        }
      }
    ]
    ```

    - `description` should be a list of *nodes* each node representing a subfeature.Inside each node,
    enter the desired feature and subfeature and its params. `params` are the parameters you should
    normally send to the subfeature as if you were doing a direct call but with a few constraints:
        + `providers` should take only one provider name, if you input multiple providers, the response
    of all the other providers will be ignored
        + `file`, `text`, `texts` shouldn't be present in `params` as these are initial inputs

    **Important!**: description should be sent as a string since the content-type is a form-data

    - `return_only_last` allows you to chose wether you want a list of all the response returned by each
    providers or just getting the last response. If set to `true` the response will be the last
    subfeature result, if set to `false` the reponse will be a list of all subfeature results.


    Args:
        body (PipelineRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
