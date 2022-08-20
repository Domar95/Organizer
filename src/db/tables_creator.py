from sqlalchemy import Table, Column, Integer, String, MetaData

from db_manager import DBManager


class TableCreator:
    def __init__(self, engine):
        self.engine = engine
        self.meta = MetaData()

    def create_tables(self):
        """Create tables in database. Normally should be used just once to create the tables in db"""
        general_category = Table(
            "general_category",
            self.meta,
            Column("id", Integer, primary_key=True),
            Column("category_name", String(300)),
            Column("category_description", String(300)),
        )

        daily_goal = Table(
            "daily_goal",
            self.meta,
            Column("id", Integer, primary_key=True),
            Column("record_name", String(300)),
            Column("record_text", String(300)),
            Column("record_general_category_id", Integer),
            Column("record_importance", Integer),
            Column("record_date", String(300)),
            Column("record_duration", Integer),
        )

        idea = Table(
            "idea",
            self.meta,
            Column("id", Integer, primary_key=True),
            Column("record_name", String(300)),
            Column("record_text", String(300)),
            Column("record_general_category_id", Integer),
            Column("record_importance", Integer),
            Column("record_date", String(300)),
            Column("record_deadline", String(50)),
            Column("record_domain", String(300)),
        )

        info = Table(
            "info",
            self.meta,
            Column("id", Integer, primary_key=True),
            Column("record_name", String(300)),
            Column("record_text", String(300)),
            Column("record_general_category_id", Integer),
            Column("record_importance", Integer),
            Column("record_date", String(300)),
            Column("record_domain", String(300)),
            Column("record_link", String(300)),
            Column("record_image", String(300)),
        )

        other_record = Table(
            "other_record",
            self.meta,
            Column("id", Integer, primary_key=True),
            Column("record_name", String(300)),
            Column("record_text", String(300)),
            Column("record_general_category_id", Integer),
            Column("record_importance", Integer),
            Column("record_date", String(300)),
            Column("record_deadline", String(50)),
            Column("record_domain", String(300)),
            Column("record_link", String(300)),
            Column("record_image", String(300)),
        )

        programming_project = Table(
            "programming_project",
            self.meta,
            Column("id", Integer, primary_key=True),
            Column("record_name", String(300)),
            Column("record_text", String(300)),
            Column("record_general_category_id", Integer),
            Column("record_importance", Integer),
            Column("record_date", String(300)),
            Column("record_deadline", String(50)),
            Column("record_used_technologies", String(300)),
        )

        reflection = Table(
            "reflection",
            self.meta,
            Column("id", Integer, primary_key=True),
            Column("record_name", String(300)),
            Column("record_text", String(300)),
            Column("record_general_category_id", Integer),
            Column("record_importance", Integer),
            Column("record_date", String(300)),
            Column("record_deadline", String(50)),
            Column("record_domain", String(300)),
            Column("record_link", String(300)),
        )

        self.meta.create_all(self.engine)


if __name__ == "__main__":
    db_manager = DBManager()
    db_manager.start_engine()
    engine = db_manager.engine

    table_creator = TableCreator(engine)
    table_creator.create_tables()
