# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pydantic_main_translationlanguage_detection_language_detection_data_class94559370153472 import PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370153472

class TestPydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370153472(unittest.TestCase):
    """PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370153472 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370153472:
        """Test PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370153472
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370153472`
        """
        model = PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370153472()
        if include_optional:
            return PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370153472(
                items = [
                    openapi_client.models.infos_language_detection_data_class.InfosLanguageDetectionDataClass(
                        language = '', 
                        display_name = '', 
                        confidence = 56, )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370153472(
                status = 'success',
        )
        """

    def testPydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370153472(self):
        """Test PydanticMainTranslationlanguageDetectionLanguageDetectionDataClass94559370153472"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
