# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pydantic_main_imageface_recognition_face_recognition_add_face_data_class94559363589408 import PydanticMainImagefaceRecognitionFaceRecognitionAddFaceDataClass94559363589408

class TestPydanticMainImagefaceRecognitionFaceRecognitionAddFaceDataClass94559363589408(unittest.TestCase):
    """PydanticMainImagefaceRecognitionFaceRecognitionAddFaceDataClass94559363589408 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PydanticMainImagefaceRecognitionFaceRecognitionAddFaceDataClass94559363589408:
        """Test PydanticMainImagefaceRecognitionFaceRecognitionAddFaceDataClass94559363589408
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PydanticMainImagefaceRecognitionFaceRecognitionAddFaceDataClass94559363589408`
        """
        model = PydanticMainImagefaceRecognitionFaceRecognitionAddFaceDataClass94559363589408()
        if include_optional:
            return PydanticMainImagefaceRecognitionFaceRecognitionAddFaceDataClass94559363589408(
                face_ids = [
                    ''
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainImagefaceRecognitionFaceRecognitionAddFaceDataClass94559363589408(
                face_ids = [
                    ''
                    ],
                status = 'success',
        )
        """

    def testPydanticMainImagefaceRecognitionFaceRecognitionAddFaceDataClass94559363589408(self):
        """Test PydanticMainImagefaceRecognitionFaceRecognitionAddFaceDataClass94559363589408"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
