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

from demisto_client.demisto_api.models.module_args import ModuleArgs  # noqa: F401,E501


class ReportAutomation(object):
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
        'args': 'ModuleArgs',
        'id': 'str',
        'name': 'str',
        'no_event': 'bool'
    }

    attribute_map = {
        'args': 'args',
        'id': 'id',
        'name': 'name',
        'no_event': 'noEvent'
    }

    def __init__(self, args=None, id=None, name=None, no_event=None):  # noqa: E501
        """ReportAutomation - a model defined in Swagger"""  # noqa: E501

        self._args = None
        self._id = None
        self._name = None
        self._no_event = None
        self.discriminator = None

        if args is not None:
            self.args = args
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if no_event is not None:
            self.no_event = no_event

    @property
    def args(self):
        """Gets the args of this ReportAutomation.  # noqa: E501


        :return: The args of this ReportAutomation.  # noqa: E501
        :rtype: ModuleArgs
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this ReportAutomation.


        :param args: The args of this ReportAutomation.  # noqa: E501
        :type: ModuleArgs
        """

        self._args = args

    @property
    def id(self):
        """Gets the id of this ReportAutomation.  # noqa: E501


        :return: The id of this ReportAutomation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReportAutomation.


        :param id: The id of this ReportAutomation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ReportAutomation.  # noqa: E501


        :return: The name of this ReportAutomation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportAutomation.


        :param name: The name of this ReportAutomation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def no_event(self):
        """Gets the no_event of this ReportAutomation.  # noqa: E501


        :return: The no_event of this ReportAutomation.  # noqa: E501
        :rtype: bool
        """
        return self._no_event

    @no_event.setter
    def no_event(self, no_event):
        """Sets the no_event of this ReportAutomation.


        :param no_event: The no_event of this ReportAutomation.  # noqa: E501
        :type: bool
        """

        self._no_event = no_event

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
        if issubclass(ReportAutomation, dict):
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
        if not isinstance(other, ReportAutomation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other