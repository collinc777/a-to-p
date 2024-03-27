# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_ocrdata_extraction_data_extraction_data_class94559367902896 import (
    PydanticMainOcrdataExtractionDataExtractionDataClass94559367902896,
)


class TestPydanticMainOcrdataExtractionDataExtractionDataClass94559367902896(
    unittest.TestCase
):
    """PydanticMainOcrdataExtractionDataExtractionDataClass94559367902896 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainOcrdataExtractionDataExtractionDataClass94559367902896:
        """Test PydanticMainOcrdataExtractionDataExtractionDataClass94559367902896
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainOcrdataExtractionDataExtractionDataClass94559367902896`
        """
        model = PydanticMainOcrdataExtractionDataExtractionDataClass94559367902896()
        if include_optional:
            return PydanticMainOcrdataExtractionDataExtractionDataClass94559367902896(
                fields = [
                    openapi_client.models.item_data_extraction.ItemDataExtraction(
                        key = '', 
                        value = null, 
                        bounding_box = openapi_client.models.bounding_box.BoundingBox(
                            left = 56, 
                            top = 56, 
                            width = 56, 
                            height = 56, ), 
                        confidence_score = 0, )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainOcrdataExtractionDataExtractionDataClass94559367902896(
                status = 'success',
        )
        """

    def testPydanticMainOcrdataExtractionDataExtractionDataClass94559367902896(self):
        """Test PydanticMainOcrdataExtractionDataExtractionDataClass94559367902896"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()