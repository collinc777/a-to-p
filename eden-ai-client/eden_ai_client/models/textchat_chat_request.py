from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.textchat_chat_request_previous_history_item import TextchatChatRequestPreviousHistoryItem


T = TypeVar("T", bound="TextchatChatRequest")


@_attrs_define
class TextchatChatRequest:
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
        settings (Union[Unset, str]): A dictionnary or a json object to specify specific models to use for some
            providers. <br>                     It can be in the following format: {"google" : "google_model", "ibm":
            "ibm_model"...}.
                                 **Caution**: setting models can be done only with `Content-Type` : `application/json`.
                                  Default: '{}'.
        text (Union[None, Unset, str]): Start your conversation here... Default: ''.
        chatbot_global_action (Union[None, Unset, str]): A system message that helps set the behavior of the assistant.
            For example, 'You are a helpful assistant'. Default: ''.
        previous_history (Union[Unset, List['TextchatChatRequestPreviousHistoryItem']]): A list containing all the
            previous conversations between the user and the chatbot AI. Each item in the list should be a dictionary with
            two keys: 'role' and 'message'. The 'role' key specifies the role of the speaker and can have the values 'user'
            or 'assistant'. The 'message' key contains the text of the conversation from the respective role. For example:
            [{'role': 'user', 'message': 'Hello'}, {'role': 'assistant', 'message': 'Hi, how can I help you?'}, ...]. This
            format allows easy identification of the speaker's role and their corresponding message.
        temperature (Union[Unset, float]): Higher values mean the model will take more risks and value 0 (argmax
            sampling) works better for scenarios with a well-defined answer. Default: 0.0.
        max_tokens (Union[Unset, int]): The maximum number of tokens to generate in the completion. The token count of
            your prompt plus max_tokens cannot exceed the model's context length. Default: 1000.
    """

    providers: str
    fallback_providers: Union[None, Unset, str] = UNSET
    response_as_dict: Union[Unset, bool] = True
    attributes_as_list: Union[Unset, bool] = False
    show_original_response: Union[Unset, bool] = False
    settings: Union[Unset, str] = "{}"
    text: Union[None, Unset, str] = ""
    chatbot_global_action: Union[None, Unset, str] = ""
    previous_history: Union[Unset, List["TextchatChatRequestPreviousHistoryItem"]] = UNSET
    temperature: Union[Unset, float] = 0.0
    max_tokens: Union[Unset, int] = 1000
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

        settings = self.settings

        text: Union[None, Unset, str]
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        chatbot_global_action: Union[None, Unset, str]
        if isinstance(self.chatbot_global_action, Unset):
            chatbot_global_action = UNSET
        else:
            chatbot_global_action = self.chatbot_global_action

        previous_history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.previous_history, Unset):
            previous_history = []
            for previous_history_item_data in self.previous_history:
                previous_history_item = previous_history_item_data.to_dict()
                previous_history.append(previous_history_item)

        temperature = self.temperature

        max_tokens = self.max_tokens

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
        if settings is not UNSET:
            field_dict["settings"] = settings
        if text is not UNSET:
            field_dict["text"] = text
        if chatbot_global_action is not UNSET:
            field_dict["chatbot_global_action"] = chatbot_global_action
        if previous_history is not UNSET:
            field_dict["previous_history"] = previous_history
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.textchat_chat_request_previous_history_item import TextchatChatRequestPreviousHistoryItem

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

        settings = d.pop("settings", UNSET)

        def _parse_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_chatbot_global_action(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        chatbot_global_action = _parse_chatbot_global_action(d.pop("chatbot_global_action", UNSET))

        previous_history = []
        _previous_history = d.pop("previous_history", UNSET)
        for previous_history_item_data in _previous_history or []:
            previous_history_item = TextchatChatRequestPreviousHistoryItem.from_dict(previous_history_item_data)

            previous_history.append(previous_history_item)

        temperature = d.pop("temperature", UNSET)

        max_tokens = d.pop("max_tokens", UNSET)

        textchat_chat_request = cls(
            providers=providers,
            fallback_providers=fallback_providers,
            response_as_dict=response_as_dict,
            attributes_as_list=attributes_as_list,
            show_original_response=show_original_response,
            settings=settings,
            text=text,
            chatbot_global_action=chatbot_global_action,
            previous_history=previous_history,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        textchat_chat_request.additional_properties = d
        return textchat_chat_request

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
