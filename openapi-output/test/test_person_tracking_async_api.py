# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.person_tracking_async_api import PersonTrackingAsyncApi


class TestPersonTrackingAsyncApi(unittest.TestCase):
    """PersonTrackingAsyncApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PersonTrackingAsyncApi()

    def tearDown(self) -> None:
        pass

    def test_video_video_person_tracking_async_create(self) -> None:
        """Test case for video_video_person_tracking_async_create

        Person Tracking Launch Job
        """
        pass

    def test_video_video_person_tracking_async_destroy(self) -> None:
        """Test case for video_video_person_tracking_async_destroy

        Person Tracking delete Jobs
        """
        pass

    def test_video_video_person_tracking_async_retrieve(self) -> None:
        """Test case for video_video_person_tracking_async_retrieve

        Person Tracking List Jobs
        """
        pass

    def test_video_video_person_tracking_async_retrieve2(self) -> None:
        """Test case for video_video_person_tracking_async_retrieve2

        Person Tracking Get Job Results
        """
        pass


if __name__ == '__main__':
    unittest.main()
