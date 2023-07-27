import os
from psycopg2 import pool

conn_pool = pool.SimpleConnectionPool (
    1, 1000000,
    database=os.getenv('DB_NAME'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_POST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS')
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
        
    ##def insert(self, columns, values):
     ##   with self.pool.getconn() as conn:
      ##      with conn.cursor() as cursor:
            ##    sql = f"INSERT INTO {self.table} ({columns}) VALUES ({values})"
              ##  cursor.execute(sql)
          ##  conn.commit()


    ##def select(self, condition=""):
     ##   with self.pool.getconn() as conn:
       ##     with conn.cursor() as cursor:
           ##     sql = f"SELECT * FROM {self.table} {condition};"
             ##   cursor.execute(sql)
              ##  rows = cursor.fetchall()
               #3 return rows 
       
       

    def select(self,condition=''):
        conn = self.pool.getconn()
        cursor = conn.cursor()

       # sql = f"SELECT {columns} FROM {self.table} {str(joins_stat or '')} {str(condition or '')};"
       
        sql = f"SELECT * FROM {self.table} {condition};"

        cursor.execute(sql)
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows  
       
      