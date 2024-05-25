# coding: utf-8

"""
    Abdm Abha

    Abdm SDK for abha

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abha.models.abdm_profile_share1_request_meta_data import AbdmProfileShare1RequestMetaData

class TestAbdmProfileShare1RequestMetaData(unittest.TestCase):
    """AbdmProfileShare1RequestMetaData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AbdmProfileShare1RequestMetaData:
        """Test AbdmProfileShare1RequestMetaData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AbdmProfileShare1RequestMetaData`
        """
        model = AbdmProfileShare1RequestMetaData()
        if include_optional:
            return AbdmProfileShare1RequestMetaData(
                lat = 20.5937,
                long = 78.9629
            )
        else:
            return AbdmProfileShare1RequestMetaData(
                lat = 20.5937,
                long = 78.9629,
        )
        """

    def testAbdmProfileShare1RequestMetaData(self):
        """Test AbdmProfileShare1RequestMetaData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
