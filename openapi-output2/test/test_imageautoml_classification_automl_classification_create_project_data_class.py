# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.imageautoml_classification_automl_classification_create_project_data_class import (
    ImageautomlClassificationAutomlClassificationCreateProjectDataClass,
)


class TestImageautomlClassificationAutomlClassificationCreateProjectDataClass(
    unittest.TestCase
):
    """ImageautomlClassificationAutomlClassificationCreateProjectDataClass unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> ImageautomlClassificationAutomlClassificationCreateProjectDataClass:
        """Test ImageautomlClassificationAutomlClassificationCreateProjectDataClass
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ImageautomlClassificationAutomlClassificationCreateProjectDataClass`
        """
        model = ImageautomlClassificationAutomlClassificationCreateProjectDataClass()
        if include_optional:
            return ImageautomlClassificationAutomlClassificationCreateProjectDataClass(
                name = '',
                project_id = '',
                original_response = None,
                status = 'success'
            )
        else:
            return ImageautomlClassificationAutomlClassificationCreateProjectDataClass(
                name = '',
                project_id = '',
                status = 'success',
        )
        """

    def testImageautomlClassificationAutomlClassificationCreateProjectDataClass(self):
        """Test ImageautomlClassificationAutomlClassificationCreateProjectDataClass"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
