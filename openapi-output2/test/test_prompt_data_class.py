# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.prompt_data_class import PromptDataClass


class TestPromptDataClass(unittest.TestCase):
    """PromptDataClass unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PromptDataClass:
        """Test PromptDataClass
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PromptDataClass`
        """
        model = PromptDataClass()
        if include_optional:
            return PromptDataClass(
                text = ''
            )
        else:
            return PromptDataClass(
                text = '',
        )
        """

    def testPromptDataClass(self):
        """Test PromptDataClass"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
