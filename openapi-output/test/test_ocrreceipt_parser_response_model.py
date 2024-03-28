# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ocrreceipt_parser_response_model import OcrreceiptParserResponseModel

class TestOcrreceiptParserResponseModel(unittest.TestCase):
    """OcrreceiptParserResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OcrreceiptParserResponseModel:
        """Test OcrreceiptParserResponseModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OcrreceiptParserResponseModel`
        """
        model = OcrreceiptParserResponseModel()
        if include_optional:
            return OcrreceiptParserResponseModel(
                klippa = openapi_client.models.ocrreceipt_parser_receipt_parser_data_class.ocrreceipt_parserReceiptParserDataClass(
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
                    original_response = null, 
                    status = null, ),
                mindee = openapi_client.models.ocrreceipt_parser_receipt_parser_data_class.ocrreceipt_parserReceiptParserDataClass(
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
                    original_response = null, 
                    status = null, ),
                affinda = openapi_client.models.ocrreceipt_parser_receipt_parser_data_class.ocrreceipt_parserReceiptParserDataClass(
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
                    original_response = null, 
                    status = null, ),
                microsoft = openapi_client.models.ocrreceipt_parser_receipt_parser_data_class.ocrreceipt_parserReceiptParserDataClass(
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
                    original_response = null, 
                    status = null, ),
                tabscanner = openapi_client.models.ocrreceipt_parser_receipt_parser_data_class.ocrreceipt_parserReceiptParserDataClass(
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
                    original_response = null, 
                    status = null, ),
                google = openapi_client.models.ocrreceipt_parser_receipt_parser_data_class.ocrreceipt_parserReceiptParserDataClass(
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
                    original_response = null, 
                    status = null, ),
                amazon = openapi_client.models.ocrreceipt_parser_receipt_parser_data_class.ocrreceipt_parserReceiptParserDataClass(
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
                    original_response = null, 
                    status = null, ),
                dataleon = openapi_client.models.ocrreceipt_parser_receipt_parser_data_class.ocrreceipt_parserReceiptParserDataClass(
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
                    original_response = null, 
                    status = null, ),
                veryfi = openapi_client.models.ocrreceipt_parser_receipt_parser_data_class.ocrreceipt_parserReceiptParserDataClass(
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
                    original_response = null, 
                    status = null, ),
                var_base64 = openapi_client.models.ocrreceipt_parser_receipt_parser_data_class.ocrreceipt_parserReceiptParserDataClass(
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
                    original_response = null, 
                    status = null, ),
                eden_ai = openapi_client.models.ocrreceipt_parser_receipt_parser_data_class.ocrreceipt_parserReceiptParserDataClass(
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
                    original_response = null, 
                    status = null, )
            )
        else:
            return OcrreceiptParserResponseModel(
        )
        """

    def testOcrreceiptParserResponseModel(self):
        """Test OcrreceiptParserResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()