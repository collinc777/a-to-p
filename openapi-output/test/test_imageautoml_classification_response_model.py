# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.imageautoml_classification_response_model import ImageautomlClassificationResponseModel

class TestImageautomlClassificationResponseModel(unittest.TestCase):
    """ImageautomlClassificationResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImageautomlClassificationResponseModel:
        """Test ImageautomlClassificationResponseModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImageautomlClassificationResponseModel`
        """
        model = ImageautomlClassificationResponseModel()
        if include_optional:
            return ImageautomlClassificationResponseModel(
                nyckel = openapi_client.models.imageautoml_classification_automl_classification_create_project_data_class.imageautoml_classificationAutomlClassificationCreateProjectDataClass(
                    name = '', 
                    project_id = '', 
                    original_response = null, 
                    status = null, )
            )
        else:
            return ImageautomlClassificationResponseModel(
        )
        """

    def testImageautomlClassificationResponseModel(self):
        """Test ImageautomlClassificationResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()