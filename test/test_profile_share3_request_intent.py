# coding: utf-8

"""
    Abdm Abha

    Abdm SDK for abha

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abha.models.profile_share3_request_intent import ProfileShare3RequestIntent

class TestProfileShare3RequestIntent(unittest.TestCase):
    """ProfileShare3RequestIntent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProfileShare3RequestIntent:
        """Test ProfileShare3RequestIntent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProfileShare3RequestIntent`
        """
        model = ProfileShare3RequestIntent()
        if include_optional:
            return ProfileShare3RequestIntent(
                context = 123,
                link_token = ''
            )
        else:
            return ProfileShare3RequestIntent(
        )
        """

    def testProfileShare3RequestIntent(self):
        """Test ProfileShare3RequestIntent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
