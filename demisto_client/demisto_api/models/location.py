# coding: utf-8

"""
    Demisto API

    This is the public REST API to integrate with the demisto server. HTTP request can be sent using any HTTP-client.  For an example dedicated client take a look at: https://github.com/demisto/demisto-py.  Requests must include API-key that can be generated in the Demisto web client under 'Settings' -> 'Integrations' -> 'API keys'   Optimistic Locking and Versioning\\:  When using Demisto REST API, you will need to make sure to work on the latest version of the item (incident, entry, etc.), otherwise, you will get a DB version error (which not allow you to override a newer item). In addition, you can pass 'version\\: -1' to force data override (make sure that other users data might be lost).  Assume that Alice and Bob both read the same data from Demisto server, then they both changed the data, and then both tried to write the new versions back to the server. Whose changes should be saved? Alice’s? Bob’s? To solve this, each data item in Demisto has a numeric incremental version. If Alice saved an item with version 4 and Bob trying to save the same item with version 3, Demisto will rollback Bob request and returns a DB version conflict error. Bob will need to get the latest item and work on it so Alice work will not get lost.  Example request using 'curl'\\:  ``` curl 'https://hostname:443/incidents/search' -H 'content-type: application/json' -H 'accept: application/json' -H 'Authorization: <API Key goes here>' --data-binary '{\"filter\":{\"query\":\"-status:closed -category:job\",\"period\":{\"by\":\"day\",\"fromValue\":7}}}' --compressed ```  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from demisto_client.demisto_api.models.array_positions import ArrayPositions  # noqa: F401,E501


class Location(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'array_positions': 'ArrayPositions',
        'end': 'int',
        'pos': 'int',
        'start': 'int'
    }

    attribute_map = {
        'array_positions': 'array_positions',
        'end': 'end',
        'pos': 'pos',
        'start': 'start'
    }

    def __init__(self, array_positions=None, end=None, pos=None, start=None):  # noqa: E501
        """Location - a model defined in Swagger"""  # noqa: E501

        self._array_positions = None
        self._end = None
        self._pos = None
        self._start = None
        self.discriminator = None

        if array_positions is not None:
            self.array_positions = array_positions
        if end is not None:
            self.end = end
        if pos is not None:
            self.pos = pos
        if start is not None:
            self.start = start

    @property
    def array_positions(self):
        """Gets the array_positions of this Location.  # noqa: E501


        :return: The array_positions of this Location.  # noqa: E501
        :rtype: ArrayPositions
        """
        return self._array_positions

    @array_positions.setter
    def array_positions(self, array_positions):
        """Sets the array_positions of this Location.


        :param array_positions: The array_positions of this Location.  # noqa: E501
        :type: ArrayPositions
        """

        self._array_positions = array_positions

    @property
    def end(self):
        """Gets the end of this Location.  # noqa: E501


        :return: The end of this Location.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this Location.


        :param end: The end of this Location.  # noqa: E501
        :type: int
        """

        self._end = end

    @property
    def pos(self):
        """Gets the pos of this Location.  # noqa: E501

        Pos is the position of the term within the field, starting at 1  # noqa: E501

        :return: The pos of this Location.  # noqa: E501
        :rtype: int
        """
        return self._pos

    @pos.setter
    def pos(self, pos):
        """Sets the pos of this Location.

        Pos is the position of the term within the field, starting at 1  # noqa: E501

        :param pos: The pos of this Location.  # noqa: E501
        :type: int
        """

        self._pos = pos

    @property
    def start(self):
        """Gets the start of this Location.  # noqa: E501

        Start and End are the byte offsets of the term in the field  # noqa: E501

        :return: The start of this Location.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this Location.

        Start and End are the byte offsets of the term in the field  # noqa: E501

        :param start: The start of this Location.  # noqa: E501
        :type: int
        """

        self._start = start

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Location, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Location):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
