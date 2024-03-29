# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.person_attributes import PersonAttributes

class TestPersonAttributes(unittest.TestCase):
    """PersonAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonAttributes:
        """Test PersonAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonAttributes`
        """
        model = PersonAttributes()
        if include_optional:
            return PersonAttributes(
                upper_cloths = [
                    openapi_client.models.upper_cloth.UpperCloth(
                        value = '', 
                        confidence = 56, )
                    ],
                lower_cloths = [
                    openapi_client.models.lower_cloth.LowerCloth(
                        value = '', 
                        confidence = 56, )
                    ]
            )
        else:
            return PersonAttributes(
        )
        """

    def testPersonAttributes(self):
        """Test PersonAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
