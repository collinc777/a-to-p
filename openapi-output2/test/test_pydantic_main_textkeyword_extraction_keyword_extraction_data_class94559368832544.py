# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_textkeyword_extraction_keyword_extraction_data_class94559368832544 import (
    PydanticMainTextkeywordExtractionKeywordExtractionDataClass94559368832544,
)


class TestPydanticMainTextkeywordExtractionKeywordExtractionDataClass94559368832544(
    unittest.TestCase
):
    """PydanticMainTextkeywordExtractionKeywordExtractionDataClass94559368832544 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainTextkeywordExtractionKeywordExtractionDataClass94559368832544:
        """Test PydanticMainTextkeywordExtractionKeywordExtractionDataClass94559368832544
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainTextkeywordExtractionKeywordExtractionDataClass94559368832544`
        """
        model = PydanticMainTextkeywordExtractionKeywordExtractionDataClass94559368832544()
        if include_optional:
            return PydanticMainTextkeywordExtractionKeywordExtractionDataClass94559368832544(
                items = [
                    openapi_client.models.infos_keyword_extraction_data_class.InfosKeywordExtractionDataClass(
                        keyword = '', 
                        importance = 56, )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainTextkeywordExtractionKeywordExtractionDataClass94559368832544(
                status = 'success',
        )
        """

    def testPydanticMainTextkeywordExtractionKeywordExtractionDataClass94559368832544(
        self,
    ):
        """Test PydanticMainTextkeywordExtractionKeywordExtractionDataClass94559368832544"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
