# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.api.logo_detection_async_api import LogoDetectionAsyncApi


class TestLogoDetectionAsyncApi(unittest.TestCase):
    """LogoDetectionAsyncApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LogoDetectionAsyncApi()

    def tearDown(self) -> None:
        pass

    def test_video_video_logo_detection_async_create(self) -> None:
        """Test case for video_video_logo_detection_async_create

        Video Logo Detection Launch Job
        """
        pass

    def test_video_video_logo_detection_async_destroy(self) -> None:
        """Test case for video_video_logo_detection_async_destroy

        Video Logo Detection delete Jobs
        """
        pass

    def test_video_video_logo_detection_async_retrieve(self) -> None:
        """Test case for video_video_logo_detection_async_retrieve

        Video Logo Detection List Jobs
        """
        pass

    def test_video_video_logo_detection_async_retrieve2(self) -> None:
        """Test case for video_video_logo_detection_async_retrieve2

        Video Logo Detection Get Job Results
        """
        pass


if __name__ == "__main__":
    unittest.main()
