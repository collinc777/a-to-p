# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pydantic_main_audiospeech_to_text_async_speech_to_text_async_data_class94559364729520 import PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559364729520

class TestPydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559364729520(unittest.TestCase):
    """PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559364729520 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559364729520:
        """Test PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559364729520
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559364729520`
        """
        model = PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559364729520()
        if include_optional:
            return PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559364729520(
                text = '',
                diarization = openapi_client.models.speech_diarization.SpeechDiarization(
                    total_speakers = 56, 
                    entries = [
                        openapi_client.models.speech_diarization_entry.SpeechDiarizationEntry(
                            segment = '', 
                            start_time = '', 
                            end_time = '', 
                            speaker = 56, 
                            confidence = 56, )
                        ], 
                    error_message = '', ),
                original_response = None,
                id = '',
                final_status = 'success',
                error = openapi_client.models.error.Error()
            )
        else:
            return PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559364729520(
                text = '',
                diarization = openapi_client.models.speech_diarization.SpeechDiarization(
                    total_speakers = 56, 
                    entries = [
                        openapi_client.models.speech_diarization_entry.SpeechDiarizationEntry(
                            segment = '', 
                            start_time = '', 
                            end_time = '', 
                            speaker = 56, 
                            confidence = 56, )
                        ], 
                    error_message = '', ),
                id = '',
                final_status = 'success',
        )
        """

    def testPydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559364729520(self):
        """Test PydanticMainAudiospeechToTextAsyncSpeechToTextAsyncDataClass94559364729520"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
