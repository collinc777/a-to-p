from io import BytesIO
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.document_type_enum import DocumentTypeEnum
from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="OcrfinancialParserFinancialParserRequest")


@_attrs_define
class OcrfinancialParserFinancialParserRequest:
    """
    Attributes:
        providers (str): It can be one (ex: **'amazon'** or **'google'**) or multiple provider(s) (ex:
            **'amazon,microsoft,google'**)             that the data will be redirected to in order to get the processed
            results.
        fallback_providers (Union[None, Unset, str]): Providers in this list will be used as fallback if the call to
            provider in `providers` parameter fails.
                To use this feature, you must input **only one** provider in the `providers` parameter. but you can put up
            to 5 fallbacks.

            They will be tried in the same order they are input, and it will stop to the first provider who doesn't fail.


            *Doesn't work with async subfeatures.*

        response_as_dict (Union[Unset, bool]): Optional : When set to **true** (default), the response is an object of
            responses with providers names as keys : <br>
                              ``` {"google" : { "status": "success", ... }, } ``` <br>
                            When set to **false** the response structure is a list of response objects : <br>
                               ``` [{"status": "success", "provider": "google" ... }, ] ```. <br>
                               Default: True.
        attributes_as_list (Union[Unset, bool]): Optional : When set to **false** (default) the structure of the
            extracted items is list of objects having different attributes : <br>
                 ```{'items': [{"attribute_1": "x1","attribute_2": "y2"}, ... ]}``` <br>
                 When it is set to **true**, the response contains an object with each attribute as a list : <br>
                 ```{ "attribute_1": ["x1","x2", ...], "attribute_2": [y1, y2, ...]}```  Default: False.
        show_original_response (Union[Unset, bool]): Optional : Shows the original response of the provider.<br>
                    When set to **true**, a new attribute *original_response* will appear in the response object. Default:
            False.
        file (Union[Unset, File]): File to analyse in binary format to be used with *content-type*: **multipart/form-
            data** <br> **Does not work with application/json !**
        file_url (Union[None, Unset, str]): File **URL** to analyse to be used with with *content-type*:
            **application/json**.
        file_password (Union[None, Unset, str]): If your PDF file has a password, you can pass it here!
        language (Union[None, Unset, str]): Language code of the language the document is written in (ex: fr (French),
            en (English), es (Spanish))
        document_type (Union[Unset, DocumentTypeEnum]): * `auto-detect` - auto-detect
            * `invoice` - invoice
            * `receipt` - receipt Default: DocumentTypeEnum.INVOICE.
        convert_to_pdf (Union[None, Unset, bool]): Boolean value to specify weather to convert the doc/docx files to pdf
            format to be accepted by a majority of the providers Default: False.
    """

    providers: str
    fallback_providers: Union[None, Unset, str] = UNSET
    response_as_dict: Union[Unset, bool] = True
    attributes_as_list: Union[Unset, bool] = False
    show_original_response: Union[Unset, bool] = False
    file: Union[Unset, File] = UNSET
    file_url: Union[None, Unset, str] = UNSET
    file_password: Union[None, Unset, str] = UNSET
    language: Union[None, Unset, str] = UNSET
    document_type: Union[Unset, DocumentTypeEnum] = DocumentTypeEnum.INVOICE
    convert_to_pdf: Union[None, Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        providers = self.providers

        fallback_providers: Union[None, Unset, str]
        if isinstance(self.fallback_providers, Unset):
            fallback_providers = UNSET
        else:
            fallback_providers = self.fallback_providers

        response_as_dict = self.response_as_dict

        attributes_as_list = self.attributes_as_list

        show_original_response = self.show_original_response

        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        file_url: Union[None, Unset, str]
        if isinstance(self.file_url, Unset):
            file_url = UNSET
        else:
            file_url = self.file_url

        file_password: Union[None, Unset, str]
        if isinstance(self.file_password, Unset):
            file_password = UNSET
        else:
            file_password = self.file_password

        language: Union[None, Unset, str]
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        document_type: Union[Unset, str] = UNSET
        if not isinstance(self.document_type, Unset):
            document_type = self.document_type.value

        convert_to_pdf: Union[None, Unset, bool]
        if isinstance(self.convert_to_pdf, Unset):
            convert_to_pdf = UNSET
        else:
            convert_to_pdf = self.convert_to_pdf

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providers": providers,
            }
        )
        if fallback_providers is not UNSET:
            field_dict["fallback_providers"] = fallback_providers
        if response_as_dict is not UNSET:
            field_dict["response_as_dict"] = response_as_dict
        if attributes_as_list is not UNSET:
            field_dict["attributes_as_list"] = attributes_as_list
        if show_original_response is not UNSET:
            field_dict["show_original_response"] = show_original_response
        if file is not UNSET:
            field_dict["file"] = file
        if file_url is not UNSET:
            field_dict["file_url"] = file_url
        if file_password is not UNSET:
            field_dict["file_password"] = file_password
        if language is not UNSET:
            field_dict["language"] = language
        if document_type is not UNSET:
            field_dict["document_type"] = document_type
        if convert_to_pdf is not UNSET:
            field_dict["convert_to_pdf"] = convert_to_pdf

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        providers = (
            self.providers if isinstance(self.providers, Unset) else (None, str(self.providers).encode(), "text/plain")
        )

        fallback_providers: Union[None, Unset, str]
        if isinstance(self.fallback_providers, Unset):
            fallback_providers = UNSET
        else:
            fallback_providers = self.fallback_providers

        response_as_dict = (
            self.response_as_dict
            if isinstance(self.response_as_dict, Unset)
            else (None, str(self.response_as_dict).encode(), "text/plain")
        )

        attributes_as_list = (
            self.attributes_as_list
            if isinstance(self.attributes_as_list, Unset)
            else (None, str(self.attributes_as_list).encode(), "text/plain")
        )

        show_original_response = (
            self.show_original_response
            if isinstance(self.show_original_response, Unset)
            else (None, str(self.show_original_response).encode(), "text/plain")
        )

        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        file_url: Union[None, Unset, str]
        if isinstance(self.file_url, Unset):
            file_url = UNSET
        else:
            file_url = self.file_url

        file_password: Union[None, Unset, str]
        if isinstance(self.file_password, Unset):
            file_password = UNSET
        else:
            file_password = self.file_password

        language: Union[None, Unset, str]
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        document_type: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.document_type, Unset):
            document_type = (None, str(self.document_type.value).encode(), "text/plain")

        convert_to_pdf: Union[None, Unset, bool]
        if isinstance(self.convert_to_pdf, Unset):
            convert_to_pdf = UNSET
        else:
            convert_to_pdf = self.convert_to_pdf

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "providers": providers,
            }
        )
        if fallback_providers is not UNSET:
            field_dict["fallback_providers"] = fallback_providers
        if response_as_dict is not UNSET:
            field_dict["response_as_dict"] = response_as_dict
        if attributes_as_list is not UNSET:
            field_dict["attributes_as_list"] = attributes_as_list
        if show_original_response is not UNSET:
            field_dict["show_original_response"] = show_original_response
        if file is not UNSET:
            field_dict["file"] = file
        if file_url is not UNSET:
            field_dict["file_url"] = file_url
        if file_password is not UNSET:
            field_dict["file_password"] = file_password
        if language is not UNSET:
            field_dict["language"] = language
        if document_type is not UNSET:
            field_dict["document_type"] = document_type
        if convert_to_pdf is not UNSET:
            field_dict["convert_to_pdf"] = convert_to_pdf

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        providers = d.pop("providers")

        def _parse_fallback_providers(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fallback_providers = _parse_fallback_providers(d.pop("fallback_providers", UNSET))

        response_as_dict = d.pop("response_as_dict", UNSET)

        attributes_as_list = d.pop("attributes_as_list", UNSET)

        show_original_response = d.pop("show_original_response", UNSET)

        _file = d.pop("file", UNSET)
        file: Union[Unset, File]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        def _parse_file_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        file_url = _parse_file_url(d.pop("file_url", UNSET))

        def _parse_file_password(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        file_password = _parse_file_password(d.pop("file_password", UNSET))

        def _parse_language(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        language = _parse_language(d.pop("language", UNSET))

        _document_type = d.pop("document_type", UNSET)
        document_type: Union[Unset, DocumentTypeEnum]
        if isinstance(_document_type, Unset):
            document_type = UNSET
        else:
            document_type = DocumentTypeEnum(_document_type)

        def _parse_convert_to_pdf(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        convert_to_pdf = _parse_convert_to_pdf(d.pop("convert_to_pdf", UNSET))

        ocrfinancial_parser_financial_parser_request = cls(
            providers=providers,
            fallback_providers=fallback_providers,
            response_as_dict=response_as_dict,
            attributes_as_list=attributes_as_list,
            show_original_response=show_original_response,
            file=file,
            file_url=file_url,
            file_password=file_password,
            language=language,
            document_type=document_type,
            convert_to_pdf=convert_to_pdf,
        )

        ocrfinancial_parser_financial_parser_request.additional_properties = d
        return ocrfinancial_parser_financial_parser_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
