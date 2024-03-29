# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.textgeneration_response_model import (
    TextgenerationResponseModel,
)


class TestTextgenerationResponseModel(unittest.TestCase):
    """TextgenerationResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextgenerationResponseModel:
        """Test TextgenerationResponseModel
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TextgenerationResponseModel`
        """
        model = TextgenerationResponseModel()
        if include_optional:
            return TextgenerationResponseModel(
                meta = openapi_client.models.textgeneration_generation_data_class.textgenerationGenerationDataClass(
                    generated_text = '', 
                    original_response = null, 
                    status = null, ),
                google = openapi_client.models.textgeneration_generation_data_class.textgenerationGenerationDataClass(
                    generated_text = '', 
                    original_response = null, 
                    status = null, ),
                cohere = openapi_client.models.textgeneration_generation_data_class.textgenerationGenerationDataClass(
                    generated_text = '', 
                    original_response = null, 
                    status = null, ),
                mistral = openapi_client.models.textgeneration_generation_data_class.textgenerationGenerationDataClass(
                    generated_text = '', 
                    original_response = null, 
                    status = null, ),
                amazon = openapi_client.models.textgeneration_generation_data_class.textgenerationGenerationDataClass(
                    generated_text = '', 
                    original_response = null, 
                    status = null, ),
                ai21labs = openapi_client.models.textgeneration_generation_data_class.textgenerationGenerationDataClass(
                    generated_text = '', 
                    original_response = null, 
                    status = null, ),
                clarifai = openapi_client.models.textgeneration_generation_data_class.textgenerationGenerationDataClass(
                    generated_text = '', 
                    original_response = null, 
                    status = null, ),
                openai = openapi_client.models.textgeneration_generation_data_class.textgenerationGenerationDataClass(
                    generated_text = '', 
                    original_response = null, 
                    status = null, ),
                anthropic = openapi_client.models.textgeneration_generation_data_class.textgenerationGenerationDataClass(
                    generated_text = '', 
                    original_response = null, 
                    status = null, )
            )
        else:
            return TextgenerationResponseModel(
        )
        """

    def testTextgenerationResponseModel(self):
        """Test TextgenerationResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
