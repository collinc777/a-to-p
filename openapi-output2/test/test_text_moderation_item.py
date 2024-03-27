# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.text_moderation_item import TextModerationItem


class TestTextModerationItem(unittest.TestCase):
    """TextModerationItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextModerationItem:
        """Test TextModerationItem
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TextModerationItem`
        """
        model = TextModerationItem()
        if include_optional:
            return TextModerationItem(
                label = '',
                likelihood = 56,
                category = 'Toxic',
                subcategory = None,
                likelihood_score = 56
            )
        else:
            return TextModerationItem(
                label = '',
                likelihood = 56,
                category = 'Toxic',
                subcategory = None,
                likelihood_score = 56,
        )
        """

    def testTextModerationItem(self):
        """Test TextModerationItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()