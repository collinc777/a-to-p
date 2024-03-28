# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.imageanonymization_anonymization_data_class import ImageanonymizationAnonymizationDataClass

class TestImageanonymizationAnonymizationDataClass(unittest.TestCase):
    """ImageanonymizationAnonymizationDataClass unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImageanonymizationAnonymizationDataClass:
        """Test ImageanonymizationAnonymizationDataClass
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImageanonymizationAnonymizationDataClass`
        """
        model = ImageanonymizationAnonymizationDataClass()
        if include_optional:
            return ImageanonymizationAnonymizationDataClass(
                image = '',
                image_resource_url = '',
                items = [
                    openapi_client.models.anonymization_item.AnonymizationItem(
                        kind = '', 
                        confidence = 56, 
                        bounding_boxes = openapi_client.models.anonymization_bounding_box.AnonymizationBoundingBox(
                            x_min = 56, 
                            x_max = 56, 
                            y_min = 56, 
                            y_max = 56, ), )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return ImageanonymizationAnonymizationDataClass(
                image = '',
                image_resource_url = '',
                status = 'success',
        )
        """

    def testImageanonymizationAnonymizationDataClass(self):
        """Test ImageanonymizationAnonymizationDataClass"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
