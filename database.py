import psycopg2
from config import *


class database(object):
    def __init__(self):
        self.connect_str = "dbname='{}' user='{}' host='{}' password='{}'".format(DB_NAME, DB_USER, DB_HOST, DB_PASSWORD)
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