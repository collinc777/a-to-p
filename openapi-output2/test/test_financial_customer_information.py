# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.financial_customer_information import (
    FinancialCustomerInformation,
)


class TestFinancialCustomerInformation(unittest.TestCase):
    """FinancialCustomerInformation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FinancialCustomerInformation:
        """Test FinancialCustomerInformation
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `FinancialCustomerInformation`
        """
        model = FinancialCustomerInformation()
        if include_optional:
            return FinancialCustomerInformation(
                name = '',
                id_reference = '',
                mailling_address = '',
                billing_address = '',
                shipping_address = '',
                service_address = '',
                remittance_address = '',
                email = '',
                phone = '',
                vat_number = '',
                abn_number = '',
                gst_number = '',
                pan_number = '',
                business_number = '',
                siret_number = '',
                siren_number = '',
                customer_number = '',
                coc_number = '',
                fiscal_number = '',
                registration_number = '',
                tax_id = '',
                website = '',
                remit_to_name = '',
                city = '',
                country = '',
                house_number = '',
                province = '',
                street_name = '',
                zip_code = '',
                municipality = ''
            )
        else:
            return FinancialCustomerInformation(
        )
        """

    def testFinancialCustomerInformation(self):
        """Test FinancialCustomerInformation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
