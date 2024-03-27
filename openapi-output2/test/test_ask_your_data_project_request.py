# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.ask_your_data_project_request import (
    AskYourDataProjectRequest,
)


class TestAskYourDataProjectRequest(unittest.TestCase):
    """AskYourDataProjectRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AskYourDataProjectRequest:
        """Test AskYourDataProjectRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AskYourDataProjectRequest`
        """
        model = AskYourDataProjectRequest()
        if include_optional:
            return AskYourDataProjectRequest(
                credential = '',
                asset = '',
                ocr_provider = '0',
                speech_to_text_provider = '0',
                llm_provider = '0',
                llm_model = '0',
                chunk_size = 1,
                chunk_separators = [
                    ''
                    ],
                project_name = '0',
                collection_name = '0',
                db_provider = 'qdrant',
                embeddings_provider = 'cohere'
            )
        else:
            return AskYourDataProjectRequest(
                ocr_provider = '0',
                speech_to_text_provider = '0',
                project_name = '0',
                collection_name = '0',
        )
        """

    def testAskYourDataProjectRequest(self):
        """Test AskYourDataProjectRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
