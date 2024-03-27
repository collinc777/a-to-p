# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.customer_information_invoice import (
    CustomerInformationInvoice,
)


class TestCustomerInformationInvoice(unittest.TestCase):
    """CustomerInformationInvoice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomerInformationInvoice:
        """Test CustomerInformationInvoice
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CustomerInformationInvoice`
        """
        model = CustomerInformationInvoice()
        if include_optional:
            return CustomerInformationInvoice(
                customer_name = '',
                customer_address = '',
                customer_email = '',
                customer_id = '',
                customer_tax_id = '',
                customer_mailing_address = '',
                customer_billing_address = '',
                customer_shipping_address = '',
                customer_service_address = '',
                customer_remittance_address = '',
                abn_number = '',
                gst_number = '',
                pan_number = '',
                vat_number = '',
                siret_number = '',
                siren_number = ''
            )
        else:
            return CustomerInformationInvoice(
                customer_name = '',
                customer_address = '',
                customer_email = '',
                customer_id = '',
                customer_tax_id = '',
                customer_mailing_address = '',
                customer_billing_address = '',
                customer_shipping_address = '',
                customer_service_address = '',
                customer_remittance_address = '',
                abn_number = '',
                gst_number = '',
                pan_number = '',
                vat_number = '',
        )
        """

    def testCustomerInformationInvoice(self):
        """Test CustomerInformationInvoice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()