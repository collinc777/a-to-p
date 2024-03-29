# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.universal_translator_createt_request import (
    UniversalTranslatorCreatetRequest,
)


class TestUniversalTranslatorCreatetRequest(unittest.TestCase):
    """UniversalTranslatorCreatetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UniversalTranslatorCreatetRequest:
        """Test UniversalTranslatorCreatetRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `UniversalTranslatorCreatetRequest`
        """
        model = UniversalTranslatorCreatetRequest()
        if include_optional:
            return UniversalTranslatorCreatetRequest(
                source_language = '0',
                target_language = '0',
                project_name = '0',
                fall_back_providers = [
                    '0'
                    ],
                provider = '0'
            )
        else:
            return UniversalTranslatorCreatetRequest(
                project_name = '0',
                provider = '0',
        )
        """

    def testUniversalTranslatorCreatetRequest(self):
        """Test UniversalTranslatorCreatetRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
