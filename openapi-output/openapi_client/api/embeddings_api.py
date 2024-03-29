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

from openapi_client.models.imageembeddings_embeddings_request import ImageembeddingsEmbeddingsRequest
from openapi_client.models.imageembeddings_response_model import ImageembeddingsResponseModel
from openapi_client.models.textembeddings_embeddings_request import TextembeddingsEmbeddingsRequest
from openapi_client.models.textembeddings_response_model import TextembeddingsResponseModel

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class EmbeddingsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def image_image_embeddings_create(
        self,
        imageembeddings_embeddings_request: ImageembeddingsEmbeddingsRequest,
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
    ) -> ImageembeddingsResponseModel:
        """Embeddings

        <details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**alephalpha**|-|`1.12.0`|0.05 (per 1 file)|1 file   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**English**|`en`| |**French**|`fr`| |**German**|`de`| |**Italian**|`it`| |**Spanish**|`es`|  </details><details><summary>Supported Models</summary><details><summary>alephalpha</summary>      |Name|Value| |----|-----| |**alephalpha**|`luminous-base`|  </details>  </details>

        :param imageembeddings_embeddings_request: (required)
        :type imageembeddings_embeddings_request: ImageembeddingsEmbeddingsRequest
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

        _param = self._image_image_embeddings_create_serialize(
            imageembeddings_embeddings_request=imageembeddings_embeddings_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ImageembeddingsResponseModel",
            '400': "BadRequest",
            '500': "Error",
            '403': "Error",
            '404': "NotFoundResponse",
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
    async def image_image_embeddings_create_with_http_info(
        self,
        imageembeddings_embeddings_request: ImageembeddingsEmbeddingsRequest,
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
    ) -> ApiResponse[ImageembeddingsResponseModel]:
        """Embeddings

        <details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**alephalpha**|-|`1.12.0`|0.05 (per 1 file)|1 file   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**English**|`en`| |**French**|`fr`| |**German**|`de`| |**Italian**|`it`| |**Spanish**|`es`|  </details><details><summary>Supported Models</summary><details><summary>alephalpha</summary>      |Name|Value| |----|-----| |**alephalpha**|`luminous-base`|  </details>  </details>

        :param imageembeddings_embeddings_request: (required)
        :type imageembeddings_embeddings_request: ImageembeddingsEmbeddingsRequest
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

        _param = self._image_image_embeddings_create_serialize(
            imageembeddings_embeddings_request=imageembeddings_embeddings_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ImageembeddingsResponseModel",
            '400': "BadRequest",
            '500': "Error",
            '403': "Error",
            '404': "NotFoundResponse",
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
    async def image_image_embeddings_create_without_preload_content(
        self,
        imageembeddings_embeddings_request: ImageembeddingsEmbeddingsRequest,
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
        """Embeddings

        <details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**alephalpha**|-|`1.12.0`|0.05 (per 1 file)|1 file   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**English**|`en`| |**French**|`fr`| |**German**|`de`| |**Italian**|`it`| |**Spanish**|`es`|  </details><details><summary>Supported Models</summary><details><summary>alephalpha</summary>      |Name|Value| |----|-----| |**alephalpha**|`luminous-base`|  </details>  </details>

        :param imageembeddings_embeddings_request: (required)
        :type imageembeddings_embeddings_request: ImageembeddingsEmbeddingsRequest
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

        _param = self._image_image_embeddings_create_serialize(
            imageembeddings_embeddings_request=imageembeddings_embeddings_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ImageembeddingsResponseModel",
            '400': "BadRequest",
            '500': "Error",
            '403': "Error",
            '404': "NotFoundResponse",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _image_image_embeddings_create_serialize(
        self,
        imageembeddings_embeddings_request,
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
        # process the body parameter
        if imageembeddings_embeddings_request is not None:
            _body_params = imageembeddings_embeddings_request


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
                        'application/json', 
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
            resource_path='/image/embeddings',
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




    @validate_call
    async def text_text_embeddings_create(
        self,
        textembeddings_embeddings_request: TextembeddingsEmbeddingsRequest,
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
    ) -> TextembeddingsResponseModel:
        """Embeddings

        <details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**openai**|-|`v3.0.0`|0.1 (per 1000000 token)|1 token |**google**|-|`v1`|0.1 (per 1000000 char)|1 char |**cohere**|-|`v1`|0.1 (per 1000000 char)|1 char |**cohere**|**4096embed-english-v2.0**|`v1`|0.1 (per 1000000 char)|1 char |**cohere**|**1024embed-english-light-v2.0**|`v1`|0.1 (per 1000000 char)|1 char |**cohere**|**768__embed-multilingual-v2.0**|`v1`|0.1 (per 1000000 char)|1 char |**mistral**|-|`v0.0.1`|0.1 (per 1000000 token)|1 token |**jina**|-|`v1`|0.018 (per 1000000 token)|1 token   </details>  <details><summary>Supported Models</summary><details><summary>openai</summary>      |Name|Value| |----|-----| |**openai**|`1536__text-embedding-ada-002`|  </details><details><summary>google</summary>      |Name|Value| |----|-----| |**google**|`768__textembedding-gecko`|  </details><details><summary>cohere</summary>      |Name|Value| |----|-----| |**cohere**|`1024__embed-english-light-v2.0`| ||`4096__embed-english-v2.0`| ||`768__embed-multilingual-v2.0`|  </details><details><summary>mistral</summary>      |Name|Value| |----|-----| |**mistral**|`1024__mistral-embed`|  </details><details><summary>jina</summary>      |Name|Value| |----|-----| |**jina**|`jina-embeddings-v2-base-code`| ||`jina-embeddings-v2-base-de`| ||`jina-embeddings-v2-base-en`| ||`jina-embeddings-v2-base-es`| ||`jina-embeddings-v2-base-zh`|  </details>  </details>

        :param textembeddings_embeddings_request: (required)
        :type textembeddings_embeddings_request: TextembeddingsEmbeddingsRequest
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

        _param = self._text_text_embeddings_create_serialize(
            textembeddings_embeddings_request=textembeddings_embeddings_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "TextembeddingsResponseModel",
            '400': "BadRequest",
            '500': "Error",
            '403': "Error",
            '404': "NotFoundResponse",
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
    async def text_text_embeddings_create_with_http_info(
        self,
        textembeddings_embeddings_request: TextembeddingsEmbeddingsRequest,
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
    ) -> ApiResponse[TextembeddingsResponseModel]:
        """Embeddings

        <details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**openai**|-|`v3.0.0`|0.1 (per 1000000 token)|1 token |**google**|-|`v1`|0.1 (per 1000000 char)|1 char |**cohere**|-|`v1`|0.1 (per 1000000 char)|1 char |**cohere**|**4096embed-english-v2.0**|`v1`|0.1 (per 1000000 char)|1 char |**cohere**|**1024embed-english-light-v2.0**|`v1`|0.1 (per 1000000 char)|1 char |**cohere**|**768__embed-multilingual-v2.0**|`v1`|0.1 (per 1000000 char)|1 char |**mistral**|-|`v0.0.1`|0.1 (per 1000000 token)|1 token |**jina**|-|`v1`|0.018 (per 1000000 token)|1 token   </details>  <details><summary>Supported Models</summary><details><summary>openai</summary>      |Name|Value| |----|-----| |**openai**|`1536__text-embedding-ada-002`|  </details><details><summary>google</summary>      |Name|Value| |----|-----| |**google**|`768__textembedding-gecko`|  </details><details><summary>cohere</summary>      |Name|Value| |----|-----| |**cohere**|`1024__embed-english-light-v2.0`| ||`4096__embed-english-v2.0`| ||`768__embed-multilingual-v2.0`|  </details><details><summary>mistral</summary>      |Name|Value| |----|-----| |**mistral**|`1024__mistral-embed`|  </details><details><summary>jina</summary>      |Name|Value| |----|-----| |**jina**|`jina-embeddings-v2-base-code`| ||`jina-embeddings-v2-base-de`| ||`jina-embeddings-v2-base-en`| ||`jina-embeddings-v2-base-es`| ||`jina-embeddings-v2-base-zh`|  </details>  </details>

        :param textembeddings_embeddings_request: (required)
        :type textembeddings_embeddings_request: TextembeddingsEmbeddingsRequest
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

        _param = self._text_text_embeddings_create_serialize(
            textembeddings_embeddings_request=textembeddings_embeddings_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "TextembeddingsResponseModel",
            '400': "BadRequest",
            '500': "Error",
            '403': "Error",
            '404': "NotFoundResponse",
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
    async def text_text_embeddings_create_without_preload_content(
        self,
        textembeddings_embeddings_request: TextembeddingsEmbeddingsRequest,
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
        """Embeddings

        <details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**openai**|-|`v3.0.0`|0.1 (per 1000000 token)|1 token |**google**|-|`v1`|0.1 (per 1000000 char)|1 char |**cohere**|-|`v1`|0.1 (per 1000000 char)|1 char |**cohere**|**4096embed-english-v2.0**|`v1`|0.1 (per 1000000 char)|1 char |**cohere**|**1024embed-english-light-v2.0**|`v1`|0.1 (per 1000000 char)|1 char |**cohere**|**768__embed-multilingual-v2.0**|`v1`|0.1 (per 1000000 char)|1 char |**mistral**|-|`v0.0.1`|0.1 (per 1000000 token)|1 token |**jina**|-|`v1`|0.018 (per 1000000 token)|1 token   </details>  <details><summary>Supported Models</summary><details><summary>openai</summary>      |Name|Value| |----|-----| |**openai**|`1536__text-embedding-ada-002`|  </details><details><summary>google</summary>      |Name|Value| |----|-----| |**google**|`768__textembedding-gecko`|  </details><details><summary>cohere</summary>      |Name|Value| |----|-----| |**cohere**|`1024__embed-english-light-v2.0`| ||`4096__embed-english-v2.0`| ||`768__embed-multilingual-v2.0`|  </details><details><summary>mistral</summary>      |Name|Value| |----|-----| |**mistral**|`1024__mistral-embed`|  </details><details><summary>jina</summary>      |Name|Value| |----|-----| |**jina**|`jina-embeddings-v2-base-code`| ||`jina-embeddings-v2-base-de`| ||`jina-embeddings-v2-base-en`| ||`jina-embeddings-v2-base-es`| ||`jina-embeddings-v2-base-zh`|  </details>  </details>

        :param textembeddings_embeddings_request: (required)
        :type textembeddings_embeddings_request: TextembeddingsEmbeddingsRequest
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

        _param = self._text_text_embeddings_create_serialize(
            textembeddings_embeddings_request=textembeddings_embeddings_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "TextembeddingsResponseModel",
            '400': "BadRequest",
            '500': "Error",
            '403': "Error",
            '404': "NotFoundResponse",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _text_text_embeddings_create_serialize(
        self,
        textembeddings_embeddings_request,
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
        # process the body parameter
        if textembeddings_embeddings_request is not None:
            _body_params = textembeddings_embeddings_request


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
                        'application/json'
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
            resource_path='/text/embeddings',
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


