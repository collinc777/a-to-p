# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pydantic_main_textquestion_answer_question_answer_data_class94559363483456 import PydanticMainTextquestionAnswerQuestionAnswerDataClass94559363483456

class TestPydanticMainTextquestionAnswerQuestionAnswerDataClass94559363483456(unittest.TestCase):
    """PydanticMainTextquestionAnswerQuestionAnswerDataClass94559363483456 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PydanticMainTextquestionAnswerQuestionAnswerDataClass94559363483456:
        """Test PydanticMainTextquestionAnswerQuestionAnswerDataClass94559363483456
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PydanticMainTextquestionAnswerQuestionAnswerDataClass94559363483456`
        """
        model = PydanticMainTextquestionAnswerQuestionAnswerDataClass94559363483456()
        if include_optional:
            return PydanticMainTextquestionAnswerQuestionAnswerDataClass94559363483456(
                answers = [
                    ''
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainTextquestionAnswerQuestionAnswerDataClass94559363483456(
                status = 'success',
        )
        """

    def testPydanticMainTextquestionAnswerQuestionAnswerDataClass94559363483456(self):
        """Test PydanticMainTextquestionAnswerQuestionAnswerDataClass94559363483456"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
