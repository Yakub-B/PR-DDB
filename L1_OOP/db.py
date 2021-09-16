from typing import List

from L1_OOP.config import DB_URL
from L1_OOP.fixtures import user2, user1
from L1_OOP.models import UserModel


class DataBase:
    """
    Mocks actual database
    """

    _db_url: str
    _users: List[UserModel]

    def __init__(self):
        self._db_url = DB_URL
        self._users = [UserModel(**user1), UserModel(**user2)]

    def _connect(self):
        """
        DB connection mock
        """

    def _insert_entry(self, **data):
        self._connect()
        self._users.append(UserModel(**data))
        # do something with data

    def create_user(self, userdata: dict):
        self._insert_entry(**userdata)

    def get_user(self, pk: int) -> UserModel:
        self._connect()
        # some logic here
        user = next(u for u in self._users if u.pk == pk)
        return user
