# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.face_features import FaceFeatures


class TestFaceFeatures(unittest.TestCase):
    """FaceFeatures unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FaceFeatures:
        """Test FaceFeatures
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `FaceFeatures`
        """
        model = FaceFeatures()
        if include_optional:
            return FaceFeatures(
                eyes_open = 56,
                smile = 56,
                mouth_open = 56
            )
        else:
            return FaceFeatures(
                eyes_open = 56,
                smile = 56,
                mouth_open = 56,
        )
        """

    def testFaceFeatures(self):
        """Test FaceFeatures"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
