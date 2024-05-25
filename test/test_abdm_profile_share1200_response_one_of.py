# coding: utf-8

"""
    Abdm Abha

    Abdm SDK for abha

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abha.models.abdm_profile_share1200_response_one_of import AbdmProfileShare1200ResponseOneOf

class TestAbdmProfileShare1200ResponseOneOf(unittest.TestCase):
    """AbdmProfileShare1200ResponseOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AbdmProfileShare1200ResponseOneOf:
        """Test AbdmProfileShare1200ResponseOneOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AbdmProfileShare1200ResponseOneOf`
        """
        model = AbdmProfileShare1200ResponseOneOf()
        if include_optional:
            return AbdmProfileShare1200ResponseOneOf(
                code = 'ABDM-1049',
                message = 'Invalid Profile Share Intent Keys'
            )
        else:
            return AbdmProfileShare1200ResponseOneOf(
                code = 'ABDM-1049',
                message = 'Invalid Profile Share Intent Keys',
        )
        """

    def testAbdmProfileShare1200ResponseOneOf(self):
        """Test AbdmProfileShare1200ResponseOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
