# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.anonymization_async_api import AnonymizationAsyncApi


class TestAnonymizationAsyncApi(unittest.TestCase):
    """AnonymizationAsyncApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AnonymizationAsyncApi()

    def tearDown(self) -> None:
        pass

    def test_ocr_ocr_anonymization_async_create(self) -> None:
        """Test case for ocr_ocr_anonymization_async_create

        Anonymization Launch Job
        """
        pass

    def test_ocr_ocr_anonymization_async_destroy(self) -> None:
        """Test case for ocr_ocr_anonymization_async_destroy

        Anonymization delete Jobs
        """
        pass

    def test_ocr_ocr_anonymization_async_retrieve(self) -> None:
        """Test case for ocr_ocr_anonymization_async_retrieve

        Anonymization List Job
        """
        pass

    def test_ocr_ocr_anonymization_async_retrieve2(self) -> None:
        """Test case for ocr_ocr_anonymization_async_retrieve2

        Anonymization Get Job Results
        """
        pass


if __name__ == '__main__':
    unittest.main()
