# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_ocridentity_parser_identity_parser_data_class94559367750928 import (
    PydanticMainOcridentityParserIdentityParserDataClass94559367750928,
)


class TestPydanticMainOcridentityParserIdentityParserDataClass94559367750928(
    unittest.TestCase
):
    """PydanticMainOcridentityParserIdentityParserDataClass94559367750928 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainOcridentityParserIdentityParserDataClass94559367750928:
        """Test PydanticMainOcridentityParserIdentityParserDataClass94559367750928
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainOcridentityParserIdentityParserDataClass94559367750928`
        """
        model = PydanticMainOcridentityParserIdentityParserDataClass94559367750928()
        if include_optional:
            return PydanticMainOcridentityParserIdentityParserDataClass94559367750928(
                extracted_data = [
                    openapi_client.models.infos_identity_parser_data_class.InfosIdentityParserDataClass(
                        last_name = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                            value = '', 
                            confidence = 56, ), 
                        given_names = [
                            openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                                value = '', 
                                confidence = 56, )
                            ], 
                        birth_place = , 
                        birth_date = , 
                        issuance_date = , 
                        expire_date = , 
                        document_id = , 
                        issuing_state = , 
                        address = , 
                        age = , 
                        country = openapi_client.models.country.Country(
                            name = '', 
                            alpha2 = '', 
                            alpha3 = '', 
                            confidence = 56, ), 
                        document_type = , 
                        gender = , 
                        image_id = [
                            
                            ], 
                        image_signature = [
                            
                            ], 
                        mrz = , 
                        nationality = , )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainOcridentityParserIdentityParserDataClass94559367750928(
                status = 'success',
        )
        """

    def testPydanticMainOcridentityParserIdentityParserDataClass94559367750928(self):
        """Test PydanticMainOcridentityParserIdentityParserDataClass94559367750928"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
