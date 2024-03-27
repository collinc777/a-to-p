# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.api.search_api import SearchApi


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SearchApi()

    def tearDown(self) -> None:
        pass

    def test_image_image_search_delete_image_create(self) -> None:
        """Test case for image_image_search_delete_image_create

        Search - Delete phase
        """
        pass

    def test_image_image_search_get_image_retrieve(self) -> None:
        """Test case for image_image_search_get_image_retrieve

        Search - get image
        """
        pass

    def test_image_image_search_get_images_retrieve(self) -> None:
        """Test case for image_image_search_get_images_retrieve

        Search - list all images
        """
        pass

    def test_image_image_search_launch_similarity_create(self) -> None:
        """Test case for image_image_search_launch_similarity_create

        Search - launch similarity
        """
        pass

    def test_image_image_search_upload_image_create(self) -> None:
        """Test case for image_image_search_upload_image_create

        Search - Upload Phase
        """
        pass

    def test_text_text_search_create(self) -> None:
        """Test case for text_text_search_create

        Search
        """
        pass


if __name__ == "__main__":
    unittest.main()
