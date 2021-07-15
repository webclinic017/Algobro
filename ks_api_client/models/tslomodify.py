# coding: utf-8

import pprint
import re  # noqa: F401

import six

from ks_api_client.configuration import Configuration


class Tslomodify(object):
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
        'orderIndicator': 'int',
        'spread': 'float',
        'trailingPrice': 'float'
    }

    attribute_map = {
        'orderIndicator': 'orderIndicator',
        'spread': 'spread',
        'trailingPrice': 'trailingPrice'
    }

    def __init__(self, orderIndicator=None, spread=None, trailingPrice=None, local_vars_configuration=None):  # noqa: E501
        """Tslomodify - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._orderIndicator = None
        self._spread = None
        self._trailingPrice = None
        self.discriminator = None

        if orderIndicator is not None:
            self.orderIndicator = orderIndicator
        if spread is not None:
            self.spread = spread
        if trailingPrice is not None:
            self.trailingPrice = trailingPrice

    @property
    def orderIndicator(self):
        """Gets the orderIndicator of this Tslomodify.  # noqa: E501

        Order Indicator to modify Order  # noqa: E501

        :return: The orderIndicator of this Tslomodify.  # noqa: E501
        :rtype: int
        """
        return self._orderIndicator

    @orderIndicator.setter
    def orderIndicator(self, orderIndicator):
        """Sets the orderIndicator of this Tslomodify.

        Order Indicator to modify Order  # noqa: E501

        :param orderIndicator: The orderIndicator of this Tslomodify.  # noqa: E501
        :type orderIndicator: int
        """

        self._orderIndicator = orderIndicator

    @property
    def spread(self):
        """Gets the spread of this Tslomodify.  # noqa: E501

        Spread of the order  # noqa: E501

        :return: The spread of this Tslomodify.  # noqa: E501
        :rtype: float
        """
        return self._spread

    @spread.setter
    def spread(self, spread):
        """Sets the spread of this Tslomodify.

        Spread of the order  # noqa: E501

        :param spread: The spread of this Tslomodify.  # noqa: E501
        :type spread: float
        """

        self._spread = spread

    @property
    def trailingPrice(self):
        """Gets the trailingPrice of this Tslomodify.  # noqa: E501

        Triling price of TSLO Order.  # noqa: E501

        :return: The trailingPrice of this Tslomodify.  # noqa: E501
        :rtype: float
        """
        return self._trailingPrice

    @trailingPrice.setter
    def trailingPrice(self, trailingPrice):
        """Sets the trailingPrice of this Tslomodify.

        Triling price of TSLO Order.  # noqa: E501

        :param trailingPrice: The trailingPrice of this Tslomodify.  # noqa: E501
        :type trailingPrice: float
        """

        self._trailingPrice = trailingPrice

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
        if not isinstance(other, Tslomodify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Tslomodify):
            return True

        return self.to_dict() != other.to_dict()
