# coding: utf-8

"""
    Eden AI

    Your project description

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.batch_launch_response import BatchLaunchResponse

class TestBatchLaunchResponse(unittest.TestCase):
    """BatchLaunchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BatchLaunchResponse:
        """Test BatchLaunchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BatchLaunchResponse`
        """
        model = BatchLaunchResponse()
        if include_optional:
            return BatchLaunchResponse(
                job_id = '',
                nb_launched = 56,
                nb_failed = 56,
                total = 56,
                failed_requests = [
                    openapi_client.models.batch_launch_failed_request.BatchLaunchFailedRequest(
                        name = '', 
                        public_id = 56, 
                        body = openapi_client.models.body.Body(), 
                        errors = openapi_client.models.errors.Errors(), )
                    ]
            )
        else:
            return BatchLaunchResponse(
                job_id = '',
                nb_launched = 56,
                nb_failed = 56,
                total = 56,
                failed_requests = [
                    openapi_client.models.batch_launch_failed_request.BatchLaunchFailedRequest(
                        name = '', 
                        public_id = 56, 
                        body = openapi_client.models.body.Body(), 
                        errors = openapi_client.models.errors.Errors(), )
                    ],
        )
        """

    def testBatchLaunchResponse(self):
        """Test BatchLaunchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
