# coding: utf-8

"""
Abdm Abha

Abdm SDK for abha

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from abha.models.generate_otp200_response import GenerateOtp200Response


class TestGenerateOtp200Response(unittest.TestCase):
    """GenerateOtp200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenerateOtp200Response:
        """Test GenerateOtp200Response
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GenerateOtp200Response`
        """
        model = GenerateOtp200Response()
        if include_optional:
            return GenerateOtp200Response(
                txn_id = 'a825f76b-0696-40f3-864c-5a3a5b389a83'
            )
        else:
            return GenerateOtp200Response(
        )
        """

    def testGenerateOtp200Response(self):
        """Test GenerateOtp200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
