# coding: utf-8

"""
Abdm Abha

Abdm SDK for abha

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from abha.models.generate_otp_request import GenerateOtpRequest


class TestGenerateOtpRequest(unittest.TestCase):
    """GenerateOtpRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenerateOtpRequest:
        """Test GenerateOtpRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GenerateOtpRequest`
        """
        model = GenerateOtpRequest()
        if include_optional:
            return GenerateOtpRequest(
                aadhaar = '123452454590'
            )
        else:
            return GenerateOtpRequest(
        )
        """

    def testGenerateOtpRequest(self):
        """Test GenerateOtpRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
