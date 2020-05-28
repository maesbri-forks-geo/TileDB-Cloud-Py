# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.0.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ArrayBrowserSidebar(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "namespaces": "list[str]",
        "result_count_for_all": "int",
        "result_count_by_namespace": "object",
    }

    attribute_map = {
        "namespaces": "namespaces",
        "result_count_for_all": "result_count_for_all",
        "result_count_by_namespace": "result_count_by_namespace",
    }

    def __init__(
        self, namespaces=None, result_count_for_all=None, result_count_by_namespace=None
    ):  # noqa: E501
        """ArrayBrowserSidebar - a model defined in OpenAPI"""  # noqa: E501

        self._namespaces = None
        self._result_count_for_all = None
        self._result_count_by_namespace = None
        self.discriminator = None

        if namespaces is not None:
            self.namespaces = namespaces
        if result_count_for_all is not None:
            self.result_count_for_all = result_count_for_all
        if result_count_by_namespace is not None:
            self.result_count_by_namespace = result_count_by_namespace

    @property
    def namespaces(self):
        """Gets the namespaces of this ArrayBrowserSidebar.  # noqa: E501

        list of all unique namespaces to display  # noqa: E501

        :return: The namespaces of this ArrayBrowserSidebar.  # noqa: E501
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this ArrayBrowserSidebar.

        list of all unique namespaces to display  # noqa: E501

        :param namespaces: The namespaces of this ArrayBrowserSidebar.  # noqa: E501
        :type: list[str]
        """

        self._namespaces = namespaces

    @property
    def result_count_for_all(self):
        """Gets the result_count_for_all of this ArrayBrowserSidebar.  # noqa: E501

        A count of \"all\" of category  # noqa: E501

        :return: The result_count_for_all of this ArrayBrowserSidebar.  # noqa: E501
        :rtype: int
        """
        return self._result_count_for_all

    @result_count_for_all.setter
    def result_count_for_all(self, result_count_for_all):
        """Sets the result_count_for_all of this ArrayBrowserSidebar.

        A count of \"all\" of category  # noqa: E501

        :param result_count_for_all: The result_count_for_all of this ArrayBrowserSidebar.  # noqa: E501
        :type: int
        """

        self._result_count_for_all = result_count_for_all

    @property
    def result_count_by_namespace(self):
        """Gets the result_count_by_namespace of this ArrayBrowserSidebar.  # noqa: E501

        A map that includes the result count by namespace  # noqa: E501

        :return: The result_count_by_namespace of this ArrayBrowserSidebar.  # noqa: E501
        :rtype: object
        """
        return self._result_count_by_namespace

    @result_count_by_namespace.setter
    def result_count_by_namespace(self, result_count_by_namespace):
        """Sets the result_count_by_namespace of this ArrayBrowserSidebar.

        A map that includes the result count by namespace  # noqa: E501

        :param result_count_by_namespace: The result_count_by_namespace of this ArrayBrowserSidebar.  # noqa: E501
        :type: object
        """

        self._result_count_by_namespace = result_count_by_namespace

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ArrayBrowserSidebar):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other