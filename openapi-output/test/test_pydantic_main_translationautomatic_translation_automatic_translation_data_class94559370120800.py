# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pydantic_main_translationautomatic_translation_automatic_translation_data_class94559370120800 import PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559370120800

class TestPydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559370120800(unittest.TestCase):
    """PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559370120800 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559370120800:
        """Test PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559370120800
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559370120800`
        """
        model = PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559370120800()
        if include_optional:
            return PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559370120800(
                text = '',
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559370120800(
                text = '',
                status = 'success',
        )
        """

    def testPydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559370120800(self):
        """Test PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559370120800"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
