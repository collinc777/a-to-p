# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.texttopic_extraction_response_model import TexttopicExtractionResponseModel

class TestTexttopicExtractionResponseModel(unittest.TestCase):
    """TexttopicExtractionResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TexttopicExtractionResponseModel:
        """Test TexttopicExtractionResponseModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TexttopicExtractionResponseModel`
        """
        model = TexttopicExtractionResponseModel()
        if include_optional:
            return TexttopicExtractionResponseModel(
                tenstorrent = openapi_client.models.texttopic_extraction_topic_extraction_data_class.texttopic_extractionTopicExtractionDataClass(
                    items = [
                        openapi_client.models.extracted_topic.ExtractedTopic(
                            category = '', 
                            importance = 56, )
                        ], 
                    original_response = null, 
                    status = null, ),
                openai = openapi_client.models.texttopic_extraction_topic_extraction_data_class.texttopic_extractionTopicExtractionDataClass(
                    items = [
                        openapi_client.models.extracted_topic.ExtractedTopic(
                            category = '', 
                            importance = 56, )
                        ], 
                    original_response = null, 
                    status = null, ),
                ibm = openapi_client.models.texttopic_extraction_topic_extraction_data_class.texttopic_extractionTopicExtractionDataClass(
                    items = [
                        openapi_client.models.extracted_topic.ExtractedTopic(
                            category = '', 
                            importance = 56, )
                        ], 
                    original_response = null, 
                    status = null, ),
                google = openapi_client.models.texttopic_extraction_topic_extraction_data_class.texttopic_extractionTopicExtractionDataClass(
                    items = [
                        openapi_client.models.extracted_topic.ExtractedTopic(
                            category = '', 
                            importance = 56, )
                        ], 
                    original_response = null, 
                    status = null, ),
                eden_ai = openapi_client.models.texttopic_extraction_topic_extraction_data_class.texttopic_extractionTopicExtractionDataClass(
                    items = [
                        openapi_client.models.extracted_topic.ExtractedTopic(
                            category = '', 
                            importance = 56, )
                        ], 
                    original_response = null, 
                    status = null, )
            )
        else:
            return TexttopicExtractionResponseModel(
        )
        """

    def testTexttopicExtractionResponseModel(self):
        """Test TexttopicExtractionResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
