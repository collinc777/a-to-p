# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.financial_bank_information import FinancialBankInformation

class TestFinancialBankInformation(unittest.TestCase):
    """FinancialBankInformation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FinancialBankInformation:
        """Test FinancialBankInformation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FinancialBankInformation`
        """
        model = FinancialBankInformation()
        if include_optional:
            return FinancialBankInformation(
                iban = '',
                swift = '',
                bsb = '',
                sort_code = '',
                account_number = '',
                routing_number = '',
                bic = ''
            )
        else:
            return FinancialBankInformation(
        )
        """

    def testFinancialBankInformation(self):
        """Test FinancialBankInformation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
