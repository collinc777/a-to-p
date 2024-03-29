# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.yoda_query_response_item import YodaQueryResponseItem


class TestYodaQueryResponseItem(unittest.TestCase):
    """YodaQueryResponseItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> YodaQueryResponseItem:
        """Test YodaQueryResponseItem
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `YodaQueryResponseItem`
        """
        model = YodaQueryResponseItem()
        if include_optional:
            return YodaQueryResponseItem(
                id = '',
                version = 56,
                score = 56,
                payload = openapi_client.models.yoda_query_response_payload.YodaQueryResponsePayload(
                    metadata = openapi_client.models.metadata.Metadata(), 
                    page_content = '', ),
                vector = None
            )
        else:
            return YodaQueryResponseItem(
                id = '',
                version = 56,
                score = 56,
                payload = openapi_client.models.yoda_query_response_payload.YodaQueryResponsePayload(
                    metadata = openapi_client.models.metadata.Metadata(), 
                    page_content = '', ),
                vector = None,
        )
        """

    def testYodaQueryResponseItem(self):
        """Test YodaQueryResponseItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
