from sqlalchemy.orm import Session
from typing import Optional
from sqlalchemy import ForeignKey

# from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped

# from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from .db_manager import DBManager

# DeclarativeBase in 2.0.0
Base = declarative_base()


class GeneralCategory(Base):
    __tablename__ = "general_category"

    id = Column(Integer, primary_key=True)
    category_name = Column(String)
    category_description = Column(String)
    records = relationship("DailyGoal")

    def __repr__(self) -> str:
        return f"GeneralCategory(id={self.id!r}, category_name={self.category_name!r}, category_description={self.category_description!r})"

    def __str__(self):
        return f"({self.id}) {self.category_name}: {self.category_description}"


class DailyGoal(Base):
    __tablename__ = "daily_goal"

    id = Column(Integer, primary_key=True)
    record_name = Column(String)
    record_text = Column(String)
    record_general_category_id = Column(
        Integer, ForeignKey("general_category.id"))
    record_importance = Column(Integer)
    record_date = Column(String)
    record_duration = Column(Integer)

    def __repr__(self) -> str:
        return f"DailyGoal(id={self.id!r}, record_name={self.record_name!r}, record_text={self.record_text!r}, record_general_category_id={self.record_general_category_id!r}, record_importance={self.record_importance!r}, record_date={self.record_date!r}, record_duration={self.record_duration!r}"

    def __str__(self):
        return f"({self.id}) {self.record_name}: {self.record_text}"

    def get_instance_attributes(self):

        attributes = []

        for attribute in dir(self):
            if attribute.startswith("record_"):
                attributes.append(attribute)

        return attributes


class Idea(Base):
    __tablename__ = "idea"

    id = Column(Integer, primary_key=True)
    record_name = Column(String)
    record_text = Column(String)
    record_general_category_id = Column(
        Integer, ForeignKey("general_category.id"))
    record_importance = Column(Integer)
    record_date = Column(String)
    record_deadline = Column(String)
    record_domain = Column(String)

    def __repr__(self) -> str:
        return f"Idea(id={self.id!r}, record_name={self.record_name!r}, record_text={self.record_text!r}, record_general_category_id={self.record_general_category_id!r}, record_importance={self.record_importance!r}, record_deadline={self.record_deadline!r}, record_domain={self.record_domain!r}"

    def __str__(self):
        return f"({self.id}) {self.record_name}: {self.record_text}"


class Info(Base):
    __tablename__ = "info"

    id = Column(Integer, primary_key=True)
    record_name = Column(String)
    record_text = Column(String)
    record_general_category_id = Column(
        Integer, ForeignKey("general_category.id"))
    record_importance = Column(Integer)
    record_date = Column(String)
    record_domain = Column(String)
    record_link = Column(String)
    record_image = Column(String)

    def __repr__(self) -> str:
        return f"Info(id={self.id!r}, record_name={self.record_name!r}, record_text={self.record_text!r}, record_general_category_id={self.record_general_category_id!r}, record_importance={self.record_importance!r}, record_date={self.record_date!r}, record_domain={self.record_domain!r}, record_link={self.record_link!r}, record_image={self.record_image}"

    def __str__(self):
        return f"({self.id}) {self.record_name}: {self.record_text}"


class OtherRecord(Base):
    __tablename__ = "other_record"

    id = Column(Integer, primary_key=True)
    record_name = Column(String)
    record_text = Column(String)
    record_general_category_id = Column(
        Integer, ForeignKey("general_category.id"))
    record_importance = Column(Integer)
    record_date = Column(String)
    record_deadline = Column(String)
    record_domain = Column(String)
    record_link = Column(String)
    record_image = Column(String)

    def __repr__(self) -> str:
        return f"OtherRecord(id={self.id!r}, record_name={self.record_name!r}, record_text={self.record_text!r}, record_general_category_id={self.record_general_category_id!r}, record_importance={self.record_importance!r}, record_date={self.record_date!r}, record_deadline={self.record_deadline!r}, record_domain={self.record_domain!r}, record_link={self.record_link!r}, record_image={self.record_image}"

    def __str__(self):
        return f"({self.id}) {self.record_name}: {self.record_text}"


class ProgrammingProject(Base):
    __tablename__ = "programming_project"

    id = Column(Integer, primary_key=True)
    record_name = Column(String)
    record_text = Column(String)
    record_general_category_id = Column(
        Integer, ForeignKey("general_category.id"))
    record_importance = Column(Integer)
    record_date = Column(String)
    record_deadline = Column(String)
    record_used_technologies = Column(String)

    def __repr__(self) -> str:
        return f"Programming Project(id={self.id!r}, record_name={self.record_name!r}, record_text={self.record_text!r}, record_general_category_id={self.record_general_category_id!r}, record_importance={self.record_importance!r}, record_date={self.record_date!r}, record_deadline={self.record_deadline!r}, record_used_technologies={self.record_used_technologies!r}"

    def __str__(self):
        return f"({self.id}) {self.record_name}: {self.record_text}"


class Reflection(Base):
    __tablename__ = "reflection"

    id = Column(Integer, primary_key=True)
    record_name = Column(String)
    record_text = Column(String)
    record_general_category_id = Column(
        Integer, ForeignKey("general_category.id"))
    record_importance = Column(Integer)
    record_date = Column(String)
    record_deadline = Column(String)
    record_domain = Column(String)
    record_link = Column(String)

    def __repr__(self) -> str:
        return f"DailyGoal(id={self.id!r}, record_name={self.record_name!r}, record_text={self.record_text!r}, record_general_category_id={self.record_general_category_id!r}, record_importance={self.record_importance!r}, record_date={self.record_date!r}, record_deadline={self.record_deadline!r}, record_domain={self.record_domain!r}, record_link={self.record_link!r}"

    def __str__(self):
        return f"({self.id}) {self.record_name}: {self.record_text}"

# Base.metadata.create_all(engine)


if __name__ == "__main__":

    db_manager = DBManager()
    db_manager.start_engine()
    engine = db_manager.engine

    with Session(engine) as session:

        my_category1 = GeneralCategory(
            category_name="Daily Goals",
            category_description="Things to do on a daily basis",
        )
        my_category2 = GeneralCategory(
            category_name="Programming Projects",
            category_description="Ideas for programming projects to build in near future",
        )
        my_category3 = GeneralCategory(
            category_name="Ideas To Implement",
            category_description="General improvement ideas to implement into real life",
        )
        my_category4 = GeneralCategory(
            category_name="Info",
            category_description="General information that may hold value",
        )
        my_category5 = GeneralCategory(
            category_name="Thoughts",
            category_description="Personal thoughts or reflections that may hold value",
        )
        my_category6 = GeneralCategory(
            category_name="Others",
            category_description="All other stuff that needs to be stored",
        )

        my_goal = DailyGoal(
            record_name="My first daily goal",
            record_text="Daily goal description",
            record_general_category_id=1,
            record_importance=6,
            record_date="20.08.2022",
            record_duration=10,
        )

        my_idea = Idea(
            record_name="My first idea",
            record_text="Idea description",
            record_general_category_id=3,
            record_importance=5,
            record_date="21.08.2022",
            record_deadline="01.01.2023",
            record_domain="Food",
        )

        my_info = Info(
            record_name="My first info",
            record_text="Info description",
            record_general_category_id=4,
            record_importance=4,
            record_date="22.08.2022",
            record_domain="Health",
            record_link="link to website with more information or source",
            record_image="related image if available",
        )

        my_other_record = OtherRecord(
            record_name="My first other record",
            record_text="Other record description",
            record_general_category_id=6,
            record_importance=7,
            record_date="23.08.2022",
            record_deadline="02.01.2023",
            record_domain="Workout",
            record_link="link to website with more information or source",
            record_image="related image if available",
        )

        my_programming_project = ProgrammingProject(
            record_name="My first programming project",
            record_text="Programming project description",
            record_general_category_id=2,
            record_importance=8,
            record_date="24.08.2022",
            record_deadline="03.01.2023",
            record_used_technologies="Python, Flask, MySQL",
        )

        my_reflection = Reflection(
            record_name="My first reflection",
            record_text="Reflection description",
            record_general_category_id=5,
            record_importance=3,
            record_date="25.08.2022",
            record_deadline="04.01.2023",
            record_domain="Activities",
            record_link="link to website with more information or source",
        )

        session.add_all(
            [
                my_category1,
                my_category2,
                my_category3,
                my_category4,
                my_category5,
                my_category6,
                my_goal,
                my_idea,
                my_info,
                my_other_record,
                my_programming_project,
                my_reflection,
            ]
        )

        session.commit()
