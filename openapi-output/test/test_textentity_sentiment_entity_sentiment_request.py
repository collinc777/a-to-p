# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.textentity_sentiment_entity_sentiment_request import TextentitySentimentEntitySentimentRequest

class TestTextentitySentimentEntitySentimentRequest(unittest.TestCase):
    """TextentitySentimentEntitySentimentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextentitySentimentEntitySentimentRequest:
        """Test TextentitySentimentEntitySentimentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TextentitySentimentEntitySentimentRequest`
        """
        model = TextentitySentimentEntitySentimentRequest()
        if include_optional:
            return TextentitySentimentEntitySentimentRequest(
                providers = '0',
                fallback_providers = '',
                response_as_dict = True,
                attributes_as_list = True,
                show_original_response = True,
                text = '0',
                language = ''
            )
        else:
            return TextentitySentimentEntitySentimentRequest(
                providers = '0',
                text = '0',
        )
        """

    def testTextentitySentimentEntitySentimentRequest(self):
        """Test TextentitySentimentEntitySentimentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
