# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pydantic_main_textsummarize_summarize_data_class94559364620768 import PydanticMainTextsummarizeSummarizeDataClass94559364620768

class TestPydanticMainTextsummarizeSummarizeDataClass94559364620768(unittest.TestCase):
    """PydanticMainTextsummarizeSummarizeDataClass94559364620768 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PydanticMainTextsummarizeSummarizeDataClass94559364620768:
        """Test PydanticMainTextsummarizeSummarizeDataClass94559364620768
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PydanticMainTextsummarizeSummarizeDataClass94559364620768`
        """
        model = PydanticMainTextsummarizeSummarizeDataClass94559364620768()
        if include_optional:
            return PydanticMainTextsummarizeSummarizeDataClass94559364620768(
                result = '',
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainTextsummarizeSummarizeDataClass94559364620768(
                result = '',
                status = 'success',
        )
        """

    def testPydanticMainTextsummarizeSummarizeDataClass94559364620768(self):
        """Test PydanticMainTextsummarizeSummarizeDataClass94559364620768"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
