# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.asyncocrcustom_document_parsing_async_response_model import AsyncocrcustomDocumentParsingAsyncResponseModel

class TestAsyncocrcustomDocumentParsingAsyncResponseModel(unittest.TestCase):
    """AsyncocrcustomDocumentParsingAsyncResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AsyncocrcustomDocumentParsingAsyncResponseModel:
        """Test AsyncocrcustomDocumentParsingAsyncResponseModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AsyncocrcustomDocumentParsingAsyncResponseModel`
        """
        model = AsyncocrcustomDocumentParsingAsyncResponseModel()
        if include_optional:
            return AsyncocrcustomDocumentParsingAsyncResponseModel(
                results = openapi_client.models.ocrcustom_document_parsing_async_model.ocrcustom_document_parsing_asyncModel(
                    extracta = null, 
                    amazon = null, ),
                error = '',
                public_id = '',
                status = ''
            )
        else:
            return AsyncocrcustomDocumentParsingAsyncResponseModel(
                results = openapi_client.models.ocrcustom_document_parsing_async_model.ocrcustom_document_parsing_asyncModel(
                    extracta = null, 
                    amazon = null, ),
                error = '',
                public_id = '',
                status = '',
        )
        """

    def testAsyncocrcustomDocumentParsingAsyncResponseModel(self):
        """Test AsyncocrcustomDocumentParsingAsyncResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
