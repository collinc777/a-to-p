# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.video_object_bounding_box import VideoObjectBoundingBox


class TestVideoObjectBoundingBox(unittest.TestCase):
    """VideoObjectBoundingBox unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VideoObjectBoundingBox:
        """Test VideoObjectBoundingBox
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `VideoObjectBoundingBox`
        """
        model = VideoObjectBoundingBox()
        if include_optional:
            return VideoObjectBoundingBox(
                top = 56,
                left = 56,
                height = 56,
                width = 56
            )
        else:
            return VideoObjectBoundingBox(
                top = 56,
                left = 56,
                height = 56,
                width = 56,
        )
        """

    def testVideoObjectBoundingBox(self):
        """Test VideoObjectBoundingBox"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
