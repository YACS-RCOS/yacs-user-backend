from pytest_postgresql import factories
import pytest

from psycopg2.extensions import connection

from database import database as Database
from Model.Session import Session

from config import DB_NAME

# Creates pytest fixture that injects connection to postgresql database
factories.postgresql_proc('test_postgresql', DB_NAME)

class TestDatabase(Database):
    def connect(self, postgresql: connection) -> None:
        self.conn = postgresql
 
class TestSession(Session):
    def __init__(self, db: Database) -> Session:
        self.pg = db 


# Creates pytest fixture for test session object and initializes session table
@pytest.fixture
def test_session(postgresql: connection) -> Session:
  test_db: Database = TestDatabase()
  test_db.connect(postgresql)
  test_db.conn.cursor().execute(open("sql/init_sessions.sql", "r").read())

  return TestSession(test_db)
