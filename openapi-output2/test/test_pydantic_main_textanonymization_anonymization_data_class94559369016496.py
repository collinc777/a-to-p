# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_textanonymization_anonymization_data_class94559369016496 import (
    PydanticMainTextanonymizationAnonymizationDataClass94559369016496,
)


class TestPydanticMainTextanonymizationAnonymizationDataClass94559369016496(
    unittest.TestCase
):
    """PydanticMainTextanonymizationAnonymizationDataClass94559369016496 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainTextanonymizationAnonymizationDataClass94559369016496:
        """Test PydanticMainTextanonymizationAnonymizationDataClass94559369016496
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainTextanonymizationAnonymizationDataClass94559369016496`
        """
        model = PydanticMainTextanonymizationAnonymizationDataClass94559369016496()
        if include_optional:
            return PydanticMainTextanonymizationAnonymizationDataClass94559369016496(
                result = '',
                entities = [
                    openapi_client.models.anonymization_entity.AnonymizationEntity(
                        offset = 0, 
                        length = 56, 
                        category = 'Toxic', 
                        subcategory = null, 
                        original_label = '0', 
                        content = '0', 
                        confidence_score = 0, )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainTextanonymizationAnonymizationDataClass94559369016496(
                result = '',
                status = 'success',
        )
        """

    def testPydanticMainTextanonymizationAnonymizationDataClass94559369016496(self):
        """Test PydanticMainTextanonymizationAnonymizationDataClass94559369016496"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
