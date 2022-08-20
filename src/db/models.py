from sqlalchemy.orm import Session
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, MetaData

# from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped

# from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Table, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

from sqlalchemy import create_engine

import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("db_username")
PASSWORD = os.getenv("db_password")


engine = create_engine(
    f"mysql://{USERNAME}:{PASSWORD}@127.0.0.1:3306/testrecorddb", echo=True
)


Base = declarative_base()
# class Base():  # DeclarativeBase in 2.0.0
#    pass


# class Record(Base):
#    pass


class GeneralCategory(Base):
    __tablename__ = "general_category"

    id = Column(Integer, primary_key=True)
    category_name = Column(String)
    category_description = Column(String)
    records = relationship("DailyGoal")

    def __repr__(self) -> str:
        return f"GeneralCategory(id={self.id!r}, category_name={self.category_name!r}, category_description={self.category_description!r})"


class DailyGoal(Base):
    __tablename__ = "daily_goal"

    id = Column(Integer, primary_key=True)
    record_name = Column(String)
    record_text = Column(String)
    record_general_category_id = Column(Integer, ForeignKey("general_category.id"))
    record_importance = Column(Integer)
    record_date = Column(String)
    record_duration = Column(Integer)


#################################### ADD OTHER MODELS


# Base.metadata.create_all(engine)

with Session(engine) as session:

    my_category1 = GeneralCategory(
        category_name="Daily Goals", category_description="These are the daily ToDos"
    )
    my_category2 = GeneralCategory(
        category_name="Programming Projects",
        category_description=str([n for n in range(77)]),
    )

    my_goal = DailyGoal(
        record_name="test",
        record_text="test",
        record_general_category_id=3,
        record_importance=5,
        record_date="test",
        record_duration=5,
    )

    session.add_all([my_category1, my_category2, my_goal])

    session.commit()
