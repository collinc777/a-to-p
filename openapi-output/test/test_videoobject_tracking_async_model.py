# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.videoobject_tracking_async_model import VideoobjectTrackingAsyncModel

class TestVideoobjectTrackingAsyncModel(unittest.TestCase):
    """VideoobjectTrackingAsyncModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VideoobjectTrackingAsyncModel:
        """Test VideoobjectTrackingAsyncModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VideoobjectTrackingAsyncModel`
        """
        model = VideoobjectTrackingAsyncModel()
        if include_optional:
            return VideoobjectTrackingAsyncModel(
                google = openapi_client.models.videoobject_tracking_async_object_tracking_async_data_class.videoobject_tracking_asyncObjectTrackingAsyncDataClass(
                    objects = [
                        openapi_client.models.object_track.ObjectTrack(
                            description = '', 
                            confidence = 56, 
                            frames = [
                                openapi_client.models.object_frame.ObjectFrame(
                                    timestamp = 56, 
                                    bounding_box = openapi_client.models.video_object_bounding_box.VideoObjectBoundingBox(
                                        top = 56, 
                                        left = 56, 
                                        height = 56, 
                                        width = 56, ), )
                                ], )
                        ], 
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), )
            )
        else:
            return VideoobjectTrackingAsyncModel(
        )
        """

    def testVideoobjectTrackingAsyncModel(self):
        """Test VideoobjectTrackingAsyncModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
