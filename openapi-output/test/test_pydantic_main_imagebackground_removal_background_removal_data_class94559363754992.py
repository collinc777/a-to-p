# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pydantic_main_imagebackground_removal_background_removal_data_class94559363754992 import PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363754992

class TestPydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363754992(unittest.TestCase):
    """PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363754992 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363754992:
        """Test PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363754992
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363754992`
        """
        model = PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363754992()
        if include_optional:
            return PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363754992(
                image_b64 = '',
                image_resource_url = '',
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363754992(
                image_b64 = '',
                image_resource_url = '',
                status = 'success',
        )
        """

    def testPydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363754992(self):
        """Test PydanticMainImagebackgroundRemovalBackgroundRemovalDataClass94559363754992"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()