# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.batch_api import BatchApi


class TestBatchApi(unittest.TestCase):
    """BatchApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BatchApi()

    def tearDown(self) -> None:
        pass

    def test_batch_batch_list(self) -> None:
        """Test case for batch_batch_list

        List Batch Jobs
        """
        pass

    def test_feature_batch_create(self) -> None:
        """Test case for feature_batch_create

        Launch Batch Job
        """
        pass

    def test_feature_batch_destroy(self) -> None:
        """Test case for feature_batch_destroy

        Delete Batch Job
        """
        pass

    def test_feature_batch_retrieve(self) -> None:
        """Test case for feature_batch_retrieve

        Get Batch Job Result
        """
        pass


if __name__ == '__main__':
    unittest.main()
