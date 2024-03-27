# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_textai_detection_ai_detection_data_class94559369241568 import (
    PydanticMainTextaiDetectionAiDetectionDataClass94559369241568,
)


class TestPydanticMainTextaiDetectionAiDetectionDataClass94559369241568(
    unittest.TestCase
):
    """PydanticMainTextaiDetectionAiDetectionDataClass94559369241568 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainTextaiDetectionAiDetectionDataClass94559369241568:
        """Test PydanticMainTextaiDetectionAiDetectionDataClass94559369241568
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainTextaiDetectionAiDetectionDataClass94559369241568`
        """
        model = PydanticMainTextaiDetectionAiDetectionDataClass94559369241568()
        if include_optional:
            return PydanticMainTextaiDetectionAiDetectionDataClass94559369241568(
                ai_score = 56,
                items = [
                    openapi_client.models.ai_detection_item.AiDetectionItem(
                        text = '', 
                        prediction = '', 
                        ai_score = 56, 
                        ai_score_detail = 56, )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainTextaiDetectionAiDetectionDataClass94559369241568(
                ai_score = 56,
                status = 'success',
        )
        """

    def testPydanticMainTextaiDetectionAiDetectionDataClass94559369241568(self):
        """Test PydanticMainTextaiDetectionAiDetectionDataClass94559369241568"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
