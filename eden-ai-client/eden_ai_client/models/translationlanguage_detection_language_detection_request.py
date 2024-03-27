from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranslationlanguageDetectionLanguageDetectionRequest")


@_attrs_define
class TranslationlanguageDetectionLanguageDetectionRequest:
    """
    Attributes:
        providers (str): It can be one (ex: **'amazon'** or **'google'**) or multiple provider(s) (ex:
            **'amazon,microsoft,google'**)             that the data will be redirected to in order to get the processed
            results.
        text (str): Text to analyze
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
    """

    providers: str
    text: str
    fallback_providers: Union[None, Unset, str] = UNSET
    response_as_dict: Union[Unset, bool] = True
    attributes_as_list: Union[Unset, bool] = False
    show_original_response: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        providers = self.providers

        text = self.text

        fallback_providers: Union[None, Unset, str]
        if isinstance(self.fallback_providers, Unset):
            fallback_providers = UNSET
        else:
            fallback_providers = self.fallback_providers

        response_as_dict = self.response_as_dict

        attributes_as_list = self.attributes_as_list

        show_original_response = self.show_original_response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providers": providers,
                "text": text,
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        providers = d.pop("providers")

        text = d.pop("text")

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

        translationlanguage_detection_language_detection_request = cls(
            providers=providers,
            text=text,
            fallback_providers=fallback_providers,
            response_as_dict=response_as_dict,
            attributes_as_list=attributes_as_list,
            show_original_response=show_original_response,
        )

        translationlanguage_detection_language_detection_request.additional_properties = d
        return translationlanguage_detection_language_detection_request

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
