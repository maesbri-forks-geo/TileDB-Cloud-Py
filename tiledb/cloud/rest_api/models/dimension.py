# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 0.6.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Dimension(object):
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
        'name': 'str',
        'type': 'Datatype',
        'domain': 'DomainArray',
        'null_tile_extent': 'bool',
        'tile_extent': 'DimensionTileExtent'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'domain': 'domain',
        'null_tile_extent': 'nullTileExtent',
        'tile_extent': 'tileExtent'
    }

    def __init__(self, name=None, type=None, domain=None, null_tile_extent=None, tile_extent=None):  # noqa: E501
        """Dimension - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._type = None
        self._domain = None
        self._null_tile_extent = None
        self._tile_extent = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.type = type
        self.domain = domain
        self.null_tile_extent = null_tile_extent
        if tile_extent is not None:
            self.tile_extent = tile_extent

    @property
    def name(self):
        """Gets the name of this Dimension.  # noqa: E501

        Dimension name  # noqa: E501

        :return: The name of this Dimension.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Dimension.

        Dimension name  # noqa: E501

        :param name: The name of this Dimension.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Dimension.  # noqa: E501


        :return: The type of this Dimension.  # noqa: E501
        :rtype: Datatype
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Dimension.


        :param type: The type of this Dimension.  # noqa: E501
        :type: Datatype
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def domain(self):
        """Gets the domain of this Dimension.  # noqa: E501


        :return: The domain of this Dimension.  # noqa: E501
        :rtype: DomainArray
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Dimension.


        :param domain: The domain of this Dimension.  # noqa: E501
        :type: DomainArray
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def null_tile_extent(self):
        """Gets the null_tile_extent of this Dimension.  # noqa: E501

        Is tile extent null  # noqa: E501

        :return: The null_tile_extent of this Dimension.  # noqa: E501
        :rtype: bool
        """
        return self._null_tile_extent

    @null_tile_extent.setter
    def null_tile_extent(self, null_tile_extent):
        """Sets the null_tile_extent of this Dimension.

        Is tile extent null  # noqa: E501

        :param null_tile_extent: The null_tile_extent of this Dimension.  # noqa: E501
        :type: bool
        """
        if null_tile_extent is None:
            raise ValueError("Invalid value for `null_tile_extent`, must not be `None`")  # noqa: E501

        self._null_tile_extent = null_tile_extent

    @property
    def tile_extent(self):
        """Gets the tile_extent of this Dimension.  # noqa: E501


        :return: The tile_extent of this Dimension.  # noqa: E501
        :rtype: DimensionTileExtent
        """
        return self._tile_extent

    @tile_extent.setter
    def tile_extent(self, tile_extent):
        """Sets the tile_extent of this Dimension.


        :param tile_extent: The tile_extent of this Dimension.  # noqa: E501
        :type: DimensionTileExtent
        """

        self._tile_extent = tile_extent

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, Dimension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
