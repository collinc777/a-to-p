# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_translationdocument_translation_document_translation_data_class94559370115408 import (
    PydanticMainTranslationdocumentTranslationDocumentTranslationDataClass94559370115408,
)


class TestPydanticMainTranslationdocumentTranslationDocumentTranslationDataClass94559370115408(
    unittest.TestCase
):
    """PydanticMainTranslationdocumentTranslationDocumentTranslationDataClass94559370115408 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainTranslationdocumentTranslationDocumentTranslationDataClass94559370115408:
        """Test PydanticMainTranslationdocumentTranslationDocumentTranslationDataClass94559370115408
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainTranslationdocumentTranslationDocumentTranslationDataClass94559370115408`
        """
        model = PydanticMainTranslationdocumentTranslationDocumentTranslationDataClass94559370115408()
        if include_optional:
            return PydanticMainTranslationdocumentTranslationDocumentTranslationDataClass94559370115408(
                file = '',
                document_resource_url = '',
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainTranslationdocumentTranslationDocumentTranslationDataClass94559370115408(
                file = '',
                document_resource_url = '',
                status = 'success',
        )
        """

    def testPydanticMainTranslationdocumentTranslationDocumentTranslationDataClass94559370115408(
        self,
    ):
        """Test PydanticMainTranslationdocumentTranslationDocumentTranslationDataClass94559370115408"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
