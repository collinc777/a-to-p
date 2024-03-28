# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.async_ocr_request import AsyncOcrRequest

class TestAsyncOcrRequest(unittest.TestCase):
    """AsyncOcrRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AsyncOcrRequest:
        """Test AsyncOcrRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AsyncOcrRequest`
        """
        model = AsyncOcrRequest()
        if include_optional:
            return AsyncOcrRequest(
                providers = '0',
                fallback_providers = '',
                show_original_response = True,
                webhook_receiver = '0',
                users_webhook_parameters = {
                    'key' : null
                    },
                file = bytes(b'blah'),
                file_url = '',
                file_password = ''
            )
        else:
            return AsyncOcrRequest(
                providers = '0',
        )
        """

    def testAsyncOcrRequest(self):
        """Test AsyncOcrRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
