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
        # might be reasonable to re-order it after deletion (so if i delete ID 9 then all above are down by one so next starts at 9 again instead of 10)
        # or maybe the pattern is that this ID remains but we sort on other thing like date or sth (but it seems better to sort by ID coz its more mistake proof)
        Session = sessionmaker(self.engine)
        with Session() as session:
            session.query(table).filter(table.id == id).delete(
                synchronize_session=False)
            session.commit()

    def update_record(self, record):
        # might be using other funtions to first find a record to update (either by id or name  (but our name search might return many records, so rather not. Rather than object itself to be inputted (which was found by probably another func or choose by ID which is passed into func and then query inside this func)), and then input that record here so it can be updated
        # or create new object and place it into its place? or 1st delete and then input into its place?
        # or just delete old, sort and input new ? so it gets on the top of a list again? reason: coz it was updated
        # have to check what are the implementations for update
        raise NotImplementedError

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
