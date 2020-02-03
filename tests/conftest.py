from pytest_postgresql import factories

from database import database

from config import DB_NAME

factories.postgresql('test_postgresql', DB_NAME)

class TestDatabase(database):
    def connect(self, postgresql):
        self.conn = postgresql
    




