# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.videoexplicit_content_detection_async_model import (
    VideoexplicitContentDetectionAsyncModel,
)


class TestVideoexplicitContentDetectionAsyncModel(unittest.TestCase):
    """VideoexplicitContentDetectionAsyncModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> VideoexplicitContentDetectionAsyncModel:
        """Test VideoexplicitContentDetectionAsyncModel
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `VideoexplicitContentDetectionAsyncModel`
        """
        model = VideoexplicitContentDetectionAsyncModel()
        if include_optional:
            return VideoexplicitContentDetectionAsyncModel(
                amazon = openapi_client.models.videoexplicit_content_detection_async_explicit_content_detection_async_data_class.videoexplicit_content_detection_asyncExplicitContentDetectionAsyncDataClass(
                    moderation = [
                        openapi_client.models.content_nsfw.ContentNSFW(
                            timestamp = 56, 
                            confidence = 56, 
                            category = '', )
                        ], 
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                google = openapi_client.models.videoexplicit_content_detection_async_explicit_content_detection_async_data_class.videoexplicit_content_detection_asyncExplicitContentDetectionAsyncDataClass(
                    moderation = [
                        openapi_client.models.content_nsfw.ContentNSFW(
                            timestamp = 56, 
                            confidence = 56, 
                            category = '', )
                        ], 
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), )
            )
        else:
            return VideoexplicitContentDetectionAsyncModel(
        )
        """

    def testVideoexplicitContentDetectionAsyncModel(self):
        """Test VideoexplicitContentDetectionAsyncModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
