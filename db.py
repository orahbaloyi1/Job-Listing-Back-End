import os
from psycopg2 import pool

conn_pool = pool.SimpleConnectionPool(
    1, 1000000,
    database="job listing Api",
    host="localhost",
    port="5432",
    user="postgres",
    password="5432"
    
)
class db:
    def __init__(self, table):
        self.table = table
        self.pool = conn_pool
        
    def insert(self, columns, values):
        conn = self.pool.getconn()
        cursor = conn.cursor()
        
        sql = f"INSERT INTO {self.table} ({columns}) VALUES ({values})"
       
        cursor.execute(sql)

        conn.commit()
        
        cursor.close()
        conn.close()


    def select(self, condition=""):
        conn = self.pool.getconn()
        cursor = conn.cursor()

        sql = f"SELECT * FROM {self.table} {condition};"

        cursor.execute(sql)
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows  
    