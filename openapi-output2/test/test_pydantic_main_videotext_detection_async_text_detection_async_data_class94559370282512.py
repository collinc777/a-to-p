# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_videotext_detection_async_text_detection_async_data_class94559370282512 import (
    PydanticMainVideotextDetectionAsyncTextDetectionAsyncDataClass94559370282512,
)


class TestPydanticMainVideotextDetectionAsyncTextDetectionAsyncDataClass94559370282512(
    unittest.TestCase
):
    """PydanticMainVideotextDetectionAsyncTextDetectionAsyncDataClass94559370282512 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainVideotextDetectionAsyncTextDetectionAsyncDataClass94559370282512:
        """Test PydanticMainVideotextDetectionAsyncTextDetectionAsyncDataClass94559370282512
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainVideotextDetectionAsyncTextDetectionAsyncDataClass94559370282512`
        """
        model = PydanticMainVideotextDetectionAsyncTextDetectionAsyncDataClass94559370282512()
        if include_optional:
            return PydanticMainVideotextDetectionAsyncTextDetectionAsyncDataClass94559370282512(
                texts = [
                    openapi_client.models.video_text.VideoText(
                        text = '', 
                        frames = [
                            openapi_client.models.video_text_frames.VideoTextFrames(
                                confidence = 56, 
                                timestamp = 56, 
                                bounding_box = openapi_client.models.video_text_bounding_box.VideoTextBoundingBox(
                                    top = 56, 
                                    left = 56, 
                                    height = 56, 
                                    width = 56, ), )
                            ], )
                    ],
                original_response = None,
                id = '',
                final_status = 'success',
                error = openapi_client.models.error.Error()
            )
        else:
            return PydanticMainVideotextDetectionAsyncTextDetectionAsyncDataClass94559370282512(
                id = '',
                final_status = 'success',
        )
        """

    def testPydanticMainVideotextDetectionAsyncTextDetectionAsyncDataClass94559370282512(
        self,
    ):
        """Test PydanticMainVideotextDetectionAsyncTextDetectionAsyncDataClass94559370282512"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
