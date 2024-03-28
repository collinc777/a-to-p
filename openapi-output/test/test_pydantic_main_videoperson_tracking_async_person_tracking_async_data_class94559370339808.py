# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pydantic_main_videoperson_tracking_async_person_tracking_async_data_class94559370339808 import PydanticMainVideopersonTrackingAsyncPersonTrackingAsyncDataClass94559370339808

class TestPydanticMainVideopersonTrackingAsyncPersonTrackingAsyncDataClass94559370339808(unittest.TestCase):
    """PydanticMainVideopersonTrackingAsyncPersonTrackingAsyncDataClass94559370339808 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PydanticMainVideopersonTrackingAsyncPersonTrackingAsyncDataClass94559370339808:
        """Test PydanticMainVideopersonTrackingAsyncPersonTrackingAsyncDataClass94559370339808
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PydanticMainVideopersonTrackingAsyncPersonTrackingAsyncDataClass94559370339808`
        """
        model = PydanticMainVideopersonTrackingAsyncPersonTrackingAsyncDataClass94559370339808()
        if include_optional:
            return PydanticMainVideopersonTrackingAsyncPersonTrackingAsyncDataClass94559370339808(
                persons = [
                    openapi_client.models.video_tracking_person.VideoTrackingPerson(
                        tracked = [
                            openapi_client.models.person_tracking.PersonTracking(
                                offset = 56, 
                                attributes = openapi_client.models.person_attributes.PersonAttributes(
                                    upper_cloths = [
                                        openapi_client.models.upper_cloth.UpperCloth(
                                            value = '', 
                                            confidence = 56, )
                                        ], 
                                    lower_cloths = [
                                        openapi_client.models.lower_cloth.LowerCloth(
                                            value = '', 
                                            confidence = 56, )
                                        ], ), 
                                landmarks = openapi_client.models.person_landmarks.PersonLandmarks(
                                    eye_left = [
                                        56
                                        ], 
                                    eye_right = [
                                        56
                                        ], 
                                    nose = [
                                        56
                                        ], 
                                    ear_left = [
                                        56
                                        ], 
                                    ear_right = [
                                        56
                                        ], 
                                    shoulder_left = [
                                        56
                                        ], 
                                    shoulder_right = [
                                        56
                                        ], 
                                    elbow_left = [
                                        56
                                        ], 
                                    elbow_right = [
                                        56
                                        ], 
                                    wrist_left = [
                                        56
                                        ], 
                                    wrist_right = [
                                        56
                                        ], 
                                    hip_left = [
                                        56
                                        ], 
                                    hip_right = [
                                        56
                                        ], 
                                    knee_left = [
                                        56
                                        ], 
                                    knee_right = [
                                        56
                                        ], 
                                    ankle_left = [
                                        56
                                        ], 
                                    ankle_right = [
                                        56
                                        ], 
                                    mouth_left = [
                                        56
                                        ], 
                                    mouth_right = [
                                        56
                                        ], ), 
                                poses = openapi_client.models.video_person_poses.VideoPersonPoses(
                                    pitch = 56, 
                                    roll = 56, 
                                    yaw = 56, ), 
                                quality = openapi_client.models.video_person_quality.VideoPersonQuality(
                                    brightness = 56, 
                                    sharpness = 56, ), 
                                bounding_box = openapi_client.models.video_tracking_bounding_box.VideoTrackingBoundingBox(
                                    top = 56, 
                                    left = 56, 
                                    height = 56, 
                                    width = 56, ), )
                            ], )
                    ],
                original_response = None,
                id = '',
                final_status = 'success',
                error = openapi_client.models.error.Error()
            )
        else:
            return PydanticMainVideopersonTrackingAsyncPersonTrackingAsyncDataClass94559370339808(
                id = '',
                final_status = 'success',
        )
        """

    def testPydanticMainVideopersonTrackingAsyncPersonTrackingAsyncDataClass94559370339808(self):
        """Test PydanticMainVideopersonTrackingAsyncPersonTrackingAsyncDataClass94559370339808"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
