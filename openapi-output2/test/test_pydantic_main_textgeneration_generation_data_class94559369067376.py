# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_textgeneration_generation_data_class94559369067376 import (
    PydanticMainTextgenerationGenerationDataClass94559369067376,
)


class TestPydanticMainTextgenerationGenerationDataClass94559369067376(
    unittest.TestCase
):
    """PydanticMainTextgenerationGenerationDataClass94559369067376 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainTextgenerationGenerationDataClass94559369067376:
        """Test PydanticMainTextgenerationGenerationDataClass94559369067376
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainTextgenerationGenerationDataClass94559369067376`
        """
        model = PydanticMainTextgenerationGenerationDataClass94559369067376()
        if include_optional:
            return PydanticMainTextgenerationGenerationDataClass94559369067376(
                generated_text = '',
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainTextgenerationGenerationDataClass94559369067376(
                generated_text = '',
                status = 'success',
        )
        """

    def testPydanticMainTextgenerationGenerationDataClass94559369067376(self):
        """Test PydanticMainTextgenerationGenerationDataClass94559369067376"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
