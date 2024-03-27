from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="YodaAskLlmResponse")


@_attrs_define
class YodaAskLlmResponse:
    """
    Attributes:
        result (str):
        llm_provider (str):
        llm_model (str):
    """

    result: str
    llm_provider: str
    llm_model: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result = self.result

        llm_provider = self.llm_provider

        llm_model = self.llm_model

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result": result,
                "llm_provider": llm_provider,
                "llm_model": llm_model,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        result = d.pop("result")

        llm_provider = d.pop("llm_provider")

        llm_model = d.pop("llm_model")

        yoda_ask_llm_response = cls(
            result=result,
            llm_provider=llm_provider,
            llm_model=llm_model,
        )

        yoda_ask_llm_response.additional_properties = d
        return yoda_ask_llm_response

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
