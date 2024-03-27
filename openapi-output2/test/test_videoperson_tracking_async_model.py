# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.videoperson_tracking_async_model import (
    VideopersonTrackingAsyncModel,
)


class TestVideopersonTrackingAsyncModel(unittest.TestCase):
    """VideopersonTrackingAsyncModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VideopersonTrackingAsyncModel:
        """Test VideopersonTrackingAsyncModel
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `VideopersonTrackingAsyncModel`
        """
        model = VideopersonTrackingAsyncModel()
        if include_optional:
            return VideopersonTrackingAsyncModel(
                amazon = openapi_client.models.videoperson_tracking_async_person_tracking_async_data_class.videoperson_tracking_asyncPersonTrackingAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), ),
                google = openapi_client.models.videoperson_tracking_async_person_tracking_async_data_class.videoperson_tracking_asyncPersonTrackingAsyncDataClass(
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
                    original_response = null, 
                    id = '', 
                    final_status = null, 
                    error = openapi_client.models.error.Error(), )
            )
        else:
            return VideopersonTrackingAsyncModel(
        )
        """

    def testVideopersonTrackingAsyncModel(self):
        """Test VideopersonTrackingAsyncModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
