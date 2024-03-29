# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.resource_list import ResourceList

class TestResourceList(unittest.TestCase):
    """ResourceList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceList:
        """Test ResourceList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceList`
        """
        model = ResourceList()
        if include_optional:
            return ResourceList(
                resource = '',
                data = 'YQ==',
                type = 'db',
                provider = '',
                assets = [
                    openapi_client.models.asset_list.AssetList(
                        sub_resource = '', 
                        data = 'YQ==', )
                    ]
            )
        else:
            return ResourceList(
                resource = '',
                data = 'YQ==',
                type = 'db',
                provider = '',
                assets = [
                    openapi_client.models.asset_list.AssetList(
                        sub_resource = '', 
                        data = 'YQ==', )
                    ],
        )
        """

    def testResourceList(self):
        """Test ResourceList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
