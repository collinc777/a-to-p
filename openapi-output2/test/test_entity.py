# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.entity import Entity


class TestEntity(unittest.TestCase):
    """Entity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Entity:
        """Test Entity
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Entity`
        """
        model = Entity()
        if include_optional:
            return Entity(
                type = '',
                text = '',
                sentiment = 'Positive',
                begin_offset = 56,
                end_offset = 56
            )
        else:
            return Entity(
                type = '',
                text = '',
                sentiment = 'Positive',
        )
        """

    def testEntity(self):
        """Test Entity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()