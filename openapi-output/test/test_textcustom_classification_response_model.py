# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.textcustom_classification_response_model import TextcustomClassificationResponseModel

class TestTextcustomClassificationResponseModel(unittest.TestCase):
    """TextcustomClassificationResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextcustomClassificationResponseModel:
        """Test TextcustomClassificationResponseModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TextcustomClassificationResponseModel`
        """
        model = TextcustomClassificationResponseModel()
        if include_optional:
            return TextcustomClassificationResponseModel(
                cohere = openapi_client.models.textcustom_classification_custom_classification_data_class.textcustom_classificationCustomClassificationDataClass(
                    classifications = [
                        openapi_client.models.item_custom_classification_data_class.ItemCustomClassificationDataClass(
                            input = '', 
                            label = '', 
                            confidence = 56, )
                        ], 
                    original_response = null, 
                    status = null, ),
                openai = openapi_client.models.textcustom_classification_custom_classification_data_class.textcustom_classificationCustomClassificationDataClass(
                    classifications = [
                        openapi_client.models.item_custom_classification_data_class.ItemCustomClassificationDataClass(
                            input = '', 
                            label = '', 
                            confidence = 56, )
                        ], 
                    original_response = null, 
                    status = null, )
            )
        else:
            return TextcustomClassificationResponseModel(
        )
        """

    def testTextcustomClassificationResponseModel(self):
        """Test TextcustomClassificationResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
