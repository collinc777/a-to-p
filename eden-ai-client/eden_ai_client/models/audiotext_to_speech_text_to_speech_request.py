from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.option_enum import OptionEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="AudiotextToSpeechTextToSpeechRequest")


@_attrs_define
class AudiotextToSpeechTextToSpeechRequest:
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
        settings (Union[Unset, str]): A dictionnary or a json object to specify specific models to use for some
            providers. <br>                     It can be in the following format: {"google" : "google_model", "ibm":
            "ibm_model"...}.
                                 **Caution**: setting models can be done only with `Content-Type` : `application/json`.
                                  Default: '{}'.
        language (Union[None, Unset, str]): Language code expected (ex: en, fr) Default: ''.
        option (Union[BlankEnum, OptionEnum, Unset]):  Default: BlankEnum.VALUE_0.
        rate (Union[Unset, int]): Increase or decrease the speaking rate by expressing a positif or negatif number
            ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%) Default: 0.
        pitch (Union[Unset, int]): Increase or decrease the speaking pitch by expressing a positif or negatif number
            ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%) Default: 0.
        volume (Union[Unset, int]): Increase or decrease the audio volume by expressing a positif or negatif number
            ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%) Default: 0.
        audio_format (Union[Unset, str]): Optional parameter to specify the audio format in which the audio will be
            generated. By default,             audios are encoded in MP3, except for lovoai which use the wav container.
            Default: ''.
        sampling_rate (Union[Unset, int]): Optional. The synthesis sample rate (in hertz) for this audio. When this is
            specified, the audio will be converted             either to the right passed value, or to a the nearest value
            acceptable by the provider Default: 0.
    """

    providers: str
    text: str
    fallback_providers: Union[None, Unset, str] = UNSET
    response_as_dict: Union[Unset, bool] = True
    attributes_as_list: Union[Unset, bool] = False
    show_original_response: Union[Unset, bool] = False
    settings: Union[Unset, str] = "{}"
    language: Union[None, Unset, str] = ""
    option: Union[BlankEnum, OptionEnum, Unset] = BlankEnum.VALUE_0
    rate: Union[Unset, int] = 0
    pitch: Union[Unset, int] = 0
    volume: Union[Unset, int] = 0
    audio_format: Union[Unset, str] = ""
    sampling_rate: Union[Unset, int] = 0
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

        settings = self.settings

        language: Union[None, Unset, str]
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        option: Union[Unset, str]
        if isinstance(self.option, Unset):
            option = UNSET
        elif isinstance(self.option, OptionEnum):
            option = self.option.value
        else:
            option = self.option.value

        rate = self.rate

        pitch = self.pitch

        volume = self.volume

        audio_format = self.audio_format

        sampling_rate = self.sampling_rate

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
        if settings is not UNSET:
            field_dict["settings"] = settings
        if language is not UNSET:
            field_dict["language"] = language
        if option is not UNSET:
            field_dict["option"] = option
        if rate is not UNSET:
            field_dict["rate"] = rate
        if pitch is not UNSET:
            field_dict["pitch"] = pitch
        if volume is not UNSET:
            field_dict["volume"] = volume
        if audio_format is not UNSET:
            field_dict["audio_format"] = audio_format
        if sampling_rate is not UNSET:
            field_dict["sampling_rate"] = sampling_rate

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

        settings = d.pop("settings", UNSET)

        def _parse_language(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_option(data: object) -> Union[BlankEnum, OptionEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                option_type_0 = OptionEnum(data)

                return option_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            option_type_1 = BlankEnum(data)

            return option_type_1

        option = _parse_option(d.pop("option", UNSET))

        rate = d.pop("rate", UNSET)

        pitch = d.pop("pitch", UNSET)

        volume = d.pop("volume", UNSET)

        audio_format = d.pop("audio_format", UNSET)

        sampling_rate = d.pop("sampling_rate", UNSET)

        audiotext_to_speech_text_to_speech_request = cls(
            providers=providers,
            text=text,
            fallback_providers=fallback_providers,
            response_as_dict=response_as_dict,
            attributes_as_list=attributes_as_list,
            show_original_response=show_original_response,
            settings=settings,
            language=language,
            option=option,
            rate=rate,
            pitch=pitch,
            volume=volume,
            audio_format=audio_format,
            sampling_rate=sampling_rate,
        )

        audiotext_to_speech_text_to_speech_request.additional_properties = d
        return audiotext_to_speech_text_to_speech_request

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
