# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.video_person_quality import VideoPersonQuality

class TestVideoPersonQuality(unittest.TestCase):
    """VideoPersonQuality unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VideoPersonQuality:
        """Test VideoPersonQuality
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VideoPersonQuality`
        """
        model = VideoPersonQuality()
        if include_optional:
            return VideoPersonQuality(
                brightness = 56,
                sharpness = 56
            )
        else:
            return VideoPersonQuality(
                brightness = 56,
                sharpness = 56,
        )
        """

    def testVideoPersonQuality(self):
        """Test VideoPersonQuality"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()