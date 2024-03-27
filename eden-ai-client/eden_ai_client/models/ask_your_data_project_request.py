from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.db_provider_enum import DbProviderEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="AskYourDataProjectRequest")


@_attrs_define
class AskYourDataProjectRequest:
    """
    Attributes:
        ocr_provider (str):
        speech_to_text_provider (str):
        project_name (str): Project name
        collection_name (str): Database Collection Name
        credential (Union[None, Unset, str]): The credential resource name
        asset (Union[None, Unset, str]): The asset sub_resource name
        llm_provider (Union[Unset, str]): Select a default LLM provider to use in your project.
        llm_model (Union[Unset, str]): Select a default Model for LLM provider to use in your project
        chunk_size (Union[None, Unset, int]):
        chunk_separators (Union[List[str], None, Unset]):
        db_provider (Union[Unset, DbProviderEnum]): * `qdrant` - qdrant
            * `supabase` - supabase Default: DbProviderEnum.QDRANT.
        embeddings_provider (Union[Unset, str]): Select an embedding provider to use in your search database. Leave
            empty for default. Default: 'cohere'.
    """

    ocr_provider: str
    speech_to_text_provider: str
    project_name: str
    collection_name: str
    credential: Union[None, Unset, str] = UNSET
    asset: Union[None, Unset, str] = UNSET
    llm_provider: Union[Unset, str] = UNSET
    llm_model: Union[Unset, str] = UNSET
    chunk_size: Union[None, Unset, int] = UNSET
    chunk_separators: Union[List[str], None, Unset] = UNSET
    db_provider: Union[Unset, DbProviderEnum] = DbProviderEnum.QDRANT
    embeddings_provider: Union[Unset, str] = "cohere"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ocr_provider = self.ocr_provider

        speech_to_text_provider = self.speech_to_text_provider

        project_name = self.project_name

        collection_name = self.collection_name

        credential: Union[None, Unset, str]
        if isinstance(self.credential, Unset):
            credential = UNSET
        else:
            credential = self.credential

        asset: Union[None, Unset, str]
        if isinstance(self.asset, Unset):
            asset = UNSET
        else:
            asset = self.asset

        llm_provider = self.llm_provider

        llm_model = self.llm_model

        chunk_size: Union[None, Unset, int]
        if isinstance(self.chunk_size, Unset):
            chunk_size = UNSET
        else:
            chunk_size = self.chunk_size

        chunk_separators: Union[List[str], None, Unset]
        if isinstance(self.chunk_separators, Unset):
            chunk_separators = UNSET
        elif isinstance(self.chunk_separators, list):
            chunk_separators = self.chunk_separators

        else:
            chunk_separators = self.chunk_separators

        db_provider: Union[Unset, str] = UNSET
        if not isinstance(self.db_provider, Unset):
            db_provider = self.db_provider.value

        embeddings_provider = self.embeddings_provider

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ocr_provider": ocr_provider,
                "speech_to_text_provider": speech_to_text_provider,
                "project_name": project_name,
                "collection_name": collection_name,
            }
        )
        if credential is not UNSET:
            field_dict["credential"] = credential
        if asset is not UNSET:
            field_dict["asset"] = asset
        if llm_provider is not UNSET:
            field_dict["llm_provider"] = llm_provider
        if llm_model is not UNSET:
            field_dict["llm_model"] = llm_model
        if chunk_size is not UNSET:
            field_dict["chunk_size"] = chunk_size
        if chunk_separators is not UNSET:
            field_dict["chunk_separators"] = chunk_separators
        if db_provider is not UNSET:
            field_dict["db_provider"] = db_provider
        if embeddings_provider is not UNSET:
            field_dict["embeddings_provider"] = embeddings_provider

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ocr_provider = d.pop("ocr_provider")

        speech_to_text_provider = d.pop("speech_to_text_provider")

        project_name = d.pop("project_name")

        collection_name = d.pop("collection_name")

        def _parse_credential(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        credential = _parse_credential(d.pop("credential", UNSET))

        def _parse_asset(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset = _parse_asset(d.pop("asset", UNSET))

        llm_provider = d.pop("llm_provider", UNSET)

        llm_model = d.pop("llm_model", UNSET)

        def _parse_chunk_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        chunk_size = _parse_chunk_size(d.pop("chunk_size", UNSET))

        def _parse_chunk_separators(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                chunk_separators_type_0 = cast(List[str], data)

                return chunk_separators_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        chunk_separators = _parse_chunk_separators(d.pop("chunk_separators", UNSET))

        _db_provider = d.pop("db_provider", UNSET)
        db_provider: Union[Unset, DbProviderEnum]
        if isinstance(_db_provider, Unset):
            db_provider = UNSET
        else:
            db_provider = DbProviderEnum(_db_provider)

        embeddings_provider = d.pop("embeddings_provider", UNSET)

        ask_your_data_project_request = cls(
            ocr_provider=ocr_provider,
            speech_to_text_provider=speech_to_text_provider,
            project_name=project_name,
            collection_name=collection_name,
            credential=credential,
            asset=asset,
            llm_provider=llm_provider,
            llm_model=llm_model,
            chunk_size=chunk_size,
            chunk_separators=chunk_separators,
            db_provider=db_provider,
            embeddings_provider=embeddings_provider,
        )

        ask_your_data_project_request.additional_properties = d
        return ask_your_data_project_request

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
