# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.logo_track import LogoTrack

class TestLogoTrack(unittest.TestCase):
    """LogoTrack unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LogoTrack:
        """Test LogoTrack
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LogoTrack`
        """
        model = LogoTrack()
        if include_optional:
            return LogoTrack(
                description = '',
                tracking = [
                    openapi_client.models.video_logo.VideoLogo(
                        timestamp = 56, 
                        bounding_box = openapi_client.models.video_logo_bounding_box.VideoLogoBoundingBox(
                            top = 56, 
                            left = 56, 
                            height = 56, 
                            width = 56, ), 
                        confidence = 56, )
                    ]
            )
        else:
            return LogoTrack(
                description = '',
        )
        """

    def testLogoTrack(self):
        """Test LogoTrack"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
