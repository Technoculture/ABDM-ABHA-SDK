# coding: utf-8

"""
    Gateway

    Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing 

    The version of the OpenAPI document: 0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abdm_gateway.models.patient_auth_notification_auth import PatientAuthNotificationAuth

class TestPatientAuthNotificationAuth(unittest.TestCase):
    """PatientAuthNotificationAuth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatientAuthNotificationAuth:
        """Test PatientAuthNotificationAuth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatientAuthNotificationAuth`
        """
        model = PatientAuthNotificationAuth()
        if include_optional:
            return PatientAuthNotificationAuth(
                transaction_id = '',
                status = 'GRANTED',
                access_token = '',
                validity = abdm_gateway.models.access_token_validity.AccessTokenValidity(
                    purpose = 'LINK', 
                    requester = abdm_gateway.models.patient_auth_requester.PatientAuthRequester(
                        type = 'HIP', 
                        id = '100005', ), 
                    expiry = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    limit = 1, ),
                patient = abdm_gateway.models.patient_demographic_response.PatientDemographicResponse(
                    id = '<patient-id>@<consent-manager-id>', 
                    name = 'Hina Patel', 
                    gender = 'M', 
                    year_of_birth = 2000, 
                    address = abdm_gateway.models.patient_address.PatientAddress(
                        line = '', 
                        district = '', 
                        state = '', 
                        pincode = '', ), 
                    identifiers = [
                        abdm_gateway.models.identifier.Identifier(
                            type = 'MR', 
                            value = '+919800083232', )
                        ], )
            )
        else:
            return PatientAuthNotificationAuth(
                transaction_id = '',
                status = 'GRANTED',
        )
        """

    def testPatientAuthNotificationAuth(self):
        """Test PatientAuthNotificationAuth"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
