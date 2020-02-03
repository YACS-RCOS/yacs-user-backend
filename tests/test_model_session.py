from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid1

from typing import List, Optional
from psycopg2.extensions import connection

from Model.Session import Session
from .conftest import TestDatabase

# Session model attributes 
@dataclass
class SessionModel:
    sessionid: str
    uid: int
    start_time: datetime 
    end_time: Optional[datetime]

# Dummy data
sessions: List[SessionModel] = [
    SessionModel(str(uuid1()), i, datetime(2000 + i, i, i, i, i, i, i, timezone.utc), None) for i in range(1, 9)
]

# Put unit tests here
def test_start_session(test_session: Session) -> None:
    s: SessionModel = sessions[0]

    assert test_session.startSession(s.sessionid, s.uid, s.start_time) == 0



