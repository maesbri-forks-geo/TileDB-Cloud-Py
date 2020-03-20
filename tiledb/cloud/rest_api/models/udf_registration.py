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


class UDFRegistration(object):
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
        "name": "str",
        "language": "UDFLanguage",
        "version": "str",
        "image_name": "str",
        "type": "UDFType",
        "_exec": "str",
        "exec_raw": "str",
        "readme": "str",
    }

    attribute_map = {
        "name": "name",
        "language": "language",
        "version": "version",
        "image_name": "image_name",
        "type": "type",
        "_exec": "exec",
        "exec_raw": "exec_raw",
        "readme": "readme",
    }

    def __init__(
        self,
        name=None,
        language=None,
        version=None,
        image_name=None,
        type=None,
        _exec=None,
        exec_raw=None,
        readme=None,
    ):  # noqa: E501
        """UDFRegistration - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._language = None
        self._version = None
        self._image_name = None
        self._type = None
        self.__exec = None
        self._exec_raw = None
        self._readme = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if language is not None:
            self.language = language
        if version is not None:
            self.version = version
        if image_name is not None:
            self.image_name = image_name
        if type is not None:
            self.type = type
        if _exec is not None:
            self._exec = _exec
        if exec_raw is not None:
            self.exec_raw = exec_raw
        if readme is not None:
            self.readme = readme

    @property
    def name(self):
        """Gets the name of this UDFRegistration.  # noqa: E501

        name of udf  # noqa: E501

        :return: The name of this UDFRegistration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UDFRegistration.

        name of udf  # noqa: E501

        :param name: The name of this UDFRegistration.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def language(self):
        """Gets the language of this UDFRegistration.  # noqa: E501


        :return: The language of this UDFRegistration.  # noqa: E501
        :rtype: UDFLanguage
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this UDFRegistration.


        :param language: The language of this UDFRegistration.  # noqa: E501
        :type: UDFLanguage
        """

        self._language = language

    @property
    def version(self):
        """Gets the version of this UDFRegistration.  # noqa: E501

        Type-specific version  # noqa: E501

        :return: The version of this UDFRegistration.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UDFRegistration.

        Type-specific version  # noqa: E501

        :param version: The version of this UDFRegistration.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def image_name(self):
        """Gets the image_name of this UDFRegistration.  # noqa: E501

        Docker image name to use for udf  # noqa: E501

        :return: The image_name of this UDFRegistration.  # noqa: E501
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this UDFRegistration.

        Docker image name to use for udf  # noqa: E501

        :param image_name: The image_name of this UDFRegistration.  # noqa: E501
        :type: str
        """

        self._image_name = image_name

    @property
    def type(self):
        """Gets the type of this UDFRegistration.  # noqa: E501


        :return: The type of this UDFRegistration.  # noqa: E501
        :rtype: UDFType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UDFRegistration.


        :param type: The type of this UDFRegistration.  # noqa: E501
        :type: UDFType
        """

        self._type = type

    @property
    def _exec(self):
        """Gets the _exec of this UDFRegistration.  # noqa: E501

        Type-specific executable text  # noqa: E501

        :return: The _exec of this UDFRegistration.  # noqa: E501
        :rtype: str
        """
        return self.__exec

    @_exec.setter
    def _exec(self, _exec):
        """Sets the _exec of this UDFRegistration.

        Type-specific executable text  # noqa: E501

        :param _exec: The _exec of this UDFRegistration.  # noqa: E501
        :type: str
        """

        self.__exec = _exec

    @property
    def exec_raw(self):
        """Gets the exec_raw of this UDFRegistration.  # noqa: E501

        optional raw text to store of serialized function, used for showing in UI  # noqa: E501

        :return: The exec_raw of this UDFRegistration.  # noqa: E501
        :rtype: str
        """
        return self._exec_raw

    @exec_raw.setter
    def exec_raw(self, exec_raw):
        """Sets the exec_raw of this UDFRegistration.

        optional raw text to store of serialized function, used for showing in UI  # noqa: E501

        :param exec_raw: The exec_raw of this UDFRegistration.  # noqa: E501
        :type: str
        """

        self._exec_raw = exec_raw

    @property
    def readme(self):
        """Gets the readme of this UDFRegistration.  # noqa: E501

        Markdown readme of udfs  # noqa: E501

        :return: The readme of this UDFRegistration.  # noqa: E501
        :rtype: str
        """
        return self._readme

    @readme.setter
    def readme(self, readme):
        """Sets the readme of this UDFRegistration.

        Markdown readme of udfs  # noqa: E501

        :param readme: The readme of this UDFRegistration.  # noqa: E501
        :type: str
        """

        self._readme = readme

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
        if not isinstance(other, UDFRegistration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other