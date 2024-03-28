# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pydantic_main_imagelandmark_detection_landmark_detection_data_class94559363407136 import PydanticMainImagelandmarkDetectionLandmarkDetectionDataClass94559363407136

class TestPydanticMainImagelandmarkDetectionLandmarkDetectionDataClass94559363407136(unittest.TestCase):
    """PydanticMainImagelandmarkDetectionLandmarkDetectionDataClass94559363407136 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PydanticMainImagelandmarkDetectionLandmarkDetectionDataClass94559363407136:
        """Test PydanticMainImagelandmarkDetectionLandmarkDetectionDataClass94559363407136
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PydanticMainImagelandmarkDetectionLandmarkDetectionDataClass94559363407136`
        """
        model = PydanticMainImagelandmarkDetectionLandmarkDetectionDataClass94559363407136()
        if include_optional:
            return PydanticMainImagelandmarkDetectionLandmarkDetectionDataClass94559363407136(
                items = [
                    openapi_client.models.landmark_item.LandmarkItem(
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
                            ], )
                    ],
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainImagelandmarkDetectionLandmarkDetectionDataClass94559363407136(
                status = 'success',
        )
        """

    def testPydanticMainImagelandmarkDetectionLandmarkDetectionDataClass94559363407136(self):
        """Test PydanticMainImagelandmarkDetectionLandmarkDetectionDataClass94559363407136"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()