# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.ocrinvoice_parser_response_model import (
    OcrinvoiceParserResponseModel,
)


class TestOcrinvoiceParserResponseModel(unittest.TestCase):
    """OcrinvoiceParserResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OcrinvoiceParserResponseModel:
        """Test OcrinvoiceParserResponseModel
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `OcrinvoiceParserResponseModel`
        """
        model = OcrinvoiceParserResponseModel()
        if include_optional:
            return OcrinvoiceParserResponseModel(
                klippa = openapi_client.models.ocrinvoice_parser_invoice_parser_data_class.ocrinvoice_parserInvoiceParserDataClass(
                    extracted_data = [
                        openapi_client.models.infos_invoice_parser_data_class.InfosInvoiceParserDataClass(
                            customer_information = null, 
                            merchant_information = null, 
                            invoice_number = '', 
                            invoice_total = 56, 
                            invoice_subtotal = 56, 
                            gratuity = 56, 
                            amount_due = 56, 
                            previous_unpaid_balance = 56, 
                            discount = 56, 
                            taxes = [
                                openapi_client.models.taxes_invoice.TaxesInvoice(
                                    value = 56, 
                                    rate = 56, )
                                ], 
                            service_charge = 56, 
                            payment_term = '', 
                            purchase_order = '', 
                            date = '', 
                            due_date = '', 
                            service_date = '', 
                            service_due_date = '', 
                            po_number = '', 
                            locale = null, 
                            bank_informations = null, 
                            item_lines = [
                                openapi_client.models.item_lines_invoice.ItemLinesInvoice(
                                    description = '', 
                                    quantity = 56, 
                                    amount = 56, 
                                    unit_price = 56, 
                                    discount = 56, 
                                    product_code = '', 
                                    date_item = '', 
                                    tax_item = 56, 
                                    tax_rate = 56, )
                                ], )
                        ], 
                    original_response = null, 
                    status = null, ),
                mindee = openapi_client.models.ocrinvoice_parser_invoice_parser_data_class.ocrinvoice_parserInvoiceParserDataClass(
                    extracted_data = [
                        openapi_client.models.infos_invoice_parser_data_class.InfosInvoiceParserDataClass(
                            customer_information = null, 
                            merchant_information = null, 
                            invoice_number = '', 
                            invoice_total = 56, 
                            invoice_subtotal = 56, 
                            gratuity = 56, 
                            amount_due = 56, 
                            previous_unpaid_balance = 56, 
                            discount = 56, 
                            taxes = [
                                openapi_client.models.taxes_invoice.TaxesInvoice(
                                    value = 56, 
                                    rate = 56, )
                                ], 
                            service_charge = 56, 
                            payment_term = '', 
                            purchase_order = '', 
                            date = '', 
                            due_date = '', 
                            service_date = '', 
                            service_due_date = '', 
                            po_number = '', 
                            locale = null, 
                            bank_informations = null, 
                            item_lines = [
                                openapi_client.models.item_lines_invoice.ItemLinesInvoice(
                                    description = '', 
                                    quantity = 56, 
                                    amount = 56, 
                                    unit_price = 56, 
                                    discount = 56, 
                                    product_code = '', 
                                    date_item = '', 
                                    tax_item = 56, 
                                    tax_rate = 56, )
                                ], )
                        ], 
                    original_response = null, 
                    status = null, ),
                affinda = openapi_client.models.ocrinvoice_parser_invoice_parser_data_class.ocrinvoice_parserInvoiceParserDataClass(
                    extracted_data = [
                        openapi_client.models.infos_invoice_parser_data_class.InfosInvoiceParserDataClass(
                            customer_information = null, 
                            merchant_information = null, 
                            invoice_number = '', 
                            invoice_total = 56, 
                            invoice_subtotal = 56, 
                            gratuity = 56, 
                            amount_due = 56, 
                            previous_unpaid_balance = 56, 
                            discount = 56, 
                            taxes = [
                                openapi_client.models.taxes_invoice.TaxesInvoice(
                                    value = 56, 
                                    rate = 56, )
                                ], 
                            service_charge = 56, 
                            payment_term = '', 
                            purchase_order = '', 
                            date = '', 
                            due_date = '', 
                            service_date = '', 
                            service_due_date = '', 
                            po_number = '', 
                            locale = null, 
                            bank_informations = null, 
                            item_lines = [
                                openapi_client.models.item_lines_invoice.ItemLinesInvoice(
                                    description = '', 
                                    quantity = 56, 
                                    amount = 56, 
                                    unit_price = 56, 
                                    discount = 56, 
                                    product_code = '', 
                                    date_item = '', 
                                    tax_item = 56, 
                                    tax_rate = 56, )
                                ], )
                        ], 
                    original_response = null, 
                    status = null, ),
                microsoft = openapi_client.models.ocrinvoice_parser_invoice_parser_data_class.ocrinvoice_parserInvoiceParserDataClass(
                    extracted_data = [
                        openapi_client.models.infos_invoice_parser_data_class.InfosInvoiceParserDataClass(
                            customer_information = null, 
                            merchant_information = null, 
                            invoice_number = '', 
                            invoice_total = 56, 
                            invoice_subtotal = 56, 
                            gratuity = 56, 
                            amount_due = 56, 
                            previous_unpaid_balance = 56, 
                            discount = 56, 
                            taxes = [
                                openapi_client.models.taxes_invoice.TaxesInvoice(
                                    value = 56, 
                                    rate = 56, )
                                ], 
                            service_charge = 56, 
                            payment_term = '', 
                            purchase_order = '', 
                            date = '', 
                            due_date = '', 
                            service_date = '', 
                            service_due_date = '', 
                            po_number = '', 
                            locale = null, 
                            bank_informations = null, 
                            item_lines = [
                                openapi_client.models.item_lines_invoice.ItemLinesInvoice(
                                    description = '', 
                                    quantity = 56, 
                                    amount = 56, 
                                    unit_price = 56, 
                                    discount = 56, 
                                    product_code = '', 
                                    date_item = '', 
                                    tax_item = 56, 
                                    tax_rate = 56, )
                                ], )
                        ], 
                    original_response = null, 
                    status = null, ),
                google = openapi_client.models.ocrinvoice_parser_invoice_parser_data_class.ocrinvoice_parserInvoiceParserDataClass(
                    extracted_data = [
                        openapi_client.models.infos_invoice_parser_data_class.InfosInvoiceParserDataClass(
                            customer_information = null, 
                            merchant_information = null, 
                            invoice_number = '', 
                            invoice_total = 56, 
                            invoice_subtotal = 56, 
                            gratuity = 56, 
                            amount_due = 56, 
                            previous_unpaid_balance = 56, 
                            discount = 56, 
                            taxes = [
                                openapi_client.models.taxes_invoice.TaxesInvoice(
                                    value = 56, 
                                    rate = 56, )
                                ], 
                            service_charge = 56, 
                            payment_term = '', 
                            purchase_order = '', 
                            date = '', 
                            due_date = '', 
                            service_date = '', 
                            service_due_date = '', 
                            po_number = '', 
                            locale = null, 
                            bank_informations = null, 
                            item_lines = [
                                openapi_client.models.item_lines_invoice.ItemLinesInvoice(
                                    description = '', 
                                    quantity = 56, 
                                    amount = 56, 
                                    unit_price = 56, 
                                    discount = 56, 
                                    product_code = '', 
                                    date_item = '', 
                                    tax_item = 56, 
                                    tax_rate = 56, )
                                ], )
                        ], 
                    original_response = null, 
                    status = null, ),
                amazon = openapi_client.models.ocrinvoice_parser_invoice_parser_data_class.ocrinvoice_parserInvoiceParserDataClass(
                    extracted_data = [
                        openapi_client.models.infos_invoice_parser_data_class.InfosInvoiceParserDataClass(
                            customer_information = null, 
                            merchant_information = null, 
                            invoice_number = '', 
                            invoice_total = 56, 
                            invoice_subtotal = 56, 
                            gratuity = 56, 
                            amount_due = 56, 
                            previous_unpaid_balance = 56, 
                            discount = 56, 
                            taxes = [
                                openapi_client.models.taxes_invoice.TaxesInvoice(
                                    value = 56, 
                                    rate = 56, )
                                ], 
                            service_charge = 56, 
                            payment_term = '', 
                            purchase_order = '', 
                            date = '', 
                            due_date = '', 
                            service_date = '', 
                            service_due_date = '', 
                            po_number = '', 
                            locale = null, 
                            bank_informations = null, 
                            item_lines = [
                                openapi_client.models.item_lines_invoice.ItemLinesInvoice(
                                    description = '', 
                                    quantity = 56, 
                                    amount = 56, 
                                    unit_price = 56, 
                                    discount = 56, 
                                    product_code = '', 
                                    date_item = '', 
                                    tax_item = 56, 
                                    tax_rate = 56, )
                                ], )
                        ], 
                    original_response = null, 
                    status = null, ),
                dataleon = openapi_client.models.ocrinvoice_parser_invoice_parser_data_class.ocrinvoice_parserInvoiceParserDataClass(
                    extracted_data = [
                        openapi_client.models.infos_invoice_parser_data_class.InfosInvoiceParserDataClass(
                            customer_information = null, 
                            merchant_information = null, 
                            invoice_number = '', 
                            invoice_total = 56, 
                            invoice_subtotal = 56, 
                            gratuity = 56, 
                            amount_due = 56, 
                            previous_unpaid_balance = 56, 
                            discount = 56, 
                            taxes = [
                                openapi_client.models.taxes_invoice.TaxesInvoice(
                                    value = 56, 
                                    rate = 56, )
                                ], 
                            service_charge = 56, 
                            payment_term = '', 
                            purchase_order = '', 
                            date = '', 
                            due_date = '', 
                            service_date = '', 
                            service_due_date = '', 
                            po_number = '', 
                            locale = null, 
                            bank_informations = null, 
                            item_lines = [
                                openapi_client.models.item_lines_invoice.ItemLinesInvoice(
                                    description = '', 
                                    quantity = 56, 
                                    amount = 56, 
                                    unit_price = 56, 
                                    discount = 56, 
                                    product_code = '', 
                                    date_item = '', 
                                    tax_item = 56, 
                                    tax_rate = 56, )
                                ], )
                        ], 
                    original_response = null, 
                    status = null, ),
                rossum = openapi_client.models.ocrinvoice_parser_invoice_parser_data_class.ocrinvoice_parserInvoiceParserDataClass(
                    extracted_data = [
                        openapi_client.models.infos_invoice_parser_data_class.InfosInvoiceParserDataClass(
                            customer_information = null, 
                            merchant_information = null, 
                            invoice_number = '', 
                            invoice_total = 56, 
                            invoice_subtotal = 56, 
                            gratuity = 56, 
                            amount_due = 56, 
                            previous_unpaid_balance = 56, 
                            discount = 56, 
                            taxes = [
                                openapi_client.models.taxes_invoice.TaxesInvoice(
                                    value = 56, 
                                    rate = 56, )
                                ], 
                            service_charge = 56, 
                            payment_term = '', 
                            purchase_order = '', 
                            date = '', 
                            due_date = '', 
                            service_date = '', 
                            service_due_date = '', 
                            po_number = '', 
                            locale = null, 
                            bank_informations = null, 
                            item_lines = [
                                openapi_client.models.item_lines_invoice.ItemLinesInvoice(
                                    description = '', 
                                    quantity = 56, 
                                    amount = 56, 
                                    unit_price = 56, 
                                    discount = 56, 
                                    product_code = '', 
                                    date_item = '', 
                                    tax_item = 56, 
                                    tax_rate = 56, )
                                ], )
                        ], 
                    original_response = null, 
                    status = null, ),
                veryfi = openapi_client.models.ocrinvoice_parser_invoice_parser_data_class.ocrinvoice_parserInvoiceParserDataClass(
                    extracted_data = [
                        openapi_client.models.infos_invoice_parser_data_class.InfosInvoiceParserDataClass(
                            customer_information = null, 
                            merchant_information = null, 
                            invoice_number = '', 
                            invoice_total = 56, 
                            invoice_subtotal = 56, 
                            gratuity = 56, 
                            amount_due = 56, 
                            previous_unpaid_balance = 56, 
                            discount = 56, 
                            taxes = [
                                openapi_client.models.taxes_invoice.TaxesInvoice(
                                    value = 56, 
                                    rate = 56, )
                                ], 
                            service_charge = 56, 
                            payment_term = '', 
                            purchase_order = '', 
                            date = '', 
                            due_date = '', 
                            service_date = '', 
                            service_due_date = '', 
                            po_number = '', 
                            locale = null, 
                            bank_informations = null, 
                            item_lines = [
                                openapi_client.models.item_lines_invoice.ItemLinesInvoice(
                                    description = '', 
                                    quantity = 56, 
                                    amount = 56, 
                                    unit_price = 56, 
                                    discount = 56, 
                                    product_code = '', 
                                    date_item = '', 
                                    tax_item = 56, 
                                    tax_rate = 56, )
                                ], )
                        ], 
                    original_response = null, 
                    status = null, ),
                var_base64 = openapi_client.models.ocrinvoice_parser_invoice_parser_data_class.ocrinvoice_parserInvoiceParserDataClass(
                    extracted_data = [
                        openapi_client.models.infos_invoice_parser_data_class.InfosInvoiceParserDataClass(
                            customer_information = null, 
                            merchant_information = null, 
                            invoice_number = '', 
                            invoice_total = 56, 
                            invoice_subtotal = 56, 
                            gratuity = 56, 
                            amount_due = 56, 
                            previous_unpaid_balance = 56, 
                            discount = 56, 
                            taxes = [
                                openapi_client.models.taxes_invoice.TaxesInvoice(
                                    value = 56, 
                                    rate = 56, )
                                ], 
                            service_charge = 56, 
                            payment_term = '', 
                            purchase_order = '', 
                            date = '', 
                            due_date = '', 
                            service_date = '', 
                            service_due_date = '', 
                            po_number = '', 
                            locale = null, 
                            bank_informations = null, 
                            item_lines = [
                                openapi_client.models.item_lines_invoice.ItemLinesInvoice(
                                    description = '', 
                                    quantity = 56, 
                                    amount = 56, 
                                    unit_price = 56, 
                                    discount = 56, 
                                    product_code = '', 
                                    date_item = '', 
                                    tax_item = 56, 
                                    tax_rate = 56, )
                                ], )
                        ], 
                    original_response = null, 
                    status = null, ),
                eden_ai = openapi_client.models.ocrinvoice_parser_invoice_parser_data_class.ocrinvoice_parserInvoiceParserDataClass(
                    extracted_data = [
                        openapi_client.models.infos_invoice_parser_data_class.InfosInvoiceParserDataClass(
                            customer_information = null, 
                            merchant_information = null, 
                            invoice_number = '', 
                            invoice_total = 56, 
                            invoice_subtotal = 56, 
                            gratuity = 56, 
                            amount_due = 56, 
                            previous_unpaid_balance = 56, 
                            discount = 56, 
                            taxes = [
                                openapi_client.models.taxes_invoice.TaxesInvoice(
                                    value = 56, 
                                    rate = 56, )
                                ], 
                            service_charge = 56, 
                            payment_term = '', 
                            purchase_order = '', 
                            date = '', 
                            due_date = '', 
                            service_date = '', 
                            service_due_date = '', 
                            po_number = '', 
                            locale = null, 
                            bank_informations = null, 
                            item_lines = [
                                openapi_client.models.item_lines_invoice.ItemLinesInvoice(
                                    description = '', 
                                    quantity = 56, 
                                    amount = 56, 
                                    unit_price = 56, 
                                    discount = 56, 
                                    product_code = '', 
                                    date_item = '', 
                                    tax_item = 56, 
                                    tax_rate = 56, )
                                ], )
                        ], 
                    original_response = null, 
                    status = null, )
            )
        else:
            return OcrinvoiceParserResponseModel(
        )
        """

    def testOcrinvoiceParserResponseModel(self):
        """Test OcrinvoiceParserResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
