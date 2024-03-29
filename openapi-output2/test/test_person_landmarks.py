# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.person_landmarks import PersonLandmarks


class TestPersonLandmarks(unittest.TestCase):
    """PersonLandmarks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonLandmarks:
        """Test PersonLandmarks
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PersonLandmarks`
        """
        model = PersonLandmarks()
        if include_optional:
            return PersonLandmarks(
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
                    ]
            )
        else:
            return PersonLandmarks(
        )
        """

    def testPersonLandmarks(self):
        """Test PersonLandmarks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
