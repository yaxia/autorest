# coding=utf-8
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UsageName(Model):
    """
    The Usage Names.

    :param value: Gets a string describing the resource name.
    :type value: str
    :param localized_value: Gets a localized string describing the resource
     name.
    :type localized_value: str
    """ 

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'localized_value': {'key': 'localizedValue', 'type': 'str'},
    }

    def __init__(self, value=None, localized_value=None, **kwargs):
        self.value = value
        self.localized_value = localized_value
