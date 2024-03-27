import json
from io import BytesIO
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

if TYPE_CHECKING:
    from ..models.speech_to_text_async_request_users_webhook_parameters import (
        SpeechToTextAsyncRequestUsersWebhookParameters,
    )


T = TypeVar("T", bound="SpeechToTextAsyncRequest")


@_attrs_define
class SpeechToTextAsyncRequest:
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

        show_original_response (Union[Unset, bool]): Optional : Shows the original response of the provider.<br>
                    When set to **true**, a new attribute *original_response* will appear in the response object. Default:
            False.
        webhook_receiver (Union[Unset, str]): Webhook receiver should be a valid https URL (ex :
            https://your.listner.com/endpoint).             After the processing is done, the webhook endpoint will receive
            a POST request with the result.
        users_webhook_parameters (Union[Unset, SpeechToTextAsyncRequestUsersWebhookParameters]): Json data that contains
            of additional parameters that will be sent back to the webhook receiver             (ex: api key for security or
            client's data ID to link the result internally).             Will only be used when webhook_receiver is set.
        settings (Union[Unset, str]): A dictionnary or a json object to specify specific models to use for some
            providers. <br>                     It can be in the following format: {"google" : "google_model", "ibm":
            "ibm_model"...}.
                                 **Caution**: setting models can be done only with `Content-Type` : `application/json`.
                                  Default: '{}'.
        provider_params (Union[Unset, str]):
            Parameters specific to the provider that you want to send along the request.

            it should take a *provider* name as key and an object of parameters as value.

            Example:

                {
                  "deepgram": {
                    "filler_words": true,
                    "smart_format": true,
                    "callback": "https://webhook.site/0000"
                  },
                  "assembly": {
                    "webhook_url": "https://webhook.site/0000"
                  }
                }

            Please refer to the documentation of each provider to see which parameters to send.
        file (Union[Unset, File]): File to analyse in binary format to be used with *content-type*: **multipart/form-
            data** <br> **Does not work with application/json !**
        file_url (Union[None, Unset, str]): File **URL** to analyse to be used with with *content-type*:
            **application/json**.
        language (Union[None, Unset, str]): Language code expected (ex: en, fr)
        speakers (Union[None, Unset, int]): Number of speakers in the file audio Default: 2.
        profanity_filter (Union[None, Unset, bool]): Boolean value to specify weather or not the service will filter
            profanity and replace inappropriate words with a series of asterisks Default: False.
        custom_vocabulary (Union[Unset, str]): List of words or composed words to be detected by the speech to text
            engine. (Ex: Word, Mike, Draw, Los Angeles,...) Default: ''.
        convert_to_wav (Union[None, Unset, bool]): Boolean value to specify weather to convert the audio/video file to
            wav format to be accepted by a majority of the providers Default: False.
    """

    providers: str
    fallback_providers: Union[None, Unset, str] = UNSET
    show_original_response: Union[Unset, bool] = False
    webhook_receiver: Union[Unset, str] = UNSET
    users_webhook_parameters: Union[Unset, "SpeechToTextAsyncRequestUsersWebhookParameters"] = UNSET
    settings: Union[Unset, str] = "{}"
    provider_params: Union[Unset, str] = UNSET
    file: Union[Unset, File] = UNSET
    file_url: Union[None, Unset, str] = UNSET
    language: Union[None, Unset, str] = UNSET
    speakers: Union[None, Unset, int] = 2
    profanity_filter: Union[None, Unset, bool] = False
    custom_vocabulary: Union[Unset, str] = ""
    convert_to_wav: Union[None, Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        providers = self.providers

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

        provider_params = self.provider_params

        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        file_url: Union[None, Unset, str]
        if isinstance(self.file_url, Unset):
            file_url = UNSET
        else:
            file_url = self.file_url

        language: Union[None, Unset, str]
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        speakers: Union[None, Unset, int]
        if isinstance(self.speakers, Unset):
            speakers = UNSET
        else:
            speakers = self.speakers

        profanity_filter: Union[None, Unset, bool]
        if isinstance(self.profanity_filter, Unset):
            profanity_filter = UNSET
        else:
            profanity_filter = self.profanity_filter

        custom_vocabulary = self.custom_vocabulary

        convert_to_wav: Union[None, Unset, bool]
        if isinstance(self.convert_to_wav, Unset):
            convert_to_wav = UNSET
        else:
            convert_to_wav = self.convert_to_wav

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providers": providers,
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
        if provider_params is not UNSET:
            field_dict["provider_params"] = provider_params
        if file is not UNSET:
            field_dict["file"] = file
        if file_url is not UNSET:
            field_dict["file_url"] = file_url
        if language is not UNSET:
            field_dict["language"] = language
        if speakers is not UNSET:
            field_dict["speakers"] = speakers
        if profanity_filter is not UNSET:
            field_dict["profanity_filter"] = profanity_filter
        if custom_vocabulary is not UNSET:
            field_dict["custom_vocabulary"] = custom_vocabulary
        if convert_to_wav is not UNSET:
            field_dict["convert_to_wav"] = convert_to_wav

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        providers = (
            self.providers if isinstance(self.providers, Unset) else (None, str(self.providers).encode(), "text/plain")
        )

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

        provider_params = (
            self.provider_params
            if isinstance(self.provider_params, Unset)
            else (None, str(self.provider_params).encode(), "text/plain")
        )

        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        file_url: Union[None, Unset, str]
        if isinstance(self.file_url, Unset):
            file_url = UNSET
        else:
            file_url = self.file_url

        language: Union[None, Unset, str]
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        speakers: Union[None, Unset, int]
        if isinstance(self.speakers, Unset):
            speakers = UNSET
        else:
            speakers = self.speakers

        profanity_filter: Union[None, Unset, bool]
        if isinstance(self.profanity_filter, Unset):
            profanity_filter = UNSET
        else:
            profanity_filter = self.profanity_filter

        custom_vocabulary = (
            self.custom_vocabulary
            if isinstance(self.custom_vocabulary, Unset)
            else (None, str(self.custom_vocabulary).encode(), "text/plain")
        )

        convert_to_wav: Union[None, Unset, bool]
        if isinstance(self.convert_to_wav, Unset):
            convert_to_wav = UNSET
        else:
            convert_to_wav = self.convert_to_wav

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "providers": providers,
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
        if provider_params is not UNSET:
            field_dict["provider_params"] = provider_params
        if file is not UNSET:
            field_dict["file"] = file
        if file_url is not UNSET:
            field_dict["file_url"] = file_url
        if language is not UNSET:
            field_dict["language"] = language
        if speakers is not UNSET:
            field_dict["speakers"] = speakers
        if profanity_filter is not UNSET:
            field_dict["profanity_filter"] = profanity_filter
        if custom_vocabulary is not UNSET:
            field_dict["custom_vocabulary"] = custom_vocabulary
        if convert_to_wav is not UNSET:
            field_dict["convert_to_wav"] = convert_to_wav

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.speech_to_text_async_request_users_webhook_parameters import (
            SpeechToTextAsyncRequestUsersWebhookParameters,
        )

        d = src_dict.copy()
        providers = d.pop("providers")

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
        users_webhook_parameters: Union[Unset, SpeechToTextAsyncRequestUsersWebhookParameters]
        if isinstance(_users_webhook_parameters, Unset):
            users_webhook_parameters = UNSET
        else:
            users_webhook_parameters = SpeechToTextAsyncRequestUsersWebhookParameters.from_dict(
                _users_webhook_parameters
            )

        settings = d.pop("settings", UNSET)

        provider_params = d.pop("provider_params", UNSET)

        _file = d.pop("file", UNSET)
        file: Union[Unset, File]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        def _parse_file_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        file_url = _parse_file_url(d.pop("file_url", UNSET))

        def _parse_language(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_speakers(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        speakers = _parse_speakers(d.pop("speakers", UNSET))

        def _parse_profanity_filter(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        profanity_filter = _parse_profanity_filter(d.pop("profanity_filter", UNSET))

        custom_vocabulary = d.pop("custom_vocabulary", UNSET)

        def _parse_convert_to_wav(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        convert_to_wav = _parse_convert_to_wav(d.pop("convert_to_wav", UNSET))

        speech_to_text_async_request = cls(
            providers=providers,
            fallback_providers=fallback_providers,
            show_original_response=show_original_response,
            webhook_receiver=webhook_receiver,
            users_webhook_parameters=users_webhook_parameters,
            settings=settings,
            provider_params=provider_params,
            file=file,
            file_url=file_url,
            language=language,
            speakers=speakers,
            profanity_filter=profanity_filter,
            custom_vocabulary=custom_vocabulary,
            convert_to_wav=convert_to_wav,
        )

        speech_to_text_async_request.additional_properties = d
        return speech_to_text_async_request

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
