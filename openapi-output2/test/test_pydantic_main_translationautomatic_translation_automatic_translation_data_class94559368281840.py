# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_translationautomatic_translation_automatic_translation_data_class94559368281840 import (
    PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559368281840,
)


class TestPydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559368281840(
    unittest.TestCase
):
    """PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559368281840 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559368281840:
        """Test PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559368281840
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559368281840`
        """
        model = PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559368281840()
        if include_optional:
            return PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559368281840(
                text = '',
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559368281840(
                text = '',
                status = 'success',
        )
        """

    def testPydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559368281840(
        self,
    ):
        """Test PydanticMainTranslationautomaticTranslationAutomaticTranslationDataClass94559368281840"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
