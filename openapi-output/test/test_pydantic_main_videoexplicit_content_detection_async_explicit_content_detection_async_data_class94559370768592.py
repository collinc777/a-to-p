# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pydantic_main_videoexplicit_content_detection_async_explicit_content_detection_async_data_class94559370768592 import PydanticMainVideoexplicitContentDetectionAsyncExplicitContentDetectionAsyncDataClass94559370768592

class TestPydanticMainVideoexplicitContentDetectionAsyncExplicitContentDetectionAsyncDataClass94559370768592(unittest.TestCase):
    """PydanticMainVideoexplicitContentDetectionAsyncExplicitContentDetectionAsyncDataClass94559370768592 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PydanticMainVideoexplicitContentDetectionAsyncExplicitContentDetectionAsyncDataClass94559370768592:
        """Test PydanticMainVideoexplicitContentDetectionAsyncExplicitContentDetectionAsyncDataClass94559370768592
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PydanticMainVideoexplicitContentDetectionAsyncExplicitContentDetectionAsyncDataClass94559370768592`
        """
        model = PydanticMainVideoexplicitContentDetectionAsyncExplicitContentDetectionAsyncDataClass94559370768592()
        if include_optional:
            return PydanticMainVideoexplicitContentDetectionAsyncExplicitContentDetectionAsyncDataClass94559370768592(
                moderation = [
                    openapi_client.models.content_nsfw.ContentNSFW(
                        timestamp = 56, 
                        confidence = 56, 
                        category = '', )
                    ],
                original_response = None,
                id = '',
                final_status = 'success',
                error = openapi_client.models.error.Error()
            )
        else:
            return PydanticMainVideoexplicitContentDetectionAsyncExplicitContentDetectionAsyncDataClass94559370768592(
                id = '',
                final_status = 'success',
        )
        """

    def testPydanticMainVideoexplicitContentDetectionAsyncExplicitContentDetectionAsyncDataClass94559370768592(self):
        """Test PydanticMainVideoexplicitContentDetectionAsyncExplicitContentDetectionAsyncDataClass94559370768592"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
