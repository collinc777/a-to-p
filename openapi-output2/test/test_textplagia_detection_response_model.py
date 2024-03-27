# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.textplagia_detection_response_model import (
    TextplagiaDetectionResponseModel,
)


class TestTextplagiaDetectionResponseModel(unittest.TestCase):
    """TextplagiaDetectionResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextplagiaDetectionResponseModel:
        """Test TextplagiaDetectionResponseModel
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TextplagiaDetectionResponseModel`
        """
        model = TextplagiaDetectionResponseModel()
        if include_optional:
            return TextplagiaDetectionResponseModel(
                originalityai = openapi_client.models.textplagia_detection_plagia_detection_data_class.textplagia_detectionPlagiaDetectionDataClass(
                    plagia_score = 56, 
                    items = [
                        openapi_client.models.plagia_detection_item.PlagiaDetectionItem(
                            text = '', 
                            candidates = [
                                openapi_client.models.plagia_detection_candidate.PlagiaDetectionCandidate(
                                    url = '', 
                                    plagia_score = 56, 
                                    prediction = '', 
                                    plagiarized_text = '', )
                                ], )
                        ], 
                    original_response = null, 
                    status = null, ),
                winstonai = openapi_client.models.textplagia_detection_plagia_detection_data_class.textplagia_detectionPlagiaDetectionDataClass(
                    plagia_score = 56, 
                    items = [
                        openapi_client.models.plagia_detection_item.PlagiaDetectionItem(
                            text = '', 
                            candidates = [
                                openapi_client.models.plagia_detection_candidate.PlagiaDetectionCandidate(
                                    url = '', 
                                    plagia_score = 56, 
                                    prediction = '', 
                                    plagiarized_text = '', )
                                ], )
                        ], 
                    original_response = null, 
                    status = null, )
            )
        else:
            return TextplagiaDetectionResponseModel(
        )
        """

    def testTextplagiaDetectionResponseModel(self):
        """Test TextplagiaDetectionResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
