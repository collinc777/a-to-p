# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.item_lines_invoice import ItemLinesInvoice


class TestItemLinesInvoice(unittest.TestCase):
    """ItemLinesInvoice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ItemLinesInvoice:
        """Test ItemLinesInvoice
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ItemLinesInvoice`
        """
        model = ItemLinesInvoice()
        if include_optional:
            return ItemLinesInvoice(
                description = '',
                quantity = 56,
                amount = 56,
                unit_price = 56,
                discount = 56,
                product_code = '',
                date_item = '',
                tax_item = 56,
                tax_rate = 56
            )
        else:
            return ItemLinesInvoice(
        )
        """

    def testItemLinesInvoice(self):
        """Test ItemLinesInvoice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()