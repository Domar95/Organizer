from sqlalchemy.orm import Session
from typing import Optional
from sqlalchemy import ForeignKey

# from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped

# from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

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
        return f"({self.id}) N: {self.record_name} | T: {self.record_text} | I: {self.record_importance} | DT: {self.record_date} | DR: {self.record_duration}"

    def update(self, record_name, record_text, record_importance, record_date, record_duration):
        self.record_name = record_name
        self.record_text = record_text
        self.record_importance = record_importance
        self.record_date = record_date
        self.record_duration = record_duration


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
        return f"({self.id}) N: {self.record_name} | T: {self.record_text} | I: {self.record_importance} | DT: {self.record_date} | DL: {self.record_deadline} | DM: {self.record_domain}"

    def update(self, record_name, record_text, record_importance, record_date, record_deadline, record_domain):
        self.record_name = record_name
        self.record_text = record_text
        self.record_importance = record_importance
        self.record_date = record_date
        self.record_deadline = record_deadline
        self.record_domain = record_domain


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
        return f"({self.id}) N: {self.record_name} | T: {self.record_text} | I: {self.record_importance} | DT: {self.record_date} | DM: {self.record_domain} | L: {self.record_link} | IMG: {self.record_image}"

    def update(self, record_name, record_text, record_importance, record_date, record_domain, record_link, record_image):
        self.record_name = record_name
        self.record_text = record_text
        self.record_importance = record_importance
        self.record_date = record_date
        self.record_domain = record_domain
        self.record_link = record_link
        self.record_image = record_image


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
        return f"({self.id}) N: {self.record_name} | T: {self.record_text} | I: {self.record_importance} | DT: {self.record_date} | DL: {self.record_deadline} | DM: {self.record_domain} | L: {self.record_link} | IMG: {self.record_image}"

    def update(self, record_name, record_text, record_importance, record_date, record_deadline, record_domain, record_link, record_image):
        self.record_name = record_name
        self.record_text = record_text
        self.record_importance = record_importance
        self.record_date = record_date
        self.record_deadline = record_deadline
        self.record_domain = record_domain
        self.record_link = record_link
        self.record_image = record_image


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
        return f"({self.id}) N: {self.record_name} | T: {self.record_text} | I: {self.record_importance} | DT: {self.record_date} | DL: {self.record_deadline} | UT: {self.record_used_technologies}"

    def update(self, record_name, record_text, record_importance, record_date, record_deadline, record_used_technologies):
        self.record_name = record_name
        self.record_text = record_text
        self.record_importance = record_importance
        self.record_date = record_date
        self.record_deadline = record_deadline
        self.record_used_technologies = record_used_technologies


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
        return f"({self.id}) N: {self.record_name} | T: {self.record_text} | I: {self.record_importance} | DT: {self.record_date} | DL: {self.record_deadline} | DM: {self.record_domain} | L: {self.record_link}"

    def update(self, record_name, record_text, record_importance, record_date, record_deadline, record_domain, record_link):
        self.record_name = record_name
        self.record_text = record_text
        self.record_importance = record_importance
        self.record_date = record_date
        self.record_deadline = record_deadline
        self.record_domain = record_domain
        self.record_link = record_link
