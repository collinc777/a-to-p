# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pydantic_main_audiotext_to_speech_text_to_speech_data_class94559359104176 import PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359104176

class TestPydanticMainAudiotextToSpeechTextToSpeechDataClass94559359104176(unittest.TestCase):
    """PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359104176 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359104176:
        """Test PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359104176
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359104176`
        """
        model = PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359104176()
        if include_optional:
            return PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359104176(
                audio = '',
                voice_type = 56,
                audio_resource_url = '',
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359104176(
                audio = '',
                voice_type = 56,
                audio_resource_url = '',
                status = 'success',
        )
        """

    def testPydanticMainAudiotextToSpeechTextToSpeechDataClass94559359104176(self):
        """Test PydanticMainAudiotextToSpeechTextToSpeechDataClass94559359104176"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
