# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pydantic_main_textsyntax_analysis_syntax_analysis_data_class94559368306288 import PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368306288

class TestPydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368306288(unittest.TestCase):
    """PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368306288 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368306288:
        """Test PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368306288
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368306288`
        """
        model = PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368306288()
        if include_optional:
            return PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368306288(
                items = [
                    openapi_client.models.infos_syntax_analysis_data_class.InfosSyntaxAnalysisDataClass(
                        word = '', 
                        importance = 56, 
                        tag = '', 
                        lemma = '', 
                        others = openapi_client.models.others.Others(), )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368306288(
                status = 'success',
        )
        """

    def testPydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368306288(self):
        """Test PydanticMainTextsyntaxAnalysisSyntaxAnalysisDataClass94559368306288"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
