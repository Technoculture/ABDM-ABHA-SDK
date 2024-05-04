# coding: utf-8

"""
    Gateway

    Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing 

    The version of the OpenAPI document: 0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abdm_gateway.models.share_profile_request import ShareProfileRequest

class TestShareProfileRequest(unittest.TestCase):
    """ShareProfileRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ShareProfileRequest:
        """Test ShareProfileRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ShareProfileRequest`
        """
        model = ShareProfileRequest()
        if include_optional:
            return ShareProfileRequest(
                request_id = '499a5a4a-7dda-4f20-9b67-e24589627061',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                profile = abdm_gateway.models.share_profile_request_profile.ShareProfileRequest_profile(
                    hip_code = '12345 (CounterId)', 
                    patient = abdm_gateway.models.share_profile_request_profile_patient.ShareProfileRequest_profile_patient(
                        health_id = '<username>@<suffix>', 
                        health_id_number = '1111-1111-1111-11', 
                        name = 'Jane Doe', 
                        gender = 'M', 
                        address = abdm_gateway.models.patient_address.PatientAddress(
                            line = '', 
                            district = '', 
                            state = '', 
                            pincode = '', ), 
                        year_of_birth = 2000, 
                        day_of_birth = 56, 
                        month_of_birth = 56, 
                        identifiers = [
                            abdm_gateway.models.identifier.Identifier(
                                type = 'MR', 
                                value = '+919800083232', )
                            ], ), )
            )
        else:
            return ShareProfileRequest(
                request_id = '499a5a4a-7dda-4f20-9b67-e24589627061',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                profile = abdm_gateway.models.share_profile_request_profile.ShareProfileRequest_profile(
                    hip_code = '12345 (CounterId)', 
                    patient = abdm_gateway.models.share_profile_request_profile_patient.ShareProfileRequest_profile_patient(
                        health_id = '<username>@<suffix>', 
                        health_id_number = '1111-1111-1111-11', 
                        name = 'Jane Doe', 
                        gender = 'M', 
                        address = abdm_gateway.models.patient_address.PatientAddress(
                            line = '', 
                            district = '', 
                            state = '', 
                            pincode = '', ), 
                        year_of_birth = 2000, 
                        day_of_birth = 56, 
                        month_of_birth = 56, 
                        identifiers = [
                            abdm_gateway.models.identifier.Identifier(
                                type = 'MR', 
                                value = '+919800083232', )
                            ], ), ),
        )
        """

    def testShareProfileRequest(self):
        """Test ShareProfileRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()