# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_ocrocr_tables_async_ocr_tables_async_data_class94559364101216 import (
    PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559364101216,
)


class TestPydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559364101216(
    unittest.TestCase
):
    """PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559364101216 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559364101216:
        """Test PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559364101216
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559364101216`
        """
        model = PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559364101216()
        if include_optional:
            return PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559364101216(
                pages = [
                    openapi_client.models.page.Page(
                        lines = [
                            openapi_client.models.line.Line(
                                text = '', 
                                words = [
                                    openapi_client.models.word.Word(
                                        text = '', 
                                        bounding_box = null, 
                                        confidence = 56, )
                                    ], 
                                bounding_box = null, 
                                confidence = 56, )
                            ], )
                    ],
                num_pages = 56,
                original_response = None,
                id = '',
                final_status = 'success',
                error = openapi_client.models.error.Error()
            )
        else:
            return PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559364101216(
                num_pages = 56,
                id = '',
                final_status = 'success',
        )
        """

    def testPydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559364101216(self):
        """Test PydanticMainOcrocrTablesAsyncOcrTablesAsyncDataClass94559364101216"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
