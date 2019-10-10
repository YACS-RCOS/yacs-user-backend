from Model.Model import *
import uuid
from datetime import datetime
class Session(Model):
    def __init__(self):
        super().__init__()


    def createSessionID(self):
        return str(uuid.uuid1())

    def appendSession(self, session, uid):
        timestamp = datetime.utcnow()
        cur = self.pg.getCursor()
        sql = """INSERT INTO yacs_user_system.public.sessions (sessionid, uid, start_time) VALUES (%s,%s,%s);"""
        args = (session,uid,timestamp)
        try:
            cur.execute(sql,args)
            self.pg.commit()
        except psycopg2.Error as e:
            print(e)
            return None
        return 0


    def checkSession(self,sessionID):
        pass

