# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.face_bounding_box import FaceBoundingBox

class TestFaceBoundingBox(unittest.TestCase):
    """FaceBoundingBox unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FaceBoundingBox:
        """Test FaceBoundingBox
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FaceBoundingBox`
        """
        model = FaceBoundingBox()
        if include_optional:
            return FaceBoundingBox(
                x_min = 56,
                x_max = 56,
                y_min = 56,
                y_max = 56
            )
        else:
            return FaceBoundingBox(
                x_min = 56,
                x_max = 56,
                y_min = 56,
                y_max = 56,
        )
        """

    def testFaceBoundingBox(self):
        """Test FaceBoundingBox"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
