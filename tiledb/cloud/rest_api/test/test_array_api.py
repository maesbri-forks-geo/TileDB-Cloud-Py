# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import rest_api
from tiledb.cloud.rest_api.api.array_api import ArrayApi  # noqa: E501
from tiledb.cloud.rest_api.rest import ApiException


class TestArrayApi(unittest.TestCase):
    """ArrayApi unit test stubs"""

    def setUp(self):
        self.api = tiledb.cloud.rest_api.api.array_api.ArrayApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_array_activity_log(self):
        """Test case for array_activity_log

        """
        pass

    def test_create_array(self):
        """Test case for create_array

        """
        pass

    def test_delete_array(self):
        """Test case for delete_array

        """
        pass

    def test_deregister_array(self):
        """Test case for deregister_array

        """
        pass

    def test_get_all_array_metadata(self):
        """Test case for get_all_array_metadata

        """
        pass

    def test_get_array(self):
        """Test case for get_array

        """
        pass

    def test_get_array_max_buffer_sizes(self):
        """Test case for get_array_max_buffer_sizes

        """
        pass

    def test_get_array_metadata(self):
        """Test case for get_array_metadata

        """
        pass

    def test_get_array_non_empty_domain(self):
        """Test case for get_array_non_empty_domain

        """
        pass

    def test_get_array_sample_data(self):
        """Test case for get_array_sample_data

        """
        pass

    def test_get_array_sharing_policies(self):
        """Test case for get_array_sharing_policies

        """
        pass

    def test_get_arrays_in_namespace(self):
        """Test case for get_arrays_in_namespace

        """
        pass

    def test_get_last_accessed_arrays(self):
        """Test case for get_last_accessed_arrays

        """
        pass

    def test_register_array(self):
        """Test case for register_array

        """
        pass

    def test_share_array(self):
        """Test case for share_array

        """
        pass

    def test_update_array_metadata(self):
        """Test case for update_array_metadata

        """
        pass


if __name__ == "__main__":
    unittest.main()
