from sqlalchemy.orm import Session
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
#from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
#from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Table, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

from sqlalchemy import create_engine

import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('db_username')
PASSWORD = os.getenv('db_password')


engine = create_engine(
    f'mysql://{USERNAME}:{PASSWORD}@127.0.0.1:3306/testrecorddb', echo=True)


Base = declarative_base()
# class Base():  # DeclarativeBase in 2.0.0
#    pass


# class Record(Base):
#    pass


class GeneralCategory(Base):
    __tablename__ = 'general_category'

    id = Column(Integer, primary_key=True)
    category_name = Column(String(40))
    category_description = Column(String(100))

    def __repr__(self) -> str:
        return f"GeneralCategory(id={self.id!r}, category_name={self.category_name!r}, category_description={self.category_description!r})"


# Base.metadata.create_all(engine)

with Session(engine) as session:

    my_category1 = GeneralCategory(
        category_name='Daily Goals',
        category_description='These are the daily ToDos'
    )
    my_category2 = GeneralCategory(
        category_name='Programming Projects',
        category_description='These are ...'
    )

    session.add_all([my_category1, my_category2])

    session.commit()
