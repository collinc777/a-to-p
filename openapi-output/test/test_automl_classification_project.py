# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.automl_classification_project import AutomlClassificationProject

class TestAutomlClassificationProject(unittest.TestCase):
    """AutomlClassificationProject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AutomlClassificationProject:
        """Test AutomlClassificationProject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AutomlClassificationProject`
        """
        model = AutomlClassificationProject()
        if include_optional:
            return AutomlClassificationProject(
                project_id = '',
                name = '',
                provider = ''
            )
        else:
            return AutomlClassificationProject(
                project_id = '',
                name = '',
                provider = '',
        )
        """

    def testAutomlClassificationProject(self):
        """Test AutomlClassificationProject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
