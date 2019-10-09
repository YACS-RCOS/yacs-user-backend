import psycopg2
from config import *


class postgres(object):
    def __init__(self):
        self.connect_str = "dbname='{}' user='{}' host='{}' password='{}'".format(DB_NAME, DB_USER, DB_HOST,
                                                                                  DB_PASSWORD)
        self.connect()
        self.close()

    def connect(self):
        try:
            self.conn = psycopg2.connect(self.connect_str)
        except:
            print("Fail to connect to database.")

    def close(self):
        self.conn.close()

    def getCursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()


class DB(object):
    def __init__(self):
        self.pg = postgres()
        self.pg.connect()

    def __del__(self):
        self.pg.close()

    def getUser(self, uid=None, email=None):
        if not uid and not email:
            return None
        cur = self.pg.getCursor()
        if uid != None:
            sql = """SELECT uid, name, email, phone, password, major, degree FROM yacs_user_system.public.users WHERE uid = %s""" % str(uid)
        else:
            sql = """SELECT uid, name, email, phone, password, major, degree FROM yacs_user_system.public.users WHERE email = '%s'""" % str(email)
        try:
            cur.execute(sql)
        except psycopg2.DatabaseError as e:
            print(e)
        return cur.fetchall()

    def addUser(self,name,email,phone,password,major,degree):
        sql = """INSERT INTO yacs_user_system.public.users (name, email, phone, password, major, degree) VALUES (%s, %s, %s, %s, %s, %s)"""
        cur = self.pg.getCursor()
        cur.execute(sql,(name,email,phone,password,major,degree))
        self.pg.commit()