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

    # function specific for this app rather than for db manager, can be done with args kwargs for db, below one is for this app
    # def insert_into_db(self, table_name, record_name=None, record_text=None, record_general_category=None, record_importance=None, record_date=None, duration=None, deadline=None, domain=None, link=None, image=None, used_technologies=None):
    #    self.mycursor.execute(f"'INSERT INTO DailyGoal (name, text, generalCategory, importance, date, duration) VALUES (%s,%s,%s,%s,%s,%s)",
#   #              ('workout', '3 times a week gym workout', 'object (reference general-cat obj)/another table', 8, '07.08.2022', 90))


if __name__ == '__main__':
    db_instance = DBManager()
    db_instance.connect_to_db()
    db_instance.create_table('testz')
