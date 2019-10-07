import psycopg2
from config import *

class DB():
    def __init__(self):
        self.connect_str = "dbname='{}' user='{}' host='{}' password='{}'".format(DB_NAME,DB_USER,DB_HOST,DB_PASSWORD)
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



if __name__ == '__main__':
    db = DB()
    db.connect()
    cur = db.getCursor()
    cur.execute("""SELECT version();""")
    rows = cur.fetchall()
    print(rows)



