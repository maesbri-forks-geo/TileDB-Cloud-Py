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


class Array(object):
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
    openapi_types = {"timestamp": "float", "query_type": "Querytype", "uri": "str"}

    attribute_map = {"timestamp": "timestamp", "query_type": "queryType", "uri": "uri"}

    def __init__(self, timestamp=None, query_type=None, uri=None):  # noqa: E501
        """Array - a model defined in OpenAPI"""  # noqa: E501

        self._timestamp = None
        self._query_type = None
        self._uri = None
        self.discriminator = None

        self.timestamp = timestamp
        self.query_type = query_type
        self.uri = uri

    @property
    def timestamp(self):
        """Gets the timestamp of this Array.  # noqa: E501

        timestamp (epoch milliseconds) array is opened at  # noqa: E501

        :return: The timestamp of this Array.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Array.

        timestamp (epoch milliseconds) array is opened at  # noqa: E501

        :param timestamp: The timestamp of this Array.  # noqa: E501
        :type: float
        """
        if timestamp is None:
            raise ValueError(
                "Invalid value for `timestamp`, must not be `None`"
            )  # noqa: E501

        self._timestamp = timestamp

    @property
    def query_type(self):
        """Gets the query_type of this Array.  # noqa: E501


        :return: The query_type of this Array.  # noqa: E501
        :rtype: Querytype
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this Array.


        :param query_type: The query_type of this Array.  # noqa: E501
        :type: Querytype
        """
        if query_type is None:
            raise ValueError(
                "Invalid value for `query_type`, must not be `None`"
            )  # noqa: E501

        self._query_type = query_type

    @property
    def uri(self):
        """Gets the uri of this Array.  # noqa: E501

        Array uri  # noqa: E501

        :return: The uri of this Array.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Array.

        Array uri  # noqa: E501

        :param uri: The uri of this Array.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError(
                "Invalid value for `uri`, must not be `None`"
            )  # noqa: E501

        self._uri = uri

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
        if not isinstance(other, Array):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
