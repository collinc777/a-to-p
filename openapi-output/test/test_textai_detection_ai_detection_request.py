# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.textai_detection_ai_detection_request import TextaiDetectionAiDetectionRequest

class TestTextaiDetectionAiDetectionRequest(unittest.TestCase):
    """TextaiDetectionAiDetectionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextaiDetectionAiDetectionRequest:
        """Test TextaiDetectionAiDetectionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TextaiDetectionAiDetectionRequest`
        """
        model = TextaiDetectionAiDetectionRequest()
        if include_optional:
            return TextaiDetectionAiDetectionRequest(
                providers = '0',
                fallback_providers = '',
                response_as_dict = True,
                attributes_as_list = True,
                show_original_response = True,
                text = '0',
                language = '',
                provider_params = ''
            )
        else:
            return TextaiDetectionAiDetectionRequest(
                providers = '0',
                text = '0',
        )
        """

    def testTextaiDetectionAiDetectionRequest(self):
        """Test TextaiDetectionAiDetectionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
