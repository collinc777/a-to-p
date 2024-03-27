# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.asyncaudiospeech_to_text_async_response_model import (
    AsyncaudiospeechToTextAsyncResponseModel,
)


class TestAsyncaudiospeechToTextAsyncResponseModel(unittest.TestCase):
    """AsyncaudiospeechToTextAsyncResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> AsyncaudiospeechToTextAsyncResponseModel:
        """Test AsyncaudiospeechToTextAsyncResponseModel
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AsyncaudiospeechToTextAsyncResponseModel`
        """
        model = AsyncaudiospeechToTextAsyncResponseModel()
        if include_optional:
            return AsyncaudiospeechToTextAsyncResponseModel(
                results = openapi_client.models.audiospeech_to_text_async_model.audiospeech_to_text_asyncModel(
                    voci = null, 
                    voxist = null, 
                    microsoft = null, 
                    google = null, 
                    ibm = null, 
                    oneai = null, 
                    revai = null, 
                    amazon = null, 
                    gladia = null, 
                    neuralspace = null, 
                    assembly = null, 
                    faker = null, 
                    speechmatics = null, 
                    symbl = null, 
                    openai = null, 
                    deepgram = null, ),
                error = '',
                public_id = '',
                status = ''
            )
        else:
            return AsyncaudiospeechToTextAsyncResponseModel(
                results = openapi_client.models.audiospeech_to_text_async_model.audiospeech_to_text_asyncModel(
                    voci = null, 
                    voxist = null, 
                    microsoft = null, 
                    google = null, 
                    ibm = null, 
                    oneai = null, 
                    revai = null, 
                    amazon = null, 
                    gladia = null, 
                    neuralspace = null, 
                    assembly = null, 
                    faker = null, 
                    speechmatics = null, 
                    symbl = null, 
                    openai = null, 
                    deepgram = null, ),
                error = '',
                public_id = '',
                status = '',
        )
        """

    def testAsyncaudiospeechToTextAsyncResponseModel(self):
        """Test AsyncaudiospeechToTextAsyncResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
