# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.nested_bad_request import NestedBadRequest


class TestNestedBadRequest(unittest.TestCase):
    """NestedBadRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NestedBadRequest:
        """Test NestedBadRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `NestedBadRequest`
        """
        model = NestedBadRequest()
        if include_optional:
            return NestedBadRequest(
                type = '',
                message = openapi_client.models.field_error.FieldError(
                    <parameter_name> = [
                        ''
                        ], )
            )
        else:
            return NestedBadRequest(
                type = '',
                message = openapi_client.models.field_error.FieldError(
                    <parameter_name> = [
                        ''
                        ], ),
        )
        """

    def testNestedBadRequest(self):
        """Test NestedBadRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
