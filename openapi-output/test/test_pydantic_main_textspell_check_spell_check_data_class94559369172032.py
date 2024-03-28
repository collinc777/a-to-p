# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pydantic_main_textspell_check_spell_check_data_class94559369172032 import PydanticMainTextspellCheckSpellCheckDataClass94559369172032

class TestPydanticMainTextspellCheckSpellCheckDataClass94559369172032(unittest.TestCase):
    """PydanticMainTextspellCheckSpellCheckDataClass94559369172032 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PydanticMainTextspellCheckSpellCheckDataClass94559369172032:
        """Test PydanticMainTextspellCheckSpellCheckDataClass94559369172032
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PydanticMainTextspellCheckSpellCheckDataClass94559369172032`
        """
        model = PydanticMainTextspellCheckSpellCheckDataClass94559369172032()
        if include_optional:
            return PydanticMainTextspellCheckSpellCheckDataClass94559369172032(
                text = '',
                items = [
                    openapi_client.models.spell_check_item.SpellCheckItem(
                        text = '', 
                        type = '', 
                        offset = 0, 
                        length = 0, 
                        suggestions = [
                            openapi_client.models.suggestion_item.SuggestionItem(
                                suggestion = '', 
                                score = 0, )
                            ], )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainTextspellCheckSpellCheckDataClass94559369172032(
                text = '',
                status = 'success',
        )
        """

    def testPydanticMainTextspellCheckSpellCheckDataClass94559369172032(self):
        """Test PydanticMainTextspellCheckSpellCheckDataClass94559369172032"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
