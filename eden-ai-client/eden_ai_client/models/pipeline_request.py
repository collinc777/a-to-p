from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="PipelineRequest")


@_attrs_define
class PipelineRequest:
    """
    Attributes:
        description (str):
        text (Union[Unset, str]): The input text for the first feature of the pipeline
        texts (Union[Unset, str]): List of texts for the first feature of the pipeline
        file (Union[Unset, File]): The input file for the first feature of the pipeline
        return_only_last (Union[Unset, bool]): This parameter allows user to choose to output only the final result or
            all the intermediate results. Default: True.
    """

    description: str
    text: Union[Unset, str] = UNSET
    texts: Union[Unset, str] = UNSET
    file: Union[Unset, File] = UNSET
    return_only_last: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        text = self.text

        texts = self.texts

        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        return_only_last = self.return_only_last

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text
        if texts is not UNSET:
            field_dict["texts"] = texts
        if file is not UNSET:
            field_dict["file"] = file
        if return_only_last is not UNSET:
            field_dict["return_only_last"] = return_only_last

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        text = self.text if isinstance(self.text, Unset) else (None, str(self.text).encode(), "text/plain")

        texts = self.texts if isinstance(self.texts, Unset) else (None, str(self.texts).encode(), "text/plain")

        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        return_only_last = (
            self.return_only_last
            if isinstance(self.return_only_last, Unset)
            else (None, str(self.return_only_last).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "description": description,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text
        if texts is not UNSET:
            field_dict["texts"] = texts
        if file is not UNSET:
            field_dict["file"] = file
        if return_only_last is not UNSET:
            field_dict["return_only_last"] = return_only_last

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        text = d.pop("text", UNSET)

        texts = d.pop("texts", UNSET)

        _file = d.pop("file", UNSET)
        file: Union[Unset, File]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        return_only_last = d.pop("return_only_last", UNSET)

        pipeline_request = cls(
            description=description,
            text=text,
            texts=texts,
            file=file,
            return_only_last=return_only_last,
        )

        pipeline_request.additional_properties = d
        return pipeline_request

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
