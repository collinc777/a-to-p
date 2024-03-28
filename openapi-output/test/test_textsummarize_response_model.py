# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.textsummarize_response_model import TextsummarizeResponseModel

class TestTextsummarizeResponseModel(unittest.TestCase):
    """TextsummarizeResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextsummarizeResponseModel:
        """Test TextsummarizeResponseModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TextsummarizeResponseModel`
        """
        model = TextsummarizeResponseModel()
        if include_optional:
            return TextsummarizeResponseModel(
                writesonic = openapi_client.models.textsummarize_summarize_data_class.textsummarizeSummarizeDataClass(
                    result = '', 
                    original_response = null, 
                    status = null, ),
                microsoft = openapi_client.models.textsummarize_summarize_data_class.textsummarizeSummarizeDataClass(
                    result = '', 
                    original_response = null, 
                    status = null, ),
                emvista = openapi_client.models.textsummarize_summarize_data_class.textsummarizeSummarizeDataClass(
                    result = '', 
                    original_response = null, 
                    status = null, ),
                cohere = openapi_client.models.textsummarize_summarize_data_class.textsummarizeSummarizeDataClass(
                    result = '', 
                    original_response = null, 
                    status = null, ),
                nlpcloud = openapi_client.models.textsummarize_summarize_data_class.textsummarizeSummarizeDataClass(
                    result = '', 
                    original_response = null, 
                    status = null, ),
                oneai = openapi_client.models.textsummarize_summarize_data_class.textsummarizeSummarizeDataClass(
                    result = '', 
                    original_response = null, 
                    status = null, ),
                ai21labs = openapi_client.models.textsummarize_summarize_data_class.textsummarizeSummarizeDataClass(
                    result = '', 
                    original_response = null, 
                    status = null, ),
                alephalpha = openapi_client.models.textsummarize_summarize_data_class.textsummarizeSummarizeDataClass(
                    result = '', 
                    original_response = null, 
                    status = null, ),
                openai = openapi_client.models.textsummarize_summarize_data_class.textsummarizeSummarizeDataClass(
                    result = '', 
                    original_response = null, 
                    status = null, ),
                meaningcloud = openapi_client.models.textsummarize_summarize_data_class.textsummarizeSummarizeDataClass(
                    result = '', 
                    original_response = null, 
                    status = null, ),
                huggingface = openapi_client.models.textsummarize_summarize_data_class.textsummarizeSummarizeDataClass(
                    result = '', 
                    original_response = null, 
                    status = null, ),
                anthropic = openapi_client.models.textsummarize_summarize_data_class.textsummarizeSummarizeDataClass(
                    result = '', 
                    original_response = null, 
                    status = null, ),
                connexun = openapi_client.models.textsummarize_summarize_data_class.textsummarizeSummarizeDataClass(
                    result = '', 
                    original_response = null, 
                    status = null, )
            )
        else:
            return TextsummarizeResponseModel(
        )
        """

    def testTextsummarizeResponseModel(self):
        """Test TextsummarizeResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
