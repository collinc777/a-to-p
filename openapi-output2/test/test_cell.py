# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.cell import Cell


class TestCell(unittest.TestCase):
    """Cell unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Cell:
        """Test Cell
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Cell`
        """
        model = Cell()
        if include_optional:
            return Cell(
                text = '',
                row_index = 56,
                col_index = 56,
                row_span = 56,
                col_span = 56,
                confidence = 56,
                bounding_box = openapi_client.models.boundix_box_ocr_table.BoundixBoxOCRTable(
                    left = 56, 
                    top = 56, 
                    width = 56, 
                    height = 56, ),
                is_header = True
            )
        else:
            return Cell(
                text = '',
                row_index = 56,
                col_index = 56,
                row_span = 56,
                col_span = 56,
                confidence = 56,
                bounding_box = openapi_client.models.boundix_box_ocr_table.BoundixBoxOCRTable(
                    left = 56, 
                    top = 56, 
                    width = 56, 
                    height = 56, ),
        )
        """

    def testCell(self):
        """Test Cell"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()