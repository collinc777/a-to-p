# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from openapi_client.models.ocrinvoice_parser_invoice_parser_request import (
    OcrinvoiceParserInvoiceParserRequest,
)
from openapi_client.models.ocrinvoice_parser_response_model import (
    OcrinvoiceParserResponseModel,
)

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class InvoiceParserApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def ocr_ocr_invoice_parser_create(
        self,
        ocrinvoice_parser_invoice_parser_request: OcrinvoiceParserInvoiceParserRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> OcrinvoiceParserResponseModel:
        """Invoice Parser

        <details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**affinda**|`v3`|0.08 (per 1 page)|1 page |**base64**|`latest`|0.25 (per 1 page)|1 page |**dataleon**|`v4.0.0`|0.05 (per 1 page)|1 page |**microsoft**|`v2.1-preview.3`|0.01 (per 1 page)|1 page |**mindee**|`v2`|0.1 (per 1 page)|1 page |**amazon**|`boto3 1.26.8`|0.01 (per 1 page)|1 page |**google**|`DocumentAI v1 beta3`|0.01 (per 1 page)|10 page |**klippa**|`v1`|0.1 (per 1 file)|1 file |**veryfi**|`v8`|0.16 (per 1 file)|1 file   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Afrikaans**|`af`| |**Albanian**|`sq`| |**Arabic**|`ar`| |**Bengali**|`bn`| |**Bulgarian**|`bg`| |**Catalan**|`ca`| |**Chinese**|`zh`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dutch**|`nl`| |**English**|`en`| |**Estonian**|`et`| |**Finnish**|`fi`| |**French**|`fr`| |**German**|`de`| |**Gujarati**|`gu`| |**Hebrew**|`he`| |**Hindi**|`hi`| |**Hungarian**|`hu`| |**Indonesian**|`id`| |**Italian**|`it`| |**Japanese**|`ja`| |**Kannada**|`kn`| |**Korean**|`ko`| |**Latvian**|`lv`| |**Lithuanian**|`lt`| |**Macedonian**|`mk`| |**Malayalam**|`ml`| |**Marathi**|`mr`| |**Modern Greek (1453-)**|`el`| |**Nepali (macrolanguage)**|`ne`| |**Norwegian**|`no`| |**Panjabi**|`pa`| |**Persian**|`fa`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Romanian**|`ro`| |**Russian**|`ru`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**Spanish**|`es`| |**Swahili (macrolanguage)**|`sw`| |**Swedish**|`sv`| |**Tagalog**|`tl`| |**Tamil**|`ta`| |**Telugu**|`te`| |**Thai**|`th`| |**Turkish**|`tr`| |**Ukrainian**|`uk`| |**Urdu**|`ur`| |**Vietnamese**|`vi`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Chinese (China)**|`zh-cn`| |**Chinese (Taiwan)**|`zh-tw`| |**Danish (Denmark)**|`da-DK`| |**English (United States)**|`en-US`| |**French (France)**|`fr-FR`| |**German (Germany)**|`de-DE`| |**Italian (Italy)**|`it-IT`| |**Portuguese (Portugal)**|`pt-PT`| |**Spanish (Spain)**|`es-ES`|  </details><strong style='color:red;'>**Note:**</strong> This feature is likely to be deprecated in future releases. It is recommended to use the `financial_parser` feature as an alternative.

        :param ocrinvoice_parser_invoice_parser_request: (required)
        :type ocrinvoice_parser_invoice_parser_request: OcrinvoiceParserInvoiceParserRequest
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
        """  # noqa: E501

        _param = self._ocr_ocr_invoice_parser_create_serialize(
            ocrinvoice_parser_invoice_parser_request=ocrinvoice_parser_invoice_parser_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "OcrinvoiceParserResponseModel",
            "400": "BadRequest",
            "500": "Error",
            "403": "Error",
            "404": "NotFoundResponse",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def ocr_ocr_invoice_parser_create_with_http_info(
        self,
        ocrinvoice_parser_invoice_parser_request: OcrinvoiceParserInvoiceParserRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[OcrinvoiceParserResponseModel]:
        """Invoice Parser

        <details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**affinda**|`v3`|0.08 (per 1 page)|1 page |**base64**|`latest`|0.25 (per 1 page)|1 page |**dataleon**|`v4.0.0`|0.05 (per 1 page)|1 page |**microsoft**|`v2.1-preview.3`|0.01 (per 1 page)|1 page |**mindee**|`v2`|0.1 (per 1 page)|1 page |**amazon**|`boto3 1.26.8`|0.01 (per 1 page)|1 page |**google**|`DocumentAI v1 beta3`|0.01 (per 1 page)|10 page |**klippa**|`v1`|0.1 (per 1 file)|1 file |**veryfi**|`v8`|0.16 (per 1 file)|1 file   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Afrikaans**|`af`| |**Albanian**|`sq`| |**Arabic**|`ar`| |**Bengali**|`bn`| |**Bulgarian**|`bg`| |**Catalan**|`ca`| |**Chinese**|`zh`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dutch**|`nl`| |**English**|`en`| |**Estonian**|`et`| |**Finnish**|`fi`| |**French**|`fr`| |**German**|`de`| |**Gujarati**|`gu`| |**Hebrew**|`he`| |**Hindi**|`hi`| |**Hungarian**|`hu`| |**Indonesian**|`id`| |**Italian**|`it`| |**Japanese**|`ja`| |**Kannada**|`kn`| |**Korean**|`ko`| |**Latvian**|`lv`| |**Lithuanian**|`lt`| |**Macedonian**|`mk`| |**Malayalam**|`ml`| |**Marathi**|`mr`| |**Modern Greek (1453-)**|`el`| |**Nepali (macrolanguage)**|`ne`| |**Norwegian**|`no`| |**Panjabi**|`pa`| |**Persian**|`fa`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Romanian**|`ro`| |**Russian**|`ru`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**Spanish**|`es`| |**Swahili (macrolanguage)**|`sw`| |**Swedish**|`sv`| |**Tagalog**|`tl`| |**Tamil**|`ta`| |**Telugu**|`te`| |**Thai**|`th`| |**Turkish**|`tr`| |**Ukrainian**|`uk`| |**Urdu**|`ur`| |**Vietnamese**|`vi`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Chinese (China)**|`zh-cn`| |**Chinese (Taiwan)**|`zh-tw`| |**Danish (Denmark)**|`da-DK`| |**English (United States)**|`en-US`| |**French (France)**|`fr-FR`| |**German (Germany)**|`de-DE`| |**Italian (Italy)**|`it-IT`| |**Portuguese (Portugal)**|`pt-PT`| |**Spanish (Spain)**|`es-ES`|  </details><strong style='color:red;'>**Note:**</strong> This feature is likely to be deprecated in future releases. It is recommended to use the `financial_parser` feature as an alternative.

        :param ocrinvoice_parser_invoice_parser_request: (required)
        :type ocrinvoice_parser_invoice_parser_request: OcrinvoiceParserInvoiceParserRequest
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
        """  # noqa: E501

        _param = self._ocr_ocr_invoice_parser_create_serialize(
            ocrinvoice_parser_invoice_parser_request=ocrinvoice_parser_invoice_parser_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "OcrinvoiceParserResponseModel",
            "400": "BadRequest",
            "500": "Error",
            "403": "Error",
            "404": "NotFoundResponse",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def ocr_ocr_invoice_parser_create_without_preload_content(
        self,
        ocrinvoice_parser_invoice_parser_request: OcrinvoiceParserInvoiceParserRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Invoice Parser

        <details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Version|Price|Billing unit| |----|-------|-----|------------| |**affinda**|`v3`|0.08 (per 1 page)|1 page |**base64**|`latest`|0.25 (per 1 page)|1 page |**dataleon**|`v4.0.0`|0.05 (per 1 page)|1 page |**microsoft**|`v2.1-preview.3`|0.01 (per 1 page)|1 page |**mindee**|`v2`|0.1 (per 1 page)|1 page |**amazon**|`boto3 1.26.8`|0.01 (per 1 page)|1 page |**google**|`DocumentAI v1 beta3`|0.01 (per 1 page)|10 page |**klippa**|`v1`|0.1 (per 1 file)|1 file |**veryfi**|`v8`|0.16 (per 1 file)|1 file   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Afrikaans**|`af`| |**Albanian**|`sq`| |**Arabic**|`ar`| |**Bengali**|`bn`| |**Bulgarian**|`bg`| |**Catalan**|`ca`| |**Chinese**|`zh`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dutch**|`nl`| |**English**|`en`| |**Estonian**|`et`| |**Finnish**|`fi`| |**French**|`fr`| |**German**|`de`| |**Gujarati**|`gu`| |**Hebrew**|`he`| |**Hindi**|`hi`| |**Hungarian**|`hu`| |**Indonesian**|`id`| |**Italian**|`it`| |**Japanese**|`ja`| |**Kannada**|`kn`| |**Korean**|`ko`| |**Latvian**|`lv`| |**Lithuanian**|`lt`| |**Macedonian**|`mk`| |**Malayalam**|`ml`| |**Marathi**|`mr`| |**Modern Greek (1453-)**|`el`| |**Nepali (macrolanguage)**|`ne`| |**Norwegian**|`no`| |**Panjabi**|`pa`| |**Persian**|`fa`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Romanian**|`ro`| |**Russian**|`ru`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**Spanish**|`es`| |**Swahili (macrolanguage)**|`sw`| |**Swedish**|`sv`| |**Tagalog**|`tl`| |**Tamil**|`ta`| |**Telugu**|`te`| |**Thai**|`th`| |**Turkish**|`tr`| |**Ukrainian**|`uk`| |**Urdu**|`ur`| |**Vietnamese**|`vi`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Auto detection**|`auto-detect`| |**Chinese (China)**|`zh-cn`| |**Chinese (Taiwan)**|`zh-tw`| |**Danish (Denmark)**|`da-DK`| |**English (United States)**|`en-US`| |**French (France)**|`fr-FR`| |**German (Germany)**|`de-DE`| |**Italian (Italy)**|`it-IT`| |**Portuguese (Portugal)**|`pt-PT`| |**Spanish (Spain)**|`es-ES`|  </details><strong style='color:red;'>**Note:**</strong> This feature is likely to be deprecated in future releases. It is recommended to use the `financial_parser` feature as an alternative.

        :param ocrinvoice_parser_invoice_parser_request: (required)
        :type ocrinvoice_parser_invoice_parser_request: OcrinvoiceParserInvoiceParserRequest
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
        """  # noqa: E501

        _param = self._ocr_ocr_invoice_parser_create_serialize(
            ocrinvoice_parser_invoice_parser_request=ocrinvoice_parser_invoice_parser_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "OcrinvoiceParserResponseModel",
            "400": "BadRequest",
            "500": "Error",
            "403": "Error",
            "404": "NotFoundResponse",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _ocr_ocr_invoice_parser_create_serialize(
        self,
        ocrinvoice_parser_invoice_parser_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

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
        if ocrinvoice_parser_invoice_parser_request is not None:
            _body_params = ocrinvoice_parser_invoice_parser_request

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json", "multipart/form-data"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = ["FeatureApiAuth"]

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/ocr/invoice_parser",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )
