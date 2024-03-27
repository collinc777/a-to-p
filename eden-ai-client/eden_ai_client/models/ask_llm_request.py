from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ask_llm_request_filter_documents import AskLLMRequestFilterDocuments
    from ..models.ask_llm_request_history_item import AskLLMRequestHistoryItem


T = TypeVar("T", bound="AskLLMRequest")


@_attrs_define
class AskLLMRequest:
    """
    Attributes:
        query (str): Enter your question or query about the data. The large language model (LLM) will provide a
            response.
        llm_provider (Union[Unset, str]): Select a provider for the large language model for processing. Leave empty for
            default. Default: 'openai'.
        llm_model (Union[Unset, str]): Specify the model to use for language processing. Leave empty for default.
        k (Union[Unset, int]): How many results chunk you want to return Default: 3.
        history (Union[Unset, List['AskLLMRequestHistoryItem']]): A list containing all the previous conversations
            between the user and the chatbot AI. Each item in the list should be a dictionary with two keys: 'user' and
            'assistant'.
        chatbot_global_action (Union[Unset, str]): A system message that helps set the behavior of the assistant.
        filter_documents (Union[Unset, AskLLMRequestFilterDocuments]): Filter uploaded documents based on their
            metadata. Specify key-value pairs where the key represents the metadata field and the value is the desired
            metadata value. Please ensure that the provided metadata keys are available in your database.
        temperature (Union[Unset, float]): Higher values mean the model will take more risks and value 0 (argmax
            sampling) works better for scenarios with a well-defined answer. Default: 0.0.
        max_tokens (Union[Unset, int]): The maximum number of tokens to generate in the completion. The token count of
            your prompt plus max_tokens cannot exceed the model's context length. Default: 100.
    """

    query: str
    llm_provider: Union[Unset, str] = "openai"
    llm_model: Union[Unset, str] = UNSET
    k: Union[Unset, int] = 3
    history: Union[Unset, List["AskLLMRequestHistoryItem"]] = UNSET
    chatbot_global_action: Union[Unset, str] = UNSET
    filter_documents: Union[Unset, "AskLLMRequestFilterDocuments"] = UNSET
    temperature: Union[Unset, float] = 0.0
    max_tokens: Union[Unset, int] = 100
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query = self.query

        llm_provider = self.llm_provider

        llm_model = self.llm_model

        k = self.k

        history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()
                history.append(history_item)

        chatbot_global_action = self.chatbot_global_action

        filter_documents: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_documents, Unset):
            filter_documents = self.filter_documents.to_dict()

        temperature = self.temperature

        max_tokens = self.max_tokens

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if llm_provider is not UNSET:
            field_dict["llm_provider"] = llm_provider
        if llm_model is not UNSET:
            field_dict["llm_model"] = llm_model
        if k is not UNSET:
            field_dict["k"] = k
        if history is not UNSET:
            field_dict["history"] = history
        if chatbot_global_action is not UNSET:
            field_dict["chatbot_global_action"] = chatbot_global_action
        if filter_documents is not UNSET:
            field_dict["filter_documents"] = filter_documents
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ask_llm_request_filter_documents import AskLLMRequestFilterDocuments
        from ..models.ask_llm_request_history_item import AskLLMRequestHistoryItem

        d = src_dict.copy()
        query = d.pop("query")

        llm_provider = d.pop("llm_provider", UNSET)

        llm_model = d.pop("llm_model", UNSET)

        k = d.pop("k", UNSET)

        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in _history or []:
            history_item = AskLLMRequestHistoryItem.from_dict(history_item_data)

            history.append(history_item)

        chatbot_global_action = d.pop("chatbot_global_action", UNSET)

        _filter_documents = d.pop("filter_documents", UNSET)
        filter_documents: Union[Unset, AskLLMRequestFilterDocuments]
        if isinstance(_filter_documents, Unset):
            filter_documents = UNSET
        else:
            filter_documents = AskLLMRequestFilterDocuments.from_dict(_filter_documents)

        temperature = d.pop("temperature", UNSET)

        max_tokens = d.pop("max_tokens", UNSET)

        ask_llm_request = cls(
            query=query,
            llm_provider=llm_provider,
            llm_model=llm_model,
            k=k,
            history=history,
            chatbot_global_action=chatbot_global_action,
            filter_documents=filter_documents,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        ask_llm_request.additional_properties = d
        return ask_llm_request

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
