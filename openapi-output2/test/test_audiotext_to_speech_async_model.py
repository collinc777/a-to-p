# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.audiotext_to_speech_async_model import (
    AudiotextToSpeechAsyncModel,
)


class TestAudiotextToSpeechAsyncModel(unittest.TestCase):
    """AudiotextToSpeechAsyncModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AudiotextToSpeechAsyncModel:
        """Test AudiotextToSpeechAsyncModel
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AudiotextToSpeechAsyncModel`
        """
        model = AudiotextToSpeechAsyncModel()
        if include_optional:
            return AudiotextToSpeechAsyncModel(
                lovoai = openapi_client.models.audiotext_to_speech_async_text_to_speech_async_data_class.audiotext_to_speech_asyncTextToSpeechAsyncDataClass(
                    audio = '', 
                    voice_type = 56, 
                    audio_resource_url = '', 
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                amazon = openapi_client.models.audiotext_to_speech_async_text_to_speech_async_data_class.audiotext_to_speech_asyncTextToSpeechAsyncDataClass(
                    audio = '', 
                    voice_type = 56, 
                    audio_resource_url = '', 
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), )
            )
        else:
            return AudiotextToSpeechAsyncModel(
        )
        """

    def testAudiotextToSpeechAsyncModel(self):
        """Test AudiotextToSpeechAsyncModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()