from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.yoda_query_response_payload import YodaQueryResponsePayload


T = TypeVar("T", bound="YodaQueryResponseItem")


@_attrs_define
class YodaQueryResponseItem:
    """
    Attributes:
        id (str):
        version (int):
        score (int):
        payload (YodaQueryResponsePayload):
        vector (Any):
    """

    id: str
    version: int
    score: int
    payload: "YodaQueryResponsePayload"
    vector: Any
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        version = self.version

        score = self.score

        payload = self.payload.to_dict()

        vector = self.vector

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "version": version,
                "score": score,
                "payload": payload,
                "vector": vector,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.yoda_query_response_payload import YodaQueryResponsePayload

        d = src_dict.copy()
        id = d.pop("id")

        version = d.pop("version")

        score = d.pop("score")

        payload = YodaQueryResponsePayload.from_dict(d.pop("payload"))

        vector = d.pop("vector")

        yoda_query_response_item = cls(
            id=id,
            version=version,
            score=score,
            payload=payload,
            vector=vector,
        )

        yoda_query_response_item.additional_properties = d
        return yoda_query_response_item

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
