# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.textsentiment_analysis_response_model import (
    TextsentimentAnalysisResponseModel,
)


class TestTextsentimentAnalysisResponseModel(unittest.TestCase):
    """TextsentimentAnalysisResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextsentimentAnalysisResponseModel:
        """Test TextsentimentAnalysisResponseModel
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TextsentimentAnalysisResponseModel`
        """
        model = TextsentimentAnalysisResponseModel()
        if include_optional:
            return TextsentimentAnalysisResponseModel(
                sapling = openapi_client.models.textsentiment_analysis_sentiment_analysis_data_class.textsentiment_analysisSentimentAnalysisDataClass(
                    general_sentiment = null, 
                    general_sentiment_rate = 0, 
                    items = [
                        openapi_client.models.segment_sentiment_analysis_data_class.SegmentSentimentAnalysisDataClass(
                            segment = '', 
                            sentiment = null, 
                            sentiment_rate = 0, )
                        ], 
                    original_response = null, 
                    status = null, ),
                tenstorrent = openapi_client.models.textsentiment_analysis_sentiment_analysis_data_class.textsentiment_analysisSentimentAnalysisDataClass(
                    general_sentiment = null, 
                    general_sentiment_rate = 0, 
                    items = [
                        openapi_client.models.segment_sentiment_analysis_data_class.SegmentSentimentAnalysisDataClass(
                            segment = '', 
                            sentiment = null, 
                            sentiment_rate = 0, )
                        ], 
                    original_response = null, 
                    status = null, ),
                microsoft = openapi_client.models.textsentiment_analysis_sentiment_analysis_data_class.textsentiment_analysisSentimentAnalysisDataClass(
                    general_sentiment = null, 
                    general_sentiment_rate = 0, 
                    items = [
                        openapi_client.models.segment_sentiment_analysis_data_class.SegmentSentimentAnalysisDataClass(
                            segment = '', 
                            sentiment = null, 
                            sentiment_rate = 0, )
                        ], 
                    original_response = null, 
                    status = null, ),
                ibm = openapi_client.models.textsentiment_analysis_sentiment_analysis_data_class.textsentiment_analysisSentimentAnalysisDataClass(
                    general_sentiment = null, 
                    general_sentiment_rate = 0, 
                    items = [
                        openapi_client.models.segment_sentiment_analysis_data_class.SegmentSentimentAnalysisDataClass(
                            segment = '', 
                            sentiment = null, 
                            sentiment_rate = 0, )
                        ], 
                    original_response = null, 
                    status = null, ),
                emvista = openapi_client.models.textsentiment_analysis_sentiment_analysis_data_class.textsentiment_analysisSentimentAnalysisDataClass(
                    general_sentiment = null, 
                    general_sentiment_rate = 0, 
                    items = [
                        openapi_client.models.segment_sentiment_analysis_data_class.SegmentSentimentAnalysisDataClass(
                            segment = '', 
                            sentiment = null, 
                            sentiment_rate = 0, )
                        ], 
                    original_response = null, 
                    status = null, ),
                google = openapi_client.models.textsentiment_analysis_sentiment_analysis_data_class.textsentiment_analysisSentimentAnalysisDataClass(
                    general_sentiment = null, 
                    general_sentiment_rate = 0, 
                    items = [
                        openapi_client.models.segment_sentiment_analysis_data_class.SegmentSentimentAnalysisDataClass(
                            segment = '', 
                            sentiment = null, 
                            sentiment_rate = 0, )
                        ], 
                    original_response = null, 
                    status = null, ),
                oneai = openapi_client.models.textsentiment_analysis_sentiment_analysis_data_class.textsentiment_analysisSentimentAnalysisDataClass(
                    general_sentiment = null, 
                    general_sentiment_rate = 0, 
                    items = [
                        openapi_client.models.segment_sentiment_analysis_data_class.SegmentSentimentAnalysisDataClass(
                            segment = '', 
                            sentiment = null, 
                            sentiment_rate = 0, )
                        ], 
                    original_response = null, 
                    status = null, ),
                amazon = openapi_client.models.textsentiment_analysis_sentiment_analysis_data_class.textsentiment_analysisSentimentAnalysisDataClass(
                    general_sentiment = null, 
                    general_sentiment_rate = 0, 
                    items = [
                        openapi_client.models.segment_sentiment_analysis_data_class.SegmentSentimentAnalysisDataClass(
                            segment = '', 
                            sentiment = null, 
                            sentiment_rate = 0, )
                        ], 
                    original_response = null, 
                    status = null, ),
                lettria = openapi_client.models.textsentiment_analysis_sentiment_analysis_data_class.textsentiment_analysisSentimentAnalysisDataClass(
                    general_sentiment = null, 
                    general_sentiment_rate = 0, 
                    items = [
                        openapi_client.models.segment_sentiment_analysis_data_class.SegmentSentimentAnalysisDataClass(
                            segment = '', 
                            sentiment = null, 
                            sentiment_rate = 0, )
                        ], 
                    original_response = null, 
                    status = null, ),
                nlpcloud = openapi_client.models.textsentiment_analysis_sentiment_analysis_data_class.textsentiment_analysisSentimentAnalysisDataClass(
                    general_sentiment = null, 
                    general_sentiment_rate = 0, 
                    items = [
                        openapi_client.models.segment_sentiment_analysis_data_class.SegmentSentimentAnalysisDataClass(
                            segment = '', 
                            sentiment = null, 
                            sentiment_rate = 0, )
                        ], 
                    original_response = null, 
                    status = null, ),
                openai = openapi_client.models.textsentiment_analysis_sentiment_analysis_data_class.textsentiment_analysisSentimentAnalysisDataClass(
                    general_sentiment = null, 
                    general_sentiment_rate = 0, 
                    items = [
                        openapi_client.models.segment_sentiment_analysis_data_class.SegmentSentimentAnalysisDataClass(
                            segment = '', 
                            sentiment = null, 
                            sentiment_rate = 0, )
                        ], 
                    original_response = null, 
                    status = null, ),
                connexun = openapi_client.models.textsentiment_analysis_sentiment_analysis_data_class.textsentiment_analysisSentimentAnalysisDataClass(
                    general_sentiment = null, 
                    general_sentiment_rate = 0, 
                    items = [
                        openapi_client.models.segment_sentiment_analysis_data_class.SegmentSentimentAnalysisDataClass(
                            segment = '', 
                            sentiment = null, 
                            sentiment_rate = 0, )
                        ], 
                    original_response = null, 
                    status = null, )
            )
        else:
            return TextsentimentAnalysisResponseModel(
        )
        """

    def testTextsentimentAnalysisResponseModel(self):
        """Test TextsentimentAnalysisResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
