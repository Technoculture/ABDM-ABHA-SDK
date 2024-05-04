# coding: utf-8

"""
    Gateway

    Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing 

    The version of the OpenAPI document: 0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abdm_gateway.models.hiu_health_information_request_response_hi_request import HIUHealthInformationRequestResponseHiRequest

class TestHIUHealthInformationRequestResponseHiRequest(unittest.TestCase):
    """HIUHealthInformationRequestResponseHiRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HIUHealthInformationRequestResponseHiRequest:
        """Test HIUHealthInformationRequestResponseHiRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HIUHealthInformationRequestResponseHiRequest`
        """
        model = HIUHealthInformationRequestResponseHiRequest()
        if include_optional:
            return HIUHealthInformationRequestResponseHiRequest(
                transaction_id = '',
                session_status = 'REQUESTED'
            )
        else:
            return HIUHealthInformationRequestResponseHiRequest(
                transaction_id = '',
                session_status = 'REQUESTED',
        )
        """

    def testHIUHealthInformationRequestResponseHiRequest(self):
        """Test HIUHealthInformationRequestResponseHiRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
