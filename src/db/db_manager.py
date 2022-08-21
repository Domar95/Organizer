import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.sql import select
from sqlalchemy import desc

from .models import *
from sqlalchemy.orm import sessionmaker


class DBManager:
    def __init__(self):
        self.db = None
        self.connected = False
        self.mycursor = None
        self.engine = None
        self.conn = None
        self.session = None

    def start_engine(self):
        """Initialize the engine"""
        load_dotenv()
        USERNAME = os.getenv("db_username")
        PASSWORD = os.getenv("db_password")

        self.engine = create_engine(
            f"mysql://{USERNAME}:{PASSWORD}@127.0.0.1:3306/organizer", echo=False
        )

        self.conn = self.engine.connect()

    def select_table(self, table):
        stmt = select(table)
        result = self.conn.execute(stmt)
        return result

    def select_table_where(self, table):
        stmt = select(table).where(table.category_name == 'Daily Goals')
        result = self.conn.execute(stmt)
        return result

    def superseded_justfyi(self, table, limit=None):

        stmt = select(table).order_by(desc(table.id)).limit(limit)
        result = self.conn.execute(stmt)
        return result

    def query_select_table_ordered_desc(self, table, limit=None):
        ''' returns most recent rows of specific table with optional limit'''
        Session = sessionmaker(self.engine)
        with Session() as session:
            result = session.query(table).order_by(desc(table.id)).limit(limit)
        return result

    def query_select_table_ordered_asc(self, table, limit=None):
        ''' returns most recent rows of specific table with optional limit'''
        Session = sessionmaker(self.engine)
        with Session() as session:
            result = session.query(table).order_by(table.id).limit(limit)
        return result

    def add_record_to_db(self, item):
        Session = sessionmaker(self.engine)
        with Session() as session:
            session.add(item)
            session.commit()

    def delete_record_from_db(self, table, id):
        Session = sessionmaker(self.engine)
        with Session() as session:
            session.query(table).filter(table.id == id).delete(
                synchronize_session=False)

    def find_record_by_id(self, table, id):
        Session = sessionmaker(self.engine)
        with Session() as session:
            result = session.query(table).filter(table.id == id)
            return result

    def find_record_by_name(self, table, data):
        Session = sessionmaker(self.engine)
        with Session() as session:
            result = session.query(table).filter(
                table.record_name.contains(data))
            return result


if __name__ == "__main__":
    db_manager = DBManager()
    db_manager.start_engine()
    table = GeneralCategory
    request = db_manager.select_table_ordered(table, 5)
    for i in request:
        print(i)
