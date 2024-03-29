# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.infos_identity_parser_data_class import (
    InfosIdentityParserDataClass,
)


class TestInfosIdentityParserDataClass(unittest.TestCase):
    """InfosIdentityParserDataClass unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InfosIdentityParserDataClass:
        """Test InfosIdentityParserDataClass
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `InfosIdentityParserDataClass`
        """
        model = InfosIdentityParserDataClass()
        if include_optional:
            return InfosIdentityParserDataClass(
                last_name = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                given_names = [
                    openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                        value = '', 
                        confidence = 56, )
                    ],
                birth_place = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                birth_date = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                issuance_date = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                expire_date = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                document_id = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                issuing_state = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                address = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                age = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                country = openapi_client.models.country.Country(
                    name = '', 
                    alpha2 = '', 
                    alpha3 = '', 
                    confidence = 56, ),
                document_type = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                gender = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                image_id = [
                    openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                        value = '', 
                        confidence = 56, )
                    ],
                image_signature = [
                    openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                        value = '', 
                        confidence = 56, )
                    ],
                mrz = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                nationality = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, )
            )
        else:
            return InfosIdentityParserDataClass(
                last_name = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                birth_place = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                birth_date = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                issuance_date = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                expire_date = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                document_id = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                issuing_state = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                address = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                age = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                country = openapi_client.models.country.Country(
                    name = '', 
                    alpha2 = '', 
                    alpha3 = '', 
                    confidence = 56, ),
                document_type = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                gender = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                mrz = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
                nationality = openapi_client.models.item_identity_parser_data_class.ItemIdentityParserDataClass(
                    value = '', 
                    confidence = 56, ),
        )
        """

    def testInfosIdentityParserDataClass(self):
        """Test InfosIdentityParserDataClass"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
