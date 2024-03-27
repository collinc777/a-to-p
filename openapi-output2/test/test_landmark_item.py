# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.landmark_item import LandmarkItem


class TestLandmarkItem(unittest.TestCase):
    """LandmarkItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LandmarkItem:
        """Test LandmarkItem
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `LandmarkItem`
        """
        model = LandmarkItem()
        if include_optional:
            return LandmarkItem(
                description = '',
                confidence = 56,
                bounding_box = [
                    openapi_client.models.landmark_vertice.LandmarkVertice(
                        x = 56, 
                        y = 56, )
                    ],
                locations = [
                    openapi_client.models.landmark_location.LandmarkLocation(
                        lat_lng = openapi_client.models.landmark_lat_lng.LandmarkLatLng(
                            latitude = 56, 
                            longitude = 56, ), )
                    ]
            )
        else:
            return LandmarkItem(
                description = '',
                confidence = 56,
        )
        """

    def testLandmarkItem(self):
        """Test LandmarkItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
