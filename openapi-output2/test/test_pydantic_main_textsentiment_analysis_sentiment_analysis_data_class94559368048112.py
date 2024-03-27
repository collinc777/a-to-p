# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_textsentiment_analysis_sentiment_analysis_data_class94559368048112 import (
    PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368048112,
)


class TestPydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368048112(
    unittest.TestCase
):
    """PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368048112 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368048112:
        """Test PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368048112
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368048112`
        """
        model = PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368048112()
        if include_optional:
            return PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368048112(
                general_sentiment = 'Positive',
                general_sentiment_rate = 0,
                items = [
                    openapi_client.models.segment_sentiment_analysis_data_class.SegmentSentimentAnalysisDataClass(
                        segment = '', 
                        sentiment = null, 
                        sentiment_rate = 0, )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368048112(
                general_sentiment = 'Positive',
                general_sentiment_rate = 0,
                status = 'success',
        )
        """

    def testPydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368048112(
        self,
    ):
        """Test PydanticMainTextsentimentAnalysisSentimentAnalysisDataClass94559368048112"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
