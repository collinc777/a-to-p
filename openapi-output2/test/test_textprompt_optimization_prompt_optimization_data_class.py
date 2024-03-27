# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.textprompt_optimization_prompt_optimization_data_class import (
    TextpromptOptimizationPromptOptimizationDataClass,
)


class TestTextpromptOptimizationPromptOptimizationDataClass(unittest.TestCase):
    """TextpromptOptimizationPromptOptimizationDataClass unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> TextpromptOptimizationPromptOptimizationDataClass:
        """Test TextpromptOptimizationPromptOptimizationDataClass
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TextpromptOptimizationPromptOptimizationDataClass`
        """
        model = TextpromptOptimizationPromptOptimizationDataClass()
        if include_optional:
            return TextpromptOptimizationPromptOptimizationDataClass(
                missing_information = '',
                items = [
                    openapi_client.models.prompt_data_class.PromptDataClass(
                        text = '', )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return TextpromptOptimizationPromptOptimizationDataClass(
                missing_information = '',
                status = 'success',
        )
        """

    def testTextpromptOptimizationPromptOptimizationDataClass(self):
        """Test TextpromptOptimizationPromptOptimizationDataClass"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()