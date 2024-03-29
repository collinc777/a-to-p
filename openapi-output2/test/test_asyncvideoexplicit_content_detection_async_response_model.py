# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.asyncvideoexplicit_content_detection_async_response_model import (
    AsyncvideoexplicitContentDetectionAsyncResponseModel,
)


class TestAsyncvideoexplicitContentDetectionAsyncResponseModel(unittest.TestCase):
    """AsyncvideoexplicitContentDetectionAsyncResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> AsyncvideoexplicitContentDetectionAsyncResponseModel:
        """Test AsyncvideoexplicitContentDetectionAsyncResponseModel
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AsyncvideoexplicitContentDetectionAsyncResponseModel`
        """
        model = AsyncvideoexplicitContentDetectionAsyncResponseModel()
        if include_optional:
            return AsyncvideoexplicitContentDetectionAsyncResponseModel(
                results = openapi_client.models.videoexplicit_content_detection_async_model.videoexplicit_content_detection_asyncModel(
                    amazon = null, 
                    google = null, ),
                error = '',
                public_id = '',
                status = ''
            )
        else:
            return AsyncvideoexplicitContentDetectionAsyncResponseModel(
                results = openapi_client.models.videoexplicit_content_detection_async_model.videoexplicit_content_detection_asyncModel(
                    amazon = null, 
                    google = null, ),
                error = '',
                public_id = '',
                status = '',
        )
        """

    def testAsyncvideoexplicitContentDetectionAsyncResponseModel(self):
        """Test AsyncvideoexplicitContentDetectionAsyncResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
