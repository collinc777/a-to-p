# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.textsyntax_analysis_response_model import (
    TextsyntaxAnalysisResponseModel,
)


class TestTextsyntaxAnalysisResponseModel(unittest.TestCase):
    """TextsyntaxAnalysisResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextsyntaxAnalysisResponseModel:
        """Test TextsyntaxAnalysisResponseModel
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TextsyntaxAnalysisResponseModel`
        """
        model = TextsyntaxAnalysisResponseModel()
        if include_optional:
            return TextsyntaxAnalysisResponseModel(
                ibm = openapi_client.models.textsyntax_analysis_syntax_analysis_data_class.textsyntax_analysisSyntaxAnalysisDataClass(
                    items = [
                        openapi_client.models.infos_syntax_analysis_data_class.InfosSyntaxAnalysisDataClass(
                            word = '', 
                            importance = 56, 
                            tag = '', 
                            lemma = '', 
                            others = openapi_client.models.others.Others(), )
                        ], 
                    original_response = null, 
                    status = null, ),
                emvista = openapi_client.models.textsyntax_analysis_syntax_analysis_data_class.textsyntax_analysisSyntaxAnalysisDataClass(
                    items = [
                        openapi_client.models.infos_syntax_analysis_data_class.InfosSyntaxAnalysisDataClass(
                            word = '', 
                            importance = 56, 
                            tag = '', 
                            lemma = '', 
                            others = openapi_client.models.others.Others(), )
                        ], 
                    original_response = null, 
                    status = null, ),
                google = openapi_client.models.textsyntax_analysis_syntax_analysis_data_class.textsyntax_analysisSyntaxAnalysisDataClass(
                    items = [
                        openapi_client.models.infos_syntax_analysis_data_class.InfosSyntaxAnalysisDataClass(
                            word = '', 
                            importance = 56, 
                            tag = '', 
                            lemma = '', 
                            others = openapi_client.models.others.Others(), )
                        ], 
                    original_response = null, 
                    status = null, ),
                amazon = openapi_client.models.textsyntax_analysis_syntax_analysis_data_class.textsyntax_analysisSyntaxAnalysisDataClass(
                    items = [
                        openapi_client.models.infos_syntax_analysis_data_class.InfosSyntaxAnalysisDataClass(
                            word = '', 
                            importance = 56, 
                            tag = '', 
                            lemma = '', 
                            others = openapi_client.models.others.Others(), )
                        ], 
                    original_response = null, 
                    status = null, ),
                lettria = openapi_client.models.textsyntax_analysis_syntax_analysis_data_class.textsyntax_analysisSyntaxAnalysisDataClass(
                    items = [
                        openapi_client.models.infos_syntax_analysis_data_class.InfosSyntaxAnalysisDataClass(
                            word = '', 
                            importance = 56, 
                            tag = '', 
                            lemma = '', 
                            others = openapi_client.models.others.Others(), )
                        ], 
                    original_response = null, 
                    status = null, ),
                eden_ai = openapi_client.models.textsyntax_analysis_syntax_analysis_data_class.textsyntax_analysisSyntaxAnalysisDataClass(
                    items = [
                        openapi_client.models.infos_syntax_analysis_data_class.InfosSyntaxAnalysisDataClass(
                            word = '', 
                            importance = 56, 
                            tag = '', 
                            lemma = '', 
                            others = openapi_client.models.others.Others(), )
                        ], 
                    original_response = null, 
                    status = null, )
            )
        else:
            return TextsyntaxAnalysisResponseModel(
        )
        """

    def testTextsyntaxAnalysisResponseModel(self):
        """Test TextsyntaxAnalysisResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
