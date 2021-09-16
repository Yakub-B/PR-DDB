from L1_OOP.config import DB_URL
from L1_OOP.fixtures import user2
from L1_OOP.models import UserModel


class DataBase:
    """
    Mocks actual database
    """

    _db_url: str

    def __init__(self):
        self._db_url = DB_URL

    def _connect(self):
        """
        DB connection mock
        """

    def _insert_entry(self, **data):
        self._connect()
        # do something with data

    def create_user(self, userdata: dict):
        self._insert_entry(**userdata)

    def get_user(self, pk: int) -> UserModel:
        self._connect()
        # some logic here
        return UserModel(**user2)
