import psycopg2
import database
class User(object):
    def __init__(self):
        self.pg = database.database()
        self.pg.connect()

    def __del__(self):
        self.pg.close()

    def getUser(self, uid=None, email=None):
        cur = self.pg.getCursor()

        if uid != None:
            sql = """SELECT uid, name, email, phone, major, degree FROM yacs_user_system.public.users WHERE uid = %s"""
            arg = (str(uid),)
        else:
            sql = """SELECT uid, name, email, phone, major, degree FROM yacs_user_system.public.users WHERE email = %s"""
            arg = (str(email),)
        try:
            cur.execute(sql,arg)
        except psycopg2.Error as e:
            print(e)
            return None
        return cur.fetchall()

    def addUser(self,name,email,phone,password,major,degree):
        sql = """INSERT INTO yacs_user_system.public.users (name, email, phone, password, major, degree) VALUES (%s, %s, %s, %s, %s, %s)"""
        cur = self.pg.getCursor()
        try:
            cur.execute(sql,(name,email,phone,password,major,degree))
            self.pg.commit()
        except psycopg2.Error as e:
            print(e)
            return None
        return 0





