# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.video_text_bounding_box import VideoTextBoundingBox

class TestVideoTextBoundingBox(unittest.TestCase):
    """VideoTextBoundingBox unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VideoTextBoundingBox:
        """Test VideoTextBoundingBox
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VideoTextBoundingBox`
        """
        model = VideoTextBoundingBox()
        if include_optional:
            return VideoTextBoundingBox(
                top = 56,
                left = 56,
                height = 56,
                width = 56
            )
        else:
            return VideoTextBoundingBox(
                top = 56,
                left = 56,
                height = 56,
                width = 56,
        )
        """

    def testVideoTextBoundingBox(self):
        """Test VideoTextBoundingBox"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
