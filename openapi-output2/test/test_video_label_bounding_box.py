# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.video_label_bounding_box import VideoLabelBoundingBox


class TestVideoLabelBoundingBox(unittest.TestCase):
    """VideoLabelBoundingBox unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VideoLabelBoundingBox:
        """Test VideoLabelBoundingBox
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `VideoLabelBoundingBox`
        """
        model = VideoLabelBoundingBox()
        if include_optional:
            return VideoLabelBoundingBox(
                top = 56,
                left = 56,
                height = 56,
                width = 56
            )
        else:
            return VideoLabelBoundingBox(
                top = 56,
                left = 56,
                height = 56,
                width = 56,
        )
        """

    def testVideoLabelBoundingBox(self):
        """Test VideoLabelBoundingBox"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
