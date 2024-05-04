# coding: utf-8

"""
    Gateway

    Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing 

    The version of the OpenAPI document: 0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abdm_gateway.api.monitoring_api import MonitoringApi


class TestMonitoringApi(unittest.TestCase):
    """MonitoringApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MonitoringApi()

    def tearDown(self) -> None:
        pass

    def test_v05_heartbeat_get(self) -> None:
        """Test case for v05_heartbeat_get

        Informs about server status
        """
        pass


if __name__ == '__main__':
    unittest.main()
