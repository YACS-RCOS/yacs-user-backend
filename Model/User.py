from Model.Model import *
class User(Model):
    def __init__(self):
        super().__init__()

    def getUser(self, name='%',email='%', password='%',phone='%',major='%',degree='%'):
        sql = """   SELECT uid, name, email, phone,password,major,degree 
                    FROM yacs_user_system.public.users
                    WHERE   name        LIKE %s AND 
                            email       LIKE %s AND 
                            phone       LIKE %s AND 
                            password    LIKE %s AND 
                            major       LIKE %s AND 
                            degree      LIKE %s"""

        args = (name,email,phone,password,major,degree)
        return self.pg.execute(sql,args,True)

    def addUser(self,name,email,phone,password,major,degree):
        sql = """INSERT INTO yacs_user_system.public.users (name, email, phone, password, major, degree) VALUES (%s, %s, %s, %s, %s, %s)"""
        args = (name,email,phone,password,major,degree)
        return self.pg.execute(sql,args,False)





