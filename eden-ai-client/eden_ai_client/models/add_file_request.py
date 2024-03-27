from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_type_enum import DataTypeEnum
from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="AddFileRequest")


@_attrs_define
class AddFileRequest:
    """
    Attributes:
        data_type (DataTypeEnum): * `pdf` - pdf
            * `audio` - audio
            * `csv` - csv
        file (Union[Unset, File]): File to analyse in binary format to be used with *content-type*: **multipart/form-
            data** <br> **Does not work with application/json !**
        file_url (Union[None, Unset, str]): File **URL** to analyse to be used with with *content-type*:
            **application/json**.
        metadata (Union[Unset, str]): Optional parameter: Attach metadata to the uploaded file data in your database.
            Provide a stringified JSON with key-value pairs. Useful in `filter_document` when querying the language model,
            it allows you to filter data with your Chatbot by considering only documents that have the specified metadata.
        provider (Union[None, Unset, str]): Select a provider to use, only for audio (speech-to-text) & pdf (ocr-async)
            files.
    """

    data_type: DataTypeEnum
    file: Union[Unset, File] = UNSET
    file_url: Union[None, Unset, str] = UNSET
    metadata: Union[Unset, str] = UNSET
    provider: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_type = self.data_type.value

        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        file_url: Union[None, Unset, str]
        if isinstance(self.file_url, Unset):
            file_url = UNSET
        else:
            file_url = self.file_url

        metadata = self.metadata

        provider: Union[None, Unset, str]
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_type": data_type,
            }
        )
        if file is not UNSET:
            field_dict["file"] = file
        if file_url is not UNSET:
            field_dict["file_url"] = file_url
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        data_type = (None, str(self.data_type.value).encode(), "text/plain")

        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        file_url: Union[None, Unset, str]
        if isinstance(self.file_url, Unset):
            file_url = UNSET
        else:
            file_url = self.file_url

        metadata = (
            self.metadata if isinstance(self.metadata, Unset) else (None, str(self.metadata).encode(), "text/plain")
        )

        provider: Union[None, Unset, str]
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "data_type": data_type,
            }
        )
        if file is not UNSET:
            field_dict["file"] = file
        if file_url is not UNSET:
            field_dict["file_url"] = file_url
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data_type = DataTypeEnum(d.pop("data_type"))

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

        metadata = d.pop("metadata", UNSET)

        def _parse_provider(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        provider = _parse_provider(d.pop("provider", UNSET))

        add_file_request = cls(
            data_type=data_type,
            file=file,
            file_url=file_url,
            metadata=metadata,
            provider=provider,
        )

        add_file_request.additional_properties = d
        return add_file_request

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
