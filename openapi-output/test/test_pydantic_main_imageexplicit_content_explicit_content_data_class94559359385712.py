# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pydantic_main_imageexplicit_content_explicit_content_data_class94559359385712 import PydanticMainImageexplicitContentExplicitContentDataClass94559359385712

class TestPydanticMainImageexplicitContentExplicitContentDataClass94559359385712(unittest.TestCase):
    """PydanticMainImageexplicitContentExplicitContentDataClass94559359385712 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PydanticMainImageexplicitContentExplicitContentDataClass94559359385712:
        """Test PydanticMainImageexplicitContentExplicitContentDataClass94559359385712
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PydanticMainImageexplicitContentExplicitContentDataClass94559359385712`
        """
        model = PydanticMainImageexplicitContentExplicitContentDataClass94559359385712()
        if include_optional:
            return PydanticMainImageexplicitContentExplicitContentDataClass94559359385712(
                nsfw_likelihood = 56,
                nsfw_likelihood_score = 56,
                items = [
                    openapi_client.models.explicit_item.ExplicitItem(
                        label = '', 
                        likelihood = 56, 
                        likelihood_score = 56, 
                        category = 'Toxic', 
                        subcategory = null, )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainImageexplicitContentExplicitContentDataClass94559359385712(
                nsfw_likelihood = 56,
                nsfw_likelihood_score = 56,
                status = 'success',
        )
        """

    def testPydanticMainImageexplicitContentExplicitContentDataClass94559359385712(self):
        """Test PydanticMainImageexplicitContentExplicitContentDataClass94559359385712"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
