from Model.Model import *
import uuid
class Session(Model):
    def __init__(self):
        super().__init__()


    def createSessionID(self):
        return uuid.uuid1()

    def saveSession(self,session,uid):
        cur = self.pg.getCursor()
        sql = """INSERT INTO yacs_user_system.public.sessions (sessionid, uid) VALUES (%s,%s);"""
        args = (session,uid)
        try:
            cur.execute(sql,args)
            self.pg.commit()
        except psycopg2.Error as e:
            print(e)
            return None
        return 0


    def checkSession(self,sessionID):
        pass

