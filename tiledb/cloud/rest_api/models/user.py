# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 1.3.13
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class User(object):
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
        "id": "str",
        "username": "str",
        "password": "str",
        "name": "str",
        "email": "str",
        "is_valid_email": "bool",
        "logo": "str",
        "last_activity_date": "datetime",
        "timezone": "str",
        "organizations": "list[OrganizationUser]",
        "allowed_actions": "list[NamespaceActions]",
    }

    attribute_map = {
        "id": "id",
        "username": "username",
        "password": "password",
        "name": "name",
        "email": "email",
        "is_valid_email": "is_valid_email",
        "logo": "logo",
        "last_activity_date": "last_activity_date",
        "timezone": "timezone",
        "organizations": "organizations",
        "allowed_actions": "allowed_actions",
    }

    def __init__(
        self,
        id=None,
        username=None,
        password=None,
        name=None,
        email=None,
        is_valid_email=None,
        logo=None,
        last_activity_date=None,
        timezone=None,
        organizations=None,
        allowed_actions=None,
    ):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._username = None
        self._password = None
        self._name = None
        self._email = None
        self._is_valid_email = None
        self._logo = None
        self._last_activity_date = None
        self._timezone = None
        self._organizations = None
        self._allowed_actions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.username = username
        if password is not None:
            self.password = password
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if is_valid_email is not None:
            self.is_valid_email = is_valid_email
        if logo is not None:
            self.logo = logo
        if last_activity_date is not None:
            self.last_activity_date = last_activity_date
        if timezone is not None:
            self.timezone = timezone
        if organizations is not None:
            self.organizations = organizations
        if allowed_actions is not None:
            self.allowed_actions = allowed_actions

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501

        unique id of user  # noqa: E501

        :return: The id of this User.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        unique id of user  # noqa: E501

        :param id: The id of this User.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this User.  # noqa: E501

        username must be unique  # noqa: E501

        :return: The username of this User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.

        username must be unique  # noqa: E501

        :param username: The username of this User.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError(
                "Invalid value for `username`, must not be `None`"
            )  # noqa: E501
        if username is not None and len(username) > 20:
            raise ValueError(
                "Invalid value for `username`, length must be less than or equal to `20`"
            )  # noqa: E501
        if username is not None and len(username) < 4:
            raise ValueError(
                "Invalid value for `username`, length must be greater than or equal to `4`"
            )  # noqa: E501
        if username is not None and not re.search(
            r"^[\w.\-]+$", username
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `username`, must be a follow pattern or equal to `/^[\w.\-]+$/`"
            )  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this User.  # noqa: E501

        password  # noqa: E501

        :return: The password of this User.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this User.

        password  # noqa: E501

        :param password: The password of this User.  # noqa: E501
        :type: str
        """
        if password is not None and len(password) < 8:
            raise ValueError(
                "Invalid value for `password`, length must be greater than or equal to `8`"
            )  # noqa: E501

        self._password = password

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501

        the user's full, real name  # noqa: E501

        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.

        the user's full, real name  # noqa: E501

        :param name: The name of this User.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) < 1:
            raise ValueError(
                "Invalid value for `name`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._name = name

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501

        the user's email  # noqa: E501

        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        the user's email  # noqa: E501

        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def is_valid_email(self):
        """Gets the is_valid_email of this User.  # noqa: E501

        user's email is validated to be correct  # noqa: E501

        :return: The is_valid_email of this User.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid_email

    @is_valid_email.setter
    def is_valid_email(self, is_valid_email):
        """Sets the is_valid_email of this User.

        user's email is validated to be correct  # noqa: E501

        :param is_valid_email: The is_valid_email of this User.  # noqa: E501
        :type: bool
        """

        self._is_valid_email = is_valid_email

    @property
    def logo(self):
        """Gets the logo of this User.  # noqa: E501

        the user's logo  # noqa: E501

        :return: The logo of this User.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this User.

        the user's logo  # noqa: E501

        :param logo: The logo of this User.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def last_activity_date(self):
        """Gets the last_activity_date of this User.  # noqa: E501

        when the user last logged in (set by the server)  # noqa: E501

        :return: The last_activity_date of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._last_activity_date

    @last_activity_date.setter
    def last_activity_date(self, last_activity_date):
        """Sets the last_activity_date of this User.

        when the user last logged in (set by the server)  # noqa: E501

        :param last_activity_date: The last_activity_date of this User.  # noqa: E501
        :type: datetime
        """

        self._last_activity_date = last_activity_date

    @property
    def timezone(self):
        """Gets the timezone of this User.  # noqa: E501


        :return: The timezone of this User.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this User.


        :param timezone: The timezone of this User.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def organizations(self):
        """Gets the organizations of this User.  # noqa: E501

        Array of organizations a user is part of and their roles  # noqa: E501

        :return: The organizations of this User.  # noqa: E501
        :rtype: list[OrganizationUser]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this User.

        Array of organizations a user is part of and their roles  # noqa: E501

        :param organizations: The organizations of this User.  # noqa: E501
        :type: list[OrganizationUser]
        """

        self._organizations = organizations

    @property
    def allowed_actions(self):
        """Gets the allowed_actions of this User.  # noqa: E501

        list of actions user is allowed to do on this organization  # noqa: E501

        :return: The allowed_actions of this User.  # noqa: E501
        :rtype: list[NamespaceActions]
        """
        return self._allowed_actions

    @allowed_actions.setter
    def allowed_actions(self, allowed_actions):
        """Sets the allowed_actions of this User.

        list of actions user is allowed to do on this organization  # noqa: E501

        :param allowed_actions: The allowed_actions of this User.  # noqa: E501
        :type: list[NamespaceActions]
        """

        self._allowed_actions = allowed_actions

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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
