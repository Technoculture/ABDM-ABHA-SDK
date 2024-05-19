# coding: utf-8

"""
ABHA Service

It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue an ABHA Number to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.  The ABHA Number will be used for the purposes of uniquely identifying persons and authenticating them. An ABHA Address will be used for threading their health records (only with the informed consent of the patient) across multiple systems and stakeholders.   <b>API Security</b>  You need Authorization Token and X-HIP-ID to consume APIs. <b>Notes:</b>  <b>1. In case you want to consume the ABHA APIs and use creation on your own interface, use authentication methods as OTP only. </b> <b>2. In order to have access to ABHA APIs, your clientId must have hid role in gateway. So if you want access to these APIs then please request it in your ABDM on-boarding request.</b> <b>3. In order to have access to Integrated Programs ABHA APIs, your clientId must have integrated_program role in gateway. So if you want access to these APIs then please request it in your ABDM on-boarding request. Also you will need to share integrated program benefit name to be used in this case.</b> <b>4. When calling APIs, please ensure that Authorization header must have format as <i>Bearer {Token_Value}</i>. Please note that prefix Bearer is followed by space before the token value.</b> <b>5. Check the state and district codes from LGD directory [click here](https://lgdirectory.gov.in/)</b>  <b>6. For the APIs </b>  - Sensitive data (Data like OTP, Aadhaar Number, Password, Username etc) have to be encrypted. - Data is encrypted by the public certificate. The certificate can be downloaded from the __/v1/auth/cert__ API under __Authentication__ tag. - RSA Encryption to encrypt the data. Cipher Type - <b>RSA/ECB/PKCS1Padding</b>.  online tool to encrypt data [click here](https://www.devglan.com/online-tools/rsa-encryption-decryption)  <b>

The version of the OpenAPI document: 1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from abha.api.authentication_api import AuthenticationApi


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthenticationApi()

    def tearDown(self) -> None:
        pass

    def test_auth_with_mobile_token_using_post(self) -> None:
        """Test case for auth_with_mobile_token_using_post

        Authenticate using verified Mobile Number and user data
        """
        pass

    def test_authenticate_user_using_post(self) -> None:
        """Test case for authenticate_user_using_post

        Authenticate request to generate Mobile OTP using ABHA number
        """
        pass

    def test_authenticate_with_password_using_post(self) -> None:
        """Test case for authenticate_with_password_using_post

        Authenticate using ABHA Number and password
        """
        pass

    def test_cert_using_get(self) -> None:
        """Test case for cert_using_get

        Authentication token public certificate. This certificate is also used to encrypt the data.
        """
        pass

    def test_confirm_with_aadhaar_bio_using_post(self) -> None:
        """Test case for confirm_with_aadhaar_bio_using_post

        Authentication with Aadhaar Biometric based auth transaction.
        """
        pass

    def test_confirm_with_aadhaar_otp_using_post(self) -> None:
        """Test case for confirm_with_aadhaar_otp_using_post

        Authentication with Aadhaar OTP based auth transaction.
        """
        pass

    def test_confirm_with_demographics_using_post(self) -> None:
        """Test case for confirm_with_demographics_using_post

        Authenticate using demographic data of user.
        """
        pass

    def test_confirm_with_mobile_using_post(self) -> None:
        """Test case for confirm_with_mobile_using_post

        Authentication with Mobile OTP based auth transaction.
        """
        pass

    def test_generate_access_token_using_post(self) -> None:
        """Test case for generate_access_token_using_post

        create Access Token From Refresh Token
        """
        pass

    def test_initiate_auth_using_post(self) -> None:
        """Test case for initiate_auth_using_post

        Initiate authentication process for a given ABHA Number
        """
        pass

    def test_initiate_reactivate_auth_using_post(self) -> None:
        """Test case for initiate_reactivate_auth_using_post

        Initiate authentication for reactivation of ABHA Number
        """
        pass

    def test_reactivate_using_post(self) -> None:
        """Test case for reactivate_using_post

        confirm reactivation txn with aadhar or mobile otp
        """
        pass

    def test_resend_auth_mobile_otp_using_post(self) -> None:
        """Test case for resend_auth_mobile_otp_using_post

        Resend Aadhaar/Mobile OTP for Authentication Transaction
        """
        pass


if __name__ == "__main__":
    unittest.main()