# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pydantic_main_textembeddings_embeddings_data_class94559369224304 import PydanticMainTextembeddingsEmbeddingsDataClass94559369224304

class TestPydanticMainTextembeddingsEmbeddingsDataClass94559369224304(unittest.TestCase):
    """PydanticMainTextembeddingsEmbeddingsDataClass94559369224304 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PydanticMainTextembeddingsEmbeddingsDataClass94559369224304:
        """Test PydanticMainTextembeddingsEmbeddingsDataClass94559369224304
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PydanticMainTextembeddingsEmbeddingsDataClass94559369224304`
        """
        model = PydanticMainTextembeddingsEmbeddingsDataClass94559369224304()
        if include_optional:
            return PydanticMainTextembeddingsEmbeddingsDataClass94559369224304(
                items = [
                    openapi_client.models.embedding_data_class.EmbeddingDataClass(
                        embedding = [
                            56
                            ], )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainTextembeddingsEmbeddingsDataClass94559369224304(
                status = 'success',
        )
        """

    def testPydanticMainTextembeddingsEmbeddingsDataClass94559369224304(self):
        """Test PydanticMainTextembeddingsEmbeddingsDataClass94559369224304"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
