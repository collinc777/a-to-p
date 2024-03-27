# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_ocrreceipt_parser_receipt_parser_data_class94559367647808 import (
    PydanticMainOcrreceiptParserReceiptParserDataClass94559367647808,
)


class TestPydanticMainOcrreceiptParserReceiptParserDataClass94559367647808(
    unittest.TestCase
):
    """PydanticMainOcrreceiptParserReceiptParserDataClass94559367647808 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainOcrreceiptParserReceiptParserDataClass94559367647808:
        """Test PydanticMainOcrreceiptParserReceiptParserDataClass94559367647808
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainOcrreceiptParserReceiptParserDataClass94559367647808`
        """
        model = PydanticMainOcrreceiptParserReceiptParserDataClass94559367647808()
        if include_optional:
            return PydanticMainOcrreceiptParserReceiptParserDataClass94559367647808(
                extracted_data = [
                    openapi_client.models.infos_receipt_parser_data_class.InfosReceiptParserDataClass(
                        invoice_number = '', 
                        invoice_total = 56, 
                        invoice_subtotal = 56, 
                        barcodes = [
                            openapi_client.models.bar_code.BarCode(
                                value = '', 
                                type = '', )
                            ], 
                        category = '', 
                        date = '', 
                        due_date = '', 
                        time = '', 
                        customer_information = null, 
                        merchant_information = null, 
                        payment_information = null, 
                        locale = null, 
                        taxes = [
                            openapi_client.models.taxes.Taxes(
                                taxes = 56, 
                                rate = 56, )
                            ], 
                        receipt_infos = openapi_client.models.receipt_infos.Receipt Infos(), 
                        item_lines = [
                            openapi_client.models.item_lines.ItemLines(
                                description = '', 
                                quantity = 56, 
                                amount = 56, 
                                unit_price = 56, )
                            ], )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainOcrreceiptParserReceiptParserDataClass94559367647808(
                status = 'success',
        )
        """

    def testPydanticMainOcrreceiptParserReceiptParserDataClass94559367647808(self):
        """Test PydanticMainOcrreceiptParserReceiptParserDataClass94559367647808"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
