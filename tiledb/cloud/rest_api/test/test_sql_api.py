# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.0.4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import rest_api
from tiledb.cloud.rest_api.api.sql_api import SqlApi  # noqa: E501
from tiledb.cloud.rest_api.rest import ApiException


class TestSqlApi(unittest.TestCase):
    """SqlApi unit test stubs"""

    def setUp(self):
        self.api = tiledb.cloud.rest_api.api.sql_api.SqlApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_run_sql(self):
        """Test case for run_sql"""
        pass


if __name__ == "__main__":
    unittest.main()
