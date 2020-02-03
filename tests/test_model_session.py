from dataclasses import dataclass
from datetime import time, timezone

from typing import List, Optional

from Model.Session import Session
from .conftest import TestDatabase

@dataclass
class SessionModel:
    sessionid: str
    uid: int
    start_time: time
    end_time: Optional[time]

sessions: List[SessionModel] = [
    SessionModel(("{0}"*6+("-"+"{0}"*3)*4+"{0}").format(i), i, time(i, i, i, i, timezone.utc), None) for i in range(9)
]

def test_start_session(postgresql) -> None:
    db: TestSession = TestSession()
    s: SessionModel = sessions[0]

    assert db.startSession(s.sessionid, s.uid, s.start_time) == 0


class TestSession(Session):
    def __init__(self, db):
        self.pg = TestDatabase()
        self.pg.connect(db)
