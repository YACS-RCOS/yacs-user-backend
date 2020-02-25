import psycopg2
from config import *


class database(object):
    def __init__(self):
        self.connect_str = "dbname='{}' user='{}' host='{}' password='{}'".format(DB_NAME, DB_USER, DB_HOST, DB_PASSWORD)
    def connect(self):
        try:
            self.conn = psycopg2.connect(self.connect_str)
        except psycopg2.Warning as w:
            print(str(w))
        except psycopg2.Error as e:
            print("class", str(e.__class__))
            print("pgerror", e.pgerror)
            print("pgcode", e.pgcode)
            print("pgcursor", e.cursor)
            print("msgprimary", e.diag.message_primary)
            print("msgdetail", e.diag.message_detail)
            print("msghint", e.diag.message_hint)
        finally:
            print("Fail to connect to database.\n" + self.connect_str)

    def close(self):
        self.conn.close()

    def execute(self,sql,args,isSELECT):
        cur = self.conn.cursor()
        try:
            if isSELECT:
                cur.execute(sql, args)
                ret = cur.fetchall()
            else:
                cur.execute(sql, args)
                ret = 0
                self.conn.commit()

        except psycopg2.Error as e:
            print(e)
            return None

        return ret