from .models import *
from .db_manager import DBManager
from sqlalchemy.orm import sessionmaker


class DataRemover:
    def __init__(self, engine):
        self.engine = engine

    def delete_all_data_from_all_tables(self):
        Session = sessionmaker(self.engine)
        with Session() as session:
            session.query(DailyGoal).delete()
            session.query(Idea).delete()
            session.query(Info).delete()
            session.query(OtherRecord).delete()
            session.query(ProgrammingProject).delete()
            session.query(Reflection).delete()
            session.commit()

    def delete_all_tables(self):
        DailyGoal.__table__.drop(self.engine)
        Idea.__table__.drop(self.engine)
        Info.__table__.drop(self.engine)
        OtherRecord.__table__.drop(self.engine)
        ProgrammingProject.__table__.drop(self.engine)
        Reflection.__table__.drop(self.engine)


if __name__ == "__main__":
    db_manager = DBManager()
    db_manager.start_engine()
    engine = db_manager.engine

    data_remover = DataRemover(engine)
    data_remover.delete_all_data_from_all_tables()
    data_remover.delete_all_tables()
