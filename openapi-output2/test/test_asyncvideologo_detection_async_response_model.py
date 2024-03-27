# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.asyncvideologo_detection_async_response_model import (
    AsyncvideologoDetectionAsyncResponseModel,
)


class TestAsyncvideologoDetectionAsyncResponseModel(unittest.TestCase):
    """AsyncvideologoDetectionAsyncResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> AsyncvideologoDetectionAsyncResponseModel:
        """Test AsyncvideologoDetectionAsyncResponseModel
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AsyncvideologoDetectionAsyncResponseModel`
        """
        model = AsyncvideologoDetectionAsyncResponseModel()
        if include_optional:
            return AsyncvideologoDetectionAsyncResponseModel(
                results = openapi_client.models.videologo_detection_async_model.videologo_detection_asyncModel(
                    twelvelabs = null, 
                    google = null, ),
                error = '',
                public_id = '',
                status = ''
            )
        else:
            return AsyncvideologoDetectionAsyncResponseModel(
                results = openapi_client.models.videologo_detection_async_model.videologo_detection_asyncModel(
                    twelvelabs = null, 
                    google = null, ),
                error = '',
                public_id = '',
                status = '',
        )
        """

    def testAsyncvideologoDetectionAsyncResponseModel(self):
        """Test AsyncvideologoDetectionAsyncResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
