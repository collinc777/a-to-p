# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.asyncvideoperson_tracking_async_response_model import (
    AsyncvideopersonTrackingAsyncResponseModel,
)


class TestAsyncvideopersonTrackingAsyncResponseModel(unittest.TestCase):
    """AsyncvideopersonTrackingAsyncResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> AsyncvideopersonTrackingAsyncResponseModel:
        """Test AsyncvideopersonTrackingAsyncResponseModel
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AsyncvideopersonTrackingAsyncResponseModel`
        """
        model = AsyncvideopersonTrackingAsyncResponseModel()
        if include_optional:
            return AsyncvideopersonTrackingAsyncResponseModel(
                results = openapi_client.models.videoperson_tracking_async_model.videoperson_tracking_asyncModel(
                    amazon = null, 
                    google = null, ),
                error = '',
                public_id = '',
                status = ''
            )
        else:
            return AsyncvideopersonTrackingAsyncResponseModel(
                results = openapi_client.models.videoperson_tracking_async_model.videoperson_tracking_asyncModel(
                    amazon = null, 
                    google = null, ),
                error = '',
                public_id = '',
                status = '',
        )
        """

    def testAsyncvideopersonTrackingAsyncResponseModel(self):
        """Test AsyncvideopersonTrackingAsyncResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
