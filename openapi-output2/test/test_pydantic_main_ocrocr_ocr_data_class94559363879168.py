# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_ocrocr_ocr_data_class94559363879168 import (
    PydanticMainOcrocrOcrDataClass94559363879168,
)


class TestPydanticMainOcrocrOcrDataClass94559363879168(unittest.TestCase):
    """PydanticMainOcrocrOcrDataClass94559363879168 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainOcrocrOcrDataClass94559363879168:
        """Test PydanticMainOcrocrOcrDataClass94559363879168
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainOcrocrOcrDataClass94559363879168`
        """
        model = PydanticMainOcrocrOcrDataClass94559363879168()
        if include_optional:
            return PydanticMainOcrocrOcrDataClass94559363879168(
                text = '',
                bounding_boxes = [
                    openapi_client.models.bounding_box.Bounding_box(
                        text = '', 
                        left = 56, 
                        top = 56, 
                        width = 56, 
                        height = 56, )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainOcrocrOcrDataClass94559363879168(
                text = '',
                status = 'success',
        )
        """

    def testPydanticMainOcrocrOcrDataClass94559363879168(self):
        """Test PydanticMainOcrocrOcrDataClass94559363879168"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
