# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_imagequestion_answer_question_answer_data_class94559363731456 import (
    PydanticMainImagequestionAnswerQuestionAnswerDataClass94559363731456,
)


class TestPydanticMainImagequestionAnswerQuestionAnswerDataClass94559363731456(
    unittest.TestCase
):
    """PydanticMainImagequestionAnswerQuestionAnswerDataClass94559363731456 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainImagequestionAnswerQuestionAnswerDataClass94559363731456:
        """Test PydanticMainImagequestionAnswerQuestionAnswerDataClass94559363731456
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainImagequestionAnswerQuestionAnswerDataClass94559363731456`
        """
        model = PydanticMainImagequestionAnswerQuestionAnswerDataClass94559363731456()
        if include_optional:
            return PydanticMainImagequestionAnswerQuestionAnswerDataClass94559363731456(
                answers = [
                    ''
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainImagequestionAnswerQuestionAnswerDataClass94559363731456(
                status = 'success',
        )
        """

    def testPydanticMainImagequestionAnswerQuestionAnswerDataClass94559363731456(self):
        """Test PydanticMainImagequestionAnswerQuestionAnswerDataClass94559363731456"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
