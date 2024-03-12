from ..auth import Auth
from ..requester import Requester


class Create:
    def __init__(self, auth=None) -> None:
        if auth is None:
            self.auth = Auth()
        else:
            self.auth = auth

        self.requester = Requester(self.auth.get_session(), self.auth.host_url)
        self.__main()

    def __main(self):
        self.__test()

    def __test(self):
        print("test")
