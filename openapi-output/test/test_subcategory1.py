# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.subcategory1 import Subcategory1

class TestSubcategory1(unittest.TestCase):
    """Subcategory1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Subcategory1:
        """Test Subcategory1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Subcategory1`
        """
        model = Subcategory1()
        if include_optional:
            return Subcategory1(
            )
        else:
            return Subcategory1(
        )
        """

    def testSubcategory1(self):
        """Test Subcategory1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()