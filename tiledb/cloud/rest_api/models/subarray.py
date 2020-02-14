# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 1.5.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Subarray(object):
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
    openapi_types = {"layout": "Layout", "ranges": "list[SubarrayRanges]"}

    attribute_map = {"layout": "layout", "ranges": "ranges"}

    def __init__(self, layout=None, ranges=None):  # noqa: E501
        """Subarray - a model defined in OpenAPI"""  # noqa: E501

        self._layout = None
        self._ranges = None
        self.discriminator = None

        if layout is not None:
            self.layout = layout
        if ranges is not None:
            self.ranges = ranges

    @property
    def layout(self):
        """Gets the layout of this Subarray.  # noqa: E501


        :return: The layout of this Subarray.  # noqa: E501
        :rtype: Layout
        """
        return self._layout

    @layout.setter
    def layout(self, layout):
        """Sets the layout of this Subarray.


        :param layout: The layout of this Subarray.  # noqa: E501
        :type: Layout
        """

        self._layout = layout

    @property
    def ranges(self):
        """Gets the ranges of this Subarray.  # noqa: E501

        List of 1D ranges, one per dimension  # noqa: E501

        :return: The ranges of this Subarray.  # noqa: E501
        :rtype: list[SubarrayRanges]
        """
        return self._ranges

    @ranges.setter
    def ranges(self, ranges):
        """Sets the ranges of this Subarray.

        List of 1D ranges, one per dimension  # noqa: E501

        :param ranges: The ranges of this Subarray.  # noqa: E501
        :type: list[SubarrayRanges]
        """

        self._ranges = ranges

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
        if not isinstance(other, Subarray):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
