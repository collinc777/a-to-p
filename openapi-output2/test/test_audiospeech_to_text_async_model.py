# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.audiospeech_to_text_async_model import (
    AudiospeechToTextAsyncModel,
)


class TestAudiospeechToTextAsyncModel(unittest.TestCase):
    """AudiospeechToTextAsyncModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AudiospeechToTextAsyncModel:
        """Test AudiospeechToTextAsyncModel
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AudiospeechToTextAsyncModel`
        """
        model = AudiospeechToTextAsyncModel()
        if include_optional:
            return AudiospeechToTextAsyncModel(
                voci = openapi_client.models.audiospeech_to_text_async_speech_to_text_async_data_class.audiospeech_to_text_asyncSpeechToTextAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                voxist = openapi_client.models.audiospeech_to_text_async_speech_to_text_async_data_class.audiospeech_to_text_asyncSpeechToTextAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                microsoft = openapi_client.models.audiospeech_to_text_async_speech_to_text_async_data_class.audiospeech_to_text_asyncSpeechToTextAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                google = openapi_client.models.audiospeech_to_text_async_speech_to_text_async_data_class.audiospeech_to_text_asyncSpeechToTextAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                ibm = openapi_client.models.audiospeech_to_text_async_speech_to_text_async_data_class.audiospeech_to_text_asyncSpeechToTextAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                oneai = openapi_client.models.audiospeech_to_text_async_speech_to_text_async_data_class.audiospeech_to_text_asyncSpeechToTextAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                revai = openapi_client.models.audiospeech_to_text_async_speech_to_text_async_data_class.audiospeech_to_text_asyncSpeechToTextAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                amazon = openapi_client.models.audiospeech_to_text_async_speech_to_text_async_data_class.audiospeech_to_text_asyncSpeechToTextAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                gladia = openapi_client.models.audiospeech_to_text_async_speech_to_text_async_data_class.audiospeech_to_text_asyncSpeechToTextAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                neuralspace = openapi_client.models.audiospeech_to_text_async_speech_to_text_async_data_class.audiospeech_to_text_asyncSpeechToTextAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                assembly = openapi_client.models.audiospeech_to_text_async_speech_to_text_async_data_class.audiospeech_to_text_asyncSpeechToTextAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                faker = openapi_client.models.audiospeech_to_text_async_speech_to_text_async_data_class.audiospeech_to_text_asyncSpeechToTextAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                speechmatics = openapi_client.models.audiospeech_to_text_async_speech_to_text_async_data_class.audiospeech_to_text_asyncSpeechToTextAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                symbl = openapi_client.models.audiospeech_to_text_async_speech_to_text_async_data_class.audiospeech_to_text_asyncSpeechToTextAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                openai = openapi_client.models.audiospeech_to_text_async_speech_to_text_async_data_class.audiospeech_to_text_asyncSpeechToTextAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                deepgram = openapi_client.models.audiospeech_to_text_async_speech_to_text_async_data_class.audiospeech_to_text_asyncSpeechToTextAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), )
            )
        else:
            return AudiospeechToTextAsyncModel(
        )
        """

    def testAudiospeechToTextAsyncModel(self):
        """Test AudiospeechToTextAsyncModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
