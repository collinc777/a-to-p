# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.translationautomatic_translation_response_model import TranslationautomaticTranslationResponseModel

class TestTranslationautomaticTranslationResponseModel(unittest.TestCase):
    """TranslationautomaticTranslationResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TranslationautomaticTranslationResponseModel:
        """Test TranslationautomaticTranslationResponseModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TranslationautomaticTranslationResponseModel`
        """
        model = TranslationautomaticTranslationResponseModel()
        if include_optional:
            return TranslationautomaticTranslationResponseModel(
                microsoft = openapi_client.models.translationautomatic_translation_automatic_translation_data_class.translationautomatic_translationAutomaticTranslationDataClass(
                    text = '', 
                    original_response = null, 
                    status = null, ),
                google = openapi_client.models.translationautomatic_translation_automatic_translation_data_class.translationautomatic_translationAutomaticTranslationDataClass(
                    text = '', 
                    original_response = null, 
                    status = null, ),
                ibm = openapi_client.models.translationautomatic_translation_automatic_translation_data_class.translationautomatic_translationAutomaticTranslationDataClass(
                    text = '', 
                    original_response = null, 
                    status = null, ),
                deepl = openapi_client.models.translationautomatic_translation_automatic_translation_data_class.translationautomatic_translationAutomaticTranslationDataClass(
                    text = '', 
                    original_response = null, 
                    status = null, ),
                amazon = openapi_client.models.translationautomatic_translation_automatic_translation_data_class.translationautomatic_translationAutomaticTranslationDataClass(
                    text = '', 
                    original_response = null, 
                    status = null, ),
                neuralspace = openapi_client.models.translationautomatic_translation_automatic_translation_data_class.translationautomatic_translationAutomaticTranslationDataClass(
                    text = '', 
                    original_response = null, 
                    status = null, ),
                openai = openapi_client.models.translationautomatic_translation_automatic_translation_data_class.translationautomatic_translationAutomaticTranslationDataClass(
                    text = '', 
                    original_response = null, 
                    status = null, ),
                phedone = openapi_client.models.translationautomatic_translation_automatic_translation_data_class.translationautomatic_translationAutomaticTranslationDataClass(
                    text = '', 
                    original_response = null, 
                    status = null, ),
                modernmt = openapi_client.models.translationautomatic_translation_automatic_translation_data_class.translationautomatic_translationAutomaticTranslationDataClass(
                    text = '', 
                    original_response = null, 
                    status = null, ),
                huggingface = openapi_client.models.translationautomatic_translation_automatic_translation_data_class.translationautomatic_translationAutomaticTranslationDataClass(
                    text = '', 
                    original_response = null, 
                    status = null, )
            )
        else:
            return TranslationautomaticTranslationResponseModel(
        )
        """

    def testTranslationautomaticTranslationResponseModel(self):
        """Test TranslationautomaticTranslationResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
