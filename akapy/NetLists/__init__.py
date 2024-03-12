"""
NetLists module
"""

from .create import Create
from .update import Update
from .list import Lists
from .delete import Delete


class NetLists:
    """
    NetLists class provides access to network list API functions
    """

    @staticmethod
    def get_all():
        """
        Get all network lists

        Returns:
            dict: API response
        """
        return Lists().list_all()
