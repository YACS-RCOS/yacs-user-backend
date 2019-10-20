from Model.Model import *
class User(Model):
    def __init__(self):
        super().__init__()

    def getUser(self, uid='%', name='%',email='%', password='%',phone='%',major='%',degree='%',enable=True):
        sql = """   SELECT uid, name, email, phone,password,major,degree,enable
                    FROM yacs_user_system.public.users
                    WHERE   uid::text   LIKE %s AND
                            name        LIKE %s AND 
                            email       LIKE %s AND 
                            phone       LIKE %s AND 
                            password    LIKE %s AND 
                            major       LIKE %s AND 
                            degree      LIKE %s AND
                            enable = %s"""

        args = (str(uid),name,email,phone,password,major,degree,enable)
        return self.pg.execute(sql,args,True)

    def addUser(self,name,email,phone,password,major,degree):
        sql = """INSERT INTO yacs_user_system.public.users (name, email, phone, password, major, degree,enable) VALUES (%s, %s, %s, %s, %s, %s, TRUE)"""
        args = (name,email,phone,password,major,degree)
        return self.pg.execute(sql,args,False)



    def deleteUser(self,uid):
        sql = """UPDATE yacs_user_system.public.users SET enable = FALSE WHERE uid = %s;"""
        args = (uid,)
        return self.pg.execute(sql,args,False)

