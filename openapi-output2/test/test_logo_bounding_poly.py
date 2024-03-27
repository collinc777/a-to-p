# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.logo_bounding_poly import LogoBoundingPoly


class TestLogoBoundingPoly(unittest.TestCase):
    """LogoBoundingPoly unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LogoBoundingPoly:
        """Test LogoBoundingPoly
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `LogoBoundingPoly`
        """
        model = LogoBoundingPoly()
        if include_optional:
            return LogoBoundingPoly(
                vertices = [
                    openapi_client.models.logo_vertice.LogoVertice(
                        x = 56, 
                        y = 56, )
                    ]
            )
        else:
            return LogoBoundingPoly(
                vertices = [
                    openapi_client.models.logo_vertice.LogoVertice(
                        x = 56, 
                        y = 56, )
                    ],
        )
        """

    def testLogoBoundingPoly(self):
        """Test LogoBoundingPoly"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
