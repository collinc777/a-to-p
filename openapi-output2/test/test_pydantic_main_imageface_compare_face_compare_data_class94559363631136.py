# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_imageface_compare_face_compare_data_class94559363631136 import (
    PydanticMainImagefaceCompareFaceCompareDataClass94559363631136,
)


class TestPydanticMainImagefaceCompareFaceCompareDataClass94559363631136(
    unittest.TestCase
):
    """PydanticMainImagefaceCompareFaceCompareDataClass94559363631136 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainImagefaceCompareFaceCompareDataClass94559363631136:
        """Test PydanticMainImagefaceCompareFaceCompareDataClass94559363631136
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainImagefaceCompareFaceCompareDataClass94559363631136`
        """
        model = PydanticMainImagefaceCompareFaceCompareDataClass94559363631136()
        if include_optional:
            return PydanticMainImagefaceCompareFaceCompareDataClass94559363631136(
                items = [
                    openapi_client.models.face_match.FaceMatch(
                        confidence = 56, 
                        bounding_box = openapi_client.models.face_compare_bounding_box.FaceCompareBoundingBox(
                            top = 56, 
                            left = 56, 
                            height = 56, 
                            width = 56, ), )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainImagefaceCompareFaceCompareDataClass94559363631136(
                status = 'success',
        )
        """

    def testPydanticMainImagefaceCompareFaceCompareDataClass94559363631136(self):
        """Test PydanticMainImagefaceCompareFaceCompareDataClass94559363631136"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
