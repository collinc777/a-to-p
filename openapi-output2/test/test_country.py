# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.country import Country


class TestCountry(unittest.TestCase):
    """Country unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Country:
        """Test Country
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Country`
        """
        model = Country()
        if include_optional:
            return Country(
                name = '',
                alpha2 = '',
                alpha3 = '',
                confidence = 56
            )
        else:
            return Country(
                name = '',
                alpha2 = '',
                alpha3 = '',
        )
        """

    def testCountry(self):
        """Test Country"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
