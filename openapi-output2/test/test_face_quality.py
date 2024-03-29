# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.face_quality import FaceQuality


class TestFaceQuality(unittest.TestCase):
    """FaceQuality unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FaceQuality:
        """Test FaceQuality
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `FaceQuality`
        """
        model = FaceQuality()
        if include_optional:
            return FaceQuality(
                noise = 56,
                exposure = 56,
                blur = 56,
                brightness = 56,
                sharpness = 56
            )
        else:
            return FaceQuality(
                noise = 56,
                exposure = 56,
                blur = 56,
                brightness = 56,
                sharpness = 56,
        )
        """

    def testFaceQuality(self):
        """Test FaceQuality"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
