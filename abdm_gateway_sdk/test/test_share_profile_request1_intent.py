# coding: utf-8

"""
    Gateway

    Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing 

    The version of the OpenAPI document: 0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abdm_gateway.models.share_profile_request1_intent import ShareProfileRequest1Intent

class TestShareProfileRequest1Intent(unittest.TestCase):
    """ShareProfileRequest1Intent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ShareProfileRequest1Intent:
        """Test ShareProfileRequest1Intent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ShareProfileRequest1Intent`
        """
        model = ShareProfileRequest1Intent()
        if include_optional:
            return ShareProfileRequest1Intent(
                type = ''
            )
        else:
            return ShareProfileRequest1Intent(
                type = '',
        )
        """

    def testShareProfileRequest1Intent(self):
        """Test ShareProfileRequest1Intent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
