# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.textkeyword_extraction_response_model import (
    TextkeywordExtractionResponseModel,
)


class TestTextkeywordExtractionResponseModel(unittest.TestCase):
    """TextkeywordExtractionResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextkeywordExtractionResponseModel:
        """Test TextkeywordExtractionResponseModel
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TextkeywordExtractionResponseModel`
        """
        model = TextkeywordExtractionResponseModel()
        if include_optional:
            return TextkeywordExtractionResponseModel(
                tenstorrent = openapi_client.models.textkeyword_extraction_keyword_extraction_data_class.textkeyword_extractionKeywordExtractionDataClass(
                    items = [
                        openapi_client.models.infos_keyword_extraction_data_class.InfosKeywordExtractionDataClass(
                            keyword = '', 
                            importance = 56, )
                        ], 
                    original_response = null, 
                    status = null, ),
                microsoft = openapi_client.models.textkeyword_extraction_keyword_extraction_data_class.textkeyword_extractionKeywordExtractionDataClass(
                    items = [
                        openapi_client.models.infos_keyword_extraction_data_class.InfosKeywordExtractionDataClass(
                            keyword = '', 
                            importance = 56, )
                        ], 
                    original_response = null, 
                    status = null, ),
                ibm = openapi_client.models.textkeyword_extraction_keyword_extraction_data_class.textkeyword_extractionKeywordExtractionDataClass(
                    items = [
                        openapi_client.models.infos_keyword_extraction_data_class.InfosKeywordExtractionDataClass(
                            keyword = '', 
                            importance = 56, )
                        ], 
                    original_response = null, 
                    status = null, ),
                emvista = openapi_client.models.textkeyword_extraction_keyword_extraction_data_class.textkeyword_extractionKeywordExtractionDataClass(
                    items = [
                        openapi_client.models.infos_keyword_extraction_data_class.InfosKeywordExtractionDataClass(
                            keyword = '', 
                            importance = 56, )
                        ], 
                    original_response = null, 
                    status = null, ),
                oneai = openapi_client.models.textkeyword_extraction_keyword_extraction_data_class.textkeyword_extractionKeywordExtractionDataClass(
                    items = [
                        openapi_client.models.infos_keyword_extraction_data_class.InfosKeywordExtractionDataClass(
                            keyword = '', 
                            importance = 56, )
                        ], 
                    original_response = null, 
                    status = null, ),
                amazon = openapi_client.models.textkeyword_extraction_keyword_extraction_data_class.textkeyword_extractionKeywordExtractionDataClass(
                    items = [
                        openapi_client.models.infos_keyword_extraction_data_class.InfosKeywordExtractionDataClass(
                            keyword = '', 
                            importance = 56, )
                        ], 
                    original_response = null, 
                    status = null, ),
                nlpcloud = openapi_client.models.textkeyword_extraction_keyword_extraction_data_class.textkeyword_extractionKeywordExtractionDataClass(
                    items = [
                        openapi_client.models.infos_keyword_extraction_data_class.InfosKeywordExtractionDataClass(
                            keyword = '', 
                            importance = 56, )
                        ], 
                    original_response = null, 
                    status = null, ),
                openai = openapi_client.models.textkeyword_extraction_keyword_extraction_data_class.textkeyword_extractionKeywordExtractionDataClass(
                    items = [
                        openapi_client.models.infos_keyword_extraction_data_class.InfosKeywordExtractionDataClass(
                            keyword = '', 
                            importance = 56, )
                        ], 
                    original_response = null, 
                    status = null, ),
                corticalio = openapi_client.models.textkeyword_extraction_keyword_extraction_data_class.textkeyword_extractionKeywordExtractionDataClass(
                    items = [
                        openapi_client.models.infos_keyword_extraction_data_class.InfosKeywordExtractionDataClass(
                            keyword = '', 
                            importance = 56, )
                        ], 
                    original_response = null, 
                    status = null, ),
                eden_ai = openapi_client.models.textkeyword_extraction_keyword_extraction_data_class.textkeyword_extractionKeywordExtractionDataClass(
                    items = [
                        openapi_client.models.infos_keyword_extraction_data_class.InfosKeywordExtractionDataClass(
                            keyword = '', 
                            importance = 56, )
                        ], 
                    original_response = null, 
                    status = null, )
            )
        else:
            return TextkeywordExtractionResponseModel(
        )
        """

    def testTextkeywordExtractionResponseModel(self):
        """Test TextkeywordExtractionResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()