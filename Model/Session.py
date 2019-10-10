from Model.Model import *
import uuid

class Session(Model):
    def __init__(self):
        super().__init__()

    def createSessionID(self):
        return str(uuid.uuid1())

    def startSession(self, session, uid, startTime):
        cur = self.pg.getCursor()
        sql = """INSERT INTO yacs_user_system.public.sessions (sessionid, uid, start_time) VALUES (%s,%s,%s);"""
        args = (session,uid,startTime)
        try:
            cur.execute(sql,args)
            self.pg.commit()
        except psycopg2.Error as e:
            print(e)
            return None
        return 0


    def getSession(self,sessionID='%'):
        cur = self.pg.getCursor()
        sql = """   SELECT sessionid, uid, start_time,end_time 
                    FROM yacs_user_system.public.sessions 
                    WHERE   sessionid::text LIKE %s"""

        arg = (sessionID,)
        try:
            cur.execute(sql,arg)
        except psycopg2.Error as e:
            print(e)
            return None
        return cur.fetchall()

    def endSession(self,sessionID,endTime):
        cur = self.pg.getCursor()
        sql = """UPDATE yacs_user_system.public.sessions SET end_time = %s WHERE sessionid::text LIKE %s;"""
        args = (endTime,sessionID)

        try:
            cur.execute(sql,args)
            self.pg.commit()
        except psycopg2.Error as e:
            print(e)
            return None
        return 0