# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_textnamed_entity_recognition_named_entity_recognition_data_class94559368908400 import (
    PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368908400,
)


class TestPydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368908400(
    unittest.TestCase
):
    """PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368908400 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368908400:
        """Test PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368908400
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368908400`
        """
        model = PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368908400()
        if include_optional:
            return PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368908400(
                items = [
                    openapi_client.models.infos_named_entity_recognition_data_class.InfosNamedEntityRecognitionDataClass(
                        entity = '', 
                        category = '', 
                        importance = 56, )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368908400(
                status = 'success',
        )
        """

    def testPydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368908400(
        self,
    ):
        """Test PydanticMainTextnamedEntityRecognitionNamedEntityRecognitionDataClass94559368908400"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()