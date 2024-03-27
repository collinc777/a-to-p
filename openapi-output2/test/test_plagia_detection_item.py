# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.plagia_detection_item import PlagiaDetectionItem


class TestPlagiaDetectionItem(unittest.TestCase):
    """PlagiaDetectionItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlagiaDetectionItem:
        """Test PlagiaDetectionItem
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PlagiaDetectionItem`
        """
        model = PlagiaDetectionItem()
        if include_optional:
            return PlagiaDetectionItem(
                text = '',
                candidates = [
                    openapi_client.models.plagia_detection_candidate.PlagiaDetectionCandidate(
                        url = '', 
                        plagia_score = 56, 
                        prediction = '', 
                        plagiarized_text = '', )
                    ]
            )
        else:
            return PlagiaDetectionItem(
                text = '',
        )
        """

    def testPlagiaDetectionItem(self):
        """Test PlagiaDetectionItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()