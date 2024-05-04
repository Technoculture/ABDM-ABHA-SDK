# coding: utf-8

"""
    Gateway

    Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing 

    The version of the OpenAPI document: 0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abdm_gateway.models.link_confirmation_request_confirmation import LinkConfirmationRequestConfirmation

class TestLinkConfirmationRequestConfirmation(unittest.TestCase):
    """LinkConfirmationRequestConfirmation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkConfirmationRequestConfirmation:
        """Test LinkConfirmationRequestConfirmation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LinkConfirmationRequestConfirmation`
        """
        model = LinkConfirmationRequestConfirmation()
        if include_optional:
            return LinkConfirmationRequestConfirmation(
                link_ref_number = '',
                token = ''
            )
        else:
            return LinkConfirmationRequestConfirmation(
                link_ref_number = '',
                token = '',
        )
        """

    def testLinkConfirmationRequestConfirmation(self):
        """Test LinkConfirmationRequestConfirmation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
