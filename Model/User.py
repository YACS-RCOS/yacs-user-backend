from Model.Model import *
class User(Model):
    def __init__(self):
        super().__init__()

    def getUser(self, name='%',email='%', password='%',phone='%',major='%',degree='%'):
        cur = self.pg.getCursor()


        sql = """   SELECT uid, name, email, phone,password,major,degree 
                    FROM yacs_user_system.public.users
                    WHERE   name        LIKE %s AND 
                            email       LIKE %s AND 
                            phone       LIKE %s AND 
                            password    LIKE %s AND 
                            major       LIKE %s AND 
                            degree      LIKE %s"""

        arg = (name,email,phone,password,major,degree)

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





