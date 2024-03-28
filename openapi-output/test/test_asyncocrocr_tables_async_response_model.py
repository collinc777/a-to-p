# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.asyncocrocr_tables_async_response_model import AsyncocrocrTablesAsyncResponseModel

class TestAsyncocrocrTablesAsyncResponseModel(unittest.TestCase):
    """AsyncocrocrTablesAsyncResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AsyncocrocrTablesAsyncResponseModel:
        """Test AsyncocrocrTablesAsyncResponseModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AsyncocrocrTablesAsyncResponseModel`
        """
        model = AsyncocrocrTablesAsyncResponseModel()
        if include_optional:
            return AsyncocrocrTablesAsyncResponseModel(
                results = openapi_client.models.ocrocr_tables_async_model.ocrocr_tables_asyncModel(
                    amazon = null, 
                    microsoft = null, 
                    google = null, ),
                error = '',
                public_id = '',
                status = ''
            )
        else:
            return AsyncocrocrTablesAsyncResponseModel(
                results = openapi_client.models.ocrocr_tables_async_model.ocrocr_tables_asyncModel(
                    amazon = null, 
                    microsoft = null, 
                    google = null, ),
                error = '',
                public_id = '',
                status = '',
        )
        """

    def testAsyncocrocrTablesAsyncResponseModel(self):
        """Test AsyncocrocrTablesAsyncResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()