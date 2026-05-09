import os
import mysql.connector

class DataBase:
    def __init__(self):
        self._conn = None
        self._cursor = None
        self._host = os.getenv("DB_HOST")
        self._user = os.getenv("DB_USER")
        self._password = os.getenv("DB_PASSWORD")
        self._database = os.getenv("DB_DATABASE")
    
    def __enter__(self):

        self._conn = mysql.connector.connect(
            host=self._host,
            user=self._user,
            password=self._password,
            database=self._database
        )

        self._cursor = self._conn.cursor(dictionary=True)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_type:
            self._rollback()
        else:
            self._commit()
        
        if self._cursor: self._cursor.close()
        if self._conn: self._conn.close()
    
    def _commit(self):
        self._conn.commit()
    
    def _rollback(self):
        self._conn.rollback()
    
    def execute(self, query, params=None):
        self._cursor.execute(
            query,
            params or ()
        )

    def fetchall(self):
        return self._cursor.fetchall()
    
    def fetchone(self):
        return self._cursor.fetchone()