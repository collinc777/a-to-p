# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.infos_named_entity_recognition_data_class import (
    InfosNamedEntityRecognitionDataClass,
)


class TestInfosNamedEntityRecognitionDataClass(unittest.TestCase):
    """InfosNamedEntityRecognitionDataClass unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InfosNamedEntityRecognitionDataClass:
        """Test InfosNamedEntityRecognitionDataClass
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `InfosNamedEntityRecognitionDataClass`
        """
        model = InfosNamedEntityRecognitionDataClass()
        if include_optional:
            return InfosNamedEntityRecognitionDataClass(
                entity = '',
                category = '',
                importance = 56
            )
        else:
            return InfosNamedEntityRecognitionDataClass(
                entity = '',
                category = '',
                importance = 56,
        )
        """

    def testInfosNamedEntityRecognitionDataClass(self):
        """Test InfosNamedEntityRecognitionDataClass"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
