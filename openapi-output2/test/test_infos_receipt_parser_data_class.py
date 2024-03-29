# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.infos_receipt_parser_data_class import (
    InfosReceiptParserDataClass,
)


class TestInfosReceiptParserDataClass(unittest.TestCase):
    """InfosReceiptParserDataClass unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InfosReceiptParserDataClass:
        """Test InfosReceiptParserDataClass
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `InfosReceiptParserDataClass`
        """
        model = InfosReceiptParserDataClass()
        if include_optional:
            return InfosReceiptParserDataClass(
                invoice_number = '',
                invoice_total = 56,
                invoice_subtotal = 56,
                barcodes = [
                    openapi_client.models.bar_code.BarCode(
                        value = '', 
                        type = '', )
                    ],
                category = '',
                var_date = '',
                due_date = '',
                time = '',
                customer_information = openapi_client.models.customer_information.CustomerInformation(
                    customer_name = '', ),
                merchant_information = openapi_client.models.merchant_information.MerchantInformation(
                    merchant_name = '', 
                    merchant_address = '', 
                    merchant_phone = '', 
                    merchant_url = '', 
                    merchant_siret = '', 
                    merchant_siren = '', 
                    merchant_vat_number = '', 
                    merchant_gst_number = '', 
                    merchant_abn_number = '', ),
                payment_information = openapi_client.models.payment_information.PaymentInformation(
                    card_type = '', 
                    card_number = '', 
                    cash = '', 
                    tip = '', 
                    discount = '', 
                    change = '', ),
                locale = openapi_client.models.locale.Locale(
                    currency = '', 
                    language = '', 
                    country = '', ),
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
                    ]
            )
        else:
            return InfosReceiptParserDataClass(
        )
        """

    def testInfosReceiptParserDataClass(self):
        """Test InfosReceiptParserDataClass"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
