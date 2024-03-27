import json
from io import BytesIO
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

if TYPE_CHECKING:
    from ..models.async_video_analysis_request_users_webhook_parameters import (
        AsyncVideoAnalysisRequestUsersWebhookParameters,
    )


T = TypeVar("T", bound="AsyncVideoAnalysisRequest")


@_attrs_define
class AsyncVideoAnalysisRequest:
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
        users_webhook_parameters (Union[Unset, AsyncVideoAnalysisRequestUsersWebhookParameters]): Json data that
            contains of additional parameters that will be sent back to the webhook receiver             (ex: api key for
            security or client's data ID to link the result internally).             Will only be used when webhook_receiver
            is set.
        file (Union[Unset, File]): File to analyse in binary format to be used with *content-type*: **multipart/form-
            data** <br> **Does not work with application/json !**
        file_url (Union[None, Unset, str]): File **URL** to analyse to be used with with *content-type*:
            **application/json**.
    """

    providers: str
    fallback_providers: Union[None, Unset, str] = UNSET
    show_original_response: Union[Unset, bool] = False
    webhook_receiver: Union[Unset, str] = UNSET
    users_webhook_parameters: Union[Unset, "AsyncVideoAnalysisRequestUsersWebhookParameters"] = UNSET
    file: Union[Unset, File] = UNSET
    file_url: Union[None, Unset, str] = UNSET
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

        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        file_url: Union[None, Unset, str]
        if isinstance(self.file_url, Unset):
            file_url = UNSET
        else:
            file_url = self.file_url

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
        if file is not UNSET:
            field_dict["file"] = file
        if file_url is not UNSET:
            field_dict["file_url"] = file_url

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

        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        file_url: Union[None, Unset, str]
        if isinstance(self.file_url, Unset):
            file_url = UNSET
        else:
            file_url = self.file_url

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
        if file is not UNSET:
            field_dict["file"] = file
        if file_url is not UNSET:
            field_dict["file_url"] = file_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.async_video_analysis_request_users_webhook_parameters import (
            AsyncVideoAnalysisRequestUsersWebhookParameters,
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
        users_webhook_parameters: Union[Unset, AsyncVideoAnalysisRequestUsersWebhookParameters]
        if isinstance(_users_webhook_parameters, Unset):
            users_webhook_parameters = UNSET
        else:
            users_webhook_parameters = AsyncVideoAnalysisRequestUsersWebhookParameters.from_dict(
                _users_webhook_parameters
            )

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

        async_video_analysis_request = cls(
            providers=providers,
            fallback_providers=fallback_providers,
            show_original_response=show_original_response,
            webhook_receiver=webhook_receiver,
            users_webhook_parameters=users_webhook_parameters,
            file=file,
            file_url=file_url,
        )

        async_video_analysis_request.additional_properties = d
        return async_video_analysis_request

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
