# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_imagesearch_search_delete_image_data_class94559363521168 import (
    PydanticMainImagesearchSearchDeleteImageDataClass94559363521168,
)


class TestPydanticMainImagesearchSearchDeleteImageDataClass94559363521168(
    unittest.TestCase
):
    """PydanticMainImagesearchSearchDeleteImageDataClass94559363521168 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainImagesearchSearchDeleteImageDataClass94559363521168:
        """Test PydanticMainImagesearchSearchDeleteImageDataClass94559363521168
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainImagesearchSearchDeleteImageDataClass94559363521168`
        """
        model = PydanticMainImagesearchSearchDeleteImageDataClass94559363521168()
        if include_optional:
            return PydanticMainImagesearchSearchDeleteImageDataClass94559363521168(
                status = 'success',
                original_response = None
            )
        else:
            return PydanticMainImagesearchSearchDeleteImageDataClass94559363521168(
                status = 'success',
        )
        """

    def testPydanticMainImagesearchSearchDeleteImageDataClass94559363521168(self):
        """Test PydanticMainImagesearchSearchDeleteImageDataClass94559363521168"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()