# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictBytes, StrictStr
from typing import Optional, Union
from typing_extensions import Annotated
from openapi_client.models.worklow_response_type import WorklowResponseType

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class WorkflowsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def pipeline_pipeline_create(
        self,
        description: Annotated[str, Field(min_length=1, strict=True)],
        text: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="The input text for the first feature of the pipeline")] = None,
        texts: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="List of texts for the first feature of the pipeline")] = None,
        file: Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="The input file for the first feature of the pipeline")] = None,
        return_only_last: Annotated[Optional[StrictBool], Field(description="This parameter allows user to choose to output only the final result or all the intermediate results.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> WorklowResponseType:
        """Launch a Workflow

         Workflow let you create a pipeline of subfeature by inputing an entry data, letting it pass through all the subfeatures and retreiving the result   **Note**: You can try Workflow on our [developer portal](https://app.edenai.run/bricks/workflows) and a `description` snippet will automatically get generated as you build your workflow  **Example:**  Schema: ocr --> automatic_translation --> summarize In this workflow we pass a file as input, ocr parse the text, pass it to translate, and summarize will return a summary of the translated text  **Inputs:**  Depending on the first subfeature you have three choice for the inital input data: `file`, `text` or `texts`.  To create a workflow you have to pass an object to the `description` parameter, the object should look like this:   ``` [   {     \"feature\": \"ocr\",     \"subfeature\": \"ocr\",     \"params\": {       \"language\": \"auto-detect\",       \"providers\": \"google\"     }   },   {     \"feature\": \"translation\",     \"subfeature\": \"automatic_translation\",     \"params\": {       \"source_language\": \"auto-detect\",       \"target_language\": \"fr\",       \"providers\": \"google\"     }   },   {     \"feature\": \"text\",     \"subfeature\": \"summarize\",     \"params\": {       \"providers\": \"openai\"     }   } ] ```  - `description` should be a list of *nodes* each node representing a subfeature.Inside each node, enter the desired feature and subfeature and its params. `params` are the parameters you should normally send to the subfeature as if you were doing a direct call but with a few constraints:     + `providers` should take only one provider name, if you input multiple providers, the response of all the other providers will be ignored     + `file`, `text`, `texts` shouldn't be present in `params` as these are initial inputs  **Important!**: description should be sent as a string since the content-type is a form-data  - `return_only_last` allows you to chose wether you want a list of all the response returned by each providers or just getting the last response. If set to `true` the response will be the last subfeature result, if set to `false` the reponse will be a list of all subfeature results.     

        :param description: (required)
        :type description: str
        :param text: The input text for the first feature of the pipeline
        :type text: str
        :param texts: List of texts for the first feature of the pipeline
        :type texts: str
        :param file: The input file for the first feature of the pipeline
        :type file: bytearray
        :param return_only_last: This parameter allows user to choose to output only the final result or all the intermediate results.
        :type return_only_last: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._pipeline_pipeline_create_serialize(
            description=description,
            text=text,
            texts=texts,
            file=file,
            return_only_last=return_only_last,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "WorklowResponseType",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def pipeline_pipeline_create_with_http_info(
        self,
        description: Annotated[str, Field(min_length=1, strict=True)],
        text: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="The input text for the first feature of the pipeline")] = None,
        texts: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="List of texts for the first feature of the pipeline")] = None,
        file: Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="The input file for the first feature of the pipeline")] = None,
        return_only_last: Annotated[Optional[StrictBool], Field(description="This parameter allows user to choose to output only the final result or all the intermediate results.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[WorklowResponseType]:
        """Launch a Workflow

         Workflow let you create a pipeline of subfeature by inputing an entry data, letting it pass through all the subfeatures and retreiving the result   **Note**: You can try Workflow on our [developer portal](https://app.edenai.run/bricks/workflows) and a `description` snippet will automatically get generated as you build your workflow  **Example:**  Schema: ocr --> automatic_translation --> summarize In this workflow we pass a file as input, ocr parse the text, pass it to translate, and summarize will return a summary of the translated text  **Inputs:**  Depending on the first subfeature you have three choice for the inital input data: `file`, `text` or `texts`.  To create a workflow you have to pass an object to the `description` parameter, the object should look like this:   ``` [   {     \"feature\": \"ocr\",     \"subfeature\": \"ocr\",     \"params\": {       \"language\": \"auto-detect\",       \"providers\": \"google\"     }   },   {     \"feature\": \"translation\",     \"subfeature\": \"automatic_translation\",     \"params\": {       \"source_language\": \"auto-detect\",       \"target_language\": \"fr\",       \"providers\": \"google\"     }   },   {     \"feature\": \"text\",     \"subfeature\": \"summarize\",     \"params\": {       \"providers\": \"openai\"     }   } ] ```  - `description` should be a list of *nodes* each node representing a subfeature.Inside each node, enter the desired feature and subfeature and its params. `params` are the parameters you should normally send to the subfeature as if you were doing a direct call but with a few constraints:     + `providers` should take only one provider name, if you input multiple providers, the response of all the other providers will be ignored     + `file`, `text`, `texts` shouldn't be present in `params` as these are initial inputs  **Important!**: description should be sent as a string since the content-type is a form-data  - `return_only_last` allows you to chose wether you want a list of all the response returned by each providers or just getting the last response. If set to `true` the response will be the last subfeature result, if set to `false` the reponse will be a list of all subfeature results.     

        :param description: (required)
        :type description: str
        :param text: The input text for the first feature of the pipeline
        :type text: str
        :param texts: List of texts for the first feature of the pipeline
        :type texts: str
        :param file: The input file for the first feature of the pipeline
        :type file: bytearray
        :param return_only_last: This parameter allows user to choose to output only the final result or all the intermediate results.
        :type return_only_last: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._pipeline_pipeline_create_serialize(
            description=description,
            text=text,
            texts=texts,
            file=file,
            return_only_last=return_only_last,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "WorklowResponseType",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def pipeline_pipeline_create_without_preload_content(
        self,
        description: Annotated[str, Field(min_length=1, strict=True)],
        text: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="The input text for the first feature of the pipeline")] = None,
        texts: Annotated[Optional[Annotated[str, Field(min_length=1, strict=True)]], Field(description="List of texts for the first feature of the pipeline")] = None,
        file: Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="The input file for the first feature of the pipeline")] = None,
        return_only_last: Annotated[Optional[StrictBool], Field(description="This parameter allows user to choose to output only the final result or all the intermediate results.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Launch a Workflow

         Workflow let you create a pipeline of subfeature by inputing an entry data, letting it pass through all the subfeatures and retreiving the result   **Note**: You can try Workflow on our [developer portal](https://app.edenai.run/bricks/workflows) and a `description` snippet will automatically get generated as you build your workflow  **Example:**  Schema: ocr --> automatic_translation --> summarize In this workflow we pass a file as input, ocr parse the text, pass it to translate, and summarize will return a summary of the translated text  **Inputs:**  Depending on the first subfeature you have three choice for the inital input data: `file`, `text` or `texts`.  To create a workflow you have to pass an object to the `description` parameter, the object should look like this:   ``` [   {     \"feature\": \"ocr\",     \"subfeature\": \"ocr\",     \"params\": {       \"language\": \"auto-detect\",       \"providers\": \"google\"     }   },   {     \"feature\": \"translation\",     \"subfeature\": \"automatic_translation\",     \"params\": {       \"source_language\": \"auto-detect\",       \"target_language\": \"fr\",       \"providers\": \"google\"     }   },   {     \"feature\": \"text\",     \"subfeature\": \"summarize\",     \"params\": {       \"providers\": \"openai\"     }   } ] ```  - `description` should be a list of *nodes* each node representing a subfeature.Inside each node, enter the desired feature and subfeature and its params. `params` are the parameters you should normally send to the subfeature as if you were doing a direct call but with a few constraints:     + `providers` should take only one provider name, if you input multiple providers, the response of all the other providers will be ignored     + `file`, `text`, `texts` shouldn't be present in `params` as these are initial inputs  **Important!**: description should be sent as a string since the content-type is a form-data  - `return_only_last` allows you to chose wether you want a list of all the response returned by each providers or just getting the last response. If set to `true` the response will be the last subfeature result, if set to `false` the reponse will be a list of all subfeature results.     

        :param description: (required)
        :type description: str
        :param text: The input text for the first feature of the pipeline
        :type text: str
        :param texts: List of texts for the first feature of the pipeline
        :type texts: str
        :param file: The input file for the first feature of the pipeline
        :type file: bytearray
        :param return_only_last: This parameter allows user to choose to output only the final result or all the intermediate results.
        :type return_only_last: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._pipeline_pipeline_create_serialize(
            description=description,
            text=text,
            texts=texts,
            file=file,
            return_only_last=return_only_last,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "WorklowResponseType",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _pipeline_pipeline_create_serialize(
        self,
        description,
        text,
        texts,
        file,
        return_only_last,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        if description is not None:
            _form_params.append(('description', description))
        if text is not None:
            _form_params.append(('text', text))
        if texts is not None:
            _form_params.append(('texts', texts))
        if file is not None:
            _files['file'] = file
        if return_only_last is not None:
            _form_params.append(('return_only_last', return_only_last))
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'multipart/form-data'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'FeatureApiAuth'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/pipeline/',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


