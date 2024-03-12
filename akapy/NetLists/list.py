from ..auth import Auth
from ..requester import Requester
from typing import List, Literal, Dict


class Lists:
    def __init__(self, auth=None) -> None:
        """
        Initialize Lists class

        Args:
            auth (Auth, optional): Authentication object. If not provided, will use Auth()
        """
        if auth is None:
            self.auth = Auth()
        else:
            self.auth = auth

        self.base_endpoint = "network-list/v2"
        self.requester = Requester(self.auth.get_session(), self.auth.host_url)

    def list_all(
        self,
        search: str | List[str] = "",
        elements: bool = False,
        extended: bool = False,
        type: Literal["IP", "GEO"] = "IP",
    ) -> Dict:
        """
        Get all lists

        Args:
            search (str|List[str]): Search term
            elements (bool): Include list elements
            extended (bool): Include additional fields
            type (Literal["IP", "GEO"]): List type

        Returns:
            dict: API response
        """

        params = {}
        if search:
            params["search"] = search
        params["includeElements"] = str(elements).lower()
        params["extended"] = str(extended).lower()
        params["listType"] = type

        return self.requester(
            endpoint=f"{self.base_endpoint}/network-lists", method="GET", params=params
        )
