# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pydantic_main_imageobject_detection_object_detection_data_class94559359068400 import PydanticMainImageobjectDetectionObjectDetectionDataClass94559359068400

class TestPydanticMainImageobjectDetectionObjectDetectionDataClass94559359068400(unittest.TestCase):
    """PydanticMainImageobjectDetectionObjectDetectionDataClass94559359068400 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PydanticMainImageobjectDetectionObjectDetectionDataClass94559359068400:
        """Test PydanticMainImageobjectDetectionObjectDetectionDataClass94559359068400
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PydanticMainImageobjectDetectionObjectDetectionDataClass94559359068400`
        """
        model = PydanticMainImageobjectDetectionObjectDetectionDataClass94559359068400()
        if include_optional:
            return PydanticMainImageobjectDetectionObjectDetectionDataClass94559359068400(
                items = [
                    openapi_client.models.object_item.ObjectItem(
                        label = '', 
                        confidence = 56, 
                        x_min = 56, 
                        x_max = 56, 
                        y_min = 56, 
                        y_max = 56, )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainImageobjectDetectionObjectDetectionDataClass94559359068400(
                status = 'success',
        )
        """

    def testPydanticMainImageobjectDetectionObjectDetectionDataClass94559359068400(self):
        """Test PydanticMainImageobjectDetectionObjectDetectionDataClass94559359068400"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
