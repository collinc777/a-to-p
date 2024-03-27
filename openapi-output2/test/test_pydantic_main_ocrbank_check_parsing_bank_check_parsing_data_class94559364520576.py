# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_ocrbank_check_parsing_bank_check_parsing_data_class94559364520576 import (
    PydanticMainOcrbankCheckParsingBankCheckParsingDataClass94559364520576,
)


class TestPydanticMainOcrbankCheckParsingBankCheckParsingDataClass94559364520576(
    unittest.TestCase
):
    """PydanticMainOcrbankCheckParsingBankCheckParsingDataClass94559364520576 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainOcrbankCheckParsingBankCheckParsingDataClass94559364520576:
        """Test PydanticMainOcrbankCheckParsingBankCheckParsingDataClass94559364520576
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainOcrbankCheckParsingBankCheckParsingDataClass94559364520576`
        """
        model = PydanticMainOcrbankCheckParsingBankCheckParsingDataClass94559364520576()
        if include_optional:
            return PydanticMainOcrbankCheckParsingBankCheckParsingDataClass94559364520576(
                extracted_data = [
                    openapi_client.models.item_bank_check_parsing_data_class.ItemBankCheckParsingDataClass(
                        amount = 56, 
                        amount_text = '', 
                        bank_address = '', 
                        bank_name = '', 
                        date = '', 
                        memo = '', 
                        payer_address = '', 
                        payer_name = '', 
                        receiver_address = '', 
                        receiver_name = '', 
                        currency = '', 
                        micr = openapi_client.models.micr_model.MicrModel(
                            raw = '', 
                            account_number = '', 
                            routing_number = '', 
                            serial_number = '', 
                            check_number = '', ), )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainOcrbankCheckParsingBankCheckParsingDataClass94559364520576(
                status = 'success',
        )
        """

    def testPydanticMainOcrbankCheckParsingBankCheckParsingDataClass94559364520576(
        self,
    ):
        """Test PydanticMainOcrbankCheckParsingBankCheckParsingDataClass94559364520576"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
