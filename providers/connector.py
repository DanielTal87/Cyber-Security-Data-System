from uuid import uuid4


class Connector:
    def __init__(self, source, payload):
        self.__id = str(uuid4())[:8]
        self.__source = source
        self.__payload = payload

    @property
    def id(self):
        return self.__id

    @property
    def source(self):
        return self.__source

    @property
    def payload(self):
        return self.__payload

    def __str__(self) -> str:
        return (
            f'Connector: '
            f'source = {self.source}, '
            f'payload = {self.payload}, '
        )

    def __repr__(self) -> str:
        return super().__str__()
