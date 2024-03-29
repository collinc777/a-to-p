# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.merchant_information import MerchantInformation


class TestMerchantInformation(unittest.TestCase):
    """MerchantInformation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantInformation:
        """Test MerchantInformation
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `MerchantInformation`
        """
        model = MerchantInformation()
        if include_optional:
            return MerchantInformation(
                merchant_name = '',
                merchant_address = '',
                merchant_phone = '',
                merchant_url = '',
                merchant_siret = '',
                merchant_siren = '',
                merchant_vat_number = '',
                merchant_gst_number = '',
                merchant_abn_number = ''
            )
        else:
            return MerchantInformation(
        )
        """

    def testMerchantInformation(self):
        """Test MerchantInformation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
