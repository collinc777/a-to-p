# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.add_file_request import AddFileRequest


class TestAddFileRequest(unittest.TestCase):
    """AddFileRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddFileRequest:
        """Test AddFileRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AddFileRequest`
        """
        model = AddFileRequest()
        if include_optional:
            return AddFileRequest(
                data_type = 'pdf',
                file = bytes(b'blah'),
                file_url = '',
                metadata = '0',
                provider = '0'
            )
        else:
            return AddFileRequest(
                data_type = 'pdf',
        )
        """

    def testAddFileRequest(self):
        """Test AddFileRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()