# coding: utf-8

import pprint
import re  # noqa: F401

import six

from ks_api_client.configuration import Configuration


class UserDetails(object):
    """
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'userid': 'str',
        'accessCode': 'str'
    }

    attribute_map = {
        'userid': 'userid',
        'accessCode': 'accessCode'
    }

    def __init__(self, userid=None, accessCode=None, local_vars_configuration=None):  # noqa: E501
        """UserDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._userid = None
        self._accessCode = None
        self.discriminator = None

        if userid is not None:
            self.userid = userid
        if accessCode is not None:
            self.accessCode = accessCode

    @property
    def userid(self):
        """Gets the userid of this UserDetails.  # noqa: E501

        Userid for which  access code validation  # noqa: E501

        :return: The userid of this UserDetails.  # noqa: E501
        :rtype: str
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """Sets the userid of this UserDetails.

        Userid for which  access code validation  # noqa: E501

        :param userid: The userid of this UserDetails.  # noqa: E501
        :type userid: str
        """

        self._userid = userid

    @property
    def accessCode(self):
        """Gets the accessCode of this UserDetails.  # noqa: E501

        Login access code received on email and mobile no  # noqa: E501

        :return: The accessCode of this UserDetails.  # noqa: E501
        :rtype: str
        """
        return self._accessCode

    @accessCode.setter
    def accessCode(self, accessCode):
        """Sets the accessCode of this UserDetails.

        Login access code received on email and mobile no  # noqa: E501

        :param accessCode: The accessCode of this UserDetails.  # noqa: E501
        :type accessCode: str
        """

        self._accessCode = accessCode

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
        if not isinstance(other, UserDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserDetails):
            return True

        return self.to_dict() != other.to_dict()
