# coding: utf-8

"""
    Abdm Abha

    Abdm SDK for abha

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abha.models.link_token1_request import LinkToken1Request

class TestLinkToken1Request(unittest.TestCase):
    """LinkToken1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkToken1Request:
        """Test LinkToken1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LinkToken1Request`
        """
        model = LinkToken1Request()
        if include_optional:
            return LinkToken1Request(
                abha_address = 'abc@abdm',
                link_token = 'eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJ2YXNhbnRoYWt1bWFyLmtlc2F2',
                response = abha.models.profile_share_2_request_one_of_response.profile_share_2_request_oneOf_response(
                    request_id = '6f0b4665-a915-4c92-aa36-65afb4a2cd71', ),
                error = abha.models.link_token_1_request_one_of_3_error.link_token_1_request_oneOf_3_error(
                    code = 'ABDM-1024', 
                    message = 'Dependent service unavailable', )
            )
        else:
            return LinkToken1Request(
                link_token = 'eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJ2YXNhbnRoYWt1bWFyLmtlc2F2',
                response = abha.models.profile_share_2_request_one_of_response.profile_share_2_request_oneOf_response(
                    request_id = '6f0b4665-a915-4c92-aa36-65afb4a2cd71', ),
                error = abha.models.link_token_1_request_one_of_3_error.link_token_1_request_oneOf_3_error(
                    code = 'ABDM-1024', 
                    message = 'Dependent service unavailable', ),
        )
        """

    def testLinkToken1Request(self):
        """Test LinkToken1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
