from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="YodaInfoResponse")


@_attrs_define
class YodaInfoResponse:
    """
    Attributes:
        db_provider (str):
        embeddings_provider (str):
        llm_provider (str):
        llm_model (str):
        collection_size (int):
    """

    db_provider: str
    embeddings_provider: str
    llm_provider: str
    llm_model: str
    collection_size: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        db_provider = self.db_provider

        embeddings_provider = self.embeddings_provider

        llm_provider = self.llm_provider

        llm_model = self.llm_model

        collection_size = self.collection_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "db_provider": db_provider,
                "embeddings_provider": embeddings_provider,
                "llm_provider": llm_provider,
                "llm_model": llm_model,
                "collection_size": collection_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        db_provider = d.pop("db_provider")

        embeddings_provider = d.pop("embeddings_provider")

        llm_provider = d.pop("llm_provider")

        llm_model = d.pop("llm_model")

        collection_size = d.pop("collection_size")

        yoda_info_response = cls(
            db_provider=db_provider,
            embeddings_provider=embeddings_provider,
            llm_provider=llm_provider,
            llm_model=llm_model,
            collection_size=collection_size,
        )

        yoda_info_response.additional_properties = d
        return yoda_info_response

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
