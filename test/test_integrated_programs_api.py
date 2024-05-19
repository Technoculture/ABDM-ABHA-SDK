# coding: utf-8

"""
ABHA Service

It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue an ABHA Number to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.  The ABHA Number will be used for the purposes of uniquely identifying persons and authenticating them. An ABHA Address will be used for threading their health records (only with the informed consent of the patient) across multiple systems and stakeholders.   <b>API Security</b>  You need Authorization Token and X-HIP-ID to consume APIs. <b>Notes:</b>  <b>1. In case you want to consume the ABHA APIs and use creation on your own interface, use authentication methods as OTP only. </b> <b>2. In order to have access to ABHA APIs, your clientId must have hid role in gateway. So if you want access to these APIs then please request it in your ABDM on-boarding request.</b> <b>3. In order to have access to Integrated Programs ABHA APIs, your clientId must have integrated_program role in gateway. So if you want access to these APIs then please request it in your ABDM on-boarding request. Also you will need to share integrated program benefit name to be used in this case.</b> <b>4. When calling APIs, please ensure that Authorization header must have format as <i>Bearer {Token_Value}</i>. Please note that prefix Bearer is followed by space before the token value.</b> <b>5. Check the state and district codes from LGD directory [click here](https://lgdirectory.gov.in/)</b>  <b>6. For the APIs </b>  - Sensitive data (Data like OTP, Aadhaar Number, Password, Username etc) have to be encrypted. - Data is encrypted by the public certificate. The certificate can be downloaded from the __/v1/auth/cert__ API under __Authentication__ tag. - RSA Encryption to encrypt the data. Cipher Type - <b>RSA/ECB/PKCS1Padding</b>.  online tool to encrypt data [click here](https://www.devglan.com/online-tools/rsa-encryption-decryption)  <b>

The version of the OpenAPI document: 1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from abha.api.integrated_programs_api import IntegratedProgramsApi


class TestIntegratedProgramsApi(unittest.TestCase):
    """IntegratedProgramsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = IntegratedProgramsApi()

    def tearDown(self) -> None:
        pass

    def test_create_health_id_by_demo_auth_using_post(self) -> None:
        """Test case for create_health_id_by_demo_auth_using_post

        Create ABHA Number using Aadhaar Demo Auth.
        """
        pass

    def test_create_health_id_by_mobile_using_post(self) -> None:
        """Test case for create_health_id_by_mobile_using_post

        Create ABHA number using mobile Authentication.
        """
        pass

    def test_create_phr_adress_with_health_id_number_using_post1(self) -> None:
        """Test case for create_phr_adress_with_health_id_number_using_post1

        Create ABHA Address With ABHA Number
        """
        pass

    def test_delink_hid_benefit_using_post(self) -> None:
        """Test case for delink_hid_benefit_using_post

        Delinks benefit programme from ABHA Number
        """
        pass

    def test_delink_user_hid_benefit_using_post(self) -> None:
        """Test case for delink_user_hid_benefit_using_post

        Delinks benefit programme from ABHA Number
        """
        pass

    def test_find_by_aadhar_using_post(self) -> None:
        """Test case for find_by_aadhar_using_post

        Search ABHA number using Aadhaar or Aadhaar token
        """
        pass

    def test_find_by_health_id_using_post(self) -> None:
        """Test case for find_by_health_id_using_post

        Search benefit using ABHA number
        """
        pass

    def test_generate_aadhar_otp_using_post2(self) -> None:
        """Test case for generate_aadhar_otp_using_post2

        Generate Aadhaar OTP on Registered mobile number
        """
        pass

    def test_generate_mobile_otp_using_post(self) -> None:
        """Test case for generate_mobile_otp_using_post

        Generate mobile OTP on Registered mobile number
        """
        pass

    def test_link_hid_benefit_using_post(self) -> None:
        """Test case for link_hid_benefit_using_post

        Links benefit programme with ABHA Number
        """
        pass

    def test_link_user_hid_benefit_using_post(self) -> None:
        """Test case for link_user_hid_benefit_using_post

        Link Benefit ID with ABHA Number after authentication.
        """
        pass

    def test_notify_benefit_using_post(self) -> None:
        """Test case for notify_benefit_using_post

        Create ABHA number using notify Benefit.
        """
        pass

    def test_update_account_information_using_post1(self) -> None:
        """Test case for update_account_information_using_post1

        Update account information
        """
        pass

    def test_update_mobile_information_using_post(self) -> None:
        """Test case for update_mobile_information_using_post

        Update mobile number for account.
        """
        pass

    def test_update_status_using_post(self) -> None:
        """Test case for update_status_using_post

        Update ABHA status
        """
        pass

    def test_verify_aadhar_otp_using_post(self) -> None:
        """Test case for verify_aadhar_otp_using_post

        Create ABHA Number using Aadhaar Number OTP
        """
        pass

    def test_verify_bio_using_post(self) -> None:
        """Test case for verify_bio_using_post

        Create ABHA Number using Biometric Authentication
        """
        pass


if __name__ == "__main__":
    unittest.main()
