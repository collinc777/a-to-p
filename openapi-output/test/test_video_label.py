# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.video_label import VideoLabel

class TestVideoLabel(unittest.TestCase):
    """VideoLabel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VideoLabel:
        """Test VideoLabel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VideoLabel`
        """
        model = VideoLabel()
        if include_optional:
            return VideoLabel(
                name = '',
                confidence = 56,
                timestamp = [
                    openapi_client.models.video_label_time_stamp.VideoLabelTimeStamp(
                        start = 56, 
                        end = 56, )
                    ],
                category = [
                    ''
                    ],
                bounding_box = [
                    openapi_client.models.video_label_bounding_box.VideoLabelBoundingBox(
                        top = 56, 
                        left = 56, 
                        height = 56, 
                        width = 56, )
                    ]
            )
        else:
            return VideoLabel(
                name = '',
                confidence = 56,
        )
        """

    def testVideoLabel(self):
        """Test VideoLabel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
