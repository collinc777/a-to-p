# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.textspell_check_response_model import TextspellCheckResponseModel

class TestTextspellCheckResponseModel(unittest.TestCase):
    """TextspellCheckResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextspellCheckResponseModel:
        """Test TextspellCheckResponseModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TextspellCheckResponseModel`
        """
        model = TextspellCheckResponseModel()
        if include_optional:
            return TextspellCheckResponseModel(
                sapling = openapi_client.models.textspell_check_spell_check_data_class.textspell_checkSpellCheckDataClass(
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
                    original_response = null, 
                    status = null, ),
                microsoft = openapi_client.models.textspell_check_spell_check_data_class.textspell_checkSpellCheckDataClass(
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
                    original_response = null, 
                    status = null, ),
                cohere = openapi_client.models.textspell_check_spell_check_data_class.textspell_checkSpellCheckDataClass(
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
                    original_response = null, 
                    status = null, ),
                ai21labs = openapi_client.models.textspell_check_spell_check_data_class.textspell_checkSpellCheckDataClass(
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
                    original_response = null, 
                    status = null, ),
                prowritingaid = openapi_client.models.textspell_check_spell_check_data_class.textspell_checkSpellCheckDataClass(
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
                    original_response = null, 
                    status = null, ),
                nlpcloud = openapi_client.models.textspell_check_spell_check_data_class.textspell_checkSpellCheckDataClass(
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
                    original_response = null, 
                    status = null, ),
                openai = openapi_client.models.textspell_check_spell_check_data_class.textspell_checkSpellCheckDataClass(
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
                    original_response = null, 
                    status = null, )
            )
        else:
            return TextspellCheckResponseModel(
        )
        """

    def testTextspellCheckResponseModel(self):
        """Test TextspellCheckResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
