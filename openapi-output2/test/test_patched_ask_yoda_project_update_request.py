# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.patched_ask_yoda_project_update_request import (
    PatchedAskYodaProjectUpdateRequest,
)


class TestPatchedAskYodaProjectUpdateRequest(unittest.TestCase):
    """PatchedAskYodaProjectUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedAskYodaProjectUpdateRequest:
        """Test PatchedAskYodaProjectUpdateRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PatchedAskYodaProjectUpdateRequest`
        """
        model = PatchedAskYodaProjectUpdateRequest()
        if include_optional:
            return PatchedAskYodaProjectUpdateRequest(
                ocr_provider = '0',
                speech_to_text_provider = '0',
                llm_provider = '0',
                llm_model = '0',
                chunk_size = 1,
                chunk_separators = [
                    ''
                    ]
            )
        else:
            return PatchedAskYodaProjectUpdateRequest(
        )
        """

    def testPatchedAskYodaProjectUpdateRequest(self):
        """Test PatchedAskYodaProjectUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
