# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_audiotext_to_speech_async_text_to_speech_async_data_class94559364747360 import (
    PydanticMainAudiotextToSpeechAsyncTextToSpeechAsyncDataClass94559364747360,
)


class TestPydanticMainAudiotextToSpeechAsyncTextToSpeechAsyncDataClass94559364747360(
    unittest.TestCase
):
    """PydanticMainAudiotextToSpeechAsyncTextToSpeechAsyncDataClass94559364747360 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainAudiotextToSpeechAsyncTextToSpeechAsyncDataClass94559364747360:
        """Test PydanticMainAudiotextToSpeechAsyncTextToSpeechAsyncDataClass94559364747360
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainAudiotextToSpeechAsyncTextToSpeechAsyncDataClass94559364747360`
        """
        model = PydanticMainAudiotextToSpeechAsyncTextToSpeechAsyncDataClass94559364747360()
        if include_optional:
            return PydanticMainAudiotextToSpeechAsyncTextToSpeechAsyncDataClass94559364747360(
                audio = '',
                voice_type = 56,
                audio_resource_url = '',
                original_response = None,
                id = '',
                final_status = 'success',
                error = openapi_client.models.error.Error()
            )
        else:
            return PydanticMainAudiotextToSpeechAsyncTextToSpeechAsyncDataClass94559364747360(
                audio = '',
                voice_type = 56,
                audio_resource_url = '',
                id = '',
                final_status = 'success',
        )
        """

    def testPydanticMainAudiotextToSpeechAsyncTextToSpeechAsyncDataClass94559364747360(
        self,
    ):
        """Test PydanticMainAudiotextToSpeechAsyncTextToSpeechAsyncDataClass94559364747360"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
