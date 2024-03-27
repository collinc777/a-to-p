# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.textcustom_classification_custom_classification_request import (
    TextcustomClassificationCustomClassificationRequest,
)


class TestTextcustomClassificationCustomClassificationRequest(unittest.TestCase):
    """TextcustomClassificationCustomClassificationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> TextcustomClassificationCustomClassificationRequest:
        """Test TextcustomClassificationCustomClassificationRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TextcustomClassificationCustomClassificationRequest`
        """
        model = TextcustomClassificationCustomClassificationRequest()
        if include_optional:
            return TextcustomClassificationCustomClassificationRequest(
                providers = '0',
                fallback_providers = '',
                response_as_dict = True,
                attributes_as_list = True,
                show_original_response = True,
                texts = [
                    '0'
                    ],
                labels = [
                    '0'
                    ],
                examples = [
                    [
                        '0'
                        ]
                    ]
            )
        else:
            return TextcustomClassificationCustomClassificationRequest(
                providers = '0',
                texts = [
                    '0'
                    ],
                labels = [
                    '0'
                    ],
                examples = [
                    [
                        '0'
                        ]
                    ],
        )
        """

    def testTextcustomClassificationCustomClassificationRequest(self):
        """Test TextcustomClassificationCustomClassificationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()