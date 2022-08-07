import os
import mysql.connector
from dotenv import load_dotenv


class DBManager():

    def __init__(self):
        self.db = None
        self.connected = False
        self.mycursor = None

    def get_credentials_from_dotenv(self):
        load_dotenv()
        username = os.getenv('db_username')
        password = os.getenv('db_password')
        return username, password

    def set_mycursor(self):
        self.mycursor = self.db.cursor()

    def connect_to_db(self):
        USERNAME, PASSWORD = self.get_credentials_from_dotenv()
        self.db = mysql.connector.connect(
            host='localhost', user=USERNAME, password=PASSWORD, database='testrecorddb')
        self.connected = True
        self.set_mycursor()

    def create_db(self, db_name):
        self.mycursor.execute(f'CREATE DATABASE {db_name}')

    def create_table(self, table_name):
        self.mycursor.execute(
            f"'CREATE TABLE testz (testID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), text VARCHAR(100), generalCategory VARCHAR(50), importance smallint UNSIGNED, date VARCHAR(20), duration smallint UNSIGNED)'")


if __name__ == '__main__':
    db_instance = DBManager()
    db_instance.connect_to_db()
    db_instance.create_table('testz')
