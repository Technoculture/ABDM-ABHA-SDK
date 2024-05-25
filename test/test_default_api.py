# coding: utf-8

"""
    Abdm Abha

    Abdm SDK for abha

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abha.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_create_health_id_with_pre_verified(self) -> None:
        """Test case for create_health_id_with_pre_verified

        Health ID creation
        """
        pass

    def test_generate_card_using_get(self) -> None:
        """Test case for generate_card_using_get

        Generate ABHA card in PDF format
        """
        pass

    def test_generate_mobile_otp(self) -> None:
        """Test case for generate_mobile_otp

        Generate Mobile OTP
        """
        pass

    def test_generate_otp(self) -> None:
        """Test case for generate_otp

        Generate OTP
        """
        pass

    def test_generate_png_card_using_get(self) -> None:
        """Test case for generate_png_card_using_get

        Generate ABHA card PNG
        """
        pass

    def test_generate_svg_card_using_get(self) -> None:
        """Test case for generate_svg_card_using_get

        Generate ABHA card SVG
        """
        pass

    def test_get_qr_code_using_get(self) -> None:
        """Test case for get_qr_code_using_get

        Get Quick Response code in PNG format for this account.
        """
        pass

    def test_verify_mobile_otp(self) -> None:
        """Test case for verify_mobile_otp

        Verify Mobile OTP
        """
        pass

    def test_verify_otp(self) -> None:
        """Test case for verify_otp

        Verify OTP
        """
        pass


if __name__ == '__main__':
    unittest.main()
