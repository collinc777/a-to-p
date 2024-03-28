# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.face_recognition_api import FaceRecognitionApi


class TestFaceRecognitionApi(unittest.TestCase):
    """FaceRecognitionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FaceRecognitionApi()

    def tearDown(self) -> None:
        pass

    def test_image_image_face_recognition_add_face_create(self) -> None:
        """Test case for image_image_face_recognition_add_face_create

        Face Recognition - Add Face
        """
        pass

    def test_image_image_face_recognition_delete_face_create(self) -> None:
        """Test case for image_image_face_recognition_delete_face_create

        Face Recognition - Delete Face
        """
        pass

    def test_image_image_face_recognition_list_faces_retrieve(self) -> None:
        """Test case for image_image_face_recognition_list_faces_retrieve

        Face Recognition - List Faces
        """
        pass

    def test_image_image_face_recognition_recognize_create(self) -> None:
        """Test case for image_image_face_recognition_recognize_create

        Face Recognition - Recognize Face
        """
        pass


if __name__ == '__main__':
    unittest.main()