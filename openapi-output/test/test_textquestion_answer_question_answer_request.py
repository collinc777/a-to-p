# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.textquestion_answer_question_answer_request import TextquestionAnswerQuestionAnswerRequest

class TestTextquestionAnswerQuestionAnswerRequest(unittest.TestCase):
    """TextquestionAnswerQuestionAnswerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextquestionAnswerQuestionAnswerRequest:
        """Test TextquestionAnswerQuestionAnswerRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TextquestionAnswerQuestionAnswerRequest`
        """
        model = TextquestionAnswerQuestionAnswerRequest()
        if include_optional:
            return TextquestionAnswerQuestionAnswerRequest(
                providers = '0',
                fallback_providers = '',
                response_as_dict = True,
                attributes_as_list = True,
                show_original_response = True,
                texts = [
                    '0'
                    ],
                question = '0',
                temperature = 0,
                examples_context = '0',
                examples = [
                    [
                        '0'
                        ]
                    ]
            )
        else:
            return TextquestionAnswerQuestionAnswerRequest(
                providers = '0',
                texts = [
                    '0'
                    ],
                question = '0',
                examples_context = '0',
                examples = [
                    [
                        '0'
                        ]
                    ],
        )
        """

    def testTextquestionAnswerQuestionAnswerRequest(self):
        """Test TextquestionAnswerQuestionAnswerRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
