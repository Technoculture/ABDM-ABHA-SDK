# coding: utf-8

"""
Abdm Abha

Abdm SDK for abha

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from abha.models.create_health_id_with_pre_verified_request import (
    CreateHealthIdWithPreVerifiedRequest,
)


class TestCreateHealthIdWithPreVerifiedRequest(unittest.TestCase):
    """CreateHealthIdWithPreVerifiedRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateHealthIdWithPreVerifiedRequest:
        """Test CreateHealthIdWithPreVerifiedRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CreateHealthIdWithPreVerifiedRequest`
        """
        model = CreateHealthIdWithPreVerifiedRequest()
        if include_optional:
            return CreateHealthIdWithPreVerifiedRequest(
                email = 'Example@Demo.com',
                first_name = 'manoj',
                health_id = 'deepak.pant',
                last_name = 'singh',
                middle_name = 'kishan',
                password = 'India@143',
                profile_photo = '/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkJCQkJCQoLCwoODw0PDhQSERESFB4WFxYXFh4uHSEdHSEdLikxKCUoMSlJOTMzOUlUR0NHVGZbW2aBeoGoqOIBCQkJCQkJCgsLCg4PDQ8OFBIRERIUHhYXFhcWHi4dIR0dIR0uKTEoJSgxKUk5MzM5SVRHQ0dUZltbZoF6gaio4v/CABEIBLAHgAMBIgACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAACAwABBAUGB//aAAgBAQAAAADwawLpMspcK7qrlE5F0Vtul2bVywMUNeBHUkW/bmxvYELGuNjh2VDvixxo5ViljKjDRMoahCULjs2JCShjhjh2OGxo0Y2MoXHOLszsKLhw7tD99mpZQxj8xceofmLEKFwXLTIyHwY1Ls+iEotjHY0M0pjRYxtGj4VFKLPohQlFQyy4Qipc0XG9pS+CP/2Q==',
                txn_id = 'a825f76b-0696-40f3-864c-5a3a5b389a83'
            )
        else:
            return CreateHealthIdWithPreVerifiedRequest(
        )
        """

    def testCreateHealthIdWithPreVerifiedRequest(self):
        """Test CreateHealthIdWithPreVerifiedRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
