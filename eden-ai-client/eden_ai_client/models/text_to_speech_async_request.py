import json
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.option_enum import OptionEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_speech_async_request_users_webhook_parameters import (
        TextToSpeechAsyncRequestUsersWebhookParameters,
    )


T = TypeVar("T", bound="TextToSpeechAsyncRequest")


@_attrs_define
class TextToSpeechAsyncRequest:
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

        show_original_response (Union[Unset, bool]): Optional : Shows the original response of the provider.<br>
                    When set to **true**, a new attribute *original_response* will appear in the response object. Default:
            False.
        webhook_receiver (Union[Unset, str]): Webhook receiver should be a valid https URL (ex :
            https://your.listner.com/endpoint).             After the processing is done, the webhook endpoint will receive
            a POST request with the result.
        users_webhook_parameters (Union[Unset, TextToSpeechAsyncRequestUsersWebhookParameters]): Json data that contains
            of additional parameters that will be sent back to the webhook receiver             (ex: api key for security or
            client's data ID to link the result internally).             Will only be used when webhook_receiver is set.
        settings (Union[Unset, str]): A dictionnary or a json object to specify specific models to use for some
            providers. <br>                     It can be in the following format: {"google" : "google_model", "ibm":
            "ibm_model"...}.
                                 **Caution**: setting models can be done only with `Content-Type` : `application/json`.
                                  Default: '{}'.
        language (Union[None, Unset, str]): Language code expected (ex: en, fr) Default: ''.
        option (Union[BlankEnum, OptionEnum, Unset]):  Default: BlankEnum.VALUE_0.
        rate (Union[None, Unset, int]): Increase or decrease the speaking rate by expressing a positif or negatif number
            ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%) Default: 0.
        pitch (Union[None, Unset, int]): Increase or decrease the speaking pitch by expressing a positif or negatif
            number ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%)
            Default: 0.
        volume (Union[None, Unset, int]): Increase or decrease the audio volume by expressing a positif or negatif
            number ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%)
            Default: 0.
        audio_format (Union[None, Unset, str]): Optional parameter to specify the audio format in which the audio will
            be generated. By default,             audios are encoded in MP3, except for lovoai which use the wav container.
            Default: ''.
        sampling_rate (Union[None, Unset, int]): Optional. The synthesis sample rate (in hertz) for this audio. When
            this is specified, the audio will be converted             either to the right passed value, or to a the nearest
            value acceptable by the provider Default: 0.
    """

    providers: str
    text: str
    fallback_providers: Union[None, Unset, str] = UNSET
    show_original_response: Union[Unset, bool] = False
    webhook_receiver: Union[Unset, str] = UNSET
    users_webhook_parameters: Union[Unset, "TextToSpeechAsyncRequestUsersWebhookParameters"] = UNSET
    settings: Union[Unset, str] = "{}"
    language: Union[None, Unset, str] = ""
    option: Union[BlankEnum, OptionEnum, Unset] = BlankEnum.VALUE_0
    rate: Union[None, Unset, int] = 0
    pitch: Union[None, Unset, int] = 0
    volume: Union[None, Unset, int] = 0
    audio_format: Union[None, Unset, str] = ""
    sampling_rate: Union[None, Unset, int] = 0
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        providers = self.providers

        text = self.text

        fallback_providers: Union[None, Unset, str]
        if isinstance(self.fallback_providers, Unset):
            fallback_providers = UNSET
        else:
            fallback_providers = self.fallback_providers

        show_original_response = self.show_original_response

        webhook_receiver = self.webhook_receiver

        users_webhook_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.users_webhook_parameters, Unset):
            users_webhook_parameters = self.users_webhook_parameters.to_dict()

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

        rate: Union[None, Unset, int]
        if isinstance(self.rate, Unset):
            rate = UNSET
        else:
            rate = self.rate

        pitch: Union[None, Unset, int]
        if isinstance(self.pitch, Unset):
            pitch = UNSET
        else:
            pitch = self.pitch

        volume: Union[None, Unset, int]
        if isinstance(self.volume, Unset):
            volume = UNSET
        else:
            volume = self.volume

        audio_format: Union[None, Unset, str]
        if isinstance(self.audio_format, Unset):
            audio_format = UNSET
        else:
            audio_format = self.audio_format

        sampling_rate: Union[None, Unset, int]
        if isinstance(self.sampling_rate, Unset):
            sampling_rate = UNSET
        else:
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
        if show_original_response is not UNSET:
            field_dict["show_original_response"] = show_original_response
        if webhook_receiver is not UNSET:
            field_dict["webhook_receiver"] = webhook_receiver
        if users_webhook_parameters is not UNSET:
            field_dict["users_webhook_parameters"] = users_webhook_parameters
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

    def to_multipart(self) -> Dict[str, Any]:
        providers = (
            self.providers if isinstance(self.providers, Unset) else (None, str(self.providers).encode(), "text/plain")
        )

        text = self.text if isinstance(self.text, Unset) else (None, str(self.text).encode(), "text/plain")

        fallback_providers: Union[None, Unset, str]
        if isinstance(self.fallback_providers, Unset):
            fallback_providers = UNSET
        else:
            fallback_providers = self.fallback_providers

        show_original_response = (
            self.show_original_response
            if isinstance(self.show_original_response, Unset)
            else (None, str(self.show_original_response).encode(), "text/plain")
        )

        webhook_receiver = (
            self.webhook_receiver
            if isinstance(self.webhook_receiver, Unset)
            else (None, str(self.webhook_receiver).encode(), "text/plain")
        )

        users_webhook_parameters: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.users_webhook_parameters, Unset):
            users_webhook_parameters = (
                None,
                json.dumps(self.users_webhook_parameters.to_dict()).encode(),
                "application/json",
            )

        settings = (
            self.settings if isinstance(self.settings, Unset) else (None, str(self.settings).encode(), "text/plain")
        )

        language: Union[None, Unset, str]
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        option: Union[BlankEnum, OptionEnum, Unset]
        if isinstance(self.option, Unset):
            option = UNSET
        elif isinstance(self.option, OptionEnum):
            option = (None, str(self.option.value).encode(), "text/plain")
        else:
            option = (None, str(self.option.value).encode(), "text/plain")

        rate: Union[None, Unset, int]
        if isinstance(self.rate, Unset):
            rate = UNSET
        else:
            rate = self.rate

        pitch: Union[None, Unset, int]
        if isinstance(self.pitch, Unset):
            pitch = UNSET
        else:
            pitch = self.pitch

        volume: Union[None, Unset, int]
        if isinstance(self.volume, Unset):
            volume = UNSET
        else:
            volume = self.volume

        audio_format: Union[None, Unset, str]
        if isinstance(self.audio_format, Unset):
            audio_format = UNSET
        else:
            audio_format = self.audio_format

        sampling_rate: Union[None, Unset, int]
        if isinstance(self.sampling_rate, Unset):
            sampling_rate = UNSET
        else:
            sampling_rate = self.sampling_rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "providers": providers,
                "text": text,
            }
        )
        if fallback_providers is not UNSET:
            field_dict["fallback_providers"] = fallback_providers
        if show_original_response is not UNSET:
            field_dict["show_original_response"] = show_original_response
        if webhook_receiver is not UNSET:
            field_dict["webhook_receiver"] = webhook_receiver
        if users_webhook_parameters is not UNSET:
            field_dict["users_webhook_parameters"] = users_webhook_parameters
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
        from ..models.text_to_speech_async_request_users_webhook_parameters import (
            TextToSpeechAsyncRequestUsersWebhookParameters,
        )

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

        show_original_response = d.pop("show_original_response", UNSET)

        webhook_receiver = d.pop("webhook_receiver", UNSET)

        _users_webhook_parameters = d.pop("users_webhook_parameters", UNSET)
        users_webhook_parameters: Union[Unset, TextToSpeechAsyncRequestUsersWebhookParameters]
        if isinstance(_users_webhook_parameters, Unset):
            users_webhook_parameters = UNSET
        else:
            users_webhook_parameters = TextToSpeechAsyncRequestUsersWebhookParameters.from_dict(
                _users_webhook_parameters
            )

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

        def _parse_rate(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        rate = _parse_rate(d.pop("rate", UNSET))

        def _parse_pitch(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pitch = _parse_pitch(d.pop("pitch", UNSET))

        def _parse_volume(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        volume = _parse_volume(d.pop("volume", UNSET))

        def _parse_audio_format(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        audio_format = _parse_audio_format(d.pop("audio_format", UNSET))

        def _parse_sampling_rate(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sampling_rate = _parse_sampling_rate(d.pop("sampling_rate", UNSET))

        text_to_speech_async_request = cls(
            providers=providers,
            text=text,
            fallback_providers=fallback_providers,
            show_original_response=show_original_response,
            webhook_receiver=webhook_receiver,
            users_webhook_parameters=users_webhook_parameters,
            settings=settings,
            language=language,
            option=option,
            rate=rate,
            pitch=pitch,
            volume=volume,
            audio_format=audio_format,
            sampling_rate=sampling_rate,
        )

        text_to_speech_async_request.additional_properties = d
        return text_to_speech_async_request

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
