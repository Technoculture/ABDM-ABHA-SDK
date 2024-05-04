# coding: utf-8

"""
    ABHA Service

    It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue an ABHA Number to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.  The ABHA Number will be used for the purposes of uniquely identifying persons and authenticating them. An ABHA Address will be used for threading their health records (only with the informed consent of the patient) across multiple systems and stakeholders.   <b>API Security</b>  You need Authorization Token and X-HIP-ID to consume APIs. <b>Notes:</b>  <b>1. In case you want to consume the ABHA APIs and use creation on your own interface, use authentication methods as OTP only. </b> <b>2. In order to have access to ABHA APIs, your clientId must have hid role in gateway. So if you want access to these APIs then please request it in your ABDM on-boarding request.</b> <b>3. In order to have access to Integrated Programs ABHA APIs, your clientId must have integrated_program role in gateway. So if you want access to these APIs then please request it in your ABDM on-boarding request. Also you will need to share integrated program benefit name to be used in this case.</b> <b>4. When calling APIs, please ensure that Authorization header must have format as <i>Bearer {Token_Value}</i>. Please note that prefix Bearer is followed by space before the token value.</b> <b>5. Check the state and district codes from LGD directory [click here](https://lgdirectory.gov.in/)</b>  <b>6. For the APIs </b>  - Sensitive data (Data like OTP, Aadhaar Number, Password, Username etc) have to be encrypted. - Data is encrypted by the public certificate. The certificate can be downloaded from the __/v1/auth/cert__ API under __Authentication__ tag. - RSA Encryption to encrypt the data. Cipher Type - <b>RSA/ECB/PKCS1Padding</b>.  online tool to encrypt data [click here](https://www.devglan.com/online-tools/rsa-encryption-decryption)  <b>

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abha.api.health_facility_api import HealthFacilityApi


class TestHealthFacilityApi(unittest.TestCase):
    """HealthFacilityApi unit test stubs"""

    def setUp(self) -> None:
        self.api = HealthFacilityApi()

    def tearDown(self) -> None:
        pass

    def test_ack_face_auth_client_using_get(self) -> None:
        """Test case for ack_face_auth_client_using_get

        Accept or reject FaceAuth Client session
        """
        pass

    def test_add_role_using_post(self) -> None:
        """Test case for add_role_using_post

        Add a role for the facilty
        """
        pass

    def test_authenticate_health_facility_using_post(self) -> None:
        """Test case for authenticate_health_facility_using_post

        Generate token for heath facility id.
        """
        pass

    def test_change_password_using_post(self) -> None:
        """Test case for change_password_using_post

        Change password for heath facility id.
        """
        pass

    def test_confirm_with_mobile_using_post1(self) -> None:
        """Test case for confirm_with_mobile_using_post1

        Verify otp to fetch the enrollment Id details
        """
        pass

    def test_create_aadhaar_account_using_post1(self) -> None:
        """Test case for create_aadhaar_account_using_post1

        Generate ABHA number card SVG
        """
        pass

    def test_create_health_id_by_facility_using_post(self) -> None:
        """Test case for create_health_id_by_facility_using_post

        Create ABHA number by Facility manager
        """
        pass

    def test_create_with_face_auth_using_post(self) -> None:
        """Test case for create_with_face_auth_using_post

        Capture Face Auth for KYC.
        """
        pass

    def test_delete_by_enrollment_number_using_delete(self) -> None:
        """Test case for delete_by_enrollment_number_using_delete

        Delete the provisional ID
        """
        pass

    def test_fetch_by_document_number_using_get(self) -> None:
        """Test case for fetch_by_document_number_using_get

        Fetch by Document Number
        """
        pass

    def test_fetch_by_enrollment_id_using_get(self) -> None:
        """Test case for fetch_by_enrollment_id_using_get

        Send the otp on linked mobile number
        """
        pass

    def test_fetch_document_using_post(self) -> None:
        """Test case for fetch_document_using_post

        Fetch The document from Document provider
        """
        pass

    def test_generate_facility_otp_using_post(self) -> None:
        """Test case for generate_facility_otp_using_post

        Generate health hacility OTP on registrered mobile number
        """
        pass

    def test_generate_mobile_otp_using_post1(self) -> None:
        """Test case for generate_mobile_otp_using_post1

        Generate health hacility create using mobile number
        """
        pass

    def test_generate_password_using_post(self) -> None:
        """Test case for generate_password_using_post

        Generates password for heath facility id.
        """
        pass

    def test_generate_pdf_card_using_get(self) -> None:
        """Test case for generate_pdf_card_using_get

        Generate ABHA number card in PDF format
        """
        pass

    def test_generate_png_card_using_get1(self) -> None:
        """Test case for generate_png_card_using_get1

        generatePngCard
        """
        pass

    def test_get_qr_code_using_get1(self) -> None:
        """Test case for get_qr_code_using_get1

        Get Quick Response code in PNG format for this account.
        """
        pass

    def test_health_facility_share_profile_using_post(self) -> None:
        """Test case for health_facility_share_profile_using_post

        Health hacility share profile
        """
        pass

    def test_init_face_auth_session_using_get(self) -> None:
        """Test case for init_face_auth_session_using_get

        Start new FaceAuth session
        """
        pass

    def test_remove_role_using_post(self) -> None:
        """Test case for remove_role_using_post

        Remove the role for the facilty
        """
        pass

    def test_reset_password_using_post(self) -> None:
        """Test case for reset_password_using_post

        Reset password for heath facility id.
        """
        pass

    def test_update_health_id_by_self_using_put(self) -> None:
        """Test case for update_health_id_by_self_using_put

        Update self created ABHA number.
        """
        pass

    def test_update_health_id_status_using_get(self) -> None:
        """Test case for update_health_id_status_using_get

        Verify the provisional ABHA number
        """
        pass

    def test_verify_document_using_post(self) -> None:
        """Test case for verify_document_using_post

        Verify documents.
        """
        pass

    def test_wait_for_face_auth_client_using_get(self) -> None:
        """Test case for wait_for_face_auth_client_using_get

        Wait for FaceAuth client to connect
        """
        pass


if __name__ == '__main__':
    unittest.main()